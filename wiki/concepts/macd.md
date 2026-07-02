# MACD — Estrutura, Linha Zero e Força de Tendência

> Parâmetros padrão: 12/26/9
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Leitura Estrutural

### Linha Zero como Divisor
- MACD **acima** da linha zero + histograma crescente = pressão compradora sustentada
- MACD **abaixo** da linha zero + cruzamento da linha de sinal = Short com maior confiabilidade
- Em tendência de baixa: repiques de preço empurram o MACD de volta à Linha Zero (reset) antes da próxima perna de queda

### Histograma
- Histograma virando **vermelho** em zona de resistência/topo = alerta crítico de Short
- Histograma virando **verde** em zona de suporte/fundo = alerta de Long
- Histograma encolhendo = momentum da tendência atual está enfraquecendo

---

## 2. Sinais por Contexto de Mercado

| Contexto | MACD | Sinal |
|----------|------|-------|
| Tendência de alta | Acima de zero, histograma crescente | Confirma Long |
| Tendência de baixa | Abaixo de zero, histograma decrescente | Confirma Short |
| Repique em bearish | MACD sobe de volta a zero (reset) | Aguardar retomada da queda |
| Topo | Histograma vira vermelho em resistência | Alerta de Short |
| Fundo | Histograma vira verde em suporte | Alerta de Long |

---

## 3. Cruzamentos Relevantes

- Cruzamento da **linha de sinal abaixo de zero** = Short de maior confiabilidade
- Cruzamento da **linha de sinal acima de zero** = Long de maior confiabilidade
- Cruzamentos acima/abaixo de zero mas próximos = sinais mais fracos, aguardar confirmação
- **Cruzamento iminente** (linhas convergindo): antecipar o sinal se houver confluência com FVG/OB

---

## 4. Direção das Linhas (OBRIGATÓRIO ler em toda análise)

> **Não basta ver o valor do MACD. A direção e a convergência das linhas definem o momentum.**

### Regras de Leitura Direcional
- **MACD subindo + acima de zero:** momentum comprador forte, mantém Long
- **MACD descendo + acima de zero:** momentum comprador enfraquecendo, alerta para saída/redução
- **MACD subindo + abaixo de zero:** momentum vendedor enfraquecendo, possível reversão
- **MACD descendo + abaixo de zero:** momentum vendedor forte, mantém Short
- **MACD e Signal convergindo:** cruzamento iminente, preparar ação
- **MACD e Signal divergindo:** tendência acelerando, manter posição

### Lado do Mercado
| MACD vs Zero | Histograma | Leitura |
|------|------------|---------|
| Acima de zero | Crescente | **Comprador forte** — manter Long |
| Acima de zero | Decrescente | Comprador enfraquecendo — preparar saída |
| Abaixo de zero | Decrescente | **Vendedor forte** — manter Short |
| Abaixo de zero | Crescente | Vendedor enfraquecendo — preparar reversão |

---

## 4. Parâmetros

- **Padrão:** 12/26/9 (fast EMA / slow EMA / signal)
- **Timeframes ideais:** **Mensal e Semanal para ciclo/regime** (obrigatórios no macro); 4H e Diário para tendência; 1H para gatilho
- **Uso no Conservative Trend Follower:** MACD é um dos 4 filtros de confirmação de momentum (junto com RSI)

---

## 5. Integração

- **MACD Mensal:** cruzamento mensal vs linha zero = **virada de regime de CICLO** (prioridade sobre o semanal). MACD mensal abaixo de zero = ciclo bearish; divergência mensal = topo/fundo de ciclo
- Usar MACD Semanal: virando vermelho = fluxo de risco global secando → bearish para BTC
- MACD + RSI divergência = dupla confirmação de exaustão
- MACD + EMA 200 (abaixo) = alinhamento completo para Short

---

## 5.5 MACD Semanal (1W) — Filtro de Regime Macro (Bull/Bear)

> **Rastreador de macrotendência do BTC.** A posição do MACD 1W vs a Linha Zero define
> matematicamente o regime de mercado e baliza os ciclos de Bull/Bear. Critério `macd-regime`
> ([[criteria-keys]]); alimenta o `macro-scan` (Regra 12) e o Confluence Score.

### Regra da Linha Zero (1W)
- **MACD 1W > 0** (acima da linha zero): EMA de 12 semanas **acima** da EMA de 26 semanas →
  momentum de alta consolidado → **regime BULL** (longs/alocação com maior probabilidade estatística).
