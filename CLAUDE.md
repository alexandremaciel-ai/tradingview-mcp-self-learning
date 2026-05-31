# TradingView MCP — Claude Instructions

68 tools for reading and controlling a live TradingView Desktop chart via CDP (port 9222).

---

## ⚡ AUTO-PILOT — Regra Obrigatória (leia PRIMEIRO)

**Se aplica a TODA interação. Não é opcional.**

### ANTES de responder qualquer pedido:
0. **🔌 Testar conexão:** `tv_health_check()` → se falhar → `tv_launch()` → 3 tentativas max
1. Ler `wiki/brain/insights.md` + `wiki/brain/mistakes.md` (últimos 10)
2. Se envolve ativo → ler `wiki/assets/{SYMBOL}.md`
3. Se envolve análise → ler `wiki/brain/predictions-log.md` → fechar previsões abertas

### Protocolo de Aplicação do Brain (executar junto com os passos 1-3):
- **mistakes.md:** Para cada um dos últimos 5 erros, perguntar: "Este cenário pode se repetir nesta análise?"
  → Se sim: declarar explicitamente "⚠️ Prevenção ativa: [erro X] → [ação preventiva]"
- **insights.md:** Identificar os 3 insights mais aplicáveis ao ativo/TF atual
  → Declarar: "💡 Aplicando: [insight X]"
- **patterns.md:** Verificar se algum padrão VALIDADO ou CONSOLIDADO está potencialmente ativo
  → Declarar: "🔄 Padrão monitorado: [nome] (N confirmações)"
- **predictions-log.md:** Se ativo tem previsão ⏳ aberta → FECHAR/ATUALIZAR antes de continuar
  → Se previsão > 48h sem atualização → marcar ⚪ expirada automaticamente

4. **⚠️ CLASSIFICAR O PEDIDO** na tabela abaixo → seguir o pipeline da classe:

| Classe | Quando | Macro Scan | Checklist | Extras |
|--------|--------|------------|-----------|--------|
| `BTC` | Análise solo de Bitcoin | **Completo** (10 passos) | Fases 1-9 completas | BTCUSDLONGS/SHORTS obrigatório |
| `BTC+ETH` | BTC e ETH juntos | Completo **1×** | BTC completo → ETH relativo (+ ETH/BTC pair) | Declarar ETH outperform/underperform |
| `ALTCOIN` | SOL, ADA, DOGE, etc. | **Reduzido**: USDT.D + BTC.D + TOTAL3 + BTC bias | Fases 1-6, 8-9. Wyckoff só se vol > $50M | Tag obrigatória: `scalp/swing/holder` |
| `EQUITIES` | AAPL, TSLA, SPX, ações | **TradFi**: DXY + SPX + VIX + setor (XLK/XLF) | Fases 1-6, 9. Sem USDT.D/Longs/Shorts | Checar earnings/eventos. Sem Funding Rate |
| `WATCHLIST` | "scan da lista", vários ativos | Completo **1×** no início | Compacto por ativo: quote + indicators + bias | Output: tabela resumo. 1 sessão total |
| `DAILY` | "daily", "morning scan" | Completo **1×** | Macro → BTC rápido (D+4H) → Watchlist → Previsões | Dashboard compacto |
| `CYCLE` | "ciclo do BTC", "topo/fundo" | Completo + on-chain | Ver operação #9 CYCLE | Score Topo/Fundo |

5. **Se análise técnica →** ler brain (indicators, patterns) + aplicar checklist da classe
6. **Se CYCLE →** ler `wiki/concepts/btc-cycle-analysis.md` + scoring

### DEPOIS de responder qualquer pedido:
1. **Sempre** — Insight → `brain/insights.md` + append `wiki/log.md`
2. **Se bias definido** — Previsão → `brain/predictions-log.md`
3. **Se indicador surpreendeu** — Atualizar `brain/indicators.md`
4. **Se padrão repetido** — Atualizar `brain/patterns.md`
5. **Se erro** — Append `brain/mistakes.md`
6. **Se indicador testado nesta sessão** → atualizar campos de performance (Sessões de uso / Acertos / Falhas) em `brain/indicators.md`
7. **Se padrão atingiu 2, 3 ou 4 confirmações** → promover Status: OBSERVAÇÃO → VALIDADO → CONSOLIDADO em `brain/patterns.md`
8. **Previsões > 48h sem atualização** → marcar ⚪ expirada automaticamente em `brain/predictions-log.md`

> Brain files inexistentes → copiar de `wiki/brain/_templates/`. Index/log → criar de `.initial.md`.

---

## Regras por Classe de Ativo

Ref: [[liquidity-wicks-trap-short-usdtd]] + [[btcusdlongs-btcusdshorts]]

### Classe BTC / BTC+ETH (crypto majors)
- Pavios HTF: mapear liquidez acima/abaixo (M/W/D). Declarar: `Liquidez por pavios: acima/abaixo/neutra`
- USDT.D: métrica inversa obrigatória. Declarar: `USDT.D: confirma/nega`
- BTCUSDLONGS/SHORTS: obrigatório. Declarar: `Ratio L/S: [X.X] | Squeeze Risk: alto/médio/baixo`
- Macro vence micro: não confiar em rompimento sem confirmação por fechamento + volume + USDT.D
- BTC+ETH: analisar BTC primeiro → ETH como relativo (ETH/BTC pair + força relativa)

### Classe ALTCOIN
- Macro reduzido: apenas USDT.D + BTC.D + TOTAL3 + bias BTC rápido
- Checar par ALTCOIN/BTC (força relativa). Se par caindo = altcoin underperformando
- Tag obrigatória: `scalp | swing | holder`. Altcoin em tendência de baixa = NÃO é holder
- Wyckoff: só aplicar se volume diário > $50M. Abaixo = estrutura manipulável
- Se BTC em risco macro → altcoins só como scalp/day trade

