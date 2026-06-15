# Referência — Confluence Score + Declaração de Bias (Fase 9)

> Detalhe completo em `[[confluence-score]]` (wiki/concepts). Esta é a regra operacional.

## Cálculo do Confluence Score (0–10)

1. Sintetizar todas as fases em um bias claro: **LONG / SHORT / NEUTRO**.
2. **Calcular o score (0–10)** — listar critérios que pontuaram e penalidades aplicadas
   (ex: `Score 7/10 = 1,3,5,6,7,8 ✓ | −2 contra-macro`).
3. Confiança DERIVADA do score: **≥8 = alta | 6–7 = média | 4–5 = baixa | <4 = NEUTRO**
   (não usar "feeling").
4. Tabela score→ação para o TAMANHO: **≥8 cheia | 6–7 reduzida | 4–5 só observar/paper | <4 não operar**.

## Penalidades

- Bias contradiz macro → rótulo `contra-macro` + **−2**.
- **USDT.D divergência (BTC/ETH):** divergência de RSI no USDT.D — ou cruzada BTC↔USDT.D — que
  **contradiz** o bias → **−1 + rótulo `usdtd-diverge`**; que **confirma** o bias → conta no
  critério de divergência confirmando.
- Refresh de feeds FALHOU (rede/erro) ou `raw/feeds/latest.md` segue `indisponível`/ausente →
  **−1 + rótulo `dados-parciais`** (não assumir funding/OI não lidos). Dados puxados com sucesso → SEM penalidade.
- Fim de semana (TradFi congelado) → rótulo `macro-parcial (dados sex)` no bloco macro.

## Regras finais

- Se nenhum framework converge → declarar `NEUTRO — sem confluência` (score < 4).
- **Checar disciplina:** se `brain/metrics.md` indicar circuit breaker 🔴 (3 losses seguidos / DD 5% no dia)
  → rebaixar para observação/paper ([[trading-psychology]]).
