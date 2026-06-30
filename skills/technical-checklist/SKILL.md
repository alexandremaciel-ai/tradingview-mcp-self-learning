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

> **Filtro Sequencial (4 camadas — gate rígido, ordem obrigatória):** falhou a camada → **NÃO avança**.
> 1. **Regime** [Fase 6.4 ADX + volatilidade]: tendência vs range. Sem classificar, não avança.
> 2. **Tendência** [Fase 2 HTF — 1W/1D/4H + EMA200].
> 3. **Momentum/Zona** [Fases 3–6: divergências MTF (peso + quórum ≥2-de-3) + zona SMC (OB/FVG/liq)].
> 4. **Gatilho de price action** [Fase 2 LTF: BOS/CHoCH/candle de confirmação].

## Fase 1 — Leitura de Contexto
Já coberto por `brain-read` (insights, mistakes, indicators, patterns, asset). Referenciar a
sessão anterior do mesmo ativo → declarar o que mudou estruturalmente.
> **Anti-alucinação (Invariante 0):** todo nível citado (S/R, OB, FVG, invalidação) carrega o **TF
> de origem** (ex.: `EQL $60,755 [4H]`). Dado não puxado da fonte real → **`DADO_INDISPONIVEL`**
> (não estimar). Fontes em conflito → reportar ambas + **`CONFLITO_DE_DADOS`**, sem forçar conclusão.

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
1. Estrutura: **BOS** (continuação) ou **CHoCH** (reversão) no 4H e 1H. **Regra de Estrutura: só é topo
   se perder fundo** — máxima não é topo até perder o último fundo relevante (CHoCH); simétrico p/ fundos.
   SMC sozinho ≈ 50% → **validar a quebra prioritariamente em D/M** (define as regiões exatas de compra/venda).
2. **FVG** (gaps de liquidez não preenchidos).
3. **Order Blocks** (último candle antes de impulso = zona institucional).
4. Liquidez: EQH/EQL, PDH/PDL, BSL/SSL.
5. Traps: Bull/Bear Trap, BSL Grab, Stop Hunt, **Inducement** (aparenta topo/fundo sem perder a estrutura
   oposta = isca de liquidez; exigir CHoCH + perda de fundo antes de tratar como reversão).
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

> 🔴 **FONTE DA DIVERGÊNCIA (obrigatório — Invariante 0).** A divergência é um **sinal computado e
> plotado pelo indicador** (V.V.I.R. / MACD Divergences Pro / Stoch RSI Div Pro), NÃO algo a inferir de
> price action. `data_get_study_values` dá só o **valor atual** do RSI/MACD — **não** mostra divergência;
> afirmar presença/ausência a partir dele é alucinação.
> ⚠️ **FATO CONFIRMADO (28/06):** nesses 3 indicadores os marcadores **Bull/Bear são `plotshape()`** —
> que **NÃO** é study-value, **NÃO** é `label.new` (`data_get_pine_labels` só devolve as projeções
> RSI78/RSI30, K90/K10), **NÃO** é `line.new`. `data_get_pine_lines(study_filter="RSI Div")` devolve as
> **~5.400 linhas do filtro MTF** (ruído, NÃO a divergência). **Nenhuma tool de dados da API lê plotshape**
> — a única fonte é o **pixel do painel**. Ordem real:
> 1. **Decisiva** (a divergência pesaria no bias/Confluence, ou o usuário pediu) → **`capture_screenshot`
>    region=`full`** e ler os marcadores Bull/Bear/Oculta no painel V.V.I.R./StochRSI/MACD.
>    ⚠️ region=`chart` **CORTA** o sub-painel do oscilador — tem que ser **`full`**. Ler o marcador no
>    candle **atual** (à direita); marcadores à esquerda = históricos.
> 2. **Não-decisiva** → registrar a leitura rápida do painel (ou pular o eixo) sem screenshot; não custa.
> 3. Sem chart/screenshot disponível (TV offline) → **`DADO_INDISPONIVEL`**. **Proibido** escrever
>    "sem divergência" por inferência de price action. (Erro de referência: CYCLE 28/06 — ver [[mistakes]].)