### Classe EQUITIES (ações, índices)
- Macro TradFi: DXY + SPX + VIX + ETF do setor (XLK, XLF, XLE, XLV)
- **NÃO usar:** USDT.D, TOTAL, BTCUSDLONGS/SHORTS, Funding Rate
- Checar: earnings iminentes (7 dias) → alertar risco de gap
- Horário: pré-market (05-10:30), regular (10:30-17:00), after-hours. Sinais em regular = mais confiáveis
- Playbook 4 (squeeze crypto) **não se aplica**. Usar: Playbooks 1-3 + cautela com gaps

### Classe WATCHLIST (scan de múltiplos ativos)
- Macro: rodar **1× completo** no início
- Cada ativo: pipeline compacto (quote + study_values + bias em 1 parágrafo)
- Output: tabela `Ativo | Preço | Bias | Confiança | Setup? | Nota`
- Destacar "Top 3 setups" com melhor confluência
- 1 sessão: `YYYY-MM-DD-WATCHLIST.md` (não 1 por ativo)

### Classe DAILY (overview diário)
- Macro: 1× completo
- BTC: análise rápida (D + 4H, não MTF completo de 5 TFs)
- Verificar previsões abertas → fechar expiradas (>48h)
- Se `wiki/watchlist.md` existir → scan compacto da lista
- Output: dashboard `Macro | BTC Bias | Alertas | Watchlist | Previsões`

---

## 📊 Análise Macro Obrigatória — Pré-Requisito para BTC/ETH

**ANTES de analisar BTC ou ETH, o agente DEVE executar um scan macro completo.**
Esta regra é obrigatória e não pode ser pulada. O macro contexto define o viés primário.

### Ativos do Scan Macro (ordem obrigatória)

| # | Ativo | Ticker TradingView | Por quê |
|---|-------|-------------------|--------|
| 1 | **USDT.D** | `USDT.D` | Métrica inversa direta de BTC. Queda = risk-on cripto. Alta = risk-off. |
| 2 | **S&P 500** | `SPX` (cash) ou `ES1!` (futuros, se mercado fechado) | Correlação positiva com BTC em ciclos risk-on. Divergência sinaliza regime shift. |
| 3 | **Ouro** | `GOLD` ou `XAUUSD` | Safe haven. Alta do ouro + alta BTC = liquidez abundante. Alta do ouro + queda BTC = flight to safety. |
| 4 | **DXY** | `DXY` | Dólar forte = pressão vendedora em BTC e commodities. Inversamente correlacionado. |
| 5 | **TOTAL** | `TOTAL` | Market cap total cripto. Tendência primária do setor. |
| 6 | **TOTAL2** | `TOTAL2` | Market cap excluindo BTC. Saúde das altcoins. |
| 7 | **TOTAL3** | `TOTAL3` | Market cap excluindo BTC e ETH. Apetite real por risco em altcoins menores. |
| 8 | **Petróleo** | `USOIL` ou `CL1!` | Proxy de inflação e custo energético. Alta persistente = hawkish = risco para BTC. |
| 9 | **BTC Longs** | `BTCUSDLONGS` | Posições long de margem na Bitfinex. Subindo = acumulação bullish. Extremo alto = risco de long squeeze. |
| 10 | **BTC Shorts** | `BTCUSDSHORTS` | Posições short de margem na Bitfinex. Subindo rápido = preparação para queda ou combustível para short squeeze. |

### Workflow do Scan Macro — Passos EXATOS

**⛔ DEVE executar `chart_set_symbol` para cada ativo. NÃO usar apenas `quote_get`.**

Para CADA ativo abaixo, executar na ordem: `chart_set_symbol` → `chart_set_timeframe("D")` → `quote_get` → `data_get_study_values`

| Passo | Ticker | Fallback |
|-------|--------|----------|
| 1 | `USDT.D` | — |
| 2 | `SPX` | `ES1!` (mercado fechado) |
| 3 | `GOLD` | `XAUUSD` |
| 4 | `DXY` | — |
| 5 | `TOTAL` | — |
| 6 | `TOTAL2` | — |
| 7 | `TOTAL3` | — |
| 8 | `USOIL` | `CL1!` |
| 9 | `BTCUSDLONGS` | — |
| 10 | `BTCUSDSHORTS` | — |

**Depois dos 10 passos:** Montar tabela de correlações, calcular ratio L/S, definir regime e squeeze risk, SÓ ENTÃO voltar para o ativo solicitado.
Anotar para cada: **tendência** (alta/baixa/lateral), **nível chave**, **sinal relevante**

### Tabela de Correlações (preencher em cada sessão)

| Ativo | Preço | Tendência D | Sinal | Correlação BTC |
|-------|-------|-------------|-------|----------------|
| USDT.D | | | | inversa |
| S&P 500 / ES1! | | | | positiva |
| Ouro | | | | contextual |
| DXY | | | | inversa |
| TOTAL | | | | direta |
| TOTAL2 | | | | direta |
| TOTAL3 | | | | direta |
| Petróleo | | | | inversa (inflação) |
| BTCUSDLONGS | | | | direta (posicionamento) |
| BTCUSDSHORTS | | | | inversa (posicionamento) |
| **Ratio L/S** | | | | **> 5 = long squeeze risk / < 1 = short squeeze risk** |

### Regras de Leitura Macro

1. **Risk-On confirmado:** DXY caindo + S&P subindo + USDT.D caindo + TOTAL subindo → BTC bullish
2. **Risk-Off confirmado:** DXY subindo + S&P caindo + USDT.D subindo + Ouro subindo → BTC bearish
3. **Divergência macro:** Se BTC sobe mas DXY também sobe e TOTAL2/3 caem → rally frágil, não confiar
4. **Petróleo em alta forte:** Sinaliza pressão inflacionária → Fed hawkish → risco médio para cripto
5. **TOTAL vs TOTAL2 vs TOTAL3:** Se TOTAL sobe mas TOTAL3 cai → dinheiro concentrado em BTC/ETH, altcoins em risco
6. **BTCUSDLONGS vs BTCUSDSHORTS — Detecção de Squeeze:**
   - **Long Squeeze Risk:** Longs em máxima histórica ou extremo relativo + Shorts em mínima + preço esticado para cima → risco alto de long squeeze
   - **Short Squeeze Risk:** Shorts subindo rapidamente ou em extremo + Longs estáveis/caindo + preço próximo de resistência → short squeeze iminente
   - **Ratio L/S > 5.0:** Mercado excessivamente long → vulnerável a long squeeze
   - **Ratio L/S < 1.0:** Mais shorts que longs → combustível para short squeeze
   - **Divergência preço × Longs:** Se preço sobe mas Longs caem → rally sem convicção, smart money saindo
   - **Divergência preço × Shorts:** Se preço cai mas Shorts caem → vendedores desistindo, fundo próximo

