# SOPR (Spent Output Profit Ratio)

> Métrica on-chain de curto prazo — revela se BTC está sendo vendido com lucro ou prejuízo.
> Criador: Renato Shirakashi | Compilado: 2026-04-23

## Definição

**SOPR** mede a razão entre o valor de Bitcoin no momento do gasto (venda/transferência) e o valor no momento da aquisição. Indica se os participantes do mercado estão realizando lucros ou prejuízos **agora**.

## Fórmula

```
SOPR = Valor de BTC quando gasto / Valor quando adquirido
```

## Leitura dos Valores

| SOPR | Situação | Interpretação |
|------|----------|--------------|
| **> 1** | Moedas vendidas com lucro | Holders estão realizando ganhos |
| **= 1** | Break-even | Vendendo exatamente no preço de compra |
| **< 1** | Moedas vendidas com prejuízo | Capitulação — vendendo abaixo do custo |

## Médias Móveis Disponíveis (bitbo.io)

- **7-day MA** — tendência de curto prazo do comportamento de gastos
- **30-day MA** — tendência de médio prazo

## Coloração por Percentis (bitbo.io)

| Cor | Percentil SOPR | Interpretação |
|-----|---------------|--------------|
| Azul escuro | Bottom 10% | Realização extrema de perdas |
| Verde | 25–50º percentil | Perdas moderadas |
| Amarelo | 65–75º percentil | Neutro |
| Laranja | 75–85º percentil | Lucros moderados |
| Vermelho | Top 15% | Realização extrema de lucros |

## Uso Operacional

**Sinal de fundo (bullish):**
- SOPR < 1 em zona de suporte técnico = capitulação de vendedores → oportunidade de entrada
- SOPR voltando acima de 1 após período abaixo = fim da capitulação

**Sinal de topo (bearish):**
- SOPR muito alto + price action em resistência = tomada de lucro em massa → possível reversão

**Nível 1 como pivô:**
- Em bull markets: SOPR testa 1 e volta acima (1 = suporte) = impulso de continuidade
- Em bear markets: SOPR tenta cruzar 1 e rejeita abaixo = resistência, tendência continua

## Diferença SOPR vs NUPL

| | SOPR | NUPL |
|--|------|------|
| **O que mede** | Lucro realizado em transações | Lucro não realizado (posição latente) |
| **Timeframe** | Comportamento atual de gastos | Situação acumulada |
| **Uso** | Timing de curto/médio prazo | Identificação de ciclo |

## Backlinks
- [[nupl]] — lucros não realizados (complemento ao SOPR)
- [[realized-price]] — Realized Price é base para calcular o lucro no momento do gasto
- [[mvrv-z-score]] — indicador de valorização macro (versus SOPR que é de gastos)
- [[research/2026-04-23-onchain-metrics-batch7]]
