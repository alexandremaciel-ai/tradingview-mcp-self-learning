# ATR — Average True Range

## O que mede
Volatilidade média em N períodos (padrão 14). É a média do "true range" — o maior entre: (high−low), |high−close_anterior|, |low−close_anterior|. Não indica direção, só amplitude esperada de movimento.

## Usos no Sistema
- **Position sizing:** dimensionar o risco pela volatilidade real, não por um valor fixo. Ref: [[position-sizing]].
- **Stop Loss dinâmico:** SL = 1.5× ATR de distância (evita ser estopado pelo ruído normal do ativo).
- **Filtro de volatilidade:** ATR muito baixo = mercado comprimido → aguardar expansão antes de operar tendência.
- **Validação do candle de gatilho (checklist):** |Abertura − Fechamento| > ATR(14) × 1.5 = movimento real, não ruído.
- **TP targets realistas:** alvos como múltiplos de ATR (1×, 2×, 3× ATR) calibram expectativa de quão longe o preço pode ir na sessão.

## Cálculo de SL
```
SL_distance = ATR(14) * 1.5
SL_price = entry - SL_distance   (long)
SL_price = entry + SL_distance   (short)
```

## Cálculo de Position Size com ATR
```
Risco $ = capital * risco_% (1–2%)
SL_distance = ATR(14) * 1.5
Tamanho da posição = Risco $ / SL_distance
```
> Ativos mais voláteis (ATR maior) → posição menor para o mesmo risco em $. Isso normaliza o risco entre BTC, altcoins e equities.

## Leitura de Regime de Volatilidade
- **ATR expandindo:** volatilidade subindo → movimentos maiores, alargar TPs e SL.
- **ATR contraindo (mínimas):** compressão → frequentemente precede expansão explosiva (cruzar com Bollinger squeeze). Aguardar o rompimento com volume.
- **ATR vs preço:** comparar ATR atual com a média histórica do ativo — ATR acima da média = sessão de alto risco (reduzir size).

## Combinação
- **ATR + ADX:** ATR baixo + ADX < 20 = range comprimido (não operar tendência). ATR subindo + ADX cruzando 25 = início de perna com volatilidade real.
- **ATR + Volume:** candle com |O−C| > ATR×1.5 E volume > SMA(20)×1.5 = gatilho de máxima qualidade.

## Falhas comuns
- Usar SL fixo em $ ignorando a volatilidade do momento → estopado por ruído (ATR alto) ou risco mal dimensionado (ATR baixo).
- Operar breakout com ATR em mínimas sem aguardar confirmação de expansão.
- Esquecer de recalcular o size quando a volatilidade muda (ATR de fim de semana ≠ ATR de NY session).

## Backlinks
- [[conservative-trend-follower-v2]]
- [[ADX]]
- [[position-sizing]]
- [[bollinger-bands]]
- [[confluence-score]]
