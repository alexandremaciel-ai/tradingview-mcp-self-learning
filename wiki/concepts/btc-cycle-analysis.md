# Análise de Ciclo do Bitcoin — Framework Completo

> Criado: 2026-05-28
> Categoria: Macro Cycle / On-Chain / Fractal Analysis
> Uso: Framework obrigatório para identificar topos em bull market e fundos em bear market
> Prioridade: **Indicadores e análise gráfica > Tempo do ciclo**

## Filosofia

O tempo do ciclo (halving-based) é um contexto importante, mas **NÃO é o driver principal**. Ciclos são confirmados por:
1. **Indicadores on-chain** (MVRV, NUPL, Puell, Realized Price) — peso 40%
2. **Análise técnica** (price action, RSI semanal, volume, Wyckoff) — peso 30%
3. **Sentimento e posicionamento** (Fear & Greed, Funding, Exchange Reserves) — peso 20%
4. **Fractais temporais e halving** (referência, não predição) — peso 10%

> **Regra:** Nunca projetar topo ou fundo apenas por tempo. O tempo confirma ou nega, mas os indicadores DEFINEM.

---

## PARTE 1: Fractais Históricos — Anatomia dos Ciclos

### Dados de Referência

| Ciclo | Topo | Fundo | Drawdown | Topo→Fundo | Fundo→ATH |
|-------|------|-------|----------|------------|-----------|
| 1 (2011) | $31.91 (Jun 2011) | $2.01 (Nov 2011) | -93.7% | ~5 meses | ~13 meses |
| 2 (2013-15) | $1,177 (Nov 2013) | $152 (Jan 2015) | -87.1% | ~14 meses | ~34 meses |
| 3 (2017-18) | $19,783 (Dez 2017) | $3,122 (Dez 2018) | -84.2% | ~12 meses | ~23 meses |
| 4 (2021-22) | $69,000 (Nov 2021) | $15,476 (Nov 2022) | -77.6% | ~12 meses | ~15 meses |

### Padrões Observados

- **Drawdowns diminuindo:** -93% → -87% → -84% → -77% (média ~4-5pp por ciclo)
- **Topo→Fundo convergindo:** para ~12 meses (exceto ciclo 1 que era imaduro)
- **Recuperação acelerando:** 34m → 23m → 15m (ciclos mais eficientes)
- **Projeção para ciclo 5:** Drawdown esperado ~70-75% (se padrão continuar)

> ⚠️ **IMPORTANTE:** Fractais são guias, não garantias. Eventos cisne negro (Luna, FTX) podem distorcer o padrão. Usar como contexto, não como regra.

---

### Halving como Metrônomo (Referência Temporal)

| Halving | Data | Topo Pós-Halving | Meses Até Topo | Fundo do Bear | Meses Até Fundo |
|---------|------|------------------|----------------|---------------|-----------------|
| 1 | 28 Nov 2012 | $1,177 | ~12m | $152 | ~26m |
| 2 | 9 Jul 2016 | $19,783 | ~17m | $3,122 | ~29m |
| 3 | 11 Mai 2020 | $69,000 | ~18m | $15,476 | ~30m |
| **4** | **20 Abr 2024** | **$???** | **?** | **$???** | **?** |

**Projeções temporais (se padrão continuar):**
- Topo: 12-18 meses pós-halving → Abr 2025 – Out 2025
- Fundo: 28-32 meses pós-halving → Ago 2026 – Dez 2026

> 🔑 **Regra:** NÃO usar essas datas como previsão. Usar como janela de atenção para monitorar indicadores com mais frequência.

---

## PARTE 2: Indicadores de Fase de Ciclo (On-Chain)

### Prioridade dos Indicadores

| Indicador | Peso | Disponível no TV | Ticker/Indicador |
|-----------|------|-------------------|-----------------|
| **MVRV Z-Score** | ⭐⭐⭐ | Via indicador comunitário | Buscar "MVRV" nos indicadores |
| **NUPL** | ⭐⭐⭐ | Via indicador comunitário | Buscar "NUPL" nos indicadores |
| **Puell Multiple** | ⭐⭐⭐ | Via indicador comunitário | Buscar "Puell Multiple" |
| **200W SMA** | ⭐⭐⭐ | ✅ Nativo | SMA(200) no gráfico Semanal |
| **Realized Price** | ⭐⭐ | Via indicador comunitário | Buscar "Realized Price" |
| **Pi Cycle Top** | ⭐⭐ | Via indicador comunitário | 111DMA vs 350DMA×2 |
| **Hash Ribbons** | ⭐⭐ | Via indicador comunitário | Buscar "Hash Ribbons" |
| **Reserve Risk** | ⭐ | Via indicador comunitário | Buscar "Reserve Risk" |

