# ATR — Average True Range

## O que mede
Volatilidade média em N períodos.

## Usos no Sistema
- **Position sizing:** risco baseado em ATR (ex: SL = 1.5x ATR)
- **Filtro de volatilidade:** ATR muito baixo = mercado comprimido, aguardar
- **TP targets:** múltiplos de ATR como alvos realistas

## Cálculo de SL
```
SL_distance = ATR(14) * 1.5
SL_price = entry - SL_distance (long) | entry + SL_distance (short)
```

## Backlinks
- [[conservative-trend-follower-v2]]
- [[ADX]]
