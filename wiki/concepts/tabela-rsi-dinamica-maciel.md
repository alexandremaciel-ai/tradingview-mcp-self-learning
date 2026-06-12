# Tabela RSI Dinâmica - Maciel

> Criado: 2026-06-12
> Categoria: Indicador custom (do usuário) / RSI / Multi-Timeframe

## Definição
Indicador **próprio do usuário** (Pine `table.new`) que consolida o RSI em todos os timeframes e — o diferencial — calcula **a que preço o RSI atinge 30, 50 e 70** em cada TF. É a origem do termo **"P.RSI50"** usado nas sessões. Componente do layout **RSI's e MACD**.

## O que plota
Tabela (ler via `data_get_pine_tables(study_filter="Tabela RSI")`) com colunas:
`Time | RSI | P. RSI 30 | P. RSI 50 | P. RSI 70`
e linhas por TF: 5m, 15m, 1h, 4h, 1D, 1S (semanal), 2S (bissemanal), 1M.

- **RSI** = valor atual do RSI naquele TF.
- **P. RSI 30/50/70** = o preço do BTC onde o RSI daquele TF bateria 30 (sobrevenda), 50 (equilíbrio) ou 70 (sobrecompra).

## Leituras práticas
- **P.RSI50** = preço de "equilíbrio" do momentum no TF → ímã/pivô. Acima dele, RSI>50 (viés comprador); abaixo, vendedor.
- **P.RSI30 (TF alto)** = alvo objetivo de realização de short / zona de bounce. **P.RSI70** = teto técnico de swing long.
- **Divergência entre TFs** = informação-chave: 5m OB (72.9) enquanto 1D OS (33.9) → momentum curto esticado contra um ciclo ainda comprado/vendido → priorizar o TF do trade.
- Alinha-se forte com Fib e SMC: quando P.RSI50 coincide com OB/Golden Zone = confluência sniper.

## Snapshot 2026-06-12 (4H)
RSI 4h 57.2 · P.RSI50 4h ≈ 62.831 · P.RSI30 4h ≈ 57.641 · P.RSI70 4h ≈ 66.723.

## Limitações
- Os preços-alvo são recalculados a cada barra (dinâmicos) — reler antes de usar.
- Em TFs muito baixos (5m) os níveis mudam rápido demais para swing.

## Backlinks
- [[rsi-divergences]] — base teórica do RSI e divergências
- [[rsi-ema-reverse-calculator]] — mesma ideia (preço-alvo de RSI) no layout RSI's e MACD
- [[fibonacci-structural]] — confluência P.RSI50 + Golden Zone
- [[layouts]]
- [[indicators]]
