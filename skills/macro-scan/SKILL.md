---
name: macro-scan
description: Scan macro obrigatório ANTES de analisar qualquer ativo — detecta o contexto de mercado (horário BRT, NYSE/CME/Forex abertos, reabertura Dom 19h), executa o Workflow da classe (A=BTC/BTC+ETH completo 10 passos · B=ALTCOIN reduzido 6 · C=BTC+ALTCOIN parcial 8 · D=EQUITIES TradFi) com os fallbacks de ticker, e aplica as Regras de Leitura Macro (Risk-On/Off, squeeze L/S, fim de semana). Use depois do brain-read e antes do technical-checklist.
---

# Macro Scan — Pré-requisito de qualquer análise

> O macro contexto define o viés primário. **DEVE** `chart_set_symbol` para cada ativo — NÃO usar
> apenas `quote_get` (o parâmetro `symbol` é ignorado, retorna o chart ativo). Detalhe de tools em
> `skills/_references/tv-tools.md`.

## Step 0 — Detector de Contexto de Mercado (SEMPRE PRIMEIRO)

| | Status |
|--|--------|
| **Horário BRT + Dia** | [HH:MM] \| [Seg…Dom] |
| **NYSE** | ABERTA (Seg-Sex 10:30–17:00 BRT / inverno 11:30–18:00) ou FECHADA |
| **CME** | ABERTO (quase 24h) ou FECHADO (Sex 18h BRT → Dom 19h BRT) |
| **Forex/DXY** | DISPONÍVEL (Seg 00h – Sex ~22h BRT) ou CONGELADO (Sex ~22h → **Dom 19h BRT**) |

**Fim de semana (Sex 18h → Dom 19h BRT):** CME/NYSE/Forex fechados → SPX/DXY/GOLD/BRENT
**congelados** (fechamento sexta). Declarar `⚠️ TradFi fechado — macro baseada no fechamento de
sexta. Cripto = único mercado ao vivo.` Focar USDT.D + TOTAL/2/3 + BTCUSDLONGS/SHORTS.

**🔓 Reabertura Dom 19h+:** `ES1!`, `DXY`, `BRENT` reabrem ao vivo → **OBRIGATÓRIO** analisá-los
(sem rótulo `congelado`). DXY = inverso ao BTC; ES1! risk-on; BRENT inflação. Declarar
`⏰ Dom pós-19h: ES1!/DXY/BRENT ao vivo (reabertura)`.

### Fallbacks por estado de mercado

| Ativo | Normal | NYSE Fechada | Fim de Semana | Dom 19h+ |
|-------|--------|--------------|---------------|----------|
| S&P 500 | `SPX` | `ES1!` | ⚠️ `ES1!` (congelado) | ✅ `ES1!` ao vivo |
| Ouro | `GOLD` | `XAUUSD` | ⚠️ `XAUUSD` (congelado) | ✅ `XAUUSD` ao vivo |
| Petróleo | `BRENT` | `BRENT` | ⚠️ `BRENT` (congelado) | ✅ `BRENT` ao vivo |
| Dólar | `DXY` | `DXY` | ⚠️ `DXY` (congelado) | ✅ `DXY` ao vivo (inverso) |
| Cripto | normais | normais | ✅ tempo real | ✅ tempo real |

> Anotar sempre qual ticker foi usado e por quê (ex: `S&P: ES1! [NYSE fechada]`).
> Para cada ticker: `chart_set_symbol` → `chart_set_timeframe("D")` → `quote_get` → `data_get_study_values`.

## Step 0.5 — Briefing macro do dia (input de eventos)

> O Step 0 lê tickers (USDT.D/DXY/SPX/Longs-Shorts) = macro **estrutural**. Este step traz o macro
> de **eventos** (calendário/ETF/black-swan), que o chart não enxerga. Vem do briefing já garantido
> pelo gate de `brain-read` (passo 2b) — aqui **não** se roda busca web; só se consome.

1. Ler `wiki/briefings/{hoje}.md` (data BRT): o `🔴 EVENTOS DE ALTO IMPACTO` + o `=== VEREDITO ===`.
2. Fundir no regime: a `Postura sugerida` e o `Risco direcional 24h/7d` entram como input macro de
   eventos, **ao lado** das Regras de Leitura Macro baseadas em ticker (abaixo).
