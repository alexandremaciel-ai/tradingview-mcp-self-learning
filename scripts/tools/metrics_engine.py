#!/usr/bin/env python3
"""
metrics_engine.py — Motor de métricas e calibração do brain.

Lê wiki/brain/predictions-log.md (formato novo com campos parseáveis E o
formato legado em texto livre) e calcula métricas objetivas de edge:

  - Win rate global e por: lado (long/short/spot), tipo (scalp/swing/holder),
    setup, playbook, regime macro (risk-on/off/misto), dia útil vs fim de semana.
  - Calibração de confiança: win rate observado por nível + Brier score.
  - Calibração por critério: Hit Rate de cada sinal listado no campo `Critérios:`
    (slugs de skills/_references/criteria-keys.md) — alimenta os pesos data-driven
    do Confluence Score.
  - Drawdown: maior sequência de losses; streak atual → flag de circuit breaker.
  - R:R planejado vs realizado.

Escreve o resultado em wiki/brain/metrics.md (consumido pela LLM e pelo Obsidian
Dataview), reescreve os campos de performance de wiki/brain/indicators.md (Sessões/
Acertos/Falhas/Hit Rate) e atualiza o bloco "Métricas Globais" de wiki/setups/index.md.

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

INDICATORS_FILE = os.path.join(BASE_DIR, 'wiki', 'brain', 'indicators.md')

# Slugs de critério (campo `Critérios:`) -> cabeçalho da seção em indicators.md.
# Mantém 1:1 com skills/_references/criteria-keys.md. Slugs de contexto (macro, usdtd,
# dxy, funding, liquidez, fib-golden, wyckoff, estrutura, poi) NÃO têm seção própria —
# aparecem só na tabela "Calibração por Critério" de metrics.md (sem writeback).
SLUG_TO_HEADER = {
    'ema200': 'EMA 50/200',
    'ema-cross': 'EMA Cross (ribbon)',
    'sma-cross': 'SMA Cross',
    'rsi': 'RSI',
    'stochrsi': 'RSI Estocástico (Stoch RSI)',
    'macd': 'MACD',
    'adx': 'ADX',
    'atr': 'ATR',
    'bollinger': 'Bollinger Awesome Alert R1.1 (JustUncleL)',
    'supertrend': 'Supertrend',
    'smc-choch': 'CHoCH / BoS (SMC)',
    'smc-fvg': 'FVG (SMC)',
    'smc-ob': 'Smart Money Concepts [LuxAlgo]',
    'volume': 'Crypto Smart Volume PRO (v1/v2)',
    'vrvp': 'Visible Range Volume Profile',
    'whale': 'Whale Liquidity and Absorption Profile [AlgoAlpha]',
    'mvrv': 'MVRV Z Score & Free Float Z-Score',
    'divergencia': 'RSI Divergences Pro + Adaptive MTF Filter (V.V.I.R.)',
    'mxwll': 'Mxwll Suite',
}

# Linha de performance em indicators.md (preserva qualquer anotação após o Hit Rate).
PERF_RE = re.compile(
    r'(- \*\*Sessões de uso:\*\*\s*)([^|]*?)'
    r'(\s*\|\s*\*\*Acertos:\*\*\s*)([^|]*?)'
    r'(\s*\|\s*\*\*Falhas:\*\*\s*)([^|]*?)'
    r'(\s*\|\s*\*\*Hit Rate:\*\*\s*)(\S+)'
)


def parse_criteria(block):
    """Lê o campo `Critérios:` → lista de (slug, sinal '+'/'-').
    Aceita `slug+`, `slug-` e `-slug`. Separadores: vírgula e `|`."""
    val = field(block, 'Critérios')
    if not val:
        return []
    out = []
    for tok in re.split(r'[,\|]', val):
        t = tok.strip()
        if not t:
            continue
        sign = '+'
        if t.startswith('-'):
            sign = '-'
            t = t[1:].strip()
        elif t.endswith('-'):
            sign = '-'
            t = t[:-1].strip()
        elif t.endswith('+'):
            t = t[:-1].strip()
        slug = re.sub(r'[^a-z0-9\-]', '', t.lower())
        if slug:
            out.append((slug, sign))
    return out


def field(block, name):
    """Extrai o valor de um campo '- **Nome:** valor' (primeira ocorrência)."""
    m = re.search(r'- \*\*' + re.escape(name) + r':\*\*\s*(.+)', block)
    return m.group(1).strip() if m else None


def detect_status(block):
    """Detecta status pelo PRIMEIRO emoji (por posição) na linha '- **Status:**'.
    Posição, não precedência: um '⚪ expirada … TP1 ✅' lê ⚪, não ✅ — a narração
    pós-fecho costuma citar outros emojis. Retorna win/loss/open/expired/None."""
    m = re.search(r'- \*\*Status:\*\*\s*(.+)', block)
    if not m:
        return None
    emoji = {'✅': 'win', '❌': 'loss', '⏳': 'open', '⚪': 'expired'}
    for ch in m.group(1):
        if ch in emoji:
            return emoji[ch]
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


def infer_postclose(block):
    """Para previsões ⚪: direção do preço na expiração.
    'errada' = preço foi contra a tese → conta como loss no WR ajustado (anti-viés)."""
    val = field(block, 'Pós-fecho')
    if not val:
        return None
    t = val.lower()
    if 'errad' in t or 'contra' in t:
        return 'errada'
    if 'cert' in t or 'a favor' in t or 'acert' in t:
        return 'certa'
    if 'neutr' in t:
        return 'neutra'
    return None


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
            'postclose': infer_postclose(block),
            'weekend': d.weekday() >= 5,
            'criteria': parse_criteria(block),
        })
    return records


def criteria_stats(records):
    """Acerto/falha por slug de critério (só sinais '+'), a partir do resultado.
    win → acerto; loss ou ⚪-errada → falha; aberta/⚪-certa/neutra → ignora."""
    stats = {}
    for r in records:
        status = r['status']
        if status == 'win':
            credit = 'acerto'
        elif status == 'loss':
            credit = 'falha'
        elif status == 'expired' and r['postclose'] == 'errada':
            credit = 'falha'
        else:
            continue  # aberta, ⚪-certa, ⚪-neutra, ⚪ sem Pós-fecho
        for slug, sign in r['criteria']:
            if sign != '+':
                continue
            s = stats.setdefault(slug, {'acertos': 0, 'falhas': 0})
            s['acertos' if credit == 'acerto' else 'falhas'] += 1
    return stats


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
    exp_wrong = sum(1 for r in records if r['status'] == 'expired' and r['postclose'] == 'errada')
    exp_graded = sum(1 for r in records if r['status'] == 'expired' and r['postclose'] is not None)
    wr_global = winrate(wins, losses)  # estrito: só ✅/❌
    # ajustado: expiradas direcionalmente erradas contam como loss (combate o viés de seleção)
    adj_den = wins + losses + exp_wrong
    wr_adjusted = (wins / adj_den * 100.0) if adj_den else None
    nontrigger = (exp / total * 100.0) if total else None

    cal_rows, brier, brier_n = calibration(records)
    crit = criteria_stats(records)
    max_streak, cur_streak = max_loss_streak(records)
    rr_plan = avg([r['rr_plan'] for r in records])
    rr_real = avg([r['rr_real'] for r in records])

    cb_active = cur_streak >= 3

    out = []
    out.append('# Brain — Métricas e Calibração')
    out.append('')
    out.append(f'> Gerado por `scripts/tools/metrics_engine.py` em {now.strftime("%Y-%m-%d %H:%M")}.')
    out.append('> **WR estrito** = só ✅/❌. **WR ajustado** = também conta as ⚪ que foram direcionalmente erradas como loss — combate o viés de marcar perdas como "expiradas". A diferença entre os dois mede o quanto o número estrito está inflado. Abertas (⏳) ficam de fora dos dois.')
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
    out.append(f'| ⚪ já graduadas (Pós-fecho) | {exp_graded} |')
    out.append(f'| ⚪ direcionalmente erradas | {exp_wrong} |')
    out.append(f'| **Win Rate AJUSTADO** (número principal — ⚪-erradas = loss) | **{fmt_wr(wr_adjusted)}** |')
    out.append(f'| Win Rate estrito (só ✅/❌, otimista) | {fmt_wr(wr_global)} |')
    out.append(f'| Taxa de não-acionamento (⚪/total) | {fmt_wr(nontrigger)} |')
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

    # Calibração por critério (pesos data-driven do Confluence Score)
    out.append('## Calibração por Critério')
    out.append('')
    out.append('> Hit Rate de cada sinal `+` listado no campo `Critérios:` das previsões fechadas.')
    out.append('> O `Confluence Score` pesa cada critério por isto (guarda: N < 8 = peso atual; '
               '< 40% & N ≥ 8 = não pontua / `sinal-fraco`). Ver `[[confluence-score]]` / `[[criteria-keys]]`.')
    out.append('')
    out.append('| Critério | Acertos | Falhas | N | Hit Rate | Peso (data-driven) |')
    out.append('|---|---|---|---|---|---|')
    for slug in sorted(crit, key=lambda k: (-(crit[k]['acertos'] + crit[k]['falhas']), k)):
        a = crit[slug]['acertos']
        f = crit[slug]['falhas']
        n = a + f
        hr = (a / n * 100.0) if n else None
        if n < 8:
            peso = 'amostra baixa (peso atual)'
        elif hr < 40:
            peso = '⚠️ sinal-fraco → NÃO pontua'
        elif hr < 55:
            peso = 'meio-peso'
        elif hr <= 70:
            peso = 'peso cheio'
        else:
            peso = 'cheio + bônus'
        out.append(f'| {slug} | {a} | {f} | {n} | {fmt_wr(hr)} | {peso} |')
    if not crit:
        out.append('| _(sem `Critérios:` taggeados ainda)_ | — | — | 0 | — | coletar amostras |')
    out.append('')

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
    if nontrigger is not None and nontrigger >= 40:
        insights.append(f'- ⚠️ Não-acionamento alto ({fmt_wr(nontrigger)}): muitas previsões expiram sem virar trade — revisar timing/zonas de entrada.')
    if exp - exp_graded > 0:
        insights.append(f'- ⚪ {exp - exp_graded} expirada(s) ainda sem `Pós-fecho` — graduar a direção para o WR ajustado refletir a realidade.')
    if wr_adjusted is not None and wr_global is not None and (wr_global - wr_adjusted) >= 10:
        insights.append(f'- ⚠️ WR estrito ({fmt_wr(wr_global)}) está {wr_global - wr_adjusted:.0f}pp acima do ajustado ({fmt_wr(wr_adjusted)}) — viés: perdas viram "expiradas".')
    # critérios fracos (anti-sinal): N>=8 e hit rate <40%
    for slug in sorted(crit):
        a, f = crit[slug]['acertos'], crit[slug]['falhas']
        n = a + f
        if n >= 8 and (a / n * 100.0) < 40:
            insights.append(f'- ⚠️ `sinal-fraco:{slug}` ({a}/{n} = {a / n * 100:.0f}%) — não pontuar no Confluence Score; considerar inverter a leitura.')
    # setups fracos: N>=10 e win rate <50%
    for k, w, l, opn, exp, wr in group_table(records, lambda r: r['setup'], 'Setup'):
        if k != '—' and wr is not None and (w + l) >= 10 and wr < 50:
            insights.append(f'- ⚠️ `setup-fraco:{k}` (WR {fmt_wr(wr)}, n={w + l}) — travar confiança em "média" + −1.')
    if not insights:
        insights.append('- Sem alertas automáticos. Continuar coletando amostras (win rate estabiliza com ≥20 trades fechados por grupo).')
    out += insights
    out.append('')

    return '\n'.join(out) + '\n', {
        'total': total, 'wins': wins, 'losses': losses,
        'wr_global': wr_global, 'wr_adjusted': wr_adjusted,
        'nontrigger': nontrigger, 'rr_real': rr_real,
    }


def update_setups_index(summary):
    """Atualiza o bloco 'Métricas Globais' de setups/index.md de forma segura."""
    if not os.path.exists(SETUPS_INDEX):
        return False
    with open(SETUPS_INDEX, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # WR ajustado é o número principal (cai para o estrito se não houver ⚪ graduadas).
    wr = fmt_wr(summary['wr_adjusted'] if summary['wr_adjusted'] is not None else summary['wr_global'])
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


def update_indicators(records):
    """Reescreve Sessões/Acertos/Falhas/Hit Rate em indicators.md a partir dos `Critérios:`.
    Só toca seções cujo cabeçalho mapeia para um slug (SLUG_TO_HEADER); preserva anotações
    após o Hit Rate. Retorna a contagem de seções atualizadas."""
    if not os.path.exists(INDICATORS_FILE):
        return 0
    stats = criteria_stats(records)
    header_to_slug = {v: k for k, v in SLUG_TO_HEADER.items()}
    with open(INDICATORS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Quebra em [preâmbulo, '## Header', corpo, '## Header', corpo, ...]
    parts = re.split(r'(?m)^(## .+)$', content)
    rebuilt = [parts[0]]
    updated = 0
    for i in range(1, len(parts), 2):
        header_line = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''
        slug = header_to_slug.get(header_line[3:].strip())
        if slug and slug in stats:
            a = stats[slug]['acertos']
            fa = stats[slug]['falhas']
            n = a + fa
            hr = f'{a / n * 100:.0f}%' if n else '—'

            def repl(m):
                return (f'{m.group(1)}{n}{m.group(3)}{a}'
                        f'{m.group(5)}{fa}{m.group(7)}{hr}')

            new_body, count = PERF_RE.subn(repl, body, count=1)
            if count:
                body = new_body
                updated += 1
        rebuilt.append(header_line)
        rebuilt.append(body)
    content = ''.join(rebuilt)

    if content != original:
        with open(INDICATORS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
    return updated


def main():
    records = parse_predictions()
    report, summary = build_report(records)
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    setups_updated = update_setups_index(summary)
    indicators_updated = update_indicators(records)

    print('Métricas geradas:', os.path.relpath(OUT_FILE, BASE_DIR))
    print(f'  Previsões parseadas: {summary["total"]}')
    print(f'  Fechadas: {summary["wins"] + summary["losses"]} (W {summary["wins"]} / L {summary["losses"]})')
    print(f'  Win Rate estrito:  {fmt_wr(summary["wr_global"])}')
    print(f'  Win Rate ajustado: {fmt_wr(summary["wr_adjusted"])}')
    print(f'  Não-acionamento:   {fmt_wr(summary["nontrigger"])}')
    print(f'  setups/index.md atualizado: {"sim" if setups_updated else "não"}')
    print(f'  indicators.md — seções calibradas: {indicators_updated}')


if __name__ == '__main__':
    main()
