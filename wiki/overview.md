# Visão Geral — Trading Wiki

## Tese Central
Sistema de análise técnica baseado em Smart Money Concepts (SMC) com filtros de estrutura multi-timeframe.

## Stack de Indicadores
- **Tendência:** EMA 50/200, ADX > 25
- **Momentum:** RSI, MACD
- **Estrutura:** CHoCH, BoS, FVG (SMC)
- **Volatilidade:** ATR para sizing

## Hierarquia de Timeframes
1D → 4H → 1H → 15m → 5m

## Regra de Conflito HTF
- LONG bloqueado quando 4H mostra estrutura bearish confirmada + ADX > 25
- Aguardar CHoCH no 4H antes de re-habilitar longs

## Ativos em Acompanhamento
- BTC/USD (principal)

## Métricas de Performance Alvo
- Win Rate mínimo: 40%
- R:R mínimo: 1:3
- Max Drawdown: < 30%
- Sharpe Ratio alvo: > 1.0