### Como registrar na sessão
- Declarar explicitamente: `Macro: Risk-On | Risk-Off | Misto`
- Declarar: `DXY: bullish/bearish/neutro | S&P: bullish/bearish/neutro`
- Se análise cripto contradiz o macro → reduzir confiança e rotular como `contra-macro`

---

## 📋 Checklist de Análise Técnica Obrigatória

**TODA análise de ativo DEVE seguir este checklist completo. Não é opcional.**
O agente DEVE ler os conceitos relevantes da wiki e aplicar cada framework sistematicamente.
Pular frameworks é PROIBIDO. Se um framework não se aplica, declarar explicitamente "N/A" com justificativa.

### Fase 0 — Pre-Analysis Self-Check (OBRIGATÓRIO antes de iniciar qualquer análise técnica)
1. **Erros prevenidos:** Listar até 3 erros de `mistakes.md` relevantes para este ativo/setup → declarar prevenção ativa para cada um
2. **Insights ativados:** Listar até 3 insights de `insights.md` mais aplicáveis → citar explicitamente no raciocínio
3. **Padrões ativos:** Verificar `patterns.md` → se padrão VALIDADO ou CONSOLIDADO presente → declarar monitoramento
4. **Previsões abertas:** Se ativo tem previsão ⏳ → atualizar/fechar antes de prosseguir com a análise
5. **Sessão anterior:** Referenciar a sessão mais recente do mesmo ativo → declarar o que mudou estruturalmente

### Fase 1 — Leitura de Contexto (antes de olhar o chart)
1. Ler `wiki/brain/insights.md` — aplicar insights validados
2. Ler `wiki/brain/mistakes.md` — evitar erros já cometidos
3. Ler `wiki/brain/indicators.md` — calibrar peso de RSI, MACD, EMA, ADX, CHoCH/BOS
4. Ler `wiki/brain/patterns.md` — aplicar padrões recorrentes
5. Ler `wiki/assets/{SYMBOL}.md` — contexto histórico do ativo

### Fase 2 — Multi-Timeframe (top-down obrigatório)
Ref: [[multi-timeframe-analysis]]
1. **Semanal/Mensal:** Tendência primária (HH/HL ou LH/LL), RSI macro, EMA 200
2. **Diário:** Ciclo secundário, sobrecompra/venda estrutural
3. **4H:** Filtro direcional (EMA 200 = above→Long only / below→Short only), ADX, estrutura
4. **1H:** Zona de entrada, FVG, OB, divergências RSI
5. **15M/5M:** Gatilho de execução, BOS de confirmação

### Fase 3 — Smart Money Concepts (SMC)
Ref: [[SMC]]
1. Identificar estrutura: **BOS** (continuação) ou **CHoCH** (reversão) no 4H e 1H
2. Mapear **FVG** (Fair Value Gaps) — buracos de liquidez não preenchidos
3. Mapear **Order Blocks** — último candle antes de impulso (zona institucional)
4. Identificar **zonas de liquidez**: EQH/EQL, PDH/PDL, BSL/SSL
5. Detectar **traps**: Bull Trap, Bear Trap, BSL Grab, Stop Hunt
6. Buscar confluências: FVG + OB + Fibonacci Golden Zone = máxima convicção

### Fase 4 — Wyckoff
Ref: [[Wyckoff]]
1. Identificar fase atual: **Acumulação / Markup / Distribuição / Markdown**
2. Buscar eventos-chave: Spring (false break down) ou UT/UTAD (false break up)
3. Aplicar Lei do Esforço × Resultado: alto volume + resultado pequeno = absorção
4. Cruzar com SMC: Spring = EQL sweep + CHoCH bullish | UT = EQH sweep + CHoCH bearish

### Fase 5 — Fibonacci + Price Action
Ref: [[fibonacci-structural]] + [[price-action-patterns]]
1. Traçar Fibonacci do último impulso relevante
2. Identificar **Golden Zone** (0.618–0.786) como zona de entrada prioritária
3. Confluência: Golden Zone + FVG + OB = entrada sniper
4. Padrões de candle: Engulfing, Pin Bar, Doji em zonas de confluência

### Fase 6 — Indicadores Técnicos (valor + direção + cruzamento + divergências)
Ref: [[rsi-divergences]] + [[macd]] + [[ADX]] + [[bollinger-bands]] + [[volume-profile]]
1. **RSI (14):**
   - Valor absoluto + zona (sobrecompra >70 / sobrevenda <30 / neutro)
   - **Direção da linha RSI:** subindo, descendo, achatando
   - **Cruzamento RSI × SMA(RSI):** RSI cruza SMA para cima = momentum bullish; para baixo = bearish
   - **Divergências clássicas e ocultas no 1H/4H** (preço vs RSI) — bearish: preço HH + RSI LH | bullish: preço LL + RSI HL
   - RSI > 70 em TF maior = teto de retração (limita upside dos TFs menores)