1. **RSI (14):** valor + zona (>70 OB / <30 OS) + direção + cruzamento RSI×SMA(RSI).
   - **M:** define teto/piso de momentum do CICLO; divergência mensal = reversão de ciclo (peso máximo).
   - **W:** limita upside/downside dos TFs menores; **divergência semanal = detector PRIMORDIAL de
     topo/fundo** — varrer a div do 1W antes dos TFs menores.
   - **Divergências MTF (OBRIGATÓRIO se RSI no layout) — varrer HTF→LTF `1M→2W→1W→1D→4H→1H→15m→5m`:**
     **ler a marca do V.V.I.R. da fonte (callout 🔴 acima), não inferir.** bearish preço HH+RSI LH |
     bullish preço LL+RSI HL (= o que o indicador já computou). **Separar Regular (reversão) de Oculta
     (continuação) — sinais OPOSTOS.** Aplicar a **tabela de pesos por TF** (FORTE = ≥2 TFs mesmo
     lado, soma ≥6 · FRACO = só LTF <3 · `DIV_CONTRA_HTF` = LTF contra HTF → não opera) e o
     **quórum de confirmação ≥2-de-3** (volume/Smart Volume+VRVP · zona SMC · price action LTF).
     Detalhe em [[rsi-divergences]] §6.5. O sub-score de força alimenta o critério `divergencia`.
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
4. **ADX (14) — força + direção ([[ADX]]; layout EMA Cross e MVRV):** linha **ADX** (branca)=força da
   tendência · **DI+** (verde)=compradores · **DI−** (vermelha)=vendedores. ADX só mede FORÇA, nunca direção.
   - **Cruzamento direcional (início de tendência):** DI+ cruza acima de DI− = potencial compra; DI− acima
     de DI+ = potencial venda. Cruzamento = **1º alerta** — confirmar com BOS/CHoCH (Fase 3), não operar isolado.
   - **Confirmação de entrada:** só abrir NOVA posição de tendência com **ADX subindo E > 25** (tendência
     forte real); ADX cruzando 25 a favor = início de perna. ADX caindo de >40 = tendência exaurindo.
   - **Range (ADX < 20):** tendência perdeu força → trend-following falha (Playbooks 1/2 desabilitados,
     ver Fase 7) → favorecer operações em faixa / P3 nas extremidades. Num flush, esperar ADX cruzar >25
     antes de tratar como trend (senão `flush≠trend`/`-adx`, ver [[indicators]]).
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
   (absorção/book). Clusters de absorção = **zona de defesa de preço médio** (acumulação vs redistribuição;
   romper a zona com volume = inversão provável da tendência primária). **Perda de LTA = capitulação final**
   = POI de máxima convicção (só com confluência) — ver [[institutional-flow-poi]].
2. **USDT.D — confirmador inverso + divergência (OBRIGATÓRIO BTC/ETH):** (a) confirma/nega o bias;
   (b) varrer div de RSI no USDT.D (W/D/4H/1H/15M, 1W primordial); (c) div cruzada BTC↔USDT.D.
3. **Funding Rate + OI + Fear&Greed:** ler `raw/feeds/latest.md` (valores REAIS de BTC/ETH — não
   estimar). Refresh falhou → penalidade `dados-parciais`.
4. **BTCUSDLONGS + BTCUSDSHORTS (obrigatório BTC/ETH):** valor/tendência/nível de cada, Ratio L/S,
   risco de squeeze (Long Squeeze ratio>5+longs extremo / Short Squeeze ratio<1+shorts subindo).
   Cruzar com Funding/OI.
5. Declarar: `Liquidez: … | USDT.D: confirma/nega | Div RSI USDT.D: [TF:tipo ou —] | BTC↔USDT.D:
   alinhado/divergente | Longs/Shorts: [ratio] [squeeze risk]`.
6. **Rotação de liquidez (consumir, não re-derivar):** ler o **Veredito de Rotação de Liquidez** do
   `macro-scan` Step 1.5 ([[liquidity-rotation-cycle]]) e declarar `Rotação liq: [fase] | BTC.D [dir]
   | TOTAL2ES/3ES [dir] | Veredito: [Otimizado/Neutro/Bull-Trap]` (EQUITIES → `N/A`). Veredito
   `Alto Risco de Bull Trap` ⇒ a Fase 9 aplica `bull-trap-liquidez`.

## Fase 9 — Declaração de Bias Final
**Declaração obrigatória do setup (4 campos — sem o `nivel_invalidacao` o setup é INVÁLIDO → NEUTRO):**
`vies_HTF` (1W/1D) · `estrutura_4H` (BULLISH/BEARISH/RANGE via HH-HL/LH-LL + ADX) ·
`nivel_invalidacao` (preço EXATO que mata a tese, com TF) · `gatilho_LTF` (BOS/CHoCH/candle).

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
> **Rotação de liquidez:** o Veredito do `macro-scan` Step 1.5 entra no score pelo critério
> `liq-rotacao` (penalidade `bull-trap-liquidez` quando o índice ES/rota contradiz o bias) — é um
> **input ao Confluence Score**, não um veredito paralelo ([[liquidity-rotation-cycle]]).

> Análise concluída → chamar `brain-write` para registrar insight/previsão/sessão.
