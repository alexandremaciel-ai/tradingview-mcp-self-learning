#!/usr/bin/env python3
"""
wiki_lint.py — Health-check automático da wiki.

Detecta:
  - Wikilinks quebrados ([[alvo]] sem arquivo .md correspondente)
  - Previsões ⏳ abertas há mais de 48h (candidatas a ⚪ expirada)
  - Setups sem estatística (win rate / total não preenchidos)
  - Conceitos órfãos (arquivo em concepts/ que ninguém referencia)
  - Contadores desatualizados em wiki/index.md (corrige automaticamente)

Saída:
  - Relatório em wiki/lint/AAAA-MM-DD.md
  - Atualização in-place dos contadores e da data em wiki/index.md

Uso:
  python scripts/tools/wiki_lint.py            # roda o lint completo
  python scripts/tools/wiki_lint.py --no-index # não mexe no index.md

Sem dependências externas (stdlib pura).
"""

import os
import re
import sys
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI_DIR = os.path.join(BASE_DIR, 'wiki')
INDEX_FILE = os.path.join(WIKI_DIR, 'index.md')
PRED_FILE = os.path.join(WIKI_DIR, 'brain', 'predictions-log.md')
SETUPS_INDEX = os.path.join(WIKI_DIR, 'setups', 'index.md')
LINT_DIR = os.path.join(WIKI_DIR, 'lint')

# Seções da wiki contadas no index (rótulo -> subpasta)
SECTIONS = {
    'brain/': 'brain',
    'assets/': 'assets',
    'setups/': 'setups',
    'strategies/': 'strategies',
    'concepts/': 'concepts',
    'sessions/': 'sessions',
    'research/': 'research',
    'analysis/': 'analysis',
    'lint/': 'lint',
}

WIKILINK_RE = re.compile(r'\[\[([^\]\|#]+)(?:[#\|][^\]]*)?\]\]')
# Anexos (imagens/arquivos) não são páginas da wiki — ignorados na checagem de links
ATTACHMENT_EXTS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf', '.csv', '.xlsx')
# Arquivos que não devem ser tratados como FONTES de links (placeholders)
# Obs: a pasta brain/_templates/ é ignorada por inteiro via skip_dirs (links de exemplo)
SKIP_SOURCE_SUFFIXES = ('_template.md', '.initial.md')
# Cabeçalho de previsão: ### [AAAA-MM-DD ...] ...
PRED_HEADER_RE = re.compile(r'^###\s+\[(\d{4}-\d{2}-\d{2})[^\]]*\]\s*(.*)$')
STATUS_OPEN_RE = re.compile(r'^- \*\*Status:\*\*\s*⏳')


def all_md_files(root, skip_dirs=()):
    """Retorna lista de caminhos absolutos de todos os .md sob root."""
    out = []
    for dirpath, _dirs, files in os.walk(root):
        if os.sep + '.git' in dirpath:
            continue
        if any((os.sep + d) in dirpath or dirpath.endswith(os.sep + d) for d in skip_dirs):
            continue
        for f in files:
            if f.endswith('.md'):
                out.append(os.path.join(dirpath, f))
    return out


def basename_index(repo_root):
    """Mapa nome-de-arquivo-sem-extensao (lowercase) -> caminho, para todo o repo."""
    idx = {}
    for path in all_md_files(repo_root):
        name = os.path.splitext(os.path.basename(path))[0].lower()
        idx.setdefault(name, path)
    return idx


def count_sections():
    counts = {}
    for label, sub in SECTIONS.items():
        d = os.path.join(WIKI_DIR, sub)
        n = 0
        if os.path.isdir(d):
            n = len([f for f in os.listdir(d) if f.endswith('.md')])
        counts[label] = n
    return counts


def _link_resolves(target, known_names):
    """Um link resolve se o nome (ou seu basename, p/ links com caminho) existe."""
    t = target.strip().lower()
    if not t:
        return True
    if t.endswith(ATTACHMENT_EXTS):
        return True  # anexo, não página
    if t in known_names:
        return True
    base = t.rsplit('/', 1)[-1]  # resolve [[brain/insights]] -> insights
    return base in known_names


def find_broken_links(known_names):
    """Procura wikilinks na wiki cujo alvo não existe em lugar nenhum do repo."""
    broken = {}  # alvo -> lista de arquivos que o citam
    for path in all_md_files(WIKI_DIR, skip_dirs=('lint', '_templates')):
        if path.endswith(SKIP_SOURCE_SUFFIXES):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except OSError:
            continue
        for m in WIKILINK_RE.finditer(content):
            target = m.group(1).strip()
            if not target:
                continue
            if not _link_resolves(target, known_names):
                rel = os.path.relpath(path, BASE_DIR)
                broken.setdefault(target, set()).add(rel)
    return broken


