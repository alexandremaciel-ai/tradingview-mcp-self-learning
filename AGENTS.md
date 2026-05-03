# TradingView MCP — Codex Instructions

68 tools for reading and controlling a live TradingView Desktop chart via CDP (port 9222).

---

## ⚡ AUTO-PILOT — Regra Obrigatória (leia PRIMEIRO)

**Este bloco se aplica a TODA interação neste projeto. Não é opcional. Não precisa ser pedido.**

### ANTES de responder qualquer pedido:
1. Ler `wiki/brain/insights.md` — aplicar aprendizados anteriores
2. Ler `wiki/brain/mistakes.md` (últimos 10) — evitar repetir erros
3. Se o pedido envolve um ativo → ler `wiki/assets/{SYMBOL}.md`
4. Se o pedido envolve análise → ler `wiki/brain/predictions-log.md` para previsões abertas
5. Se previsão aberta existe para o ativo → comparar com estado atual → fechar como ✅/❌

### DEPOIS de responder qualquer pedido:
1. **Sempre** — Extrair insight da interação → append em `wiki/brain/insights.md`
2. **Se bias definido** — Registrar previsão em `wiki/brain/predictions-log.md`
3. **Se indicador surpreendeu** — Atualizar `wiki/brain/indicators.md`
4. **Se padrão já visto antes** — Atualizar `wiki/brain/patterns.md`
5. **Se erro confirmado** — Append em `wiki/brain/mistakes.md`
6. **Sempre** — Append em `wiki/log.md`

> Se algum brain file não existir, criar cópia de `wiki/brain/_templates/{nome}.md`.
> Se `wiki/index.md` não existir, criar de `wiki/index.initial.md`.
> Se `wiki/log.md` não existir, criar de `wiki/log.initial.md`.

---

## Decision Tree — Which Tool When

### "What's on my chart right now?"
1. `chart_get_state` → symbol, timeframe, chart type, list of all indicators with entity IDs
2. `data_get_study_values` → current numeric values from all visible indicators (RSI, MACD, BBands, EMAs, etc.)
3. `quote_get` → real-time price, OHLC, volume for current symbol

### "What levels/lines/labels are showing?"
Custom Pine indicators draw with `line.new()`, `label.new()`, `table.new()`, `box.new()`. These are invisible to normal data tools. Use:

1. `data_get_pine_lines` → horizontal price levels drawn by indicators (deduplicated, sorted high→low)
2. `data_get_pine_labels` → text annotations with prices (e.g., "PDH 24550", "Bias Long ✓")
3. `data_get_pine_tables` → table data formatted as rows (e.g., session stats, analytics dashboards)
4. `data_get_pine_boxes` → price zones / ranges as {high, low} pairs

Use `study_filter` parameter to target a specific indicator by name substring (e.g., `study_filter: "Profiler"`).

### "Give me price data"
- `data_get_ohlcv` with `summary: true` → compact stats (high, low, range, change%, avg volume, last 5 bars)
- `data_get_ohlcv` without summary → all bars (use `count` to limit, default 100)
- `quote_get` → single latest price snapshot

### "Analyze my chart" (full report workflow)
1. `quote_get` → current price
2. `data_get_study_values` → all indicator readings
3. `data_get_pine_lines` → key price levels from custom indicators
4. `data_get_pine_labels` → labeled levels with context (e.g., "Settlement", "ASN O/U")
5. `data_get_pine_tables` → session stats, analytics tables
6. `data_get_ohlcv` with `summary: true` → price action summary
7. `capture_screenshot` → visual confirmation

### "Change the chart"
- `chart_set_symbol` → switch ticker (e.g., "AAPL", "ES1!", "NYMEX:CL1!")
- `chart_set_timeframe` → switch resolution (e.g., "1", "5", "15", "60", "D", "W")
- `chart_set_type` → switch chart style (Candles, HeikinAshi, Line, Area, Renko, etc.)
- `chart_manage_indicator` → add or remove studies (use full name: "Relative Strength Index", not "RSI")
- `chart_scroll_to_date` → jump to a date (ISO format: "2025-01-15")
- `chart_set_visible_range` → zoom to exact date range (unix timestamps)