3. Se ausente (gate não rodou por algum motivo) → rótulo `briefing-ausente` e seguir só com tickers.

## Step 1.5 — Roteamento de Liquidez + Fase de Rotação (OBRIGATÓRIO onde aplicável)

> Doutrina: [[liquidity-rotation-cycle]]. Antes do bias, **selecionar a combinação de índices certa
> para o target** e classificar onde a liquidez sistêmica está. Emite o **Veredito de Rotação de
> Liquidez** (saída) + o critério `liq-rotacao±` (Confluence Score). É **camada de confirmação**, não
> reclassifica o ativo (ETH segue Workflow A).

**1) Mapa target → índices (puxar via `chart_set_symbol` → `data_get_study_values`):**

| Target | Índice base | Índice de confirmação (ES = sem stablecoins) |
|--------|-------------|-----------------------------------------------|
| **ETH** | `BTC.D` | `TOTAL2ES` (cap total ex-BTC, ex-stables) |
| **Altcoin menor** (≠BTC,≠ETH) | `BTC.D` | `TOTAL3ES` (cap total ex-BTC, ex-ETH, ex-stables) |
| **BTC-solo** | `BTC.D` + `USDT.D` | — (só classificador de fase; **não** forçar TOTAL2ES/3ES) |
| **EQUITIES** | — | **N/A** (declarar `Rotação liq: N/A`; não puxar índices cripto) |

**2) Regra de validação (força do target):**
- **ETH forte** = `BTC.D` falhando suporte / em tendência de baixa **E** `TOTAL2ES` ganhando momentum
  de alta. Se BTC.D sobe junto = a "força" do ETH é só beta de BTC → rebaixar.
- **Altcoin forte** = `BTC.D` em queda **+** ETH lateral/subindo com menos força **+** `TOTAL3ES`
  rompendo resistência ou expansão de volatilidade. Cruza com a medição dupla ALT/BTC ([[class-rules]]).

**3) Índice-TA anti-bull-trap (rodar RSI/MACD/Bollinger/Fib NO gráfico do índice ES, não só no ativo):**
- **RSI:** exaustão macro de capital — **não validar compra** se o índice ES estiver em sobrecompra
  forte. Simétrico: índice ES em sobrevenda profunda = risco de **bear-trap**/capitulação (não chase short).
- **MACD:** cruzamento + histograma no índice = entrada/saída real de capital confirmando a tendência.
- **Bollinger:** squeeze (compressão) antecede explosão de liquidez; rompimento da banda superior do
  índice = fluxo direcional forte.
- **Fibonacci:** retrações/extensões no índice mapeiam alvos macro onde a liquidez tende a secar/reverter.

**4) Classificador de Fase do Ciclo de Liquidez** (consome Step 0/1.5 — **não** repete as Regras 5/9/10):
- **Migração para BTC:** `BTC.D`↑ + `USDT.D` estável/baixo → capital concentra em BTC (alts sangram).
- **Rotação para ETH:** `BTC.D`↓ + `TOTAL2ES`↑ com `TOTAL3ES` lateral → dinheiro sai de BTC p/ ETH.
- **Altseason (TOTAL3ES):** `BTC.D`↓ + `TOTAL3ES`↑ + `OTHERS`↑ → risco se espalha p/ small-caps.
- **Fuga para Stablecoins:** `USDT.D`↑ domina (risk-off) → liquidez sai de tudo p/ stables.

## Workflow A — BTC / BTC+ETH / DAILY / CYCLE (10 passos — COMPLETO)

1 `USDT.D` · 2 `SPX`(→ES1!) · 3 `GOLD`(→XAUUSD) · 4 `DXY` · 5 `TOTAL` · 6 `TOTAL2` · 7 `TOTAL3`
· 8 `BRENT` · 9 `BTCUSDLONGS` · 10 `BTCUSDSHORTS`.
**Depois:** tabela de correlações (10 linhas), ratio L/S, regime + squeeze risk → SÓ ENTÃO BTC/ETH.
> **Rota de liquidez (se o target inclui ETH):** somar `BTC.D` + `TOTAL2ES` (Step 1.5). Os TOTAL/2/3
> aqui são o scan amplo (Regra 5); o **ES** (sem stablecoins) é o índice de confirmação da rota ETH.

