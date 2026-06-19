# Referência — Vocabulário de Critérios (campo `Critérios:`)

> O campo `- **Critérios:**` de cada previsão em `wiki/brain/predictions-log.md` é a **lista
> parseável** dos sinais que sustentaram o bias. É o elo que liga o RESULTADO do trade à
> CONFIABILIDADE de cada sinal: `metrics_engine.py` lê esses slugs e, quando a previsão fecha,
> credita (✅) ou debita (❌) cada critério, recalculando o Hit Rate em `wiki/brain/indicators.md`.
> Daí o `Confluence Score` passa a **pesar cada sinal pela performance empírica** (ver
> `[[confluence-score]]`). Sem tagueamento consistente, a calibração não acontece — use SEMPRE os
> slugs desta tabela.

## Sintaxe

```
- **Critérios:** ema200+, macd+, rsi+, smc-ob+, usdtd+, macro+ | -adx, -funding
```

- Lista separada por vírgula. Cada item é `slug` + sinal:
  - `slug+` → o critério **pontuou A FAVOR** do bias (contribuiu para o score).
  - `slug-` (ou prefixo `-slug`) → o critério **contradisse / foi penalidade** (não conta como acerto;
    se a previsão fechar como win, esse `-` NÃO é creditado; ajuda só a auditar contradições).
- Use só os slugs abaixo. Slug desconhecido é ignorado pelo parser (não quebra), mas perde-se o aprendizado.
- Mínimo recomendado: liste TODOS os critérios `+` que entraram no Confluence Score (os mesmos
  que a Fase 9 do `technical-checklist` enumerou). Quanto mais fiel, melhor a calibração.

## Regra de crédito (aplicada por `metrics_engine.py`)

| Resultado da previsão | O que acontece com cada `slug+` |
|---|---|
| `✅ win` | +1 **Acerto** |
| `❌ loss` | +1 **Falha** |
| `⚪ expirou` + `Pós-fecho: errada` | +1 **Falha** (anti-viés) |
| `⚪ expirou` + `Pós-fecho: certa/neutra` | ignorado |
| `⏳ aberta` | ignorado (ainda não resolvida) |

`Hit Rate = Acertos / (Acertos + Falhas)`. Itens com sinal `-` nunca recebem crédito.

## Slugs canônicos

### Backed por seção em `indicators.md` (Hit Rate é reescrito lá)
| slug | Seção em `indicators.md` |
|---|---|
| `ema200` | EMA 50/200 |
| `ema-cross` | EMA Cross (ribbon) |
| `sma-cross` | SMA Cross |
| `rsi` | RSI |
| `stochrsi` | RSI Estocástico (Stoch RSI) |
| `macd` | MACD |
| `adx` | ADX |
| `atr` | ATR |
| `bollinger` | Bollinger Awesome Alert R1.1 (JustUncleL) |
| `supertrend` | Supertrend |
| `smc-choch` | CHoCH / BoS (SMC) |
| `smc-fvg` | FVG (SMC) |
| `smc-ob` | Smart Money Concepts [LuxAlgo] |
| `volume` | Crypto Smart Volume PRO (v1/v2) |
| `vrvp` | Visible Range Volume Profile |
| `whale` | Whale Liquidity and Absorption Profile [AlgoAlpha] |
| `mvrv` | MVRV Z Score & Free Float Z-Score |
| `divergencia` | RSI Divergences Pro + Adaptive MTF Filter (V.V.I.R.) |
| `mxwll` | Mxwll Suite |

### Critérios de contexto (Hit Rate só na tabela de `metrics.md`, sem seção própria)
| slug | Significado |
|---|---|
| `macro` | Bias alinhado ao Veredito macro do briefing (risk-on/off) |
| `usdtd` | USDT.D confirmando o lado (mola/topo, divergência a favor) |
| `dxy` | DXY a favor do bias |
| `funding` | Funding/OI a favor (squeeze risk a favor) |
| `liquidez` | Sweep/grab de liquidez ou POI HTF a favor |
| `fib-golden` | Golden Zone Fibonacci (0.618–0.65) na zona de entrada |
| `wyckoff` | Fase de Wyckoff (SC/AR/Spring/UTAD) confirmando |
| `estrutura` | Estrutura MTF (BoS/tendência) a favor |
| `poi` | POI institucional alinhado ([[institutional-flow-poi]]) |

> Mantenha esta lista 1:1 com os cabeçalhos `##` de `indicators.md`. Ao adicionar um indicador
> novo lá, adicione o slug aqui (e no mapa `SLUG_TO_HEADER` de `metrics_engine.py`).

## Backlinks
- [[confluence-score]] — consome o Hit Rate por critério para pesar o score.
- [[indicators]] — destino do writeback de Acertos/Falhas/Hit Rate.
