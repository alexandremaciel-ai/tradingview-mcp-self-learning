# TradingView MCP — Gemini Instructions

79 tools for reading and controlling a live TradingView Desktop chart via CDP (port 9222).

---

## ⚡ AUTO-PILOT — Regra Obrigatória (leia PRIMEIRO)

**Se aplica a TODA interação. Não é opcional.**

### ANTES de responder qualquer pedido:
0. **🔌 Testar conexão:** `tv_health_check()` → se falhar → `tv_launch()` → 3 tentativas max
0b. **📡 Feeds (classes cripto):** se `raw/feeds/latest.md` estiver `indisponível` **ou** com timestamp > 2h → rodar `python3 scripts/tools/fetch_feeds.py` (carrega o `.env` sozinho) e reler. Rede falhou → seguir com o cache + rótulo `dados-parciais`. EQUITIES pula (sem funding).
1. Ler `wiki/brain/insights.md` (Top N quentes; histórico em `insights-archive/` só sob demanda) + `wiki/brain/mistakes.md` (últimos 10)
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
- **metrics.md:** Consultar `brain/metrics.md` (circuit breaker + calibração de confiança). Se 🔴 ativo (3 losses seguidos / DD 5% no dia) → rebaixar recomendação para "somente observação / paper" e declarar `⛔ Disciplina: [estado]`. Ref: [[trading-psychology]]

4. **⚠️ CLASSIFICAR O PEDIDO** na tabela abaixo → seguir o pipeline da classe:

| Classe | Quando | Macro Scan | Checklist | Extras |
|--------|--------|------------|-----------|--------|
| `BTC` | Análise solo de Bitcoin | **Completo** (10 passos) | Fases 1-9 completas | BTCUSDLONGS/SHORTS obrigatório |
| `BTC+ETH` | BTC e ETH juntos | Completo **1×** | BTC completo → ETH relativo (+ ETH/BTC pair) | Declarar ETH outperform/underperform |
| `BTC+ALTCOIN` | BTC + altcoin específica (BTC+SOL, BTC+ADA) | **Parcial** (7 passos): USDT.D + BTC.D + TOTAL3 + BTC + Longs/Shorts + par | BTC: Fases 1-6,8-9 → Altcoin: Fases 1-6,8-9 | ALTCOIN/BTC pair obrigatório. Wyckoff só se vol > $50M |
| `ALTCOIN` | SOL, ADA, DOGE, etc. | **Reduzido** (5 passos): USDT.D + BTC.D + TOTAL3 + BTC bias + par | Fases 1-6, 8-9. Wyckoff só se vol > $50M | Tag obrigatória: `scalp/swing/holder` |
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

> Brain files inexistentes → copiar de `wiki/brain/_templates/`. Arquivos locais ausentes → criar do seed `.initial.md`: `index.md`, `log.md`, `setups/index.md`, `watchlist.md`, `library.md` (todos gitignored — só os `.initial.md` são versionados).

---

## Regras Especiais por Classe

**BTC:** Macro vence micro — não confiar em rompimento sem fechamento + volume + USDT.D confirmando.

**ALTCOIN:** Se BTC em risco macro → altcoins só como scalp/day trade. Wyckoff: só se vol diário > $50M.

**EQUITIES:** Checar earnings iminentes (7 dias) → alertar risco de gap. Horário: pré-market (05h–10:30h BRT), regular (10:30–17:00h), after-hours — sinais em regular = mais confiáveis. Playbook 4 (squeeze crypto) **não se aplica** — usar Playbooks 1-3.

**WATCHLIST:** Macro 1× no início. Output: tabela `Ativo | Preço | Bias | Confiança | Setup? | Nota`. Destacar "Top 3". 1 sessão: `YYYY-MM-DD-WATCHLIST.md`.

**DAILY:** Macro 1× completo. BTC rápido (D+4H). Fechar previsões expiradas (>48h). Output: dashboard `Macro | BTC Bias | Alertas | Watchlist | Previsões`.

---

## 📊 Análise Macro Obrigatória — Pré-Requisito para Qualquer Análise

**ANTES de analisar qualquer ativo, o agente DEVE identificar o contexto de mercado e executar o scan da classe.** Regra obrigatória — o macro contexto define o viés primário.