### 2.1 MVRV Z-Score
Ref: [[mvrv-z-score]]

| Zona | Z-Score | Fase do Ciclo |
|------|---------|---------------|
| >7 | Extremo positivo | 🔴 TOPO — todos os topos históricos |
| 3-7 | Alto | 🟠 Bull maduro — início de distribuição |
| 1-3 | Moderado | 🟡 Neutro-bullish |
| 0-1 | Baixo | 🟢 Acumulação |
| <0 | Negativo | 🟢🟢 FUNDO — todos os fundos históricos |

**Regra de ciclo:** Se MVRV Z-Score < 0 e revertendo para cima → fundo formado ou formando.

### 2.2 NUPL (Net Unrealized Profit/Loss)
Ref: [[nupl]]

| Zona | NUPL | Emoção | Fase |
|------|------|--------|------|
| >0.75 | Euforia/Ganância | 🔴 Topo | DISTRIBUIÇÃO |
| 0.5-0.75 | Crença/Negação | 🟠 Bull maduro | MARKUP |
| 0.25-0.5 | Otimismo/Ansiedade | 🟡 Tendência confirmada | MARKUP INICIAL |
| 0-0.25 | Esperança/Medo | 🟢 Pós-fundo | ACUMULAÇÃO |
| <0 | Desespero | 🟢🟢 Capitulação | FUNDO |

**Regra de ciclo:** NUPL < 0 por semanas = capitulação. NUPL revertendo de <0 para >0 = fundo confirmado.

### 2.3 Puell Multiple

Mede a receita dos mineradores em relação à média de 365 dias.

| Zona | Puell | Interpretação |
|------|-------|--------------|
| >4 | Mineradores com receita extrema | 🔴 Topo — mineradores vendendo agressivamente |
| 1-4 | Receita saudável | 🟡 Neutro |
| 0.5-1 | Receita abaixo da média | 🟢 Acumulação |
| <0.5 | Mineradores em estresse | 🟢🟢 FUNDO — capitulação de mineradores |

**Regra de ciclo:** Puell < 0.5 + Hash Ribbons em capitulação = sinal histórico de fundo.

### 2.4 200W SMA (Média Móvel de 200 Semanas)

A 200W SMA é possivelmente o **indicador mais confiável de fundo de ciclo**.

**Fatos históricos:**
- Em **TODOS** os bear markets, o preço tocou ou caiu abaixo da 200W SMA
- 2015: preço caiu ~14% abaixo da 200W SMA
- 2018: preço caiu ~1% abaixo da 200W SMA
- 2022: preço caiu ~28% abaixo (evento Luna/FTX = cisne negro)

**Regra absoluta:**
> Se o preço NÃO tocou a 200W SMA neste ciclo → o fundo provavelmente ainda NÃO foi atingido.
> Se tocou e reverteu → candidato forte a fundo.

**Workflow MCP:**
```
chart_set_symbol({symbol: "BTCUSD"})
chart_set_timeframe({timeframe: "W"})
chart_manage_indicator({action: "add", name: "Moving Average"})  // configurar período 200
data_get_study_values()
```

### 2.5 Realized Price
Ref: [[realized-price]]

O "preço médio de compra de toda a rede". Funciona como suporte fundamental.

**Fatos históricos:**
- 2015: preço caiu ~20% abaixo do Realized Price
- 2018: preço caiu ~10% abaixo do Realized Price
- 2022: preço caiu ~15% abaixo do Realized Price

**Regra:** Preço abaixo do Realized Price = rede inteira está em prejuízo = capitulação final.

### 2.6 Pi Cycle Top Indicator

Usa o cruzamento entre 111DMA e 350DMA×2 para marcar topos de ciclo.

**Histórico:** Marcou topos de 2013, 2017 e 2021 com precisão de **dias**.

- 111DMA cruza acima de 350DMA×2 → **TOPO DE CICLO**
- Se não cruzaram ainda → topo pode não ter ocorrido

### 2.7 Hash Ribbons

Mede capitulação de mineradores via cruzamento de hash rate (30DMA vs 60DMA).