def find_referenced_names():
    """Conjunto de todos os alvos de wikilink citados na wiki (lowercase)."""
    refs = set()
    for path in all_md_files(WIKI_DIR, skip_dirs=('lint', '_templates')):
        if path.endswith(SKIP_SOURCE_SUFFIXES):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except OSError:
            continue
        for m in WIKILINK_RE.finditer(content):
            refs.add(m.group(1).strip().lower())
    return refs


def find_orphan_concepts(referenced):
    concepts_dir = os.path.join(WIKI_DIR, 'concepts')
    orphans = []
    if not os.path.isdir(concepts_dir):
        return orphans
    for f in os.listdir(concepts_dir):
        if not f.endswith('.md'):
            continue
        name = os.path.splitext(f)[0].lower()
        if name not in referenced:
            orphans.append(f)
    return sorted(orphans)


def find_expired_predictions(now):
    """Previsões com Status ⏳ cujo cabeçalho tem data > 48h atrás."""
    expired = []
    if not os.path.exists(PRED_FILE):
        return expired
    with open(PRED_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cutoff = now - timedelta(hours=48)
    current = None  # (date, title)
    for line in lines:
        hm = PRED_HEADER_RE.match(line.rstrip('\n'))
        if hm:
            try:
                d = datetime.strptime(hm.group(1), '%Y-%m-%d')
            except ValueError:
                d = None
            current = (d, hm.group(2).strip())
            continue
        if current and STATUS_OPEN_RE.match(line.rstrip('\n')):
            d, title = current
            if d is not None and d < cutoff:
                age = (now - d).days
                expired.append((d.strftime('%Y-%m-%d'), title, age))
            current = None
    return expired


def find_setups_without_stats():
    """Lê setups/index.md e retorna setups com win rate ou total ausente."""
    issues = []
    if not os.path.exists(SETUPS_INDEX):
        return issues
    with open(SETUPS_INDEX, 'r', encoding='utf-8') as f:
        for line in f:
            # linha de tabela: | [[setup]] | win | rr | total | ... |
            if line.strip().startswith('|') and '[[' in line:
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) >= 4:
                    name = cells[0]
                    win = cells[1]
                    total = cells[3]
                    if win in ('—', '-', '') or total in ('—', '-', '', '0'):
                        issues.append(name)
    return issues


def find_compliance_gaps(now):
    """Sessões recentes (7d) sem WRITE correspondente no brain (indicators/patterns).
    Expõe o gap de processo: análises feitas mas o ciclo de aprendizado não atualizado.
    Heurística por mtime — best-effort (clone/checkout reseta mtime)."""
    issues = []
    sessions_dir = os.path.join(WIKI_DIR, 'sessions')
    if not os.path.isdir(sessions_dir):
        return issues
    cutoff = now - timedelta(days=7)
    recent = []
    for f in os.listdir(sessions_dir):
        if not f.endswith('.md') or f.startswith('_'):
            continue
        mt = datetime.fromtimestamp(os.path.getmtime(os.path.join(sessions_dir, f)))
        if mt >= cutoff:
            recent.append(mt)
    if not recent:
        return issues
    newest_session = max(recent)
    for brain_file in ('indicators.md', 'patterns.md'):
        bpath = os.path.join(WIKI_DIR, 'brain', brain_file)
        if not os.path.exists(bpath):
            continue
        bmt = datetime.fromtimestamp(os.path.getmtime(bpath))
        if bmt < newest_session:
            issues.append((brain_file, len(recent), (newest_session - bmt).days))
    return issues


