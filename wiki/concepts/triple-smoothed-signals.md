# Triple Smoothed Signals [AlgoAlpha]

> Criado: 2026-06-12
> Categoria: Indicador / Tendência / Sinais

## Definição
Indicador de sinais de tendência com **tripla suavização** (AlgoAlpha) — reduz ruído para emitir sinais Bullish/Bearish mais limpos. Componente do layout **Trade Diario**. (Há também uma entrada em [[indicators]] sob "AlgoAlpha — Triple Smoothed Signals".)

## O que plota
- `Bullish Signal` / `Bearish Signal` — marcadores de virada de tendência (com o preço do sinal).
- Linha/zona suavizada de tendência sobreposta ao preço.

## Leituras práticas
- A tripla suavização → **menos sinais, mais confiáveis**, porém **mais atrasados**. Bom filtro de tendência; ruim como gatilho exato de topo/fundo.
- Usar a direção do sinal como **permissão direcional** (Bullish = preferir longs) e deixar o timing fino para osciladores (RSI/StochRSI/MACD do mesmo layout).
- Sinal contra a tendência HTF = ignorar ou aguardar confirmação.

## Limitações
- Atraso inerente à suavização tripla — em reversões rápidas, sinaliza depois do movimento.
- Caixa-preta proprietária.

## Backlinks
- [[multi-timeframe-analysis]] — direção HTF
- [[layouts]] — layout Trade Diario
- [[indicators]]