2. **RSI Estocástico (Stoch RSI):**
   - %K e %D: valores + cruzamento (%K cruza %D para cima = bullish, para baixo = bearish)
   - Zona: sobrecompra (>80) / sobrevenda (<20)
   - **Direção:** linhas subindo/descendo dentro da zona
   - **Divergências StochRSI (1H/15M):** preço HH + %K LH em >80 = bearish | preço LL + %K HL em <20 = bullish
   - Reset de oversold em tendência de alta = continuação; reset de overbought em bear = continuação
   **⚠️ Regra RSI+StochRSI combinado (Ref: [[rsi-stochrsi-combined]]):**
   - RSI (D/4H) define DIREÇÃO → RSI > 50 = Long only / RSI < 50 = Short only
   - StochRSI (1H/15M) define TIMING → cruzamento em zona extrema = gatilho de entrada
   - **NUNCA operar StochRSI contra a direção do RSI HTF**
   - StochRSI overbought + RSI HTF bullish = continuação (NÃO shortear)
   - StochRSI oversold + RSI HTF bearish = continuação bearish (NÃO longear)
3. **MACD (12/26/9):**
   - **Posição relativa à linha zero:** acima = lado comprador / abaixo = lado vendedor
   - **Cruzamento MACD × Signal Line:** cross up = gatilho bullish / cross down = bearish
   - **Onde ocorre o cruzamento:** acima de zero = mais forte bullish / abaixo = mais forte bearish
   - **Histograma:** crescente (momentum aumentando) / decrescente (enfraquecendo)
   - **Divergências MACD (4H/D):** preço HH + MACD LH = bearish | preço LL + MACD HL = bullish (hist. ou linhas)
   - **Direção das linhas:** MACD e Signal convergindo ou divergindo
   - Cross sem volume = sinal fraco → aguardar confirmação
4. **ADX (14):** > 25 = tendência forte (respeitar direção). < 20 = range (aguardar). DI+ > DI- = bullish / DI- > DI+ = bearish
5. **EMA 50/200:** Posição do preço + cruzamento (Golden Cross / Death Cross) + direção da inclinação
6. **Volume / OBV:**
   - POC como magneto, HVN como suporte/resistência
   - **Divergências Volume×Preço:** preço subindo + volume caindo = rally fraco (bearish) | preço caindo + volume caindo = queda enfraquecendo (bullish)
   - **Divergências OBV:** preço HH + OBV LH = distribuição | preço LL + OBV HL = acumulação

### Fase 7 — Playbook Match
Ref: [[trade-playbooks]]
1. Verificar se o cenário atual se encaixa em algum dos 4 playbooks:
   - **Playbook 1:** Long em retração de tendência de alta
   - **Playbook 2:** Short em repique de tendência de baixa
   - **Playbook 3:** Stop Hunt Reversal
   - **Playbook 4:** Squeeze de Alavancagem
2. Executar checklist de entrada obrigatório (8 critérios, mínimo 6)
3. Se nenhum playbook se aplica → declarar "Nenhum setup identificado"

### Fase 8 — Liquidez, Correlações e Posicionamento de Margem
Ref: [[liquidity-wicks-trap-short-usdtd]] + [[btc-macro-correlations]] + [[btcusdlongs-btcusdshorts]]
1. Mapear pavios HTF (mensal/semanal/diário) → liquidez acima ou abaixo
2. USDT.D: confirma ou nega o bias?
3. Funding Rate + Open Interest (se disponível)
4. **BTCUSDLONGS + BTCUSDSHORTS (obrigatório para BTC/ETH):**
   - Consultar `BTCUSDLONGS` → valor atual, tendência (subindo/caindo/lateral), nível relativo (alto/médio/baixo)
   - Consultar `BTCUSDSHORTS` → valor atual, tendência, nível relativo
   - Calcular Ratio L/S = BTCUSDLONGS / BTCUSDSHORTS
   - Avaliar risco de squeeze: `Long Squeeze Risk` (ratio > 5 + longs em extremo) ou `Short Squeeze Risk` (ratio < 1 + shorts subindo)
   - Cruzar com Funding Rate: FR muito positiva + Longs extremos = dupla confirmação de long squeeze risk
   - Cruzar com OI: OI alto + Ratio extremo = squeeze de alta probabilidade
5. Declarar: `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega | Longs/Shorts: [ratio] [squeeze risk]`

### Fase 9 — Declaração de Bias Final
1. Sintetizar todas as fases acima em um bias claro: **LONG / SHORT / NEUTRO**
2. Declarar confiança: **alta / média / baixa**
3. Se bias contradiz macro → rotular como `contra-macro` e reduzir confiança
4. Se nenhum framework converge → declarar `NEUTRO — sem confluência`

### Como escrever na sessão (adaptar por classe)

**Todas as classes:**
- `Classe: BTC | BTC+ETH | ALTCOIN | EQUITIES | WATCHLIST | DAILY`
- `MTF: W/D/4H/1H → [resumo]` (DAILY: só D+4H)
- `Indicadores: RSI [valor] [direção] | StochRSI [%K/%D] [cross] | MACD [vs zero] [cross] [hist] | ADX [valor]`
- `Bias: LONG/SHORT/NEUTRO | Confiança: alta/média/baixa`

**BTC / BTC+ETH — adicionar:**
- `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega`
- `Longs/Shorts: BTCUSDLONGS [valor] | BTCUSDSHORTS [valor] | Ratio [X.X] | Squeeze Risk: [nível]`
- (BTC+ETH) `ETH/BTC: [valor] [outperform/underperform] [%]`

**ALTCOIN — adicionar:**
- `Setor: DeFi/AI/L2/meme/infra | Par/BTC: [subindo/caindo] | BTC.D: [valor] [tendência]`
- `Tipo: scalp | swing | holder`

**EQUITIES — adicionar:**
- `VIX: [valor] [tendência] | Setor ETF: [ticker] [tendência] | Earnings: [data ou N/A]`

**WATCHLIST — usar tabela:**
- `| Ativo | Preço | Bias | Confiança | Setup? | Nota |`

**DAILY — usar dashboard:**
- `Macro: Risk-On/Off/Misto | BTC: [bias] | Alertas: [N] | Previsões abertas: [N]`

---

## Decision Tree — Which Tool When