### "Work on Pine Script"
1. `pine_set_source` → inject code into editor
2. `pine_smart_compile` → compile with auto-detection + error check
3. `pine_get_errors` → read compilation errors
4. `pine_get_console` → read log.info() output
5. `pine_get_source` → read current code back (WARNING: can be very large for complex scripts)
6. `pine_save` → save to TradingView cloud
7. `pine_new` → create blank indicator/strategy/library
8. `pine_open` → load a saved script by name

### "Practice trading with replay"
1. `replay_start` with `date: "2025-03-01"` → enter replay mode
2. `replay_step` → advance one bar
3. `replay_autoplay` → auto-advance (set speed with `speed` param in ms)
4. `replay_trade` with `action: "buy"/"sell"/"close"` → execute trades
5. `replay_status` → check position, P&L, current date
6. `replay_stop` → return to realtime

### "Screen multiple symbols"
- `batch_run` with `symbols: ["ES1!", "NQ1!", "YM1!"]` and `action: "screenshot"` or `"get_ohlcv"`

### "Draw on the chart"
- `draw_shape` → horizontal_line, trend_line, rectangle, text (pass point + optional point2)
- `draw_list` → see what's drawn
- `draw_remove_one` → remove by ID
- `draw_clear` → remove all

### "Manage alerts"
- `alert_create` → set price alert (condition: "crossing", "greater_than", "less_than")
- `alert_list` → view active alerts
- `alert_delete` → remove alerts

### "Navigate the UI"
- `ui_open_panel` → open/close pine-editor, strategy-tester, watchlist, alerts, trading
- `ui_click` → click buttons by aria-label, text, or data-name
- `layout_switch` → load a saved layout by name
- `ui_fullscreen` → toggle fullscreen
- `capture_screenshot` → take a screenshot (regions: "full", "chart", "strategy_tester")

### "TradingView isn't running"
- `tv_launch` → auto-detect and launch TradingView with CDP on Mac/Win/Linux
- `tv_health_check` → verify connection is working

## Context Management Rules

These tools can return large payloads. Follow these rules to avoid context bloat:

1. **Always use `summary: true` on `data_get_ohlcv`** unless you specifically need individual bars
2. **Always use `study_filter`** on pine tools when you know which indicator you want — don't scan all studies unnecessarily
3. **Never use `verbose: true`** on pine tools unless the user specifically asks for raw drawing data with IDs/colors
4. **Avoid calling `pine_get_source`** on complex scripts — it can return 200KB+. Only read if you need to edit the code.
5. **Avoid calling `data_get_indicator`** on protected/encrypted indicators — their inputs are encoded blobs. Use `data_get_study_values` instead for current values.
6. **Use `capture_screenshot`** for visual context instead of pulling large datasets — a screenshot is ~300KB but gives you the full visual picture
7. **Call `chart_get_state` once** at the start to get entity IDs, then reference them — don't re-call repeatedly
8. **Cap your OHLCV requests** — `count: 20` for quick analysis, `count: 100` for deeper work, `count: 500` only when specifically needed

### Output Size Estimates (compact mode)
| Tool | Typical Output |
|------|---------------|
| `quote_get` | ~200 bytes |
| `data_get_study_values` | ~500 bytes (all indicators) |
| `data_get_pine_lines` | ~1-3 KB per study (deduplicated levels) |
| `data_get_pine_labels` | ~2-5 KB per study (capped at 50) |
| `data_get_pine_tables` | ~1-4 KB per study (formatted rows) |
| `data_get_pine_boxes` | ~1-2 KB per study (deduplicated zones) |
| `data_get_ohlcv` (summary) | ~500 bytes |
| `data_get_ohlcv` (100 bars) | ~8 KB |
| `capture_screenshot` | ~300 bytes (returns file path, not image data) |

## Tool Conventions

- All tools return `{ success: true/false, ... }`
- Entity IDs (from `chart_get_state`) are session-specific — don't cache across sessions
- Pine indicators must be **visible** on chart for pine graphics tools to read their data
- `chart_manage_indicator` requires **full indicator names**: "Relative Strength Index" not "RSI", "Moving Average Exponential" not "EMA", "Bollinger Bands" not "BB"
- Screenshots save to `screenshots/` directory with timestamps
- OHLCV capped at 500 bars, trades at 20 per request
- Pine labels capped at 50 per study by default (pass `max_labels` to override)

