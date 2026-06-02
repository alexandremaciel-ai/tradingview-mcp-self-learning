#!/usr/bin/env python3
"""
metrics_engine.py — Motor de métricas e calibração do brain.

Lê wiki/brain/predictions-log.md (formato novo com campos parseáveis E o
formato legado em texto livre) e calcula métricas objetivas de edge:

  - Win rate global e por: lado (long/short/spot), tipo (scalp/swing/holder),
    setup, playbook, regime macro (risk-on/off/misto), dia útil vs fim de semana.
  - Calibração de confiança: win rate observado por nível + Brier score.
  - Drawdown: maior sequência de losses; streak atual → flag de circuit breaker.
  - R:R planejado vs realizado.

Escreve o resultado em wiki/brain/metrics.md (consumido pela LLM e pelo Obsidian
Dataview) e atualiza o bloco "Métricas Globais" de wiki/setups/index.md.

Uso:
  python scripts/tools/metrics_engine.py

Sem dependências externas (stdlib pura).
"""

import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRED_FILE = os.path.join(BASE_DIR, 'wiki', 'brain', 'predictions-log.md')
OUT_FILE = os.path.join(BASE_DIR, 'wiki', 'brain', 'metrics.md')
SETUPS_INDEX = os.path.join(BASE_DIR, 'wiki', 'setups', 'index.md')

# Mapa de confiança -> probabilidade implícita de acerto (para Brier score)
CONFIDENCE_PROB = {
    'alta': 0.75,
    'média-alta': 0.65,
    'media-alta': 0.65,
    'média': 0.55,
    'media': 0.55,
    'baixa': 0.45,
}

HEADER_RE = re.compile(r'^###\s+\[(\d{4}-\d{2}-\d{2})[^\]]*\]\s*(.*)$')


def field(block, name):
    """Extrai o valor de um campo '- **Nome:** valor' (primeira ocorrência)."""
    m = re.search(r'- \*\*' + re.escape(name) + r':\*\*\s*(.+)', block)
    return m.group(1).strip() if m else None


def detect_status(block):
    """Detecta status pelo emoji na linha '- **Status:**'. Retorna win/loss/open/expired/None."""
    m = re.search(r'- \*\*Status:\*\*\s*(.+)', block)
    if not m:
        return None
    s = m.group(1)
    if '✅' in s:
        return 'win'
    if '❌' in s:
        return 'loss'
    if '⏳' in s:
        return 'open'
    if '⚪' in s:
        return 'expired'
    return None


def infer_side(block, header_rest):
    """Lê o campo Lado; se ausente, infere do header/título."""
    lado = field(block, 'Lado')
    if lado:
        t = lado.lower()
        if 'long' in t:
            return 'long'
        if 'short' in t:
            return 'short'
        if 'spot' in t:
            return 'spot'
    hay = (header_rest + ' ' + block).lower()
    if re.search(r'\b(long|bullish|bull|compra)\b', hay) and not re.search(r'\b(short|bearish)\b', hay):
        return 'long'
    if re.search(r'\b(short|bearish|sell)\b', hay):
        return 'short'
    if 'spot' in hay:
        return 'spot'
    return 'indefinido'


def infer_type(block):
    val = field(block, 'Tipo')
    hay = (val or block).lower()
    if 'holder' in hay:
        return 'holder'
    if 'swing' in hay:
        return 'swing'
    if 'scalp' in hay:
        return 'scalp'
    return 'indefinido'


def infer_confidence(block):
    val = field(block, 'Confiança')
    if not val:
        return None
    t = val.lower()
    if 'média-alta' in t or 'media-alta' in t or 'média alta' in t:
        return 'média-alta'
    if 'alta' in t:
        return 'alta'
    if 'média' in t or 'media' in t:
        return 'média'
    if 'baixa' in t:
        return 'baixa'
    return None


def infer_regime(block):
    val = field(block, 'Regime')
    hay = (val or block).lower()
    if 'risk-off' in hay or 'risk off' in hay:
        return 'risk-off'
    if 'risk-on' in hay or 'risk on' in hay:
        return 'risk-on'
    if 'misto' in hay:
        return 'misto'
    return 'indefinido'


