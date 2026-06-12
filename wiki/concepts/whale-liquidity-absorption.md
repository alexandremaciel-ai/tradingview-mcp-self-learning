# Whale Liquidity and Absorption Profile [AlgoAlpha]

> Criado: 2026-06-12
> Categoria: Indicador / Liquidez / Order Flow

## Definição
Perfil granular de **absorção e liquidez por faixa de preço** (AlgoAlpha). Plota dezenas a centenas de zonas finas `{high, low}` que indicam onde grandes players absorveram ordens — um mapa de liquidez institucional. Componente do layout **Liquidity e SMC**.

## O que plota e como ler
- Zonas `{high, low}` via `data_get_pine_boxes(study_filter="Whale")` — cada zona é uma faixa estreita de preço com absorção registrada.
- **Clusters densos de zonas** = forte interesse institucional → ímã de preço / suporte-resistência probabilístico.
- Faixas vazias entre clusters = vácuo de liquidez → preço tende a atravessar rápido.

## Leituras práticas
- Identificar o **cluster mais próximo** acima e abaixo do preço = zonas de defesa/alvo.
- Confluência cluster Whale + Order Block (SMC) + Fib = zona de altíssima convicção.
- Preço entrando num cluster denso com volume fraco (ver [[crypto-smart-volume]]) = absorção → possível reversão.

## Limitações
- Probabilístico, não S/R rígido — usar como contexto, não como linha exata.
- Muitas zonas (centenas) — sempre reduzir ao cluster relevante perto do preço atual.

## Backlinks
- [[smc-luxalgo]] — estrutura + OB complementam o mapa de liquidez
- [[liquidity-wicks-trap-short-usdtd]] — varredura de liquidez / pavios
- [[layouts]] — layout Liquidity e SMC
- [[indicators]]