## Workflow B — ALTCOIN (6 passos — REDUZIDO)

1 `USDT.D` · 2 `BTC.D` · 3 `TOTAL3ES` · 4 `OTHERS` (apetite small-cap) · 5 `BTCUSD` (chart) ·
6 `{ALT}BTC` (par). ⚠️ **Medição DUPLA: ler `{ALT}USDT` E `{ALT}BTC`** (força absoluta × relativa).
**Depois:** tabela reduzida, BTC bias + **HTF block** → SÓ ENTÃO a altcoin. (Rota de liquidez:
`BTC.D` + `TOTAL3ES` = índice de confirmação — Step 1.5.)

## Workflow C — BTC+ALTCOIN (8 passos — PARCIAL)

1 `USDT.D` · 2 `BTC.D` · 3 `TOTAL3ES` · 4 `OTHERS` · 5 `BTCUSD` · 6 `BTCUSDLONGS` · 7 `BTCUSDSHORTS` ·
8 `{ALT}BTC`. ⚠️ **ler `{ALT}USDT` E `{ALT}BTC`**.
**Depois:** ratio L/S (obrigatório), BTC bias + **HTF block** → BTC → altcoin como relativo.

## Workflow D — EQUITIES (5 passos — TRADFI)

1 `DXY` · 2 `SPX`(→ES1!) · 3 `VIX` · 4 ETF do setor (`XLK`/`XLF`/`XLE`/`XLV`/`XLB`/`XLY`/`XLRE`) · 5 `GOLD`(→XAUUSD).
**⛔ NÃO usar:** USDT.D, TOTAL/2/3, BTCUSDLONGS/SHORTS. **Depois:** tabela TradFi (5 linhas),
regime SPX/DXY/VIX → SÓ ENTÃO o ativo.

## Regras de Leitura Macro

1. **Risk-On:** DXY↓ + S&P↑ + USDT.D↓ + TOTAL↑ → BTC bullish.
2. **Risk-Off:** DXY↑ + S&P↓ + USDT.D↑ + Ouro↑ → BTC bearish.
3. **Divergência macro:** BTC↑ mas DXY↑ e TOTAL2/3↓ → rally frágil.
4. **BRENT em alta forte:** pressão inflacionária → Fed hawkish → risco médio p/ cripto.
5. **TOTAL vs TOTAL3:** TOTAL↑ mas TOTAL3↓ → dinheiro em BTC/ETH, altcoins em risco.
6. **BTCUSDLONGS vs SHORTS (squeeze):** Long Squeeze Risk = longs extremo + shorts mínima + preço
   esticado↑. Short Squeeze Risk = shorts subindo/extremo + longs estáveis/caindo + preço em
   resistência. Ratio L/S >5 = vulnerável a long squeeze; <1 = combustível p/ short squeeze.
   Divergências: preço↑ mas longs↓ = rally sem convicção; preço↓ mas shorts↓ = vendedores desistindo.
7. **Fim de semana:** Sex 18h → Dom 19h: TradFi congelado → reduzir peso de SPX/DXY/GOLD/BRENT,
   rótulo `macro-parcial (dados sex)`. **Dom 19h+: ES1!/DXY/BRENT ao vivo e obrigatórios.**
8. **Evento macro iminente (do briefing — Step 0.5):** se o briefing marca evento 🔴
   (FOMC/CPI/NFP/PCE/Powell) dentro da janela da operação → **rebaixar confiança** e rotular
   `pré-evento (X)`; a postura tende a `aguardar evento`. Conflito entre a leitura de ticker e o
   Veredito do briefing → **declarar a divergência, não forçar conclusão**.