| Estado | Significado |
|--------|-------------|
| **Capitulação** | Hash rate 30DMA < 60DMA → mineradores desligando máquinas |
| **Recuperação** | Hash rate 30DMA volta acima de 60DMA → sinal de compra |
| **Expansão** | Hash rate em alta saudável |

**Regra de fundo:** Hash Ribbons saindo de capitulação → historicamente melhor sinal de compra macro.

### 2.8 STH/LTH Realized Price Ratio

- **STH Realized Price:** custo médio dos compradores recentes (<155 dias)
- **LTH Realized Price:** custo médio dos holders de longo prazo (>155 dias)
- Quando STH RP cai abaixo do LTH RP → **deep bear** (mãos fracas perdendo mais que mãos fortes)
- Quando STH RP volta acima do LTH RP → saindo do bear

---

## PARTE 3: Análise Técnica de Ciclo (Price Action)

### 3.0 Estrutura de Timeframes Altos de Ciclo (6M / 3M / M) (OBRIGATÓRIO — ler primeiro)

> Hierarquia de ciclo (top-down): **6M = âncora máxima** · **3M = confirmação intermediária** ·
> **M = teto/piso de momentum macro** e alvos mensais. Leitura obrigatória em toda análise CYCLE, de
> cima para baixo, antes de descer ao semanal.

**O bear é a correção do gráfico de 6M.** Topos e fundos de ciclo **confirmam no FECHAMENTO** dos
candles de 6M/3M/M — um candle ainda **em formação** revertendo é sinal **preliminar**, não confirmado
até fechar.

**Regra dos "2 candles de 6M" (janela de atenção, não predição):** os últimos fundos cíclicos vieram
**~2 candles de 6 meses após o topo** (≈12 meses), cruzando com a coluna Topo→Fundo da Parte 1 — Ciclo 3
(2017→2018) ~12m e Ciclo 4 (2021→2022) ~12m; Ciclo 2 (2013→2015) ~14m ≈ 2-3 candles. Usar como **janela
de atenção** para monitorar indicadores com mais frequência e como **confirmação por fechamento** de
6M/3M, **nunca** como gatilho temporal isolado (tempo = peso 10%; os indicadores DEFINEM).

> **Fonte 6M/3M:** tentar `chart_set_timeframe({timeframe: "6M"/"3M"})`; se o TF nativo não existir no
> setup, **agregar do Mensal** (`data_get_ohlcv({summary:true})`, ≥4 anos) e declarar `fonte:
> agregado-do-mensal`. Não inventar fechamentos — declarar a fonte.

Leitura sistemática do timeframe mensal (`chart_set_timeframe({timeframe: "M"})`):

- **RSI Mensal:** valor + zona + cruzamento de 50. RSI mensal cruzando 50 para **baixo** = virada macro bearish do ciclo; para **cima** = virada macro bullish. Divergência mensal (preço HH + RSI LH em topo / preço LL + RSI HL em fundo) = sinal de reversão de **ciclo** (peso máximo, acima da semanal).
- **P.RSI50 Mensal** (nível de preço onde o RSI mensal = 50): funciona como **teto/piso de ciclo** — em bear, o preço respeita o P.RSI50 mensal como resistência; em bull, como suporte.
- **MACD Mensal:** posição vs zero + cruzamento + histograma. Cruzamento mensal vs linha zero = **mudança de regime de ciclo** (prioridade sobre o semanal).
- **MACD Semanal (1W) — filtro de regime macro:** posição vs linha zero (>0 Bull / <0 Bear) = **confirmação de regime** que reage antes dos on-chain reverterem (early-warning de flip bull↔bear), **abaixo** da prioridade do cross Mensal. Filtro lagging de direção p/ swing/alocação, não timing de topo/fundo; cruzamento fresco = transição. Ver [[macd]] §5.5.
- **Candles mensais de reversão:** pavios longos (rejeição), candle bearish climático pós-ATH (sign of weakness) ou candle bullish climático pós-capitulação (sign of strength).
- **Volume mensal climático:** spike de volume em candle mensal = clímax de distribuição (topo) ou capitulação (fundo).
- **Estrutura mensal:** HH/HL (bull de ciclo) ou LH/LL (bear de ciclo). O primeiro LH/LL mensal após ATH = confirmação de topo de ciclo.

### 3.1 Sinais de Topo de Ciclo (Chart)