- **MACD 1W < 0** (abaixo da linha zero): EMA de 12 semanas cruzou **abaixo** da EMA de 26 semanas →
  força vendedora domina a perspectiva de médio/longo prazo → **regime BEAR** (shorts favorecidos).
- A matemática é a divergência EMA12/EMA26; o eixo zero é o divisor de momentum direcional macro.

### Validação Histórica nos Ciclos do BTC
| Regime | Período | MACD 1W |
|--------|---------|---------|
| 🐻 Bear | 2014-2015 | Abaixo de zero ~1 ano, acompanhando a formação do fundo |
| 🐻 Bear | 2018 | Afundou < 0 meses após o topo de 2017; sustentou baixa até início 2019 |
| 🐻 Bear | 2022 | Perdeu a linha zero no 1º semestre; fundo formado em território negativo |
| 🐂 Bull | 2016-2017 | Rompeu > 0 no início de 2016; positivo até o topo ~$20k (dez/2017) |
| 🐂 Bull | 2020-2021 | Cruzou > 0 fim de abr/início mai 2020; sustentou a corrida até $64k-$69k |
| 🐂 Bull | 2023-2024 | Rompeu > 0 no início de 2023; suporte estrutural até o ATH ~$73k (mar/2024) |

### Nota Operacional (OBRIGATÓRIA)
- **Validador de tendência consolidada (lagging), NÃO timing de topo/fundo.** Não fornece o topo/fundo
  absoluto — atua como **filtro de regime**, indicando em que direção swing trades e alocação têm a
  maior probabilidade a médio/longo prazo.
- **Cruzamento fresco da linha zero = TRANSIÇÃO de regime** → filtro ambíguo/fraco: tratar regime como
  **neutro** (não pontua, sem penalidade) e reduzir size até o cruzamento consolidar.
- **Hierarquia de regime:** **Mensal = regime de CICLO (prioridade — ver §5); 1W = regime macro
  operável** para swing. Aplica-se ao BTC; via âncora HTF gate também altcoins/ETH. **EQUITIES = N/A.**

---

## 6. Divergências no MACD

> Divergências no MACD são tão importantes quanto no RSI, mas frequentemente ignoradas.
> O MACD diverge quando o histograma ou as linhas MACD/Signal não acompanham o preço.

### Divergência Bearish (Clássica)
- Preço faz **topo mais alto** (HH)
- MACD faz **topo mais baixo** (linhas ou histograma)
- Significado: momentum comprador exaurindo apesar do preço subir
- **Ação:** Alerta de reversão → preparar short se confirmado por zona de resistência
- **TF ideal:** 4H e Diário para swing. 1H para intraday.

### Divergência Bullish (Clássica)
- Preço faz **fundo mais baixo** (LL)
- MACD faz **fundo mais alto** (linhas ou histograma)
- Significado: momentum vendedor exaurindo apesar do preço cair
- **Ação:** Alerta de reversão → preparar long se confirmado por zona de suporte
- **TF ideal:** 4H e Diário para swing. 1H para intraday.

### Divergência Oculta (Continuação)
- **Oculta Bullish:** Preço faz HL, MACD faz LL → tendência de alta continua
- **Oculta Bearish:** Preço faz LH, MACD faz HH → tendência de baixa continua
- **Ação:** Reforça a direção da tendência vigente (entrar na continuação)

### Onde observar
- **TF de ciclo:** Mensal e Semanal para divergências de **topo/fundo de ciclo** (peso máximo). 4H/Diário para swing, 1H para intraday.
- **Histograma:** divergência mais sensível (barras encurtando enquanto preço avança = primeiro alerta)
- **Linhas MACD/Signal:** divergência mais confiável (mais lenta, menos falsos sinais)
- **Regra:** Divergência no histograma é o primeiro alerta. Divergência nas linhas confirma.

### Confluência com outros indicadores
- MACD div. + RSI div. no mesmo TF = **dupla confirmação** → alta convicção
- MACD div. + preço em FVG/OB = setup de reversão de alta qualidade
- MACD div. sem confirmação RSI = sinal mais fraco → aguardar

---

## Backlinks
- [[rsi-divergences]] — divergência combinada MACD + RSI
- [[conservative-trend-follower-v2]]
- [[trade-playbooks]]
- [[multi-timeframe-analysis]]
- [[btc-cycle-analysis]] — cruzamentos W/M confirmam mudança de fase de ciclo
- [[institutional-flow-poi]] — regime macro é lente do Pilar Contexto/Ciclos
- [[liquidity-rotation-cycle]] — regime 1W cruza com a Fase de rotação de liquidez
- [[confluence-score]] — critério `macd-regime` (crédito/`contra-regime` −1)
