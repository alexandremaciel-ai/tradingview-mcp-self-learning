---
type: prediction
symbol: {SYMBOL}
tf: {TF}
date: {YYYY-MM-DD}
time: "{HH:MM}"
side: {long|short|spot}
kind: {scalp|swing|holder}
setup: {slug-do-setup|null}
playbook: {1|2|3|4|null}
confluence: {N}
confidence: {alta|média-alta|média|baixa}
regime: {risk-on|risk-off|misto}
price: {preço na análise}
entry: {zona de entrada}
sl: {stop}
tps: [{tp1}, {tp2}, {tp3}]
rr_plan: {X.X}
rr_real: null
criteria: ["ema200+", "macd+", "rsi+", "-stochrsi"]
status: open
postclose: null
superseded: false
tags: [side/{long}, regime/{misto}, setup/{slug}]
---

# {SYMBOL} {TF} — {BIAS} · {YYYY-MM-DD HH:MM BRT}

> Nota atômica de previsão (fonte: brain-write). O **frontmatter acima é a fonte única**
> parseável (Dataview/Bases/`metrics_engine.py`) — não repetir os campos como prosa.
> Grading (✅/❌/⚪) é feito pela skill `prediction-feedback` editando `status`/`rr_real`/`postclose`.

## Contexto
_(1-2 linhas de macro/estrutura)_

## Tese
_(o racional do trade)_

## Invalidação
_(condição que mata a tese)_

## Resultado
_(preenchido no feedback — o que o mercado fez, TP/SL cravados)_

## Lição
_(preenchida no feedback)_

## Backlinks
- [[{SYMBOL}]] · [[predictions-log]] · sessão [[{YYYY-MM-DD-SYMBOL-TF}]]
- setup [[{slug-do-setup}]] · [[criteria-keys]] · [[confluence-score]]
