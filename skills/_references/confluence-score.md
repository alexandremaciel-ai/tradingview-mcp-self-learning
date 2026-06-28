# Referência — Confluence Score + Declaração de Bias (Fase 9)

> Detalhe completo em `[[confluence-score]]` (wiki/concepts). Esta é a regra operacional.

## Cálculo do Confluence Score (0–10)

1. Sintetizar todas as fases em um bias claro: **LONG / SHORT / NEUTRO**.
2. **Calcular o score (0–10)** — listar critérios que pontuaram e penalidades aplicadas
   (ex: `Score 7/10 = 1,3,5,6,7,8 ✓ | −2 contra-macro`).
3. Confiança DERIVADA do score: **≥8 = alta | 6–7 = média | 4–5 = baixa | <4 = NEUTRO**
   (não usar "feeling").
4. Tabela score→ação para o TAMANHO: **≥8 cheia | 6–7 reduzida | 4–5 só observar/paper | <4 não operar**.

## Pesos dirigidos por dados (calibração empírica)

> O score **aprende com o resultado**: o peso de cada critério é escalado pelo Hit Rate empírico
> que o `metrics_engine.py` mantém em `wiki/brain/indicators.md` (alimentado pelo campo
> `Critérios:` das previsões — ver `[[criteria-keys]]`). O `brain-read` injeta esses números no
> **Cartão de Calibração**; aplicá-los aqui NÃO é opcional.

Para CADA critério que pontuaria, olhar `Acertos/Falhas` (= N amostras) e o Hit Rate:

| Amostra (N = Acertos+Falhas) | Hit Rate | Efeito no critério |
|---|---|---|
| **< 8 (guarda)** | qualquer | peso **atual/cheio**, SEM ajuste (amostra pequena = não confiar ainda) |
| ≥ 8 | **< 40%** | **não pontua** + rótulo `sinal-fraco:<slug>` (anti-sinal — considerar inverter a leitura) |
| ≥ 8 | 40–55% | **meio-peso** (conta 0.5 ponto) |
| ≥ 8 | 55–70% | peso cheio |
| ≥ 8 | **> 70%** | peso cheio + **elegível ao bônus de confluência** |

- A guarda de amostra (< 8) existe para 1–2 trades não distorcerem o peso de um sinal — honesto por
  construção. Critério sem registro em `indicators.md` = tratar como < 8 (peso atual).
- Declarar no bloco de bias os ajustes aplicados, ex.: `−adx (sinal-fraco 32%, n=11) | macd meio-peso (52%, n=9)`.

**Trava por setup** (Win Rate em `wiki/setups/index.md`, mesma guarda de amostra ≥ 10):
- WR < 50% e N ≥ 10 → teto de confiança em **"média"** + **−1** (rótulo `setup-fraco`).
- WR ≥ 70% e N ≥ 10 → **+1** (cap em 10).

## Penalidades

- Bias contradiz macro → rótulo `contra-macro` + **−2**.
- **USDT.D divergência (BTC/ETH):** divergência de RSI no USDT.D — ou cruzada BTC↔USDT.D — que
  **contradiz** o bias → **−1 + rótulo `usdtd-diverge`**; que **confirma** o bias → conta no
  critério de divergência confirmando.
- Refresh de feeds FALHOU (rede/erro) ou `raw/feeds/latest.md` segue `indisponível`/ausente →
  **−1 + rótulo `dados-parciais`** (não assumir funding/OI não lidos). Dados puxados com sucesso → SEM penalidade.
- Fim de semana (TradFi congelado) → rótulo `macro-parcial (dados sex)` no bloco macro.
- **`DADO_INDISPONIVEL` (anti-alucinação, Invariante 0):** qualquer dado que sustentaria o bias e
  **não foi puxado da fonte real** → NÃO assumir valor; tratar como `dados-parciais` (**−1**) e
  marcar o critério ausente. Nunca pontuar um critério com número inventado.
- **`CONFLITO_DE_DADOS`:** fontes que divergem para o mesmo dado (ex.: preço MCP × TradingView) →
  declarar AMBAS, **−1**, e **não forçar conclusão** (não escolher a que confirma o bias).
- **Rotação de liquidez (Veredito do `macro-scan` Step 1.5 — [[liquidity-rotation-cycle]]):** veredito
  **Alto Risco de Bull Trap** (rota de liquidez contradiz o bias, ou índice ES `TOTAL2ES`/`TOTAL3ES`
  em sobrecompra macro contra um LONG) → **−1 + rótulo `bull-trap-liquidez`** (critério `-liq-rotacao`).
  Veredito **Cenário Otimizado** alinhado ao bias → conta no critério **`liq-rotacao+`** (elegível à
  confluência). **Neutro** = não pontua. EQUITIES = critério ausente (rota `N/A`, sem efeito).

## Regras finais

- **Setup sem `nivel_invalidacao` explícito = INVÁLIDO** — não emitir bias acionável. Todo bias
  LONG/SHORT declara os 4 campos (`vies_HTF | estrutura_4H | nivel_invalidacao | gatilho_LTF`,
  Fase 9 do `technical-checklist`); faltando o preço exato que mata a tese, rebaixar a `NEUTRO`.
- Se nenhum framework converge → declarar `NEUTRO — sem confluência` (score < 4).
- **Checar disciplina:** se `brain/metrics.md` indicar circuit breaker 🔴 (3 losses seguidos / DD 5% no dia)
  → rebaixar para observação/paper ([[trading-psychology]]).
