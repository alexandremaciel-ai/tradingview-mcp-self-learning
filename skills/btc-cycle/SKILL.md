---
name: btc-cycle
description: Análise de ciclo do Bitcoin — onde estamos no ciclo, projeção de topo/fundo, score de capitulação/euforia. Use quando o usuário pede "análise de ciclo", "onde estamos no ciclo", "projeção de fundo/topo", ou quando o macro scan indica transição de fase. Combina price action W/M, 200W SMA, indicadores on-chain (MVRV/NUPL/Puell/Pi Cycle/Hash Ribbons) e Fibonacci log.
---

# CYCLE — Análise de Ciclo do BTC

Ref: [[btc-cycle-analysis]] · [[institutional-flow-poi]] (acumulação cíclica, POIs, gatilhos de sobrevenda)

1. **[BRAIN READ]** Rodar `brain-read` + ler `wiki/concepts/btc-cycle-analysis.md`.
2. **[MACRO SCAN]** Rodar `macro-scan` Workflow A completo (10 passos). Target = BTC-solo → o
   **Step 1.5 usa só o classificador de Fase** (BTC.D/USDT.D; **não** forçar TOTAL2ES/3ES). A Fase é
   um *tell* de timing de ciclo ([[liquidity-rotation-cycle]]): **Migração para BTC** (BTC.D↑) = bear/
   recuperação inicial (capital foge das alts p/ BTC) · **Altseason** (BTC.D↓ + TOTAL3ES↑) = euforia
   tardia/distribuição · **Fuga Stablecoins** (USDT.D↑) = capitulação. Cruzar com o Score de Fundo/Topo.
3. **[PRICE ACTION HTF→W — top-down de ciclo 6M→3M→M→W]** Princípio: topos/fundos de ciclo
   **confirmam no FECHAMENTO** de 6M/3M/M; o bear histórico durou **~2 candles de 6M (≈12m)** — o bear é
   a correção do gráfico de 6M ([[btc-cycle-analysis]] §3.0). Candle de 6M/3M ainda **em formação**
   revertendo = sinal **preliminar**, não confirmado até fechar.
   a. **[HTF 6M/3M]** `BTCUSD` → tentar `chart_set_timeframe("6M")` e `("3M")`. Se o TF nativo não existir
      no setup → **agregar do Mensal** via `data_get_ohlcv({summary:true})` com `count` cobrindo ≥4 anos e
      declarar `fonte: agregado-do-mensal`. Avaliar: estrutura HH/HL vs LH/LL no 6M/3M, **candle de
      reversão no fechamento** (martelo/engolfo) e posição vs ATH.
   b. TF `W` → `data_get_study_values` → `capture_screenshot`.
   c. TF `M` → `data_get_ohlcv({summary:true})` → `capture_screenshot`.
   d. RSI semanal (divergências — **ler a marca da fonte**: `data_get_pine_lines(study_filter="RSI Div",
      verbose=true)`/screenshot do pane, nunca inferir; ver `technical-checklist` Fase 6 callout 🔴),
      MACD semanal (cruzamento vs zero), volume (climático?).
4. **[200W SMA]** Obter o valor REAL: `chart_manage_indicator(action:"add", name:"Moving Average")` no
   Semanal com `length=200` (`indicator_set_inputs`) → `data_get_study_values`. Preço vs 200W SMA — se NÃO
   tocou → fundo provavelmente NÃO ocorreu. ⚠️ Indisponível (não plotada) → rotular `200W-estimada
   (computada)` e NUNCA apresentar como nível lido do chart (Invariante 0).
5. **[ON-CHAIN]** Fonte primária = feed dedicado (não depende mais do chart). **Gate de frescor
   (~1×/dia, OBRIGATÓRIO):** se `raw/feeds/onchain-latest.md` ausente **ou** timestamp > 24h → rodar
   `python3 scripts/tools/fetch_onchain.py`; senão só ler o arquivo. ⚠️ O BGeometrics tem limite
   **8 req/h · 15/dia** — NÃO re-rodar no mesmo dia (o gate evita isso; re-run no mesmo hora → 429,
   que degrada para proxy/chart sem quebrar).
   - **Todas KEYLESS** (api.bitcoin-data.com `/v1/<slug>/last`, sem key): **NUPL** (>0.75 euforia /
     <0 capitulação) · **Puell** (>4 topo / <0.5 fundo) · **MVRV Z** (>7 topo / <0 fundo) ·
     **Realized Price** (preço<RP = capitulação) · **Reserve Risk**.
   - **Computadas (blockchain.com / preço):** **Pi Cycle Top** (111DMA vs 2×350DMA) · **Hash Ribbons**
     (MA30<MA60 = capitulação de mineradores; cruz↑ = compra histórica) · Puell proxy (fallback).
   - **MVRV Z primário = o FEED** (BGeometrics keyless). ⚠️ Nenhum layout plota MVRV desde 12/06 (removido
     do "EMA Cross e MVRV"; Emas é price-action puro — ver [[layouts]]). O chart só serve de confirmação
     cruzada **se** o MVRV for adicionado **ad-hoc** (`chart_manage_indicator`); não existindo, **não
     citar valor de chart** (seria estimativa).
   - `BGEO_API_KEY` (opcional, no `.env`) **não é necessária** — só eleva os limites do tier free.
     Métrica `indisponível`/`429` → **não pontua** (não estimar).
6. **[FIBONACCI LOG]** Fib do low do ciclo anterior ao ATH (escala log).
7. **[SCORING]** Score de Topo [X/10] + Score de Fundo [X/15]. Sobrevenda Semanal/Mensal e funding
   negativo extremo entram como critérios de fundo (gatilhos de acumulação — [[institutional-flow-poi]]).
8. **[PROJEÇÃO]** Se bear confirmado → zona de fundo com 6 métodos: Fractal drawdown · 200W SMA ·
   Realized Price · Fibonacci log · Temporal · Confluência técnica. Zona onde 3+ convergem.
9. **[OUTPUT]** Diagnóstico: Fase de ciclo | **Fase de liquidez** (BTC.D tell) | Scores | Indicadores | Projeção | Estratégia de acumulação.
   A estratégia mapeia **POIs** (primário = onde 3+ métodos convergem; secundários abaixo) para
   **compras escalonadas** ancoradas a [[position-sizing]] — não adivinhar o fundo absoluto.
10. **[BRAIN WRITE]** Registrar `wiki/sessions/YYYY-MM-DD-BTC-CYCLE.md` + previsão em
    `predictions-log.md` + append `wiki/log.md` (`cycle | BTC | Fase: [X]`).
