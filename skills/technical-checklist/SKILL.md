---
name: technical-checklist
description: Checklist de análise técnica obrigatória (Fases 1-9) — MTF top-down (M→15m), Smart Money Concepts, Wyckoff, Fibonacci+Price Action, Indicadores dirigidos pelo layout ativo (RSI/StochRSI/MACD/ADX/EMA/Volume com divergências), Playbook match, Liquidez+USDT.D+Longs/Shorts, e Declaração de Bias com Confluence Score. Use depois do macro-scan, ao analisar qualquer ativo. Pular frameworks é PROIBIDO (declarar N/A com justificativa).
---

# Checklist Técnico Obrigatório (Fases 1-9)

> Ler os conceitos da wiki e aplicar cada framework. Pular é PROIBIDO; se não se aplica, declarar
> "N/A" com justificativa. Detalhe de score em `skills/_references/confluence-score.md`.
>
> **Lente obrigatória — 4 Pilares + Fluxo Institucional** ([[institutional-flow-poi]]): toda análise
> cruza Estrutura (Fases 2-3), Ciclos (Fase 4/macro), Volume (Fase 6) e Contexto Macro (`macro-scan`),
> mapeia **POIs** (zonas de demanda institucional) e observa os **gatilhos de reversão** (CHoCH,
> sobrevenda Diário/Semanal, perda de LTA). Toda ação de exposição é ancorada à disciplina.

## Fase 1 — Leitura de Contexto
Já coberto por `brain-read` (insights, mistakes, indicators, patterns, asset). Referenciar a
sessão anterior do mesmo ativo → declarar o que mudou estruturalmente.

## Fase 2 — Multi-Timeframe (top-down obrigatório) — Ref: [[multi-timeframe-analysis]]
Ordem: **M → W → D → 4H → 1H → 15M**. O M é o âncora de ciclo — limita upside/downside de TODOS.
1. **Mensal (M):** tendência de ciclo (HH/HL ou LH/LL), RSI/MACD mensal vs zero, EMA macro.
   Define teto/piso de ciclo + alvos mensais. **Obrigatório no macro; recomendado em scalp.**
2. **Semanal (W):** regime (Bull/Bear), RSI/MACD semanal, EMA 200.
3. **Diário:** ciclo secundário, sobrecompra/venda estrutural.
4. **4H:** filtro direcional (EMA 200: above→Long only / below→Short only), ADX, estrutura.
5. **1H:** zona de entrada, FVG, OB, divergências RSI.
6. **15M/5M:** gatilho de execução, BOS de confirmação.

## Fase 3 — Smart Money Concepts — Ref: [[SMC]]
1. Estrutura: **BOS** (continuação) ou **CHoCH** (reversão) no 4H e 1H.
2. **FVG** (gaps de liquidez não preenchidos).
3. **Order Blocks** (último candle antes de impulso = zona institucional).
4. Liquidez: EQH/EQL, PDH/PDL, BSL/SSL.
5. Traps: Bull/Bear Trap, BSL Grab, Stop Hunt.
6. Confluência: FVG + OB + Fib Golden Zone = máxima convicção (= **POI**, ver [[institutional-flow-poi]]).
7. **CHoCH = gatilho de reversão** (fim da acumulação/distribuição do Smart Money): confirmar no TF
   relevante + volume; usar para mudar bias ou manter posição.

## Fase 4 — Wyckoff — Ref: [[Wyckoff]]
1. Fase: Acumulação / Markup / Distribuição / Markdown.
2. Eventos: Spring (false break down) ou UT/UTAD (false break up).
3. Esforço × Resultado: alto volume + resultado pequeno = absorção.
4. Cruzar com SMC: Spring = EQL sweep + CHoCH bull | UT = EQH sweep + CHoCH bear.
5. **Acumulação cíclica** (transferência de riqueza): se em fase de Acumulação/Markdown tardio,
   mapear os **POIs** abaixo (primário + secundários) para entradas escalonadas — ver [[institutional-flow-poi]].

## Fase 5 — Fibonacci + Price Action — Ref: [[fibonacci-structural]] + [[price-action-patterns]]
1. Fib do último impulso relevante.
2. **Golden Zone** (0.618–0.786) = zona de entrada prioritária.
3. Confluência: Golden Zone + FVG + OB = entrada sniper.
4. Candles: Engulfing, Pin Bar, Doji em zonas de confluência.

## Fase 6 — Indicadores (DIRIGIDA PELO LAYOUT ATIVO)
> Aplicar cada sub-item só se o indicador estiver no layout; ausente → `N/A — fora do layout`.
> Custom (V.V.I.R., MVRV Z, SMC LuxAlgo, Tabela RSI Maciel) têm leitura própria em [[layouts]]/[[indicators]].
> **M e W em RSI/StochRSI/MACD são OBRIGATÓRIOS no macro**; M tem peso de ciclo acima do W.

