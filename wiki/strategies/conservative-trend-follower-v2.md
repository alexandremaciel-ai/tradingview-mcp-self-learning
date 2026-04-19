# Conservative Trend Follower v2.0

> Estratégia principal. Última revisão: 2026-04-19

## Parâmetros
- **Alavancagem padrão:** 3x–5x
- **Alavancagem máxima:** 10x (alta convicção)
- **R:R mínimo:** 1:3
- **Time stop:** 48 horas
- **Trailing stop breakeven:** ativado em +10%

## Progressão do Trailing Stop
1. Entrada → SL no setup
2. +10% → SL move para breakeven
3. +20% → SL move para +10%
4. +30% → SL move para +20%

## Regras de Entrada
- EMA 50 alinhada com direção do trade
- RSI não sobrecomprado/sobrevendido extremo
- Volume acima da média
- R:R ≥ 1:3

## Filtros HTF (4H)
- **Hard block LONG:** estrutura bearish confirmada + ADX > 25
- **Aguardar:** CHoCH no 4H para re-habilitar

## Filtros de Entrada (4 camadas)
1. ADX > 20 (tendência presente)
2. ATR normalizado (volatilidade adequada)
3. EMA 50/200 alinhadas com direção
4. MACD + RSI confirmando momentum

## Performance Histórica
| Período | Trades | Win Rate | Drawdown | Sharpe |
|---------|--------|----------|----------|--------|
| _(vazio)_ | | | | |

## Backlinks
- [[BTCUSD]]
- [[ADX]]
- [[ATR]]
- [[multi-timeframe-analysis]]
- [[SMC]]
