---
name: btc-cycle
description: Análise de ciclo do Bitcoin — onde estamos no ciclo, projeção de topo/fundo, score de capitulação/euforia. Use quando o usuário pede "análise de ciclo", "onde estamos no ciclo", "projeção de fundo/topo", ou quando o macro scan indica transição de fase. Combina price action W/M, 200W SMA, indicadores on-chain (MVRV/NUPL/Puell/Pi Cycle/Hash Ribbons) e Fibonacci log.
---

# CYCLE — Análise de Ciclo do BTC

Ref: [[btc-cycle-analysis]]

1. **[BRAIN READ]** Rodar `brain-read` + ler `wiki/concepts/btc-cycle-analysis.md`.
2. **[MACRO SCAN]** Rodar `macro-scan` Workflow A completo (10 passos).
3. **[PRICE ACTION W/M]**
   a. `BTCUSD` → TF `W` → `data_get_study_values` → `capture_screenshot`.
   b. TF `M` → `data_get_ohlcv({summary:true})` → `capture_screenshot`.
   c. RSI semanal (divergências), MACD semanal (cruzamento vs zero), volume (climático?).
4. **[200W SMA]** Preço vs 200W SMA — se NÃO tocou → fundo provavelmente NÃO ocorreu.
5. **[ON-CHAIN]** (se instalados no chart): MVRV Z >7 topo / <0 fundo · NUPL >0.75 euforia / <0
   capitulação · Puell >4 topo / <0.5 fundo · Pi Cycle Top (111DMA vs 350DMA×2) · Hash Ribbons ·
   Realized Price (acima/abaixo). _MVRV foi removido do layout "EMA Cross" — adicionar ad-hoc via
   `chart_manage_indicator` se preciso._
6. **[FIBONACCI LOG]** Fib do low do ciclo anterior ao ATH (escala log).
7. **[SCORING]** Score de Topo [X/10] + Score de Fundo [X/15].
8. **[PROJEÇÃO]** Se bear confirmado → zona de fundo com 6 métodos: Fractal drawdown · 200W SMA ·
   Realized Price · Fibonacci log · Temporal · Confluência técnica. Zona onde 3+ convergem.
9. **[OUTPUT]** Diagnóstico: Fase atual | Scores | Indicadores | Projeção | Estratégia de acumulação.
10. **[BRAIN WRITE]** Registrar `wiki/sessions/YYYY-MM-DD-BTC-CYCLE.md` + previsão em
    `predictions-log.md` + append `wiki/log.md` (`cycle | BTC | Fase: [X]`).
