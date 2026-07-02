# Referência — TradingView Tools (Decision Tree + Context Management)

> Carregada por path quando uma skill de análise/Pine precisa do detalhe completo de tools.
> O `CLAUDE.md` mantém só um cheatsheet de 5–8 linhas; o detalhe vive aqui.

## Decision Tree — Which Tool When

- **Ler chart:** `chart_get_state` (symbol/TF/IDs dos indicadores — chamar 1×) → `data_get_study_values` (valores numéricos dos indicadores visíveis) → `quote_get` (snapshot de preço/OHLC/vol).
- ⚠️ **`data_get_study_values` dá só o VALOR ATUAL.** Marcas de **divergência** (Bull/Bear) e estruturas (**OB/FVG/CHoCH/BOS/EQH/EQL**) NÃO saem por ele — são `line/label/box/plotshape`. Lê-las exige os pine tools abaixo ou `capture_screenshot` do pane. Afirmar divergência/estrutura a partir de `study_values` (ou por inferência de price action) viola o Invariante 0 → use a fonte ou declare `DADO_INDISPONIVEL`.
- 🔴 **Divergência Bull/Bear (V.V.I.R./MACD Div Pro/Stoch RSI Div Pro) = `plotshape` → NENHUMA tool de dados lê** (confirmado 28/06). `data_get_pine_labels` devolve só projeções (RSI78/30, K90/10); `data_get_pine_lines("RSI Div")` devolve ~5.400 linhas do filtro MTF (ruído). **Única fonte = `capture_screenshot(region="full")`** — region `chart` **CORTA** o sub-painel do oscilador. Ler o marcador no candle atual; só quando a divergência for decisiva ao bias.
- **Pine custom drawings** (indicador precisa estar visível): `data_get_pine_lines` (níveis horizontais + alguns segmentos via `verbose=true`; **NÃO** serve p/ a divergência dos indicadores acima), `_labels` (texto+preço — `label.new`, não `plotshape`), `_tables` (linhas), `_boxes` ({high,low}); `study_filter` p/ alvejar um indicador.
- **Price data:** `data_get_ohlcv` (sempre `summary: true`; `count` limita) | `quote_get` (último preço).
- **Mudar chart:** `chart_set_symbol` | `chart_set_timeframe` | `chart_set_type` | `chart_manage_indicator` (nome completo) | `chart_scroll_to_date` | `chart_set_visible_range` | `indicator_set_inputs`.
- **Pine Script:** `pine_set_source` → `pine_smart_compile` → `pine_get_errors`/`pine_get_console` | `pine_save`/`pine_new`/`pine_open`. ⚠️ evitar `pine_get_source` (200KB+).
- **Desenhar:** `draw_shape` (horizontal_line/trend_line/rectangle/text) | `draw_list` | `draw_remove_one` | `draw_clear`.
- **Alertas:** `alert_create` (crossing/greater_than/less_than) | `alert_list` | `alert_delete`.
- **UI:** `ui_open_panel` | `ui_click` | `ui_fullscreen` | `capture_screenshot` (full/chart/strategy_tester).
- **Layout:** `layout_list` | trocar = `ui_evaluate` navegando `/chart/{slug}/` (`layout_switch` não recarrega o Desktop) | `pane_list`. Perfis em `wiki/brain/layouts.md`.
- **TV offline:** `tv_launch` | `tv_health_check`.

## Context Management Rules

Evitar context bloat: (1) `data_get_ohlcv` sempre `summary: true` (exceto barras individuais); (2) `study_filter` nos pine tools; (3) nunca `verbose: true` sem pedido; (4) evitar `pine_get_source` (200KB+); (5) indicadores protegidos → `data_get_study_values`, não `data_get_indicator`; (6) preferir `capture_screenshot` a datasets grandes; (7) `chart_get_state` só 1× no início; (8) cap OHLCV: `count: 20` rápida / `100` profunda / `500` só se necessário.

## Tool Conventions

- Tools retornam `{ success: true/false, ... }`. Entity IDs (`chart_get_state`) são por sessão — não cachear.
- Pine indicators precisam estar **visíveis** para os pine graphics tools lerem.
- `chart_manage_indicator` exige **nome completo**: "Relative Strength Index" (não "RSI"), "Moving Average Exponential" (não "EMA"), "Bollinger Bands" (não "BB").
- Screenshots → `screenshots/` com timestamp. OHLCV cap 500 barras, trades 20/req. Pine labels cap 50/study (override via `max_labels`).
- ⚠️ **Bug `quote_get(symbol=...)` (12/06):** ignora o parâmetro e retorna o chart ativo → para o macro, **DEVE** `chart_set_symbol` por ticker (não confiar em "quotes paralelos por símbolo").
- ⚠️ **Race condition pós `chart_set_symbol`/navegação de layout (confirmado 02/07):** `data_get_pine_boxes`/`_labels`/`_lines` podem retornar vazio (`total_boxes: 0` / `showing: 0`) logo após trocar de símbolo ou navegar para outro layout — o indicador (ex.: Whale Liquidity and Absorption, SMC LuxAlgo) ainda não recalculou no novo símbolo, mesmo com `chart_ready: true` no retorno do `chart_set_symbol`/`chart_set_timeframe`. **Um resultado vazio nesse contexto NÃO é `DADO_INDISPONIVEL`** — re-consultar a MESMA tool 1× (sem re-navegar) antes de aceitar "nenhuma zona/label". Só declarar `DADO_INDISPONIVEL` se a 2ª tentativa também vier vazia. Mesma cautela vale pra `capture_screenshot` logo após troca de símbolo (canvas pode estar em branco/stale enquanto o data-layer já respondeu — ver [[feedback_tv_canvas_desync_recovery]] na memória).

## Architecture

```
Claude Code ←→ MCP Server (stdio) ←→ CDP (localhost:9222) ←→ TradingView Desktop (Electron)
```

Pine graphics path: `study._graphics._primitivesCollection.dwglines.get('lines').get(false)._primitivesDataById`
