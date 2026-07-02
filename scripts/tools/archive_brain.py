#!/usr/bin/env python3
"""
archive_brain.py — Memória em camadas do brain (anti-bloat).

O AUTO-PILOT manda ler `insights.md` ANTES de toda análise. Sem poda, o arquivo
cresce sem limite (já passou de 100KB) e o LLM passa a só "skim" — o autoaprendizado
degrada silenciosamente. Este script mantém em `insights.md` apenas os insights
QUENTES (Top N por recência, com bônus para os já validados) e move o restante para
`wiki/brain/insights-archive/YYYY-MM.md`, agrupado por mês.

É idempotente: entradas movidas saem de `insights.md`, então rodar de novo não duplica.

Uso:
  python scripts/tools/archive_brain.py                 # mantém Top 30 insights
  python scripts/tools/archive_brain.py --keep 40       # mantém Top 40
  python scripts/tools/archive_brain.py --predictions   # também arquiva previsões
                                                        # fechadas com > 90 dias
  python scripts/tools/archive_brain.py --dry-run       # só mostra o que faria

Sem dependências externas (stdlib pura).
"""

import os
import re
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRAIN_DIR = os.path.join(BASE_DIR, 'wiki', 'brain')
INSIGHTS_FILE = os.path.join(BRAIN_DIR, 'insights.md')
INSIGHTS_ARCHIVE_DIR = os.path.join(BRAIN_DIR, 'insights-archive')
PRED_FILE = os.path.join(BRAIN_DIR, 'predictions-log.md')
PRED_DIR = os.path.join(BRAIN_DIR, 'predictions')            # notas atômicas quentes
PRED_ARCHIVE_DIR = os.path.join(BRAIN_DIR, 'predictions-archive')

DEFAULT_KEEP = 30
PRED_MAX_AGE_DAYS = 90

ENTRY_HEADER_RE = re.compile(r'^###\s+\[(\d{4}-\d{2}-\d{2})', re.MULTILINE)
# Marcadores de que um insight já foi validado → ganha bônus para ficar mais tempo no hot
VALIDATED_RE = re.compile(r'confirmaç|validad|consolidad|✅', re.IGNORECASE)


def split_entries(text):
    """Separa (preâmbulo, [entradas]). Cada entrada começa em '### [data'."""
    matches = list(ENTRY_HEADER_RE.finditer(text))
    if not matches:
        return text, []
    preamble = text[:matches[0].start()]
    entries = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        date = datetime.strptime(m.group(1), '%Y-%m-%d')
        body = text[start:end]
        entries.append({'date': date, 'text': body.rstrip('\n') + '\n', 'month': m.group(1)[:7]})
    return preamble, entries