### "What's on my chart right now?"
1. `chart_get_state` → symbol, timeframe, chart type, list of all indicators with entity IDs
2. `data_get_study_values` → current numeric values from all visible indicators (RSI, MACD, BBands, EMAs, etc.)
3. `quote_get` → real-time price, OHLC, volume for current symbol

### "What levels/lines/labels are showing?"
Custom Pine indicators draw with `line.new()`, `label.new()`, `table.new()`, `box.new()`. These are invisible to normal data tools. Use:

1. `data_get_pine_lines` → horizontal price levels drawn by indicators (deduplicated, sorted high→low)
2. `data_get_pine_labels` → text annotations with prices (e.g., "PDH 24550", "Bias Long ✓")
3. `data_get_pine_tables` → table data formatted as rows (e.g., session stats, analytics dashboards)
4. `data_get_pine_boxes` → price zones / ranges as {high, low} pairs

Use `study_filter` parameter to target a specific indicator by name substring (e.g., `study_filter: "Profiler"`).

### "Give me price data"
- `data_get_ohlcv` with `summary: true` → compact stats (high, low, range, change%, avg volume, last 5 bars)
- `data_get_ohlcv` without summary → all bars (use `count` to limit, default 100)
- `quote_get` → single latest price snapshot

### "Analyze my chart" (full report workflow)
1. `quote_get` → current price
2. `data_get_study_values` → all indicator readings
3. `data_get_pine_lines` → key price levels from custom indicators
4. `data_get_pine_labels` → labeled levels with context (e.g., "Settlement", "ASN O/U")
5. `data_get_pine_tables` → session stats, analytics tables
6. `data_get_ohlcv` with `summary: true` → price action summary
7. `capture_screenshot` → visual confirmation

### "Change the chart"
- `chart_set_symbol` → switch ticker (e.g., "AAPL", "ES1!", "NYMEX:CL1!")
- `chart_set_timeframe` → switch resolution (e.g., "1", "5", "15", "60", "D", "W")
- `chart_set_type` → switch chart style (Candles, HeikinAshi, Line, Area, Renko, etc.)
- `chart_manage_indicator` → add or remove studies (use full name: "Relative Strength Index", not "RSI")
- `chart_scroll_to_date` → jump to a date (ISO format: "2025-01-15")
- `chart_set_visible_range` → zoom to exact date range (unix timestamps)

### "Work on Pine Script"
1. `pine_set_source` → inject code into editor
2. `pine_smart_compile` → compile with auto-detection + error check
3. `pine_get_errors` → read compilation errors
4. `pine_get_console` → read log.info() output
5. `pine_get_source` → read current code back (WARNING: can be very large for complex scripts)
6. `pine_save` → save to TradingView cloud
7. `pine_new` → create blank indicator/strategy/library
8. `pine_open` → load a saved script by name

### "Practice trading with replay"
1. `replay_start` with `date: "2025-03-01"` → enter replay mode
2. `replay_step` → advance one bar
3. `replay_autoplay` → auto-advance (set speed with `speed` param in ms)
4. `replay_trade` with `action: "buy"/"sell"/"close"` → execute trades
5. `replay_status` → check position, P&L, current date
6. `replay_stop` → return to realtime

### "Screen multiple symbols"
- `batch_run` with `symbols: ["ES1!", "NQ1!", "YM1!"]` and `action: "screenshot"` or `"get_ohlcv"`

### "Draw on the chart"
- `draw_shape` → horizontal_line, trend_line, rectangle, text (pass point + optional point2)
- `draw_list` → see what's drawn
- `draw_remove_one` → remove by ID
- `draw_clear` → remove all

### "Manage alerts"
- `alert_create` → set price alert (condition: "crossing", "greater_than", "less_than")
- `alert_list` → view active alerts
- `alert_delete` → remove alerts

### "Navigate the UI"
- `ui_open_panel` → open/close pine-editor, strategy-tester, watchlist, alerts, trading
- `ui_click` → click buttons by aria-label, text, or data-name
- `layout_switch` → load a saved layout by name
- `ui_fullscreen` → toggle fullscreen
- `capture_screenshot` → take a screenshot (regions: "full", "chart", "strategy_tester")

### "TradingView isn't running"
- `tv_launch` → auto-detect and launch TradingView with CDP on Mac/Win/Linux
- `tv_health_check` → verify connection is working

## Context Management Rules

These tools can return large payloads. Follow these rules to avoid context bloat:

1. **Always use `summary: true` on `data_get_ohlcv`** unless you specifically need individual bars
2. **Always use `study_filter`** on pine tools when you know which indicator you want — don't scan all studies unnecessarily
3. **Never use `verbose: true`** on pine tools unless the user specifically asks for raw drawing data with IDs/colors
4. **Avoid calling `pine_get_source`** on complex scripts — it can return 200KB+. Only read if you need to edit the code.
5. **Avoid calling `data_get_indicator`** on protected/encrypted indicators — their inputs are encoded blobs. Use `data_get_study_values` instead for current values.
6. **Use `capture_screenshot`** for visual context instead of pulling large datasets — a screenshot is ~300KB but gives you the full visual picture
7. **Call `chart_get_state` once** at the start to get entity IDs, then reference them — don't re-call repeatedly
8. **Cap your OHLCV requests** — `count: 20` for quick analysis, `count: 100` for deeper work, `count: 500` only when specifically needed

### Output Size Estimates (compact mode)
| Tool | Typical Output |
|------|---------------|
| `quote_get` | ~200 bytes |
| `data_get_study_values` | ~500 bytes (all indicators) |
| `data_get_pine_lines` | ~1-3 KB per study (deduplicated levels) |
| `data_get_pine_labels` | ~2-5 KB per study (capped at 50) |
| `data_get_pine_tables` | ~1-4 KB per study (formatted rows) |
| `data_get_pine_boxes` | ~1-2 KB per study (deduplicated zones) |
| `data_get_ohlcv` (summary) | ~500 bytes |
| `data_get_ohlcv` (100 bars) | ~8 KB |
| `capture_screenshot` | ~300 bytes (returns file path, not image data) |