- [ ] RSI semanal > 90 ou com divergência bearish (preço HH, RSI LH)
- [ ] MACD semanal cruzando para baixo acima de zero após rally prolongado
- [ ] Volume semanal declinando com preço subindo (distribuição)
- [ ] Wyckoff: Fase de Distribuição identificada (PSY → BC → UT/UTAD)
- [ ] Candle semanal de rejeição (shooting star, bearish engulfing) em ATH
- [ ] EMA 21 semanal perdida como suporte pela primeira vez no ciclo
- [ ] BOS bearish no semanal (primeiro LL confirmado)
- [ ] Bollinger Bands semanal: preço fora da banda superior por semanas → retorno
- [ ] Candle de 6M/3M **fechando** bearish (engolfo/rejeição) após ATH = topo de ciclo confirmado

### 3.2 Sinais de Fundo de Ciclo (Chart)

- [ ] Volume climático de capitulação (spike extremo de venda)
- [ ] Candle semanal de reversão (martelo / engolfo bullish com volume)
- [ ] Divergência bullish no RSI semanal (preço LL, RSI HL)
- [ ] MACD semanal cruzando para cima abaixo de zero
- [ ] Wyckoff Spring: sweep de low seguido de reversão agressiva
- [ ] Re-acumulação: semanas de range apertado após capitulação
- [ ] Preço recupera e fecha acima do Realized Price
- [ ] 200W SMA recuperada como suporte (fecha acima por 2+ semanas)
- [ ] Candle de 6M/3M **fechando** bullish (martelo/engolfo) com volume = fundo de ciclo confirmado

### 3.3 Fibonacci de Ciclo (Escala Log)

Para projeção de fundo, usar Fibonacci na escala LOG do gráfico semanal/mensal:

1. Traçar do fundo do ciclo anterior ao ATH do ciclo atual
2. Retrações relevantes:
   - **0.786:** zona de fundo em ciclos mais maduros (drawdown ~78%)
   - **0.886:** zona de fundo em bear markets profundos (~88%)
   - **0.618:** retração mais rasa (ciclo acelerado / sem cisne negro)

> ⚠️ Usar escala LOG, não linear. Em escalas lineares, as retrações de Fibonacci são distorcidas em ativos com crescimento exponencial.

---

## PARTE 4: Sentimento e Posicionamento

### 4.1 Fear & Greed Index
- Fundos de ciclo: permanência prolongada (semanas/meses) abaixo de 20
- Topos de ciclo: permanência prolongada acima de 80
- **Ticker TV:** Buscar "Crypto Fear and Greed" nos indicadores

### 4.2 Funding Rates
Ref: [[funding-rate]]
- Bear markets: funding persistentemente negativo (shorts dominam)
- Bull markets: funding persistentemente positivo (longs dominam)
- Extremos: sinal contrário (funding muito positivo = longs sobrecarregados)

### 4.3 Exchange Reserves
- Tendência caindo = acumulação off-exchange = bullish longo prazo
- Tendência subindo = preparação para venda = bearish curto prazo
- Em fundos de ciclo: reserves em queda constante (smart money sacando)

### 4.4 LTH Supply (Long-Term Holders)
- LTH acumulação máxima = fase de fundo (compram durante o pânico)
- LTH distribuição = fase de topo (vendem durante a euforia)

### 4.5 Narrativa e Mídia
- "Bitcoin morreu" / "Crypto is dead" / "Going to zero" → probabilidade de fundo alta
- "Bitcoin vai para $1M" / "Mainstream adoption" / "No more bear markets" → probabilidade de topo alta
- YouTubers/influencers abandonando crypto → sinal contrário → fundo

---

## PARTE 5: Métodos de Projeção de Fundo

Quando bear market é confirmado, usar múltiplos métodos e buscar **confluência**:

### Método 1 — Fractal de Drawdown Decrescente
```
Drawdowns: -93% → -87% → -84% → -77%
Projeção: -70% a -75%
Fundo = ATH × (1 - drawdown)
```

### Método 2 — 200W SMA como Piso
```
200W SMA na data estimada de fundo
Cenário base: preço toca a 200W SMA
Cenário pessimista: 15-20% abaixo (sem cisne negro)
Cenário catastrófico: 30%+ abaixo (com cisne negro)
```

### Método 3 — Realized Price como Suporte
```
Realized Price na data estimada de fundo
Cenário base: preço toca o Realized Price
Cenário profundo: 15% abaixo do Realized Price
```

### Método 4 — Fibonacci Log do Ciclo
```
Fib do low anterior ao ATH atual (escala log)
0.618 = retração rasa (otimista)
0.786 = retração padrão
0.886 = retração profunda (com cisne negro)
```