def archive_insights(keep, dry_run):
    if not os.path.exists(INSIGHTS_FILE):
        print('  insights.md inexistente — nada a arquivar.')
        return 0
    with open(INSIGHTS_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
    preamble, entries = split_entries(text)
    if len(entries) <= keep:
        print(f'  insights.md: {len(entries)} insights ≤ keep={keep} — nada a arquivar.')
        return 0

    # Ordena: validados primeiro, depois mais recentes. Mantém os Top {keep}.
    ranked = sorted(
        entries,
        key=lambda e: (bool(VALIDATED_RE.search(e['text'])), e['date']),
        reverse=True,
    )
    hot = ranked[:keep]
    cold = ranked[keep:]

    # Reordena o hot por data desc (mais recente no topo, como o arquivo já fazia)
    hot_sorted = sorted(hot, key=lambda e: e['date'], reverse=True)

    # Agrupa o cold por mês
    by_month = {}
    for e in cold:
        by_month.setdefault(e['month'], []).append(e)

    print(f'  insights.md: {len(entries)} insights → mantém {len(hot)} quentes, '
          f'arquiva {len(cold)} em {len(by_month)} arquivo(s) mensal(is).')
    if dry_run:
        for month in sorted(by_month):
            print(f'    [dry-run] {month}: +{len(by_month[month])}')
        return len(cold)

    os.makedirs(INSIGHTS_ARCHIVE_DIR, exist_ok=True)
    for month in sorted(by_month):
        path = os.path.join(INSIGHTS_ARCHIVE_DIR, month + '.md')
        chunk = sorted(by_month[month], key=lambda e: e['date'], reverse=True)
        header = '' if os.path.exists(path) else f'# Insights arquivados — {month}\n\n> Movidos de `insights.md` por `archive_brain.py`.\n\n'
        with open(path, 'a', encoding='utf-8') as f:
            f.write(header + '\n'.join(e['text'] for e in chunk) + '\n')

    new_text = preamble.rstrip('\n') + '\n\n' + '\n'.join(e['text'] for e in hot_sorted)
    with open(INSIGHTS_FILE, 'w', encoding='utf-8') as f:
        f.write(new_text.rstrip('\n') + '\n')
    return len(cold)


def archive_predictions(now, dry_run):
    """Arquiva previsões FECHADAS (✅/❌/⚪) com data > 90 dias. Mantém as abertas (⏳)."""
    if not os.path.exists(PRED_FILE):
        print('  predictions-log.md inexistente — nada a arquivar.')
        return 0
    with open(PRED_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
    preamble, entries = split_entries(text)
    if not entries:
        print('  predictions-log.md sem entradas datadas — nada a arquivar.')
        return 0

    keep, cold = [], []
    for e in entries:
        age = (now - e['date']).days
        is_open = '⏳' in e['text']
        if age > PRED_MAX_AGE_DAYS and not is_open:
            cold.append(e)
        else:
            keep.append(e)

    if not cold:
        print(f'  predictions-log.md: nenhuma previsão fechada com > {PRED_MAX_AGE_DAYS}d — nada a arquivar.')
        return 0

    by_month = {}
    for e in cold:
        by_month.setdefault(e['month'], []).append(e)

    print(f'  predictions-log.md: arquiva {len(cold)} previsão(ões) > {PRED_MAX_AGE_DAYS}d '
          f'em {len(by_month)} arquivo(s).')
    if dry_run:
        return len(cold)

    os.makedirs(PRED_ARCHIVE_DIR, exist_ok=True)
    for month in sorted(by_month):
        path = os.path.join(PRED_ARCHIVE_DIR, month + '.md')
        chunk = sorted(by_month[month], key=lambda e: e['date'])
        header = '' if os.path.exists(path) else f'# Previsões arquivadas — {month}\n\n> Movidas de `predictions-log.md` por `archive_brain.py`.\n\n'
        with open(path, 'a', encoding='utf-8') as f:
            f.write(header + '\n'.join(e['text'] for e in chunk) + '\n')

    keep_sorted = sorted(keep, key=lambda e: e['date'])
    new_text = preamble.rstrip('\n') + '\n\n' + '\n'.join(e['text'] for e in keep_sorted)
    with open(PRED_FILE, 'w', encoding='utf-8') as f:
        f.write(new_text.rstrip('\n') + '\n')
    return len(cold)


def archive_note_predictions(now, dry_run):
    """Move NOTAS atômicas de previsão FECHADAS (status != open) com > 90 dias de
    `predictions/` para `predictions-archive/`. Elas somem do recall quente
    (brain-read/check_predictions só varrem `predictions/`) mas continuam contando nas
    métricas (metrics_engine varre os dois). Não toca abertas. Idempotente (move arquivo)."""
    import glob
    if not os.path.isdir(PRED_DIR):
        return 0
    moved = 0
    for path in sorted(glob.glob(os.path.join(PRED_DIR, '*.md'))):
        with open(path, 'r', encoding='utf-8') as f:
            head = f.read(600)
        m = re.search(r'(?m)^status:\s*(\S+)', head)
        dm = re.search(r'(?m)^date:\s*(\d{4}-\d{2}-\d{2})', head)
        if not m or not dm:
            continue
        status = m.group(1).strip().strip('"\'').lower()
        if status in ('open', 'aberta'):
            continue
        try:
            age = (now - datetime.strptime(dm.group(1), '%Y-%m-%d')).days
        except ValueError:
            continue
        if age <= PRED_MAX_AGE_DAYS:
            continue
        moved += 1
        if dry_run:
            continue
        os.makedirs(PRED_ARCHIVE_DIR, exist_ok=True)
        os.rename(path, os.path.join(PRED_ARCHIVE_DIR, os.path.basename(path)))
    print(f'  predictions/ (notas): arquiva {moved} nota(s) fechada(s) > {PRED_MAX_AGE_DAYS}d.')
    return moved


def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args
    do_pred = '--predictions' in args
    keep = DEFAULT_KEEP
    if '--keep' in args:
        try:
            keep = int(args[args.index('--keep') + 1])
        except (IndexError, ValueError):
            print('--keep requer um inteiro.')
            return

    now = datetime.now()
    print('Arquivamento do brain' + (' [DRY-RUN]' if dry_run else '') + ':')
    moved = archive_insights(keep, dry_run)
    if do_pred:
        moved += archive_predictions(now, dry_run)
        moved += archive_note_predictions(now, dry_run)
    print(f'Total movido: {moved} entrada(s).')


if __name__ == '__main__':
    main()