## Architecture

```
Codex CLI ←→ MCP Server (stdio) ←→ CDP (localhost:9222) ←→ TradingView Desktop (Electron)
```

Pine graphics path: `study._graphics._primitivesCollection.dwglines.get('lines').get(false)._primitivesDataById`

---

# Wiki Maintenance Protocol

> Este repositório implementa o padrão LLM Wiki (Karpathy) com **brain ativo**.
> O LLM lê o brain ANTES de analisar e escreve nele DEPOIS de cada interação.
> O humano raramente edita. O cérebro cresce sozinho.

## Estrutura da Wiki
- `wiki/` — wiki compilada em markdown
- `wiki/brain/` — **cérebro ativo** (insights, erros, previsões, padrões, indicadores)
- `wiki/brain/_templates/` — templates iniciais dos brain files (comitados no git)
- `raw/` — dados brutos imutáveis (screenshots, OHLCV, pine exports)
- `wiki/index.md` — índice mestre (gitignored — criado a partir de `index.initial.md`)
- `wiki/log.md` — append-only log (gitignored — criado a partir de `log.initial.md`)

> **IMPORTANTE:** Os brain files (`wiki/brain/*.md`) são gitignored — dados pessoais.
> Se um brain file não existir, criar cópia de `wiki/brain/_templates/{nome}.md`.
> O `setup.sh` faz isso automaticamente. Se rodando sem setup, criar manualmente.

## Brain — O Cérebro da Aplicação

O diretório `wiki/brain/` é o núcleo de autoaprendizado:

| Arquivo | Propósito | Quando ler | Quando escrever |
|---------|-----------|------------|-----------------|
| `brain/insights.md` | Insights acumulados de todas as análises | ANTES de cada análise | DEPOIS de cada análise |
| `brain/mistakes.md` | Erros cometidos e lições aprendidas | ANTES de cada análise | Quando feedback confirma erro |
| `brain/predictions-log.md` | Previsões com outcomes (aberta/acertou/errou) | Ao analisar ativo com previsão aberta | Quando análise gera bias definido |
| `brain/indicators.md` | Aprendizados sobre cada indicador | ANTES de analisar indicadores | Quando indicador surpreende (acerta/falha) |
| `brain/patterns.md` | Padrões comportamentais recorrentes | ANTES de cada análise | Quando padrão se repete pela 2ª+ vez |

---

## REGRA ZERO — Ciclo Automático de Aprendizado

**TODA interação com chart/análise segue este ciclo. Não é opcional.**

### ANTES de analisar (READ):
1. Ler `wiki/brain/insights.md` — aplicar top insights à análise atual
2. Ler `wiki/brain/mistakes.md` (últimos 10) — evitar repetir erros
3. Ler `wiki/assets/{SYMBOL}.md` — contexto histórico do ativo
4. Ler `wiki/brain/predictions-log.md` — verificar se há previsão aberta para o ativo
5. Se previsão aberta existe → comparar previsão com estado atual → fechar como ✅/❌

### DEPOIS de analisar (WRITE):
1. **Sempre** — Extrair insight da análise → append em `brain/insights.md`
2. **Se bias definido** — Registrar previsão em `brain/predictions-log.md`
3. **Se indicador surpreendeu** — Atualizar `brain/indicators.md`
4. **Se padrão visto antes** — Atualizar `brain/patterns.md`
5. **Se erro identificado** (via feedback) — Append em `brain/mistakes.md`
6. **Sempre** — Append em `wiki/log.md`

### Formato de Insight (brain/insights.md)
```markdown
### [YYYY-MM-DD] {título curto}
_{descrição em 1-2 linhas}_
- **Ativo:** {SYMBOL} | **TF:** {timeframe}
- **Confiança:** alta | média | baixa
- **Baseado em:** {indicadores/padrões usados}
```

### Formato de Previsão (brain/predictions-log.md)
```markdown
### [YYYY-MM-DD HH:MM] SYMBOL TF — BIAS
- **Preço na previsão:** $XX,XXX
- **Alvo:** $XX,XXX
- **Invalidação:** $XX,XXX
- **Confiança:** alta | média | baixa
- **Indicadores base:** [lista]
- **Status:** ⏳ aberta
```