### Método 5 — Temporal (menor peso)
```
Topo → Fundo: ~12 meses (média histórica)
Halving → Fundo: ~28-32 meses
Usar apenas como janela de atenção
```

### Método 6 — Confluência Técnica
```
Combinar:
- 200W SMA
- Realized Price
- Fib 0.786 (log)
- Order Block semanal não mitigado
- Volume Profile VAL do ciclo
- Zona psicológica ($XX,000)
Zonas onde 3+ métodos convergem = maior probabilidade
```

---

## PARTE 6: Scoring System — Diagnóstico de Ciclo

### Score de Topo (máximo 10 pontos)

```
[ ] MVRV Z-Score > 7                                    (+2)
[ ] NUPL > 0.75 (Euforia)                               (+2)
[ ] Puell Multiple > 4                                   (+1)
[ ] Pi Cycle Top: 111DMA cruzou 350DMA×2                 (+2)
[ ] RSI semanal/mensal > 90 ou divergência bearish       (+1)  (mensal = peso máximo)
[ ] Volume declinando com preço subindo (distribuição)   (+1)
[ ] LTH em modo distribuição                             (+1)
Score: [X/10]
```

### Score de Fundo (máximo 15 pontos)

```
[ ] MVRV Z-Score < 0 e revertendo                        (+2)
[ ] NUPL < 0 (Capitulação) e estabilizando               (+2)
[ ] Puell Multiple < 0.5 e revertendo                    (+1)
[ ] Preço tocou ou caiu abaixo da 200W SMA               (+2)
[ ] Preço tocou ou caiu abaixo do Realized Price          (+2)
[ ] Hash Ribbons: capitulação terminando → compra         (+1)
[ ] RSI semanal/mensal com divergência bullish            (+1)  (mensal = peso máximo)
[ ] MACD semanal/mensal cruzando para cima abaixo de zero (+1)  (cross mensal = virada de ciclo)
[ ] Wyckoff Spring identificado                           (+1)
[ ] Volume climático de capitulação                       (+1)
[ ] Fear & Greed < 20 por semanas                         (+1)
Score: [X/15]
```

### Interpretação

| Score de Fundo | Interpretação |
|----------------|---------------|
| 0-4 | Bear market em andamento, longe do fundo |
| 5-8 | Aproximando do fundo — monitorar semanalmente |
| 9-11 | Alta probabilidade de fundo — acumulação agressiva |
| 12-15 | Fundo confirmado — o mercado já virou |

---

## PARTE 7: Output Obrigatório (Como Escrever)

Toda análise de ciclo DEVE incluir:

```
=== DIAGNÓSTICO DE CICLO — BTC ===

FASE ATUAL: [BULL INICIAL / BULL MADURO / DISTRIBUIÇÃO / BEAR INICIAL / BEAR PROFUNDO / CAPITULAÇÃO / ACUMULAÇÃO / FUNDO FORMADO]

INDICADORES ON-CHAIN:
- MVRV Z-Score: [valor] → [fase]
- NUPL: [valor] → [fase]
- Puell Multiple: [valor] → [fase]
- 200W SMA: $XX,XXX | Preço vs 200W: [acima/abaixo/tocando]
- Realized Price: $XX,XXX | Preço vs RP: [acima/abaixo]
- Pi Cycle Top: [cruzou/não cruzou]
- Hash Ribbons: [capitulação/recuperação/expansão]

ANÁLISE TÉCNICA:
- Estrutura 6M/3M: [HH/HL | LH/LL] | candle 6M atual: [em formação/fechado: bull/bear] | fonte: [nativo/agregado-do-mensal]
- RSI Mensal: [valor] [vs 50: acima/abaixo] [divergência: sim/não] | P.RSI50 Mensal: $XX,XXX
- MACD Mensal: [acima/abaixo zero] [cross: up/down]
- RSI Semanal: [valor] [divergência: sim/não]
- MACD Semanal: [acima/abaixo zero] [cross: up/down]
- Estrutura Mensal: [HH/HL bull | LH/LL bear] [candle de reversão: sim/não]
- Wyckoff: [fase] [evento: Spring/UT/N.A.]
- Volume: [climático/declinando/normal]

SENTIMENTO:
- Fear & Greed: [valor]
- Funding Rate: [positivo/negativo/neutro]
- Narrativa dominante: [descrição]

SCORES:
- Score de Topo: [X/10]
- Score de Fundo: [X/15]

DRAWDOWN ATUAL DO ATH: -XX.X%
TEMPO DESDE O ATH: XX meses

PROJEÇÃO (se bear confirmado):
- Zona de Fundo: $XX,XXX — $XX,XXX
- Métodos convergentes: [X/6]
- Janela temporal: [mês/ano] — [mês/ano]
- Cenário base: $XX,XXX
- Cenário otimista: $XX,XXX (sem cisne negro)
- Cenário pessimista: $XX,XXX (com cisne negro)

CONFIANÇA: [ALTA / MÉDIA / BAIXA]
```

