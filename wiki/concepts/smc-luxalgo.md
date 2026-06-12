# Smart Money Concepts [LuxAlgo] (indicador)

> Criado: 2026-06-12
> Categoria: Indicador / SMC / Estrutura & Liquidez

## Definição
Implementação Pine do LuxAlgo dos conceitos de Smart Money. É a ferramenta central do layout **Liquidity e SMC**. Para a teoria, ver [[SMC]]; esta página documenta os **outputs do indicador** e como lê-los via MCP.

## O que plota e como ler (pine tools)
| Output | Tool MCP | Significado |
|--------|----------|-------------|
| `CHoCH` / `BOS` (labels) | `data_get_pine_labels(study_filter="Smart Money")` | CHoCH = mudança de caráter (reversão); BOS = rompimento de estrutura (continuação) |
| `EQH` / `EQL` (labels) | idem | Equal Highs/Lows = liquidez igual acumulada (alvo de varredura) |
| Níveis de estrutura | `data_get_pine_lines(study_filter="Smart Money")` | swing highs/lows e níveis internos |
| Order Blocks | `data_get_pine_boxes(study_filter="Smart Money")` | zonas `{high,low}` institucionais de entrada |

## Leituras práticas
- **BOS** na direção da tendência HTF = continuação válida; **CHoCH** contra a tendência = alerta de reversão (confirmar com HTF).
- **EQH/EQL** = ímãs de liquidez: preço tende a varrê-los antes de reverter (stop hunt).
- **OB + FVG + Fib Golden Zone** = entrada sniper (Fase 3 + Fase 5 do checklist).
- Sempre filtrar CHoCH de TF baixo com a estrutura do HTF (evita ruído).

## Limitações
- Gera muitos labels históricos (até 500) — focar nos mais recentes/próximos ao preço.
- Sensível ao parâmetro de swing; CHoCH frequente em range = ruído.

## Backlinks
- [[SMC]] — teoria (BOS/CHoCH/FVG/OB/EQH/EQL)
- [[layouts]] — layout Liquidity e SMC
- [[whale-liquidity-absorption]] — complementa o mapa de liquidez
- [[indicators]]