1. **RSI (14):** valor + zona (>70 OB / <30 OS) + direção + cruzamento RSI×SMA(RSI).
   - **M:** define teto/piso de momentum do CICLO; divergência mensal = reversão de ciclo (peso máximo).
   - **W:** limita upside/downside dos TFs menores; **divergência semanal = detector PRIMORDIAL de
     topo/fundo** — varrer a div do 1W antes dos TFs menores.
   - **Divergências M/W/D/4H/1H/15M (OBRIGATÓRIO se RSI no layout):** bearish preço HH+RSI LH |
     bullish preço LL+RSI HL. 1W/1M = topo/fundo de CICLO; D/4H = swing; 1H/15M = gatilho.
     ⚠️ Divergência sozinha NÃO é gatilho — confirmar com cruzamento RSI×SMA, CHoCH/BOS ou candle.
   - **USDT.D (BTC/ETH — OBRIGATÓRIO):** USDT.D INVERSO ao BTC. Varrer div de RSI no USDT.D (W/D/4H/
     1H/15M, **1W primordial**). USDT.D bullish → BTC **baixista**; USDT.D bearish → BTC **altista**.
     Div cruzada **BTC↔USDT.D** (BTC HH sem USDT.D fazer LL / fazendo HL = topo do BTC). Ref:
     [[liquidity-wicks-trap-short-usdtd]].
   - **Sobrevenda como GATILHO de entrada** ([[institutional-flow-poi]]): **RSI 1W em OS = ótimo ponto
     de aporte/long (quase sempre)**; **RSI 1D em OS = exaustão vendedora → gatilho de aumento
     ESCALONADO de exposição**. ⚠️ Sempre confirmar com confluência (POI, divergência, CHoCH) e
     respeitar SL/circuit breaker — gatilho de alta probabilidade ≠ ignorar risco.
2. **Stoch RSI:** %K/%D + cruzamento + zona (>80 OB / <20 OS) + direção.
   - **W (OBRIGATÓRIO):** reset semanal de OS/OB = virada de ciclo.
   - **Divergências (1H/15M):** preço HH+%K LH em >80 = bearish | preço LL+%K HL em <20 = bullish.
   - ⚠️ **RSI+StochRSI combinado** ([[rsi-stochrsi-combined]]): RSI (M/W/D/4H) define DIREÇÃO
     (>50 Long only / <50 Short only); StochRSI (1H/15M) define TIMING. **NUNCA StochRSI contra o RSI HTF.**
3. **MACD (12/26/9):** posição vs zero + cruzamento×Signal + histograma.
   - M: cruzamento mensal vs zero = virada de regime de CICLO. W: idem de momentum.
   - Divergências M/W/D/4H: preço HH+MACD LH=bearish | preço LL+MACD HL=bullish. Cross sem volume = fraco.
4. **ADX (14):** >25 tendência forte | <20 range. DI+>DI- bull / DI->DI+ bear.
5. **EMA 50/200:** posição+cruzamento (Golden/Death Cross)+inclinação. 200W SMA = piso de ciclo.
6. **Volume/OBV:** POC magneto, HVN S/R. Div Vol×Preço: preço↑+vol↓=rally fraco. OBV: preço HH+OBV
   LH=distribuição | preço LL+OBV HL=acumulação.

## Fase 7 — Playbook Match — Ref: [[trade-playbooks]]
1. Encaixa em algum dos 4 playbooks? **P1** Long retração de alta · **P2** Short repique de baixa ·
   **P3** Stop Hunt Reversal · **P4** Squeeze de Alavancagem.
2. Checklist de entrada (8 critérios, mínimo 6).
3. Nenhum → "Nenhum setup identificado".

## Fase 8 — Liquidez, Correlações e Posicionamento de Margem
Ref: [[liquidity-wicks-trap-short-usdtd]] + [[btc-macro-correlations]] + [[btcusdlongs-btcusdshorts]]
1. Mapear pavios HTF (M/W/D) → liquidez acima ou abaixo. Pavios + OB/FVG = **POIs** institucionais
   (absorção/book). **Perda de LTA = capitulação final** = POI de máxima convicção (só com
   confluência) — ver [[institutional-flow-poi]].
2. **USDT.D — confirmador inverso + divergência (OBRIGATÓRIO BTC/ETH):** (a) confirma/nega o bias;
   (b) varrer div de RSI no USDT.D (W/D/4H/1H/15M, 1W primordial); (c) div cruzada BTC↔USDT.D.
3. **Funding Rate + OI + Fear&Greed:** ler `raw/feeds/latest.md` (valores REAIS de BTC/ETH — não
   estimar). Refresh falhou → penalidade `dados-parciais`.
4. **BTCUSDLONGS + BTCUSDSHORTS (obrigatório BTC/ETH):** valor/tendência/nível de cada, Ratio L/S,
   risco de squeeze (Long Squeeze ratio>5+longs extremo / Short Squeeze ratio<1+shorts subindo).
   Cruzar com Funding/OI.
5. Declarar: `Liquidez: … | USDT.D: confirma/nega | Div RSI USDT.D: [TF:tipo ou —] | BTC↔USDT.D:
   alinhado/divergente | Longs/Shorts: [ratio] [squeeze risk]`.

## Fase 9 — Declaração de Bias Final
Ver `skills/_references/confluence-score.md`: bias LONG/SHORT/NEUTRO, **Confluence Score (0–10)**,
confiança derivada (≥8 alta / 6–7 média / 4–5 baixa / <4 NEUTRO), penalidades (`contra-macro −2`,
`usdtd-diverge −1`, `dados-parciais −1`), disciplina (circuit breaker 🔴 → observação).
> **Pesos dirigidos por dados:** aplicar a calibração empírica do Cartão de Calibração (Hit Rate por
> critério em `indicators.md` + Win Rate do setup) — `sinal-fraco` não pontua, `setup-fraco` trava a
> confiança. Ao declarar o score, **emitir os critérios que pontuaram como slugs de
> `skills/_references/criteria-keys.md`** (ex.: `ema200+, macd+, rsi+, smc-ob+, macro+ | -adx`) — o
> `brain-write` copia essa lista para o campo `Critérios:` da previsão (alimenta a calibração futura).
> Gatilhos institucionais confirmados (CHoCH + Sobrevenda Semanal + POI alinhado) **reforçam** o
> Confluence Score pelos critérios que já existem — **não** criam score paralelo e **nunca** burlam
> a disciplina ([[institutional-flow-poi]]).

> Análise concluída → chamar `brain-write` para registrar insight/previsão/sessão.