### Formato de Erro (brain/mistakes.md)
```markdown
### [YYYY-MM-DD] {categoria}: {título}
- **O que aconteceu:** _{descrição}_
- **Por que errou:** _{causa raiz}_
- **Lição:** _{o que fazer diferente}_
- **Sessão:** [[YYYY-MM-DD-SYMBOL-TF]]
```

Categorias de erro: `falso-sinal` | `bias-errado` | `timing` | `indicador` | `htf-ignorado` | `overtrading` | `sl-apertado`

---

## Operações Disponíveis

### 1. INGEST — Análise de gráfico com registro
Trigger: "Analyze the current graph and record it on the wiki" ou qualquer pedido de análise de chart

Workflow:
1. **[BRAIN READ]** Executar ciclo READ (insights, mistakes, asset, predictions)
2. Chamar: `chart_get_state` → `data_get_study_values` → `quote_get` → `data_get_pine_lines` → `data_get_pine_labels` → `capture_screenshot`
3. Analisar com contexto do brain (aplicar insights, evitar erros passados)
4. Criar `wiki/sessions/YYYY-MM-DD-SYMBOL-TF.md` usando o template
5. Atualizar `wiki/assets/{SYMBOL}.md` com novos dados
6. Se setup identificado → criar/atualizar `wiki/setups/{nome}.md`
7. Atualizar `wiki/index.md` (contadores e links)
8. **[BRAIN WRITE]** Executar ciclo WRITE (insight, prediction, indicators)
9. Append em `wiki/log.md`: `## [YYYY-MM-DD HH:MM] ingest | {SYMBOL} {TF}`

### 2. QUERY — Perguntas contra a wiki
Trigger: "Baseado na wiki, [pergunta]" ou qualquer pergunta sobre mercado/estratégia

Workflow:
1. **[BRAIN READ]** Ler brain relevante ao tema da pergunta
2. Ler `wiki/index.md` para mapear páginas relevantes
3. Ler páginas relevantes
4. Sintetizar resposta com contexto do brain
5. Se resposta gerou novo insight → append em `brain/insights.md`
6. Se resposta é valiosa → arquivar em `wiki/analysis/YYYY-MM-DD-{slug}.md`
7. Append em `wiki/log.md`: `## [YYYY-MM-DD] query | {resumo da pergunta}`

### 3. FEEDBACK — Fechar loop de aprendizado
Trigger: "Como foi minha previsão?" ou "O mercado confirmou?" ou ao analisar ativo com previsão aberta

Workflow:
1. Ler `wiki/brain/predictions-log.md` → buscar previsões abertas (⏳)
2. Comparar previsão com estado atual do mercado
3. Marcar como ✅ acertou | ❌ errou | ⚪ expirou
4. Se ❌ errou:
   - Identificar causa raiz
   - Append em `brain/mistakes.md` com categoria e lição
   - Atualizar `brain/indicators.md` se indicador falhou
5. Se ✅ acertou:
   - Reforçar insight em `brain/insights.md`
   - Atualizar confiabilidade em `brain/indicators.md`
6. Atualizar `brain/patterns.md` se padrão se confirmou/negou
7. Append em `wiki/log.md`: `## [YYYY-MM-DD] feedback | {SYMBOL} {resultado}`

### 4. LINT — Health-check periódico
Trigger: "Faça o lint da wiki" ou "Health-check da wiki"

Workflow:
1. Ler `wiki/index.md` completo
2. Usar a tool `wiki_search` para cruzar conceitos soltos e sugerir novas páginas em `wiki/research/`
3. Cruzar `wiki/setups/` com `wiki/sessions/` para atualizar estatísticas
4. **Verificar previsões expiradas** em `brain/predictions-log.md` (> 48h abertas)
5. **Ranquear insights** em `brain/insights.md` (mover mais validados para cima)
6. Identificar conceitos mencionados em `raw/clippings/` mas sem página `wiki/concepts/` própria
7. **Regenerar `wiki/library.md`** — garantir que todos os clippings estejam linkados no Graph View
8. Criar `wiki/lint/YYYY-MM-DD.md` com relatório
9. Append em `wiki/log.md`: `## [YYYY-MM-DD] lint | {N} issues encontrados`