## Tool Conventions

- All tools return `{ success: true/false, ... }`
- Entity IDs (from `chart_get_state`) are session-specific — don't cache across sessions
- Pine indicators must be **visible** on chart for pine graphics tools to read their data
- `chart_manage_indicator` requires **full indicator names**: "Relative Strength Index" not "RSI", "Moving Average Exponential" not "EMA", "Bollinger Bands" not "BB"
- Screenshots save to `screenshots/` directory with timestamps
- OHLCV capped at 500 bars, trades at 20 per request
- Pine labels capped at 50 per study by default (pass `max_labels` to override)

## Architecture

```
Claude Code ←→ MCP Server (stdio) ←→ CDP (localhost:9222) ←→ TradingView Desktop (Electron)
```

Pine graphics path: `study._graphics._primitivesCollection.dwglines.get('lines').get(false)._primitivesDataById`

---

# Wiki Maintenance Protocol

> Este repositório implementa o padrão LLM Wiki (Karpathy) com **brain ativo**.
> O LLM lê o brain ANTES de analisar e escreve nele DEPOIS de cada interação.
> O humano raramente edita. O cérebro cresce sozinho.

## Estrutura da Wiki
- `wiki/` — wiki compilada em markdown
- `wiki/brain/` — **cérebro ativo** (insights, erros, previsões, padrões, indicadores)
- `wiki/brain/_templates/` — templates iniciais dos brain files (comitados no git)
- `raw/` — dados brutos imutáveis (screenshots, OHLCV, pine exports)
- `wiki/index.md` — índice mestre (gitignored — criado a partir de `index.initial.md`)
- `wiki/log.md` — append-only log (gitignored — criado a partir de `log.initial.md`)

> **IMPORTANTE:** Os brain files (`wiki/brain/*.md`) são gitignored — dados pessoais.
> Se um brain file não existir, criar cópia de `wiki/brain/_templates/{nome}.md`.
> O `setup.sh` faz isso automaticamente. Se rodando sem setup, criar manualmente.

## Brain — O Cérebro da Aplicação

O diretório `wiki/brain/` é o núcleo de autoaprendizado:

| Arquivo | Propósito | Quando ler | Quando escrever |
|---------|-----------|------------|-----------------|
| `brain/insights.md` | Insights acumulados de todas as análises | ANTES de cada análise | DEPOIS de cada análise |
| `brain/mistakes.md` | Erros cometidos e lições aprendidas | ANTES de cada análise | Quando feedback confirma erro |
| `brain/predictions-log.md` | Previsões com outcomes (aberta/acertou/errou) | Ao analisar ativo com previsão aberta | Quando análise gera bias definido |
| `brain/indicators.md` | Aprendizados sobre cada indicador | ANTES de analisar indicadores | Quando indicador surpreende (acerta/falha) |
| `brain/patterns.md` | Padrões comportamentais recorrentes | ANTES de cada análise | Quando padrão se repete pela 2ª+ vez |

---

> **REGRA ZERO:** O ciclo READ/WRITE do AUTO-PILOT (seção ⚡ acima) é obrigatório em TODA interação.
> Formatos de escrita: usar templates em `wiki/brain/_templates/`. Categorias de erro: `falso-sinal` | `bias-errado` | `timing` | `indicador` | `htf-ignorado` | `overtrading` | `sl-apertado`

---

## Operações Disponíveis

### 1. INGEST — Análise de gráfico com registro
Trigger: qualquer pedido de análise de chart ou ativo

Workflow:
1. **[CLASSIFICAR]** Determinar classe do pedido (ver tabela AUTO-PILOT)
2. **[BRAIN READ]** Executar ciclo READ (insights, mistakes, asset, predictions)
3. **[MACRO SCAN]** Executar scan conforme a classe:
   - BTC/BTC+ETH: completo (10 passos) | ALTCOIN: reduzido (4 passos) | EQUITIES: TradFi | WATCHLIST/DAILY: 1× completo
3. Chamar: `chart_get_state` → `data_get_study_values` → `quote_get` → `data_get_pine_lines` → `data_get_pine_labels` → `capture_screenshot`
4. Analisar com contexto do brain + macro (aplicar insights, evitar erros passados)
5. Criar `wiki/sessions/YYYY-MM-DD-SYMBOL-TF.md` usando o template:
   - **OBRIGATÓRIO:** Seção "Brain Read Summary" preenchida (erros prevenidos, insights ativados, padrões monitorados)
   - **OBRIGATÓRIO:** Seção "Contexto Macro" preenchida (se BTC/ETH/Altcoin)
   - **OBRIGATÓRIO:** Seção "Setups Identificados" deve ser preenchida
     (mesmo que com "Nenhum setup reconhecido nesta sessão")
   - **OBRIGATÓRIO:** Seção "Plano de Operação" com entrada/stop/TP/R:R
   - **OBRIGATÓRIO:** Seção "Comparação com Sessão Anterior" preenchida
   - **OBRIGATÓRIO:** Seção "Resultado" inicializada com `⏳ aberta`
   - **OBRIGATÓRIO:** Seção "Aprendizados desta Sessão" preenchida ao final
6. **Setup Match Check (antes de criar/atualizar setup):**
   - Verificar `wiki/setups/index.md` → o setup atual corresponde a algum existente?
   - Se **sim** → linkar ao setup existente e atualizar "Histórico de Ocorrências"
   - Se **não** e setup apareceu em 2+ sessões anteriores → criar `wiki/setups/{nome}.md`
   - Se **não** e é primeira ocorrência → registrar como "candidato" em `wiki/setups/index.md` sem criar arquivo
7. **Se setup identificado e match confirmado:**
   a. Criar ou atualizar `wiki/setups/{nome}.md` (usar `_template.md`)
   b. Adicionar nova linha na tabela "Histórico de Ocorrências" com data, ativo, TF
   c. Recalcular seção "Estatísticas" (Total, Win, Loss, Win Rate, R:R Médio)
   d. Atualizar `wiki/setups/index.md` — atualizar linha do setup na tabela de ranking
