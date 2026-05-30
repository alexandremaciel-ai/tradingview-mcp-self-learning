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
- **Timeframes ideais:** 4H e Diário para tendência; 1H para gatilho
- **Uso no Conservative Trend Follower:** MACD é um dos 4 filtros de confirmação de momentum (junto com RSI)

---

## 5. Integração

- Usar MACD Semanal: virando vermelho = fluxo de risco global secando → bearish para BTC
- MACD + RSI divergência = dupla confirmação de exaustão
- MACD + EMA 200 (abaixo) = alinhamento completo para Short

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
