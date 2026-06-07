# Liquidez, Pavios HTF, Traps e a Leitura do USDT.D

> Onde estão os stops, o preço vai buscar. Pavios longos em timeframes maiores são o mapa da
> liquidez; traps são a colheita dessa liquidez; e o USDT.D é o confirmador/negador macro que diz
> se o movimento do BTC tem combustível ou é só barulho. Esta página junta os três na Fase 8.

## 1. Pavios HTF = mapa de liquidez
- Um pavio (wick) longo no mensal/semanal/diário marca onde o preço **rejeitou** após varrer ordens.
- Acima de topos iguais (EQH) e máximas anteriores (PDH/PWH) acumula **buy-side liquidity (BSL)**.
- Abaixo de fundos iguais (EQL) e mínimas (PDL/PWL) acumula **sell-side liquidity (SSL)**.
- Regra prática: o preço tende a **buscar a liquidez** antes de reverter. Pavio HTF não preenchido
  = ímã. Mapear pavios M/W/D **antes** de definir alvos ([[SMC]]).

## 2. Traps — a colheita da liquidez
| Trap | O que acontece | Confirmação |
|------|----------------|-------------|
| **Bull Trap / UT** | Rompe resistência (EQH/PDH), puxa breakout buyers, e reverte | EQH sweep + CHoCH bearish |
| **Bear Trap / Spring** | Perde suporte (EQL/PDL), tira stops de longs, e reverte | EQL sweep + CHoCH bullish |
| **BSL Grab / Stop Hunt** | Pavio rápido além do nível só para pegar stops | Rejeição imediata + volume de absorção |

> Cruzar com [[Wyckoff]]: Spring = sweep de SSL na base da acumulação; UTAD = sweep de BSL no topo
> da distribuição. Cruzar com [[bull-bear-traps]] para os padrões de candle.

## 3. USDT.D — o confirmador macro inverso
O índice de dominância do Tether (USDT.D) é **inversamente correlacionado** ao mercado cripto:
dinheiro entrando em stablecoin = saindo de risco.

| USDT.D | Cripto | Leitura |
|--------|--------|---------|
| Subindo / rompendo resistência | Bearish | Capital fugindo p/ stable → **nega** bias de long |
| Caindo / perdendo suporte | Bullish | Capital saindo de stable p/ risco → **confirma** bias de long |
| Lateral | Neutro | Sem confirmação macro — reduzir convicção |

### O setup "short do USDT.D que não materializa" (armadilha comum)
Em markdown, esperar o USDT.D **rejeitar** uma resistência para shortar o BTC frequentemente falha:
se o USDT.D rompe e segura, o BTC continua caindo (não há repique para shortar) — o trade de short
"perfeito" nunca aciona. **Inversão:** quando o USDT.D finalmente *exaure* (rejeita de verdade,
com pavio + volume), aí sim o BTC ganha o repique. Ler o USDT.D é ler o combustível, não o preço.

## 4. Síntese na Fase 8
Declarar sempre: `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega | Trap ativo: [tipo ou —]`
- Se o bias de long depende de um pavio de SSL já varrido **e** USDT.D caindo = dupla confirmação.
- Se o bias contradiz o USDT.D = rotular `contra-macro` e aplicar penalidade no [[confluence-score]].

## Backlinks
- [[SMC]] — BSL/SSL, EQH/EQL, FVG, Order Blocks, CHoCH/BOS
- [[Wyckoff]] — Spring e UTAD como sweeps de liquidez
- [[bull-bear-traps]] · [[short-long-squeeze]] — mecânica das armadilhas
- [[btc-macro-correlations]] — USDT.D no conjunto DXY/SPX/TOTAL
- [[confluence-score]] — penalidade contra-macro
- [[liquidation-heatmap]] — onde a liquidez de alavancagem se acumula