7. Atualizar `wiki/assets/{SYMBOL}.md` com novos dados
8. Atualizar `wiki/index.md` (contadores e links)
9. **[BRAIN WRITE]** Executar ciclo WRITE (insight, prediction, indicators)
10. Append em `wiki/log.md`: `## [YYYY-MM-DD HH:MM] ingest | {SYMBOL} {TF}`

### 2. QUERY — Perguntas contra a wiki
Trigger: "Baseado na wiki, [pergunta]" ou qualquer pergunta sobre mercado/estratégia

Workflow:
1. **[BRAIN READ]** Ler brain relevante ao tema da pergunta
2. Ler `wiki/index.md` para mapear páginas relevantes
3. Ler páginas relevantes
4. Sintetizar resposta com contexto do brain
5. Se resposta gerou novo insight → append em `brain/insights.md`
6. Se resposta é valiosa → arquivar em `wiki/analysis/YYYY-MM-DD-{slug}.md`
7. Append em `wiki/log.md`: `## [YYYY-MM-DD] query | {resumo da pergunta}`

### 3. FEEDBACK — Fechar loop de aprendizado e métricas
Trigger: "Como foi minha previsão?" ou "O mercado confirmou?" ou ao analisar ativo com previsão aberta

Workflow:
1. Ler `wiki/brain/predictions-log.md` → buscar previsões abertas (⏳)
2. Comparar previsão com estado atual do mercado
3. Marcar como ✅ acertou | ❌ errou | ⚪ expirou
4. **Atualizar a sessão original** (`wiki/sessions/`):
   a. Preencher seção "Resultado": outcome, entrada/saída real, R:R alcançado, P&L, tempo
   b. Preencher "Setup utilizado" com link para o setup
5. **Se setup foi utilizado no trade:**
   a. Atualizar resultado na tabela "Histórico de Ocorrências" do setup
   b. Recalcular "Estatísticas" do setup (Total, Win, Loss, Win Rate, R:R Médio)
   c. Atualizar `wiki/setups/index.md` com métricas recalculadas
6. Se ❌ errou:
   - Identificar causa raiz
   - Append em `brain/mistakes.md` com categoria, lição **e campo "Prevenção"** (check para próximo setup similar)
   - Atualizar `brain/indicators.md`: incrementar "Falhas" + recalcular Hit Rate do indicador que falhou
7. Se ✅ acertou:
   - Reforçar insight em `brain/insights.md`
   - Atualizar `brain/indicators.md`: incrementar "Acertos" + recalcular Hit Rate dos indicadores usados
8. Atualizar `brain/patterns.md` se padrão se confirmou/negou → promover Status se atingiu threshold
9. Preencher seção "Aprendizados desta Sessão" na sessão original se ainda não preenchida
10. Append em `wiki/log.md`: `## [YYYY-MM-DD] feedback | {SYMBOL} {resultado}`

### 4. LINT — Health-check periódico
Trigger: "Faça o lint da wiki" ou "Health-check da wiki"

Workflow:
1. Ler `wiki/index.md` completo
2. Usar a tool `wiki_search` para cruzar conceitos soltos e sugerir novas páginas em `wiki/research/`
3. Cruzar `wiki/setups/` com `wiki/sessions/` para atualizar estatísticas
4. **Verificar previsões expiradas** em `brain/predictions-log.md` (> 48h abertas)
5. **Ranquear insights** em `brain/insights.md` (mover mais validados para cima)
6. Identificar conceitos mencionados em `raw/clippings/` mas sem página `wiki/concepts/` própria
7. **Regenerar `wiki/library.md`** — garantir que todos os clippings estejam linkados no Graph View
8. Criar `wiki/lint/YYYY-MM-DD.md` com relatório
9. Append em `wiki/log.md`: `## [YYYY-MM-DD] lint | {N} issues encontrados`

### 5. UPDATE STRATEGY — Revisão de estratégia com métricas
Trigger: "Atualize a estratégia com base nos resultados recentes"

Workflow:
1. Ler `wiki/setups/index.md` → ranking de setups por win rate
2. Ler todas as sessões com Resultado preenchido (✅/❌/⚪)
3. **Calcular métricas globais:**
   - **Win Rate global:** (total wins / total trades fechados) × 100
   - **R:R Médio:** média de R:R alcançado em trades fechados
   - **Drawdown máximo:** sequência máxima de losses consecutivos
   - **Sharpe simplificado:** (win_rate × avg_win - loss_rate × avg_loss) / desvio
4. Ler `brain/mistakes.md` + `brain/indicators.md` (aprendizados)
5. Ler `brain/patterns.md` para padrões validados/negados
6. **Propor ajustes com evidência numérica:**
   - Setups com win rate < 40% → candidato a remoção ou ajuste de regras
   - Setups com win rate > 60% → candidato a aumento de posição
   - Indicadores que falharam consistentemente → reduzir peso no checklist
   - Padrões validados pelo brain → adicionar como filtro ou regra
7. **Atualizar tabela "Performance Histórica"** na estratégia com dados reais
8. Atualizar `wiki/setups/index.md` seção "Métricas Globais"
9. Versionar: incrementar data de "Última revisão" na estratégia
10. Append em `wiki/log.md`: `## [YYYY-MM-DD] update-strategy | {resumo dos ajustes}`

### 6. COMPILE — Ingestão de clippings e artigos
Trigger: "Compile os clippings recentes na wiki"

Workflow:
1. Ler arquivos `.md` novos em `raw/clippings/` e `raw/papers/`
2. Extrair conceitos chave, dados, e insights
3. Atualizar `wiki/concepts/` ou criar arquivos em `wiki/research/`
4. Inserir backlinks bidirecionais
5. Atualizar `wiki/index.md` e `wiki/search-index.md`
6. **Regenerar `wiki/library.md`** — listar TODOS os `.md` de `raw/clippings/` como wikilinks `[[nome]]` (garante Graph View conectado)
7. Append em `wiki/log.md`: `## [YYYY-MM-DD] compile | {N} artigos processados`

