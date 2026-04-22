# Wyckoff Method

> Atualizado: 2026-04-21 — Conexões com SMC e Brain expandidas

## As 4 Fases

| Fase | Descrição | Bias operacional |
|------|-----------|-----------------|
| **Acumulação** | Lateral após downtrend — smart money comprando | Aguardar Spring → Long |
| **Markup** | Uptrend após acumulação | Long (pivot pullback) |
| **Distribuição** | Lateral após uptrend — smart money vendendo | Aguardar UT → Short |
| **Markdown** | Downtrend após distribuição | Short (pivot bounces) |

## Eventos Chave — Acumulação

| Evento | Descrição | Sinal |
|--------|-----------|-------|
| SC (Selling Climax) | Queda abrupta com alto volume | Suporte formado |
| AR (Automatic Rally) | Rally automático pós-SC | Resistência formada |
| ST (Secondary Test) | Reteste do SC com menor volume | Confirma suporte |
| **Spring** | **Falsa quebra ABAIXO do suporte** | **Entrada de LONG — melhor R:R** |
| LPS | Last Point of Support — pullback antes do markup | Entrada de long confirmada |
| SOS | Sign of Strength — rally com volume após Spring | Confirma markup iminente |

## Eventos Chave — Distribuição

| Evento | Descrição | Sinal |
|--------|-----------|-------|
| BC (Buying Climax) | Rally abrupto com alto volume | Resistência formada |
| AR (Automatic Reaction) | Queda automática pós-BC | Suporte formado |
| ST (Secondary Test) | Reteste do BC com menor volume | Confirma fraqueza compradora |
| **UT (Upthrust)** | **Falsa quebra ACIMA da resistência** | **Entrada de SHORT — melhor R:R** |
| LPSY | Last Point of Supply — bounce fraco antes do markdown | Entrada de short confirmada |
| SOW | Sign of Weakness — queda com volume após UT | Confirma markdown iminente |

## Lei do Esforço × Resultado

> "Alto volume com resultado pequeno = absorção = inversão iminente"

- Volume de venda alto + preço não cai muito = compradores institucionais absorvendo → Spring
- Volume de compra alto + preço não sobe muito = vendedores institucionais distribuindo → UT
- Aplicação: verificar volume do candle de sweep ANTES de confirmar Spring/UT

## Conexões com SMC LuxAlgo (Unificação de Frameworks)

| Wyckoff | SMC LuxAlgo | Brain/Insights |
|---------|-------------|---------------|
| Spring | EQL sweep + CHoCH bullish | "Sweep de liquidez = pós-short-squeeze" |
| UT/UTAD | EQH sweep + CHoCH bearish | "CHoCH Sweep Diário = UT de distribuição" |
| Acumulação | BOS bullish sequence | Rally de BTC 73k→78k (Abr/2026) |
| Distribuição | CHoCH bearish sequence | AAVE 95.65 wick (21/Abr/2026) |

**Implicação:** Quando SMC mostra sweep de EQL/EQH + CHoCH, verificar se há estrutura Wyckoff no TF maior. Confluência SMC + Wyckoff = entrada de máxima convicção.

## Exemplo Observado — BTC Abr/2026

- Spring: mínima 73,256 (16/Abr) → varreu suporte → reversão para 78,300
- Acumulação: range 73,256–78,300 (3 dias) → Markup iniciado → BOS 75,999 quebrado
- LPS: pullback atual 75,232–75,500 após BOS = LPS antes de continuar para 77,810+

## Exemplo Observado — AAVE 21/Abr/2026

- Distribuição: downtrend prolongado (de $400+ para $92)
- UT: candle diário com wick em 95.65 (CHoCH 95.52 varrido) + fechamento em 93.21
- Próximo evento esperado: SOW (queda com volume) → Markdown rumo a 89-84

## Detecção no TradingView MCP

```
chart_get_state → verificar TF (4H/D para fases maiores)
data_get_pine_labels → "EQH", "EQL", "CHoCH", "BOS" do SMC LuxAlgo
data_get_study_values → RSI (posição macro) + Volume
quote_get → OHLC para verificar wick/body do candle de Spring/UT
```

## Backlinks
- [[SMC]]
- [[BTCUSD]]
- [[research/2026-04-21-price-action-wyckoff-volume-batch5]]
- [[brain/patterns]]
- [[brain/insights]]