---

## PARTE 8: Workflow MCP (Passos Práticos)

### Para análise de ciclo via TradingView MCP:

**1. Price Action + Indicadores Nativos:**
```
chart_set_symbol({symbol: "BTCUSD"})
chart_set_timeframe({timeframe: "W"})
data_get_study_values()        // RSI, MACD, EMAs semanais
data_get_ohlcv({summary: true})
capture_screenshot()
```

**2. 200W SMA (verificação de fundo):**
```
chart_set_timeframe({timeframe: "W"})
// Adicionar SMA 200 se não estiver no chart
chart_manage_indicator({action: "add", name: "Moving Average"})
data_get_study_values()
```

**3. Mensal (contexto de ciclo completo):**
```
chart_set_timeframe({timeframe: "M"})
data_get_ohlcv({summary: true})
capture_screenshot()
```

**4. Fibonacci Log (projeção):**
```
chart_set_timeframe({timeframe: "W"})
// Traçar Fibonacci manualmente ou via draw_shape
// Low do ciclo anterior → ATH do ciclo atual
```

> **Nota:** Indicadores on-chain (MVRV, NUPL, Puell, Hash Ribbons) dependem de indicadores comunitários instalados no TradingView. Se não disponíveis, usar dados de Glassnode/CryptoQuant/LookIntoBitcoin como referência externa e registrar valores manualmente na análise.

---

## PARTE 9: Estratégia de Acumulação em Fundo

Quando o Score de Fundo atingir 9+:

```
Zona 1 (agressiva):    Score 9-11 → alocar 30% do capital em DCA semanal
Zona 2 (principal):    Score 12-13 → alocar 50% do capital
Zona 3 (deep value):   Score 14-15 → alocar 20% restante (all-in gradual)

Regra de ouro: NÃO tentar acertar o fundo exato.
A diferença entre comprar no fundo e 15% acima é
irrelevante quando o próximo topo for 5-10x mais alto.
```

---

## Frequência de Execução

| Contexto | Frequência |
|----------|-----------|
| Bull market confirmado | Mensal (monitorar sinais de topo) |
| Possível transição bull→bear | Quinzenal |
| Bear market confirmado | Semanal (monitorar sinais de fundo) |
| Proximidade de fundo (Score 9+) | Diário |
| Fundo confirmado (Score 12+) | Semanal (monitorar recuperação) |

---

## Riscos para Projeções

1. **Regulação draconiana** — proibição em economia G7 pode criar fundo mais profundo
2. **Evento cisne negro** — colapso de exchange (tipo FTX) pode antecipar e aprofundar fundo
3. **Recessão global prolongada** — bear market mais longo e profundo que o histórico
4. **Ciclo quebra o padrão** — cada ciclo é um evento com amostra n=4, padrões podem mudar
5. **Adoção institucional** — pode criar piso mais alto (drawdown menor que projetado)
6. **ETFs** — novo fluxo institucional pode diminuir volatilidade de ciclo

---

## Backlinks
- [[mvrv-z-score]] — indicador primário de ciclo
- [[nupl]] — sentimento on-chain de ciclo
- [[realized-price]] — suporte fundamental de fundo
- [[btc-macro-correlations]] — contexto macro
- [[Wyckoff]] — Spring = fundo, UTAD = topo
- [[fibonacci-structural]] — zonas de retração para projeção
- [[short-long-squeeze]] — squeezes amplificam movimentos de topo e fundo
- [[btcusdlongs-btcusdshorts]] — posicionamento de margem em extremos de ciclo
- [[funding-rate]] — regime de funding indica fase bull/bear
- [[trade-playbooks]] — Playbook 4 (Squeeze) frequente em extremos de ciclo
- [[liquidity-wicks-trap-short-usdtd]] — liquidez por pavios em zonas de fundo
- [[rsi-divergences]] — divergências semanais marcam topos e fundos de ciclo
- [[macd]] — cruzamentos semanais confirmam mudanças de fase