### Step 0 — Detector de Contexto de Mercado (SEMPRE PRIMEIRO)

Antes de qualquer scan, declarar explicitamente o contexto temporal:

| | Status |
|--|--------|
| **Horário BRT + Dia** | [HH:MM] \| [Seg/Ter/Qua/Qui/Sex/Sáb/Dom] |
| **NYSE** | ABERTA (Seg-Sex 10:30–17:00 BRT / inverno 11:30–18:00) ou FECHADA |
| **CME** | ABERTO (quase 24h) ou FECHADO (Sex 18h BRT → Dom 19h BRT) |
| **Forex/DXY** | DISPONÍVEL (Seg 00h – Sex ~22h BRT) ou CONGELADO (Sex ~22h → **Dom 19h BRT**) — **REABRE Dom 19h BRT** |

**Protocolo de fim de semana (Sex 18h → Dom 19h BRT):**
- CME, NYSE e Forex **fechados** → SPX, DXY, GOLD, BRENT = **dados congelados do fechamento de sexta**
- Declarar: `⚠️ Mercados TradFi fechados — macro TradFi baseada no último fechamento de sexta. Cripto é o único mercado em tempo real.`
- Reduzir o peso de SPX/DXY/GOLD/Petróleo nas conclusões macro (dados sem liquidez nova)
- Focar nos dados ao vivo: USDT.D + TOTAL + TOTAL2 + TOTAL3 + BTCUSDLONGS/SHORTS