### 7. REVIEW / VISUALIZE — Outputs visuais no Obsidian
Trigger: "Gere a revisão semanal" ou "Visualize os resultados"

Workflow:
1. Analisar as sessões do período solicitado (ex: últimos 7 dias)
2. Extrair métricas (win rate, total profit, drawdown, key insights)
3. Executar o script Python `scripts/tools/plot_accuracy.py` para gerar o gráfico na pasta `wiki/outputs/charts/`
4. Criar uma apresentação usando formato Marp (`wiki/outputs/YYYY-MM-DD-review.md`)
5. Append em `wiki/log.md`

### 8. SEARCH — Pesquisa indexada
Trigger: "Ache na wiki..." para consultas que superem o limite de leitura direta

Workflow:
1. Executar no sistema a tool nativa do MCP conectada: `wiki_search` passando a `query` desejada.
2. Analisar o ranqueamento retornado e ler trechos (snippets) para orientar decisões avançadas.
3. Sintetizar os resultados com backlinks

### 9. CYCLE — Análise de Ciclo do Bitcoin
Trigger: "Análise de ciclo" ou "Onde estamos no ciclo?" ou "Projeção de fundo/topo" ou quando macro scan indica transição de fase

Ref: [[btc-cycle-analysis]]

Workflow:
1. **[BRAIN READ]** Ler brain + `wiki/concepts/btc-cycle-analysis.md`
2. **[MACRO SCAN]** Executar scan macro completo (10 passos obrigatórios)
3. **[PRICE ACTION SEMANAL/MENSAL]**
   a. `chart_set_symbol({symbol: "BTCUSD"})` → `chart_set_timeframe({timeframe: "W"})` → `data_get_study_values()` → `capture_screenshot()`
   b. `chart_set_timeframe({timeframe: "M"})` → `data_get_ohlcv({summary: true})` → `capture_screenshot()`
   c. Verificar: RSI semanal (divergências), MACD semanal (cruzamento vs zero), volume (climático?)
4. **[200W SMA]** Verificar posição do preço vs 200W SMA — se preço NÃO tocou → fundo provavelmente NÃO ocorreu
5. **[INDICADORES ON-CHAIN]** Ler indicadores comunitários no chart (se instalados):
   - MVRV Z-Score: >7 = topo | <0 = fundo
   - NUPL: >0.75 = euforia | <0 = capitulação
   - Puell Multiple: >4 = topo | <0.5 = fundo
   - Pi Cycle Top: 111DMA vs 350DMA×2 cruzaram?
   - Hash Ribbons: capitulação ativa?
   - Realized Price: preço acima ou abaixo?
6. **[FIBONACCI LOG]** Traçar Fib do low do ciclo anterior ao ATH atual (escala log)
7. **[SCORING]** Preencher:
   - Score de Topo: [X/10]
   - Score de Fundo: [X/15]
8. **[PROJEÇÃO]** Se bear confirmado → calcular zona de fundo com 6 métodos:
   - Fractal drawdown | 200W SMA | Realized Price | Fibonacci log | Temporal | Confluência técnica
   - Identificar zona onde 3+ métodos convergem
9. **[OUTPUT]** Gerar diagnóstico completo conforme template:
   - Fase atual | Scores | Indicadores | Projeção (se aplicável) | Estratégia de acumulação
10. **[BRAIN WRITE]** Registrar em `wiki/sessions/YYYY-MM-DD-BTC-CYCLE.md`
11. Append previsão em `brain/predictions-log.md`
12. Append em `wiki/log.md`: `## [YYYY-MM-DD] cycle | BTC | Fase: [X]`

---

## Prioridade de Contexto (o que ler primeiro)

Quando o contexto é limitado, carregar nesta ordem:

1. `wiki/brain/insights.md` — SEMPRE (resumo compacto do que já sabe)
2. `wiki/brain/mistakes.md` — SEMPRE (últimos 10, evitar repetir)
3. `wiki/assets/{SYMBOL}.md` — quando analisando um ativo específico
4. `wiki/brain/predictions-log.md` — quando analisando ativo com previsão aberta
5. `wiki/brain/indicators.md` — quando interpretando indicadores
6. `wiki/brain/patterns.md` — quando buscando recorrências
7. `wiki/strategies/` — quando avaliando entrada
8. `wiki/concepts/` — quando conceito específico é relevante

## Convenções de Backlinks
- Use `[[nome-do-arquivo]]` (sem extensão, sem path)
- Toda página nova deve ter seção `## Backlinks`
- Ao atualizar uma página, verificar e adicionar backlinks bidirecionais

## Convenções de Nomenclatura
- Sessões: `YYYY-MM-DD-SYMBOL-TF.md` (ex: `2026-04-19-BTCUSD-4H.md`)
- Setups: `kebab-case` descritivo (ex: `fvg-pullback-bull-ob.md`)
- Analysis: `YYYY-MM-DD-slug.md`
- Lint: `YYYY-MM-DD.md`

## Regras Críticas
1. NUNCA modificar arquivos em `raw/` — são imutáveis
2. SEMPRE executar ciclo READ antes de qualquer análise
3. SEMPRE executar ciclo WRITE depois de qualquer análise
4. SEMPRE atualizar `wiki/log.md` após qualquer operação
5. SEMPRE atualizar `wiki/index.md` quando criar nova página
6. SEMPRE preencher "Setups Identificados" em cada sessão (mesmo se nenhum)
7. SEMPRE preencher "Resultado" quando feedback fecha previsão
8. SEMPRE atualizar `wiki/setups/index.md` após criar/atualizar setup
9. SEMPRE recalcular Estatísticas do setup após FEEDBACK com resultado
10. Screenshots vão em `raw/screenshots/` antes de referenciar na wiki
11. Dados OHLCV exportados vão em `raw/ohlcv/`
12. Previsões abertas > 48h devem ser marcadas como ⚪ expiradas no próximo LINT
