# RSI + StochRSI Combinados — Direção (HTF) × Timing (LTF)

> O erro clássico é operar o StochRSI isolado e shortar todo overbought (ou comprar todo oversold).
> Em tendência forte o oscilador fica "colado" no extremo e o trade morre. A regra que evita isso:
> **o RSI dos timeframes maiores decide a DIREÇÃO; o StochRSI dos menores decide só o TIMING.**

## A regra-mestre

| Camada | Indicador | TF | Papel |
|--------|-----------|-----|-------|
| Direção | **RSI (14)** | M / W / D / 4H | Define o lado permitido. RSI > 50 = **long only** / RSI < 50 = **short only** |
| Timing | **Stoch RSI** | 1H / 15M | Libera o gatilho: cruzamento %K×%D em zona extrema |

- **M = direção de ciclo, W = regime** — ambos têm peso macro acima do D/4H ([[multi-timeframe-analysis]]).
- **NUNCA operar o StochRSI contra a direção do RSI HTF.** É a regra inegociável.

## As 4 combinações

| RSI HTF | StochRSI LTF | Leitura | Ação |
|---------|--------------|---------|------|
| Bullish (>50) | Oversold + cross↑ | Pullback terminando em tendência de alta | **Gatilho de long** ✅ |
| Bullish (>50) | Overbought | Continuação — força, não exaustão | **NÃO shortear** (segurar/adicionar) |
| Bearish (<50) | Overbought + cross↓ | Repique terminando em tendência de baixa | **Gatilho de short** ✅ |
| Bearish (<50) | Oversold | Continuação bearish | **NÃO comprar** (oversold pode esticar) |

> Resumo: o StochRSI em extremo **a favor** do RSI HTF = continuação (não reverter).
> O StochRSI em extremo **contra** o RSI HTF, com cross, = gatilho de entrada na direção do HTF.

## Por que funciona
O StochRSI é o RSI normalizado na sua própria faixa — hiper-sensível, ótimo para *timing*, péssimo
para *direção*. O RSI HTF filtra os sinais ruins: em bull, todo "overbought" do StochRSI seria um
short perdedor; o filtro de direção simplesmente os descarta. Sobram só os gatilhos de pullback
a favor da tendência maior — onde o R:R é melhor.

## Reset de oscilador
- **Reset de oversold em tendência de alta** = continuação (combustível para a próxima perna).
- **Reset de overbought em tendência de baixa** = continuação do markdown.
- O StochRSI mensal/semanal é *contextual* (reset macro de ciclo), nunca gatilho de execução.
  O timing fino permanece em W/1H/15M.

## Divergências de StochRSI (1H/15M)
- Preço HH + %K LH em zona >80 = **bearish** (só vale se o RSI HTF também permitir short).
- Preço LL + %K HL em zona <20 = **bullish** (só vale se o RSI HTF permitir long).

## Como registrar na sessão
`Indicadores: RSI [M/W/D/4H direção] | StochRSI [1H/15M %K/%D + cross + zona]`
→ declarar explicitamente: "RSI HTF = [long/short] only; StochRSI = [gatilho/continuação]".

## Backlinks
- [[rsi-divergences]] — mecânica do RSI, divergências clássicas e ocultas
- [[multi-timeframe-analysis]] — hierarquia M→W→D→4H→1H→15M
- [[confluence-score]] — o StochRSI não soma ponto isolado, só libera o gatilho na direção do RSI HTF
- [[trade-playbooks]] — gatilho de execução dos playbooks 1 e 2