9. **Acumulação/Distribuição Cíclica (fluxo institucional — [[institutional-flow-poi]]):**
   *Fundo de ciclo* = sobrevenda Semanal/Mensal + DXY enfraquecendo + USDT.D em recuo + shorts
   extremos/funding negativo (combustível de short squeeze) → setup de acumulação institucional.
   *Topo de ciclo* = sobrecompra Semanal/Mensal + DXY forte + USDT.D subindo + longs extremos/funding
   positivo (long squeeze) → setup de distribuição. Cruzar com a Regra 6 (squeeze L/S).
10. **Força dupla de altcoin (B/C) — ver `[[class-rules]]`:** ler ALT/USDT × ALT/BTC (ALT/BTC↑ =
    força real · ALT/BTC↓ com USDT↑ = fake-pump → rebaixar · ALT/USDT↓ + ALT/BTC↑ = acumulação).
    **`HTF_BEARISH_HARD_BLOCK` absoluto:** BTC HTF bearish-hard → **nenhum long em altcoin, inclusive
    scalp**. Beta vs BTC dimensiona size/leverage; OTHERS = apetite small-cap.
11. **Roteamento de liquidez (Step 1.5 — [[liquidity-rotation-cycle]]):** classificar a **Fase**
    (Migração BTC / Rotação ETH / Altseason / Fuga Stablecoins) e validar o target pelo par
    `BTC.D` + índice ES (`TOTAL2ES` p/ ETH, `TOTAL3ES` p/ alt). Esta regra é o **classificador que
    consome** as leituras das Regras 5 (TOTAL vs TOTAL3), 9 (acum/distrib cíclica) e 10 (força dupla)
    — **não as repete**. Índice ES em sobrecompra macro contra um LONG (índice-TA) ⇒ `Alto Risco de
    Bull Trap` (penalidade `bull-trap-liquidez`, ver `[[confluence-score]]`). Target = EQUITIES → `N/A`.
12. **Regime Macro (MACD 1W — [[macd]]):** ler o MACD no Semanal do BTC (`chart_set_symbol("BTCUSD")`
    → `chart_set_timeframe("W")` → `data_get_study_values`). **> 0 = regime BULL** (longs favorecidos)
    · **< 0 = regime BEAR** (shorts favorecidos) · **cruzamento fresco da linha zero = Transição**
    (regime neutro, não pontua). Filtro de tendência consolidada (lagging) — direção de maior
    probabilidade p/ swing, **não** timing de topo/fundo. Emite `macd-regime+` (bias alinhado) /
    `contra-regime` (−1, bias contra — ver `[[confluence-score]]`). Altcoins/ETH herdam o regime do
    BTC (via âncora HTF); **EQUITIES = N/A**. Sem chart → `DADO_INDISPONIVEL` (não inventar).

## Registrar na sessão

- `Contexto: [hora] | NYSE: …| CME: …| Workflow: A/B/C/D`
- `Macro: Risk-On/Off/Misto | DXY: bull/bear/neutro | S&P: bull/bear/neutro | Regime 1W: Bull/Bear/Transição`
- `Briefing: [postura sugerida] | 🔴 janela: [evento ou —]` (do Step 0.5)
- Cripto contradiz o macro → reduzir confiança e rotular `contra-macro`.

### Veredito de Rotação de Liquidez (obrigatório p/ cripto; EQUITIES → `N/A`)
Bloco compacto de 4 linhas (Step 1.5) que **alimenta** o Confluence Score (não substitui a Fase 9):
1. **Fase do Ciclo de Liquidez:** [Migração BTC / Rotação ETH / Altseason (TOTAL3ES) / Fuga Stablecoins].
2. **Leitura dos Índices Macro:** `BTC.D [dir/nível]` + `TOTAL2ES/3ES [dir/momentum]` (status cruzado) + `Regime 1W [Bull>0 / Bear<0 / Transição]` (Regra 12).
3. **Confluência Técnica (no índice ES):** `RSI [val/zona] | MACD [cross/hist] | Boll [squeeze/break] | Fib [retração/alvo]`.
4. **Veredito Estratégico:** **Cenário Otimizado** / **Neutro** / **Alto Risco de Bull Trap** p/ o target.
→ emite o critério `liq-rotacao+` (Otimizado alinhado) / `-liq-rotacao` ou `bull-trap-liquidez` (contra).

> Próximo passo: `technical-checklist`.