### 5. UPDATE STRATEGY — Revisão de estratégia
Trigger: "Atualize a estratégia com base nos resultados recentes"

Workflow:
1. Ler `wiki/strategies/` + `wiki/setups/index.md` + últimas 10 sessões
2. Ler `brain/mistakes.md` + `brain/indicators.md` (aprendizados)
3. Calcular win rate, R:R médio, drawdown
4. Propor ajustes **baseados nos erros e padrões identificados pelo brain**
5. Atualizar `wiki/strategies/conservative-trend-follower-v2.md`
6. Append no log

### 6. COMPILE — Ingestão de clippings e artigos
Trigger: "Compile os clippings recentes na wiki"

Workflow:
1. Ler arquivos `.md` novos em `raw/clippings/` e `raw/papers/`
2. Extrair conceitos chave, dados, e insights
3. Atualizar `wiki/concepts/` ou criar arquivos em `wiki/research/`
4. Inserir backlinks bidirecionais
5. Atualizar `wiki/index.md` e `wiki/search-index.md`
6. **Regenerar `wiki/library.md`** — listar TODOS os `.md` de `raw/clippings/` como wikilinks `[[nome]]` (garante Graph View conectado)
7. Append em `wiki/log.md`: `## [YYYY-MM-DD] compile | {N} artigos processados`

### 7. REVIEW / VISUALIZE — Outputs visuais no Obsidian
Trigger: "Gere a revisão semanal" ou "Visualize os resultados"

Workflow:
1. Analisar as sessões do período solicitado (ex: últimos 7 dias)
2. Extrair métricas (win rate, total profit, drawdown, key insights)
3. Executar o script Python `scripts/tools/plot_accuracy.py` para gerar o gráfico na pasta `wiki/outputs/charts/`
4. Criar uma apresentação usando formato Marp (`wiki/outputs/YYYY-MM-DD-review.md`)
5. Append em `wiki/log.md`

### 8. SEARCH — Pesquisa indexada
Trigger: "Ache na wiki..." para consultas que superem o limite de leitura direta

Workflow:
1. Executar no sistema a tool nativa do MCP conectada: `wiki_search` passando a `query` desejada.
2. Analisar o ranqueamento retornado e ler trechos (snippets) para orientar decisões avançadas.
3. Sintetizar os resultados com backlinks

---

## Prioridade de Contexto (o que ler primeiro)

Quando o contexto é limitado, carregar nesta ordem:

1. `wiki/brain/insights.md` — SEMPRE (resumo compacto do que já sabe)
2. `wiki/brain/mistakes.md` — SEMPRE (últimos 10, evitar repetir)
3. `wiki/assets/{SYMBOL}.md` — quando analisando um ativo específico
4. `wiki/brain/predictions-log.md` — quando analisando ativo com previsão aberta
5. `wiki/brain/indicators.md` — quando interpretando indicadores
6. `wiki/brain/patterns.md` — quando buscando recorrências
7. `wiki/strategies/` — quando avaliando entrada
8. `wiki/concepts/` — quando conceito específico é relevante

## Convenções de Backlinks
- Use `[[nome-do-arquivo]]` (sem extensão, sem path)
- Toda página nova deve ter seção `## Backlinks`
- Ao atualizar uma página, verificar e adicionar backlinks bidirecionais

## Convenções de Nomenclatura
- Sessões: `YYYY-MM-DD-SYMBOL-TF.md` (ex: `2026-04-19-BTCUSD-4H.md`)
- Setups: `kebab-case` descritivo (ex: `fvg-pullback-bull-ob.md`)
- Analysis: `YYYY-MM-DD-slug.md`
- Lint: `YYYY-MM-DD.md`

## Regras Críticas
1. NUNCA modificar arquivos em `raw/` — são imutáveis
2. SEMPRE executar ciclo READ antes de qualquer análise
3. SEMPRE executar ciclo WRITE depois de qualquer análise
4. SEMPRE atualizar `wiki/log.md` após qualquer operação
5. SEMPRE atualizar `wiki/index.md` quando criar nova página
6. Screenshots vão em `raw/screenshots/` antes de referenciar na wiki
7. Dados OHLCV exportados vão em `raw/ohlcv/`
8. Previsões abertas > 48h devem ser marcadas como ⚪ expiradas no próximo LINT