def infer_playbook(block):
    val = field(block, 'Playbook')
    if val:
        m = re.search(r'([1-4])', val)
        if m:
            return 'Playbook ' + m.group(1)
    m = re.search(r'Playbook\s*([1-4])', block)
    if m:
        return 'Playbook ' + m.group(1)
    return None


def infer_setup(block):
    """Só conta setup quando referenciado como wikilink [[nome]] (evita texto livre)."""
    val = field(block, 'Setup')
    if val:
        m = re.search(r'\[\[([^\]\|#]+)', val)
        if m:
            return m.group(1).strip()
    return None


def parse_float(s):
    if not s:
        return None
    m = re.search(r'(\d+(?:\.\d+)?)', s.replace(',', ''))
    return float(m.group(1)) if m else None


def infer_rr_real(block, status):
    """R:R real do campo explícito; fallback: 'R:R estimado ~X:1' no texto (só wins)."""
    val = field(block, 'R:R real')
    rr = parse_float(val) if val and val not in ('_(preenchido no feedback)_',) else None
    if rr is not None:
        return rr
    if status == 'win':
        m = re.search(r'R:R[^\n]*?(\d+(?:\.\d+)?)\s*:\s*1', block)
        if m:
            return float(m.group(1))
    return None


def parse_predictions():
    if not os.path.exists(PRED_FILE):
        return []
    with open(PRED_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Localiza início de cada bloco "### [data...]"
    headers = []
    for i, line in enumerate(lines):
        hm = HEADER_RE.match(line.rstrip('\n'))
        if hm:
            headers.append((i, hm.group(1), hm.group(2).strip()))

    records = []
    for idx, (start, date_str, rest) in enumerate(headers):
        end = headers[idx + 1][0] if idx + 1 < len(headers) else len(lines)
        block = ''.join(lines[start:end])
        status = detect_status(block)
        if status is None:
            continue
        try:
            d = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            continue
        records.append({
            'date': d,
            'title': rest,
            'status': status,
            'side': infer_side(block, rest),
            'type': infer_type(block),
            'confidence': infer_confidence(block),
            'regime': infer_regime(block),
            'playbook': infer_playbook(block),
            'setup': infer_setup(block),
            'rr_plan': parse_float(field(block, 'R:R plan')),
            'rr_real': infer_rr_real(block, status),
            'weekend': d.weekday() >= 5,
        })
    return records


# ---------- Agregações ----------

def wl(records):
    wins = sum(1 for r in records if r['status'] == 'win')
    losses = sum(1 for r in records if r['status'] == 'loss')
    return wins, losses


def winrate(wins, losses):
    closed = wins + losses
    return (wins / closed * 100.0) if closed else None


def group_table(records, keyfn, label):
    """Tabela win rate por grupo (apenas trades fechados contam no win rate)."""
    groups = {}
    for r in records:
        k = keyfn(r)
        if k is None:
            k = '—'
        groups.setdefault(k, []).append(r)
    rows = []
    for k in sorted(groups):
        recs = groups[k]
        w, l = wl(recs)
        wr = winrate(w, l)
        opn = sum(1 for r in recs if r['status'] == 'open')
        exp = sum(1 for r in recs if r['status'] == 'expired')
        rows.append((k, w, l, opn, exp, wr))
    return rows


def fmt_wr(wr):
    return '—' if wr is None else f'{wr:.0f}%'


def render_group(title, label, rows):
    out = [f'### {title}', '', f'| {label} | Win | Loss | Win Rate | Abertas | Expiradas |',
           '|---|---|---|---|---|---|']
    for k, w, l, opn, exp, wr in rows:
        out.append(f'| {k} | {w} | {l} | {fmt_wr(wr)} | {opn} | {exp} |')
    out.append('')
    return out


def calibration(records):
    """Win rate observado por nível de confiança + Brier score global."""
    levels = ['alta', 'média-alta', 'média', 'baixa']
    rows = []
    brier_sum = 0.0
    brier_n = 0
    for lvl in levels:
        recs = [r for r in records if r['confidence'] == lvl and r['status'] in ('win', 'loss')]
        w, l = wl(recs)
        wr = winrate(w, l)
        prob = CONFIDENCE_PROB.get(lvl, 0.5)
        rows.append((lvl, prob, w, l, wr))
        for r in recs:
            outcome = 1.0 if r['status'] == 'win' else 0.0
            brier_sum += (prob - outcome) ** 2
            brier_n += 1
    brier = (brier_sum / brier_n) if brier_n else None
    return rows, brier, brier_n


def max_loss_streak(records):
    """Maior sequência de losses e streak atual (em ordem cronológica)."""
    closed = [r for r in sorted(records, key=lambda x: x['date']) if r['status'] in ('win', 'loss')]
    max_streak = 0
    cur = 0
    for r in closed:
        if r['status'] == 'loss':
            cur += 1
            max_streak = max(max_streak, cur)
        else:
            cur = 0
    return max_streak, cur


def avg(values):
    vals = [v for v in values if v is not None]
    return (sum(vals) / len(vals)) if vals else None


def build_report(records):
    now = datetime.now()
    total = len(records)
    wins, losses = wl(records)
    opn = sum(1 for r in records if r['status'] == 'open')
    exp = sum(1 for r in records if r['status'] == 'expired')
    wr_global = winrate(wins, losses)

    cal_rows, brier, brier_n = calibration(records)
    max_streak, cur_streak = max_loss_streak(records)
    rr_plan = avg([r['rr_plan'] for r in records])
    rr_real = avg([r['rr_real'] for r in records])

    cb_active = cur_streak >= 3

    out = []
    out.append('# Brain — Métricas e Calibração')
    out.append('')
    out.append(f'> Gerado por `scripts/tools/metrics_engine.py` em {now.strftime("%Y-%m-%d %H:%M")}.')
    out.append('> Win rate considera apenas trades FECHADOS (✅/❌). Abertas (⏳) e expiradas/não-acionadas (⚪) são contadas à parte.')
    out.append('')

    # Resumo
    out.append('## Resumo Global')
    out.append('')
    out.append('| Métrica | Valor |')
    out.append('|---|---|')
    out.append(f'| Previsões totais | {total} |')
    out.append(f'| Fechadas (✅+❌) | {wins + losses} |')
    out.append(f'| Wins ✅ | {wins} |')
    out.append(f'| Losses ❌ | {losses} |')
    out.append(f'| Abertas ⏳ | {opn} |')
    out.append(f'| Expiradas/não-acionadas ⚪ | {exp} |')
    out.append(f'| **Win Rate global** | **{fmt_wr(wr_global)}** |')
    out.append(f'| R:R plan médio | {("—" if rr_plan is None else f"{rr_plan:.2f}")} |')
    out.append(f'| R:R real médio | {("—" if rr_real is None else f"{rr_real:.2f}")} |')
    out.append(f'| Maior sequência de losses | {max_streak} |')
    out.append(f'| Sequência atual de losses | {cur_streak} |')
    out.append('')

    # Circuit breaker
    out.append('## ⚠️ Circuit Breaker')
    out.append('')
    if cb_active:
        out.append(f'🔴 **ATIVO** — {cur_streak} losses consecutivos (≥3). Rebaixar novas recomendações para "somente observação / paper" até um win resetar a série. Ver [[trading-psychology]].')
    else:
        out.append(f'🟢 Inativo — sequência atual de losses: {cur_streak} (limite: 3).')
    out.append('')

    # Calibração
    out.append('## Calibração de Confiança')
    out.append('')
    out.append('> Se "alta" não vence "média", a confiança está descalibrada — recalibrar o peso dos sinais.')
    out.append('> Brier score: 0 = perfeito, 0.25 = aleatório (chute 50%), 1 = sempre errado. Menor é melhor.')
    out.append('')
    out.append('| Confiança | Prob. implícita | Win | Loss | Win Rate observado |')
    out.append('|---|---|---|---|---|')
    for lvl, prob, w, l, wr in cal_rows:
        out.append(f'| {lvl} | {prob:.0%} | {w} | {l} | {fmt_wr(wr)} |')
    out.append('')
    if brier is not None:
        out.append(f'**Brier score** ({brier_n} trades fechados com confiança): **{brier:.3f}**')
    else:
        out.append('**Brier score:** — (sem dados suficientes)')
    out.append('')

    # Quebras
    out.append('## Segmentação')
    out.append('')
    out += render_group('Por Lado', 'Lado', group_table(records, lambda r: r['side'], 'Lado'))
    out += render_group('Por Tipo', 'Tipo', group_table(records, lambda r: r['type'], 'Tipo'))
    out += render_group('Por Regime Macro', 'Regime', group_table(records, lambda r: r['regime'], 'Regime'))
    out += render_group('Por Playbook', 'Playbook', group_table(records, lambda r: r['playbook'], 'Playbook'))
    out += render_group('Por Setup', 'Setup', group_table(records, lambda r: r['setup'], 'Setup'))
    out += render_group('Dia Útil vs Fim de Semana', 'Período',
                        group_table(records, lambda r: 'fim de semana' if r['weekend'] else 'dia útil', 'Período'))

    # Leitura recomendada
    out.append('## Leitura Automática')
    out.append('')
    insights = []
    # melhor/pior lado
    side_rows = [(k, wr) for k, w, l, o, e, wr in group_table(records, lambda r: r['side'], 'Lado') if wr is not None]
    if side_rows:
        best = max(side_rows, key=lambda x: x[1])
        worst = min(side_rows, key=lambda x: x[1])
        if best[0] != worst[0]:
            insights.append(f'- Melhor lado: **{best[0]}** ({fmt_wr(best[1])}) vs pior: **{worst[0]}** ({fmt_wr(worst[1])}).')
    # calibração invertida?
    wr_by_level = {lvl: wr for lvl, prob, w, l, wr in cal_rows if wr is not None}
    if 'alta' in wr_by_level and 'média' in wr_by_level and wr_by_level['alta'] < wr_by_level['média']:
        insights.append('- ⚠️ Confiança DESCALIBRADA: "alta" está acertando MENOS que "média". Revisar critérios de confiança.')
    if cb_active:
        insights.append('- 🔴 Circuit breaker ativo — reduzir tamanho/parar até resetar a série.')
    if not insights:
        insights.append('- Sem alertas automáticos. Continuar coletando amostras (win rate estabiliza com ≥20 trades fechados por grupo).')
    out += insights
    out.append('')

    return '\n'.join(out) + '\n', {
        'total': total, 'wins': wins, 'losses': losses,
        'wr_global': wr_global, 'rr_real': rr_real,
    }


def update_setups_index(summary):
    """Atualiza o bloco 'Métricas Globais' de setups/index.md de forma segura."""
    if not os.path.exists(SETUPS_INDEX):
        return False
    with open(SETUPS_INDEX, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    wr = fmt_wr(summary['wr_global'])
    rr = '—' if summary['rr_real'] is None else f"{summary['rr_real']:.2f}"
    closed = summary['wins'] + summary['losses']

    repl = {
        r'(- \*\*Total de trades rastreados:\*\* ).*': r'\g<1>' + str(closed) + '  <!-- previsões fechadas -->',
        r'(- \*\*Win Rate global:\*\* ).*': r'\g<1>' + wr,
        r'(- \*\*R:R Médio global:\*\* ).*': r'\g<1>' + rr,
    }
    for pat, sub in repl.items():
        content = re.sub(pat, sub, content)

    if content != original:
        with open(SETUPS_INDEX, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    records = parse_predictions()
    report, summary = build_report(records)
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    setups_updated = update_setups_index(summary)

    print('Métricas geradas:', os.path.relpath(OUT_FILE, BASE_DIR))
    print(f'  Previsões parseadas: {summary["total"]}')
    print(f'  Fechadas: {summary["wins"] + summary["losses"]} (W {summary["wins"]} / L {summary["losses"]})')
    print(f'  Win Rate global: {fmt_wr(summary["wr_global"])}')
    print(f'  setups/index.md atualizado: {"sim" if setups_updated else "não"}')


if __name__ == '__main__':
    main()
