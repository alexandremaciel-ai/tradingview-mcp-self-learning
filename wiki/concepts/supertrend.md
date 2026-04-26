# Supertrend

> Criado: 2026-04-26
> Categoria: Indicador / Trend-Following / Trailing Stop

## Definição

Supertrend é um indicador de tendência baseado no **ATR (Average True Range)**, criado por Olivier Seban. Combina detecção de direção de tendência e volatilidade em uma única linha sobreposta ao gráfico. Usado para identificar reversões de tendência e posicionar stops dinâmicos.

---

## Como Funciona

### Cálculo Simplificado
```
hl2 = (high + low) / 2
upperBand = hl2 + (multiplier × ATR)
lowerBand = hl2 - (multiplier × ATR)
```
- Quando o preço está **acima** do Supertrend → indicador fica **verde** → tendência de alta
- Quando o preço cai **abaixo** do Supertrend → indicador fica **vermelho** → tendência de baixa
- A cada fechamento fora da banda, a tendência muda

### Inputs Ajustáveis
| Input | Padrão | Efeito |
|-------|--------|--------|
| ATR Length | 10 | Comprimento do lookback ATR — maior = mais suave |
| Multiplier | 3.0 | Afasta as bandas — maior = menos sensível |

- Multiplier alto + ATR longo → menos sinais, menos falsos (bom para swing)
- Multiplier baixo + ATR curto → mais sinais, mais noise (cuidado com scalp)

---

## Leituras Práticas

### Trailing Stop
O Supertrend funciona como trailing stop automático:
- Em tendência de alta: a linha verde abaixo do preço sobe junto → stop se aproxima
- Em tendência de baixa: a linha vermelha acima do preço desce → stop se aproxima
- Virada do indicador = stop executado = novo sinal de reversão

### Confirmação de Tendência
- Supertrend **verde** em H4 = permissão para longs no H1/M15
- Supertrend **vermelho** em H4 = permissão para shorts no H1/M15
- Conflito entre TFs = range/consolidação provável

---

## Uso no Contexto deste Wiki

### Regra ST 4H (da wiki/brain/mistakes.md)
> SEMPRE verificar o Supertrend 4H antes de entrar long no 1H. Se ST 4H estiver vermelho, o setup long só é válido com confirmação de CHoCH no 4H ou stop abaixo de suporte 4H relevante.

Esta regra foi adicionada após erro de 2026-04-19 onde BTC long no 1H foi stoppado porque ST 4H estava bearish em 77,076.

### Combinações Recomendadas
- Supertrend + RSI: confirmar que RSI está acima de 50 quando ST vira verde
- Supertrend + MACD: MACD cruzar acima da zero line com ST verde = entrada mais segura
- Supertrend + SMC: ST confirma tendência do HTF; SMC define a entrada OTE/FVG no LTF

---

## Limitações
- Gera sinais falsos em mercados laterais (consolidação) — pode flipar várias vezes
- Não antecipa — só confirma após fechamento da vela
- Parâmetros default podem ser muito sensíveis para cripto — ajustar multiplier para 2-3 em H4

---

## Backlinks
- [[ATR]] — base do cálculo
- [[multi-timeframe-analysis]] — ST H4 como filtro de direção para setups LTF
- [[SMC]] — ST define tendência macro; SMC define a entrada
- [[bull-bear-traps]] — ST virando verde sem candle fechado acima = bull trap potencial