**🔓 Reabertura de domingo (Dom 19h BRT em diante):**
- CME (`ES1!`), Forex (`DXY`) e petróleo (`BRENT`) **reabrem** → dado ao vivo, **não mais congelado**.
- **OBRIGATÓRIO** a partir de dom 19h: ler e analisar `ES1!`, `DXY` e `BRENT` ao vivo em **toda** análise (não rotular como `congelado` nem reduzir peso por fim de semana após esse horário).
- **DXY** = inversamente proporcional ao BTC (DXY↑ → pressão de baixa no BTC). `ES1!` e `BRENT` mantêm leitura padrão (`ES1!` risk-on positivo; `BRENT` inflação — ver Regra de Leitura Macro #4).
- Declarar na sessão: `⏰ Dom pós-19h: ES1!/DXY/BRENT ao vivo (reabertura)`.

### Tabela de Fallbacks por Estado de Mercado

**⛔ DEVE executar `chart_set_symbol` para cada ativo. NÃO usar apenas `quote_get`.**

| Ativo | Ticker Normal | NYSE Fechada (pré/pós-market) | Fim de Semana (Sáb–Dom19h) | Dom 19h+ (reabertura) |
|-------|---------------|-------------------------------|----------------------------|-----------------------|
| **S&P 500** | `SPX` | `ES1!` | ⚠️ `ES1!` (congelado desde sexta) | ✅ `ES1!` ao vivo |
| **Ouro** | `GOLD` | `XAUUSD` | ⚠️ `XAUUSD` (congelado) | ✅ `XAUUSD` ao vivo |
| **Petróleo** | `BRENT` | `BRENT` | ⚠️ `BRENT` (congelado desde sexta) | ✅ `BRENT` ao vivo |
| **Dólar** | `DXY` | `DXY` | ⚠️ `DXY` (congelado) | ✅ `DXY` ao vivo (inverso ao BTC) |
| **Cripto** | tickers normais | tickers normais | ✅ tempo real | ✅ tempo real |

> Anotar sempre na sessão qual ticker foi usado e por quê (ex: `S&P: ES1! [NYSE fechada]`)

---

### Workflow A — Classe BTC / BTC+ETH (10 passos — COMPLETO)

**Aplicar quando:** Classe = `BTC` | `BTC+ETH` | `DAILY` | `CYCLE`

Para CADA ativo, executar: `chart_set_symbol` → `chart_set_timeframe("D")` → `quote_get` → `data_get_study_values`

| Passo | Ticker | Fallback | Observação |
|-------|--------|----------|------------|
| 1 | `USDT.D` | — | Sempre disponível |
| 2 | `SPX` | `ES1!` | NYSE fechada ou fim de semana → ES1!; **ao vivo após Dom 19h** |
| 3 | `GOLD` | `XAUUSD` | |
| 4 | `DXY` | — | Congelado Sáb–Dom19h; **reabre/ao vivo após Dom 19h** (inverso ao BTC) |
| 5 | `TOTAL` | — | Sempre disponível |
| 6 | `TOTAL2` | — | Sempre disponível |
| 7 | `TOTAL3` | — | Sempre disponível |
| 8 | `BRENT` | — | Petróleo padrão; congelado Sáb–Dom19h, **ao vivo após Dom 19h** |
| 9 | `BTCUSDLONGS` | — | Sempre disponível |
| 10 | `BTCUSDSHORTS` | — | Sempre disponível |

**Depois:** Montar tabela de correlações completa (10 linhas), calcular ratio L/S, definir regime e squeeze risk, SÓ ENTÃO analisar BTC/ETH.

---

### Workflow B — Classe ALTCOIN (5 passos — REDUZIDO)

**Aplicar quando:** Classe = `ALTCOIN` (análise solo de altcoin)

| Passo | Ticker | Fallback | Observação |
|-------|--------|----------|------------|
| 1 | `USDT.D` | — | Obrigatório — métrica inversa cripto |
| 2 | `BTC.D` | — | Dominância BTC vs altcoins |
| 3 | `TOTAL3` | — | Market cap altcoins menores |
| 4 | `BTCUSD` | — | Bias BTC (chart, não só quote) |
| 5 | `{ALT}BTC` | — | Par altcoin vs BTC (ex: SOLBTC, ADABTC, DOGEBTC) |

**Depois:** Montar tabela reduzida (5 linhas), declarar BTC bias, SÓ ENTÃO analisar a altcoin.

---

### Workflow C — Classe BTC+ALTCOIN (7 passos — PARCIAL)

**Aplicar quando:** Classe = `BTC+ALTCOIN` (BTC + altcoin específica juntos)

| Passo | Ticker | Fallback | Observação |
|-------|--------|----------|------------|
| 1 | `USDT.D` | — | Obrigatório |
| 2 | `BTC.D` | — | Dominância |
| 3 | `TOTAL3` | — | Altcoins |
| 4 | `BTCUSD` | — | Chart completo do BTC |
| 5 | `BTCUSDLONGS` | — | Posicionamento |
| 6 | `BTCUSDSHORTS` | — | Posicionamento |
| 7 | `{ALT}BTC` | — | Par altcoin vs BTC (força relativa) |

**Depois:** Calcular ratio L/S (obrigatório), definir BTC bias, SÓ ENTÃO → analisar BTC → depois a altcoin como relativo.

---

### Workflow D — Classe EQUITIES (5 passos — TRADFI)

**Aplicar quando:** Classe = `EQUITIES`

| Passo | Ticker | Fallback | Observação |
|-------|--------|----------|------------|
| 1 | `DXY` | — | Força do dólar |
| 2 | `SPX` | `ES1!` (NYSE fechada) | Ver Step 0 |
| 3 | `VIX` | — | Volatilidade / medo-ganância |
| 4 | ETF do setor | `XLK` tech \| `XLF` financeiro \| `XLE` energia \| `XLV` saúde \| `XLB` materiais \| `XLY` consumo \| `XLRE` imóveis | Conforme o setor do ativo |
| 5 | `GOLD` | `XAUUSD` | Safe haven / apetite de risco |

**⛔ NÃO usar:** USDT.D, TOTAL, TOTAL2, TOTAL3, BTCUSDLONGS, BTCUSDSHORTS

**Depois:** Montar tabela TradFi (5 linhas), declarar regime SPX/DXY/VIX, SÓ ENTÃO analisar o ativo.

---

### Regras de Leitura Macro

1. **Risk-On:** DXY↓ + S&P↑ + USDT.D↓ + TOTAL↑ → BTC bullish.
2. **Risk-Off:** DXY↑ + S&P↓ + USDT.D↑ + Ouro↑ → BTC bearish.
3. **Divergência macro:** BTC↑ mas DXY↑ e TOTAL2/3↓ → rally frágil, não confiar.
4. **Petróleo (`BRENT`) em alta forte:** pressão inflacionária → Fed hawkish → risco médio p/ cripto.
5. **TOTAL vs TOTAL2 vs TOTAL3:** TOTAL↑ mas TOTAL3↓ → dinheiro em BTC/ETH, altcoins em risco.
6. **BTCUSDLONGS vs SHORTS (squeeze):** Long Squeeze Risk = longs em extremo + shorts em mínima + preço esticado↑. Short Squeeze Risk = shorts subindo/extremo + longs estáveis/caindo + preço em resistência. Ratio L/S >5 = vulnerável a long squeeze; <1 = combustível p/ short squeeze. Divergências: preço↑ mas longs↓ = rally sem convicção (smart money saindo); preço↓ mas shorts↓ = vendedores desistindo, fundo próximo.
7. **Fim de semana:** TradFi congelado **somente Sex 18h → Dom 19h BRT** → reduzir peso de SPX/DXY/GOLD/Petróleo e rotular `macro-parcial (dados sex)`. **A partir de Dom 19h, `ES1!`/`DXY`/`BRENT` voltam ao vivo e são obrigatórios** (sem penalidade de fim de semana).

### Como registrar na sessão
- Declarar: `Contexto: [hora] | NYSE: ABERTA/FECHADA | CME: ABERTO/FECHADO | Workflow: A/B/C/D`
- Declarar: `Macro: Risk-On/Off/Misto | DXY: bull/bear/neutro | S&P: bull/bear/neutro`
- Cripto contradiz o macro → reduzir confiança e rotular `contra-macro`
- Fim de semana (Sáb 00h → Dom 19h) → rotular macro TradFi como `macro-parcial (dados sex)`
- Dom 19h em diante → declarar `⏰ Dom pós-19h: ES1!/DXY/BRENT ao vivo (reabertura)` e analisar os 3 obrigatoriamente (sem rótulo de congelado)

---

## 📋 Checklist de Análise Técnica Obrigatória

**TODA análise DEVE seguir este checklist completo — ler os conceitos da wiki e aplicar cada framework sistematicamente. Pular frameworks é PROIBIDO. Se um não se aplica, declarar "N/A" com justificativa.**

### Fase 1 — Leitura de Contexto (antes de olhar o chart)
1. Ler `wiki/brain/insights.md` — aplicar insights validados
2. Ler `wiki/brain/mistakes.md` — evitar erros já cometidos
3. Ler `wiki/brain/indicators.md` — calibrar peso de RSI, MACD, EMA, ADX, CHoCH/BOS
4. Ler `wiki/brain/patterns.md` — aplicar padrões recorrentes
5. Ler `wiki/assets/{SYMBOL}.md` — contexto histórico do ativo
6. Referenciar sessão anterior do mesmo ativo → declarar o que mudou estruturalmente

### Fase 2 — Multi-Timeframe (top-down obrigatório)
Ref: [[multi-timeframe-analysis]]
Ordem de leitura: **M → W → D → 4H → 1H → 15M**. O M é o âncora de ciclo — limita o upside/downside de TODOS os TFs abaixo (inclusive o W).
1. **Mensal (M) — macro de ciclo:** Tendência primária de ciclo (HH/HL ou LH/LL), RSI mensal, MACD mensal vs zero, EMA macro. Define teto/piso de ciclo e **alvos mensais**. **Obrigatório no macro (CYCLE/swing/classes BTC/BTC+ETH/ALTCOIN/EQUITIES); recomendado em scalp puro intraday.**
2. **Semanal (W):** Regime de mercado (Bull/Bear dentro do ciclo), RSI/MACD semanal, EMA 200
3. **Diário:** Ciclo secundário, sobrecompra/venda estrutural
4. **4H:** Filtro direcional (EMA 200 = above→Long only / below→Short only), ADX, estrutura
5. **1H:** Zona de entrada, FVG, OB, divergências RSI
6. **15M/5M:** Gatilho de execução, BOS de confirmação

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
> **M e W em RSI/StochRSI/MACD são OBRIGATÓRIOS no macro** (CYCLE/swing/classes BTC/BTC+ETH/ALTCOIN/EQUITIES); recomendados em scalp. M tem peso de ciclo acima do W; W acima do D/4H.
1. **RSI (14):** valor + zona (>70 OB / <30 OS) + direção da linha + cruzamento RSI×SMA(RSI) (up=bullish / down=bearish).
   - **M (macro de ciclo):** valor+zona+direção+cruzamento de 50. Define teto/piso de momentum do CICLO e alvos mensais; divergência mensal = reversão de ciclo (peso máximo).
   - **W (regime):** valor+zona+direção. Limita upside/downside dos TFs menores; divergência semanal = reversão de alto peso.
   - **Divergências M/W/D/4H/1H:** bearish preço HH+RSI LH | bullish preço LL+RSI HL. RSI>70 em M/W/D = teto de retração.
2. **Stoch RSI:** %K/%D valores + cruzamento (%K×%D up=bullish / down=bearish) + zona (>80 OB / <20 OS) + direção.
   - **W (OBRIGATÓRIO):** %K/%D+zona. Reset semanal de OS/OB = virada de ciclo; confirma/nega o timing dos TFs menores. _(StochRSI mensal só contextual; timing fica em W/1H/15M.)_
   - **Divergências (1H/15M):** preço HH+%K LH em >80 = bearish | preço LL+%K HL em <20 = bullish. Reset OS em alta / OB em baixa = continuação.
   **⚠️ RSI+StochRSI combinado (Ref: [[rsi-stochrsi-combined]]):** RSI (M/W/D/4H) define DIREÇÃO (>50 Long only / <50 Short only); StochRSI (1H/15M) define TIMING (cross em zona extrema). **NUNCA operar StochRSI contra o RSI HTF** (OB+RSI bull=continuação, não shortear; OS+RSI bear=continuação, não longear).
3. **MACD (12/26/9):** posição vs zero (acima=comprador / abaixo=vendedor) + cruzamento×Signal (acima de zero=bullish mais forte) + histograma (crescente/decrescente).
   - **M (macro):** cruzamento mensal vs zero = virada de regime de CICLO (prioridade sobre o semanal).
   - **W:** cruzamento semanal vs zero = mudança de regime de momentum (prioridade sobre TFs menores).
   - **Divergências M/W/D/4H:** preço HH+MACD LH=bearish | preço LL+MACD HL=bullish (hist. ou linhas). Cross sem volume = fraco → aguardar confirmação.
4. **ADX (14):** >25 tendência forte (respeitar direção) | <20 range (aguardar). DI+>DI- bullish / DI->DI+ bearish.
5. **EMA 50/200:** posição+cruzamento (Golden/Death Cross)+inclinação. Ciclo: EMA mensal e 200W SMA = teto/piso (preço vs 200W define fundo de ciclo não tocado).
6. **Volume/OBV:** POC magneto, HVN S/R. Divergências Vol×Preço: preço↑+vol↓=rally fraco | preço↓+vol↓=queda enfraquecendo. OBV: preço HH+OBV LH=distribuição | preço LL+OBV HL=acumulação.

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
3. **Funding Rate + OI + Fear&Greed:** **rodar `python3 scripts/tools/fetch_feeds.py` se o cache estiver `indisponível` ou com timestamp > 2h, depois ler** `raw/feeds/latest.md` (o script carrega o `.env` sozinho). Consumir os valores REAIS de funding/OI de BTC e ETH — não estimar. Só se o refresh FALHAR (rede/erro) → penalidade `dados-parciais` (Fase 9)
4. **BTCUSDLONGS + BTCUSDSHORTS (obrigatório para BTC/ETH):**
   - Consultar `BTCUSDLONGS` → valor atual, tendência (subindo/caindo/lateral), nível relativo (alto/médio/baixo)
   - Consultar `BTCUSDSHORTS` → valor atual, tendência, nível relativo
   - Calcular Ratio L/S = BTCUSDLONGS / BTCUSDSHORTS
   - Avaliar risco de squeeze: `Long Squeeze Risk` (ratio > 5 + longs em extremo) ou `Short Squeeze Risk` (ratio < 1 + shorts subindo)
   - Cruzar com Funding/OI (de `raw/feeds/latest.md`): FR muito positiva + Longs extremos, ou OI alto + Ratio extremo = squeeze de alta probabilidade
5. Declarar: `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega | Longs/Shorts: [ratio] [squeeze risk]`

### Fase 9 — Declaração de Bias Final
1. Sintetizar todas as fases acima em um bias claro: **LONG / SHORT / NEUTRO**
2. **Calcular o Confluence Score (0–10)** — ver [[confluence-score]]. Listar critérios que pontuaram e penalidades aplicadas (ex: `Score 7/10 = 1,3,5,6,7,8 ✓ | −2 contra-macro`)
3. Declarar confiança DERIVADA do score: **≥8 = alta | 6–7 = média | 4–5 = baixa | <4 = NEUTRO** (não usar "feeling")
4. Aplicar a tabela score→ação para o TAMANHO: ≥8 cheia | 6–7 reduzida | 4–5 só observar/paper | <4 não operar
5. Se bias contradiz macro → rotular `contra-macro` e aplicar penalidade −2 no score
6. Se o refresh de feeds FALHOU (rede/erro) ou `raw/feeds/latest.md` segue `indisponível`/ausente → **−1 no score** + rótulo `dados-parciais` (não assumir funding/OI que não foram lidos). Dados puxados com sucesso → SEM penalidade
7. Se nenhum framework converge → declarar `NEUTRO — sem confluência` (score < 4)
8. **Checar disciplina:** se `brain/metrics.md` indicar circuit breaker 🔴 → rebaixar para observação ([[trading-psychology]])

### Como escrever na sessão (adaptar por classe)

**Todas as classes:**
- `Classe: BTC | BTC+ETH | ALTCOIN | EQUITIES | WATCHLIST | DAILY`
- `MTF: M/W/D/4H/1H → [resumo]` (DAILY: D+4H, mas citar o M no contexto de ciclo)
- `Indicadores: RSI [M/W/D/4H/1H valores+direção] | StochRSI [W/1H/15M %K/%D+cross] | MACD [M/W/D/4H vs zero+cross+hist] | ADX [valor]`
- `Bias: LONG/SHORT/NEUTRO | Confiança: alta/média/baixa`

**BTC / BTC+ETH — adicionar:**
- `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega`
- `Derivativos: BTC FR [valor] OI [valor] | ETH FR [valor] OI [valor] | F&G [valor]` (de raw/feeds/latest.md)
- `Longs/Shorts: BTCUSDLONGS [valor] | BTCUSDSHORTS [valor] | Ratio [X.X] | Squeeze Risk: [nível]`
- (BTC+ETH) `ETH/BTC: [valor] [outperform/underperform] [%]`

**BTC+ALTCOIN — adicionar:**
- `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega`
- `Derivativos: BTC FR [valor] OI [valor] | F&G [valor]` (de raw/feeds/latest.md)
- `Longs/Shorts: Ratio [X.X] | Squeeze Risk: [nível]`
- `{ALT}/BTC: [valor] [outperform/underperform] [%]`
- `Tipo: scalp | swing`

**ALTCOIN — adicionar:**
- `Setor: DeFi/AI/L2/meme/infra | Par/BTC: [subindo/caindo] | BTC.D: [valor] [tendência]`
- `Sentimento: F&G [valor]` (de raw/feeds/latest.md; funding default cobre BTC/ETH)
- `Tipo: scalp | swing | holder`

**EQUITIES — adicionar:**
- `VIX: [valor] [tendência] | Setor ETF: [ticker] [tendência] | Earnings: [data ou N/A]`

**WATCHLIST — usar tabela:**
- `| Ativo | Preço | Bias | Confiança | Setup? | Nota |`

**DAILY — usar dashboard:**
- `Macro: Risk-On/Off/Misto | BTC: [bias] | Alertas: [N] | Previsões abertas: [N]`

---

## Decision Tree — Which Tool When

- **Ler chart:** `chart_get_state` (symbol/TF/IDs dos indicadores — chamar 1×) → `data_get_study_values` (valores numéricos dos indicadores visíveis) → `quote_get` (snapshot de preço/OHLC/vol).
- **Pine custom drawings** (line/label/table/box — invisíveis aos tools normais; indicador precisa estar visível): `data_get_pine_lines` (níveis), `data_get_pine_labels` (texto+preço), `data_get_pine_tables` (linhas), `data_get_pine_boxes` ({high,low}). Usar `study_filter` p/ alvejar um indicador.
- **Price data:** `data_get_ohlcv` (sempre `summary: true`; `count` limita) | `quote_get` (último preço).
- **Mudar chart:** `chart_set_symbol` | `chart_set_timeframe` | `chart_set_type` | `chart_manage_indicator` (nome completo) | `chart_scroll_to_date` | `chart_set_visible_range` | `indicator_set_inputs`.
- **Pine Script:** `pine_set_source` → `pine_smart_compile` → `pine_get_errors`/`pine_get_console` | `pine_save`/`pine_new`/`pine_open`. ⚠️ evitar `pine_get_source` (200KB+).
- **Desenhar:** `draw_shape` (horizontal_line/trend_line/rectangle/text) | `draw_list` | `draw_remove_one` | `draw_clear`.
- **Alertas:** `alert_create` (crossing/greater_than/less_than) | `alert_list` | `alert_delete`.
- **UI:** `ui_open_panel` | `ui_click` | `layout_switch` | `ui_fullscreen` | `capture_screenshot` (full/chart/strategy_tester).
- **TV offline:** `tv_launch` | `tv_health_check`.

## Context Management Rules

Evitar context bloat: (1) `data_get_ohlcv` sempre com `summary: true` salvo se precisar de barras individuais; (2) usar `study_filter` nos pine tools; (3) nunca `verbose: true` salvo pedido explícito; (4) evitar `pine_get_source` em scripts complexos (200KB+); (5) evitar `data_get_indicator` em indicadores protegidos — usar `data_get_study_values`; (6) preferir `capture_screenshot` (~300KB) a puxar datasets grandes; (7) `chart_get_state` só 1× no início; (8) cap OHLCV: `count: 20` rápida / `100` profunda / `500` só quando necessário.

## Tool Conventions

- Tools retornam `{ success: true/false, ... }`. Entity IDs (`chart_get_state`) são por sessão — não cachear.
- Pine indicators precisam estar **visíveis** para os pine graphics tools lerem.
- `chart_manage_indicator` exige **nome completo**: "Relative Strength Index" (não "RSI"), "Moving Average Exponential" (não "EMA"), "Bollinger Bands" (não "BB").
- Screenshots → `screenshots/` com timestamp. OHLCV cap 500 barras, trades 20/req. Pine labels cap 50/study (override via `max_labels`).

## Architecture

```
Gemini CLI ←→ MCP Server (stdio) ←→ CDP (localhost:9222) ←→ TradingView Desktop (Electron)
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
2. **Grading objetivo (regra, não opinião):** com `data_get_ohlcv` buscar o range real desde a data da previsão e comparar com os campos `Entrada/SL/TPs`
3. Marcar pela regra: **TP antes do SL = ✅ | SL antes do TP = ❌ | nenhum no prazo = ⚪**. Se ⚪, preencher `Pós-fecho:` pela direção na expiração (a favor=certa / contra=errada / neutra)
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
5. **Rodar `python scripts/tools/archive_brain.py`** → mantém Top N insights em `insights.md` (recência + validações) e arquiva o resto em `brain/insights-archive/YYYY-MM.md`
6. Identificar conceitos mencionados em `raw/clippings/` mas sem página `wiki/concepts/` própria
7. **Regenerar `wiki/library.md`** — garantir que todos os clippings estejam linkados no Graph View
8. **Rodar `python scripts/tools/wiki_lint.py`** → gera `wiki/lint/YYYY-MM-DD.md` (wikilinks quebrados, previsões expiradas, setups sem stats) e atualiza contadores do `index.md`
9. **Rodar `python scripts/tools/metrics_engine.py`** → recalcula `brain/metrics.md` e as métricas globais de `setups/index.md`
10. Append em `wiki/log.md`: `## [YYYY-MM-DD] lint | {N} issues encontrados`

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
7. **Métricas numéricas reais** (win rate, drawdown, Sharpe, R:R) → gravar SOMENTE em `brain/metrics.md` + `wiki/setups/index.md` (ambos gitignored). ⚠️ NÃO escrever números de performance pessoal nos arquivos `wiki/strategies/*.md` (são versionados/públicos): manter a tabela "Performance Histórica" como placeholder qualitativo apontando para `[[metrics]]`.
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
3. Executar `scripts/tools/plot_accuracy.py` + `scripts/tools/plot_metrics.py` (calibração de confiança e win rate por lado/regime) para gerar os gráficos em `wiki/outputs/charts/`
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