def update_index(counts, now):
    """Atualiza contadores na tabela de estrutura e a data em index.md."""
    if not os.path.exists(INDEX_FILE):
        return False
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Atualiza a data
    content = re.sub(
        r'(> Última atualização: )\d{4}-\d{2}-\d{2}',
        r'\g<1>' + now.strftime('%Y-%m-%d'),
        content,
    )

    # Atualiza contadores na tabela: | [brain/](brain/) | ... | N |
    for label, n in counts.items():
        # linha começa com | [label]( ... e termina com | N |
        pattern = re.compile(
            r'(\|\s*\[' + re.escape(label) + r'\][^\n|]*\|[^\n|]*\|\s*)\d+(\s*\|)'
        )
        content = pattern.sub(r'\g<1>' + str(n) + r'\g<2>', content)

    if content != original:
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def write_report(now, counts, broken, expired, setup_issues, orphans, compliance, index_updated):
    os.makedirs(LINT_DIR, exist_ok=True)
    report_path = os.path.join(LINT_DIR, now.strftime('%Y-%m-%d') + '.md')

    total_issues = len(broken) + len(expired) + len(setup_issues) + len(orphans) + len(compliance)

    lines = []
    lines.append('# Wiki Lint — ' + now.strftime('%Y-%m-%d %H:%M'))
    lines.append('')
    lines.append('> Gerado por `scripts/tools/wiki_lint.py`. ' + str(total_issues) + ' issue(s) encontrado(s).')
    lines.append('')

    lines.append('## Contadores por Seção')
    lines.append('')
    lines.append('| Seção | Arquivos |')
    lines.append('|-------|----------|')
    for label, n in counts.items():
        lines.append('| ' + label + ' | ' + str(n) + ' |')
    lines.append('')
    lines.append('Index atualizado: ' + ('✅ sim' if index_updated else '— sem mudança'))
    lines.append('')

    lines.append('## Wikilinks Quebrados (' + str(len(broken)) + ')')
    lines.append('')
    if broken:
        for target in sorted(broken):
            srcs = ', '.join(sorted(broken[target]))
            lines.append('- `[[' + target + ']]` — citado em: ' + srcs)
    else:
        lines.append('Nenhum. ✅')
    lines.append('')

    lines.append('## Previsões Expiradas (>48h abertas) (' + str(len(expired)) + ')')
    lines.append('')
    if expired:
        lines.append('> Marcar como ⚪ expirada em `brain/predictions-log.md`.')
        lines.append('')
        for date, title, age in expired:
            lines.append('- [' + date + '] (' + str(age) + 'd) ' + title)
    else:
        lines.append('Nenhuma. ✅')
    lines.append('')

    lines.append('## Setups sem Estatística (' + str(len(setup_issues)) + ')')
    lines.append('')
    if setup_issues:
        lines.append('> Win rate ou total ausente — fechar trades e rodar `metrics_engine.py`.')
        lines.append('')
        for name in setup_issues:
            lines.append('- ' + name)
    else:
        lines.append('Nenhum. ✅')
    lines.append('')

    lines.append('## Conceitos Órfãos (sem backlink) (' + str(len(orphans)) + ')')
    lines.append('')
    if orphans:
        lines.append('> Conceito existe mas ninguém o referencia com [[...]]. Adicionar backlink ou arquivar.')
        lines.append('')
        for f in orphans:
            lines.append('- ' + f)
    else:
        lines.append('Nenhum. ✅')
    lines.append('')

    lines.append('## Compliance de Processo — WRITE do Brain (' + str(len(compliance)) + ')')
    lines.append('')
    if compliance:
        lines.append('> Sessões recentes existem mas o ciclo WRITE não atualizou o brain. O autoaprendizado só funciona se cada análise alimentar indicators/patterns.')
        lines.append('')
        for brain_file, n_sessions, days in compliance:
            lines.append('- ⚠️ `brain/' + brain_file + '` sem atualização há ' + str(days)
                         + 'd, apesar de ' + str(n_sessions) + ' sessão(ões) nos últimos 7 dias.')
    else:
        lines.append('Nenhum. ✅')
    lines.append('')

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return report_path, total_issues


def main():
    no_index = '--no-index' in sys.argv
    now = datetime.now()

    counts = count_sections()
    known = basename_index(BASE_DIR)
    broken = find_broken_links(known)
    referenced = find_referenced_names()
    orphans = find_orphan_concepts(referenced)
    expired = find_expired_predictions(now)
    setup_issues = find_setups_without_stats()
    compliance = find_compliance_gaps(now)

    index_updated = False
    if not no_index:
        index_updated = update_index(counts, now)

    report_path, total = write_report(
        now, counts, broken, expired, setup_issues, orphans, compliance, index_updated
    )

    rel = os.path.relpath(report_path, BASE_DIR)
    print('Wiki lint concluído: ' + str(total) + ' issue(s).')
    print('  Wikilinks quebrados: ' + str(len(broken)))
    print('  Previsões expiradas: ' + str(len(expired)))
    print('  Setups sem stats:    ' + str(len(setup_issues)))
    print('  Conceitos órfãos:    ' + str(len(orphans)))
    print('  Compliance brain:    ' + str(len(compliance)))
    print('  Index atualizado:    ' + ('sim' if index_updated else 'não'))
    print('Relatório: ' + rel)


if __name__ == '__main__':
    main()
