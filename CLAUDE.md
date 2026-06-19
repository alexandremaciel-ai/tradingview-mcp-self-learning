# TradingView MCP — Claude Instructions

79 tools para ler e controlar um chart TradingView Desktop ao vivo via CDP (port 9222).

```
Claude Code ←→ MCP Server (stdio) ←→ CDP (localhost:9222) ←→ TradingView Desktop (Electron)
```

> **Arquitetura skill-first:** a lógica detalhada (AUTO-PILOT, macro, Fases 1-9, operações da wiki)
> vive em **skills carregadas sob demanda** (`skills/<nome>/SKILL.md`). Este arquivo é o **router**:
> invariantes + tabela de dispatch + cheatsheet. Carregue a skill certa e siga-a — não reimplemente.

---

## ⚡ AUTO-PILOT — Invariantes (valem em TODA interação)

1. **Antes de qualquer análise →** invocar a skill **`brain-read`** (conexão TV, feeds, layout
   ativo, classe do pedido, leitura do brain por relevância, prevenções/insights, fechar previsões).
2. **Depois de qualquer análise →** invocar a skill **`brain-write`** (insight, previsão, sessão, log).
3. Estas duas pontas são **obrigatórias** mesmo num pedido "rápido". O dispatcher `analyze` já as chama.
4. Feeds (cripto): `raw/feeds/latest.md` `indisponível` ou > 2h → `python3 scripts/tools/fetch_feeds.py`.
5. **Gate matinal (briefing):** `brain-read` (passo 2b) roda `python3 scripts/tools/check_briefing.py`
   → 1ª análise do dia sem `wiki/briefings/{hoje}.md` invoca **`btc-macro-briefing`** (que persiste o
   arquivo); toda análise do dia consome o Veredito (`macro-scan` Step 0.5). Refresh só por evento 🔴.
6. Circuit breaker 🔴 em `brain/metrics.md` (3 losses seguidos / DD 5% dia) → rebaixar p/ observação/paper.

---

## 🧭 Tabela de Dispatch — pedido → skill

| Pedido do usuário | Skill |
|---|---|
| "analise BTC/ETH/SOL/AAPL…", bias, setup de **um** ativo (default) | **`analyze`** |
| "scan multi-layout", "varredura de todos os layouts", análise consolidada | **`multi-layout-scan`** |
| "scan da lista", "watchlist", comparar vários ativos | **`multi-symbol-scan`** |
| "daily", "morning scan", resumo de abertura | **`daily-scan`** |
| "briefing macro", "agenda da semana", "calendário econômico", "o que pode afetar o BTC" (via web) | **`btc-macro-briefing`** |
| "ciclo", "topo/fundo", "onde estamos no ciclo" | **`btc-cycle`** |
| "como foi minha previsão?", "o mercado confirmou?", fechar previsão | **`prediction-feedback`** |
| "lint", "health-check", "atualize a estratégia", "compile clippings", "revisão semanal", "ache na wiki" | **`wiki-maintenance`** |
| "recalibrar layouts", mudou indicadores no TV | **`recalibrate-layouts`** |
| construir indicador/estratégia Pine | **`pine-develop`** |
| praticar em replay / backtest manual | **`replay-practice`** |
| relatório de performance de backtest | **`strategy-report`** |

**Camadas reutilizáveis** (o `analyze` e os scans as encadeiam; invocáveis isoladamente):
`brain-read` · `macro-scan` · `technical-checklist` · `brain-write` ·
`btc-macro-briefing` (disparada pelo **gate matinal** do `brain-read` passo 2b — web-search, não lê chart; o `macro-scan` Step 0.5 consome o Veredito que ela persiste).

**Referências** (markdown carregado por path quando uma skill cita):
`skills/_references/class-rules.md` · `confluence-score.md` · `tv-tools.md` · `criteria-keys.md`.

**Doutrina de leitura (lente ativa em TODA análise):** `wiki/concepts/institutional-flow-poi.md` —
os 4 Pilares (Estrutura/Ciclos/Volume/Macro), POIs, acumulação cíclica e gatilhos de reversão (CHoCH,
sobrevenda Diário/Semanal, perda de LTA). Aplicada pelo `technical-checklist`; ações de exposição
sempre ancoradas à disciplina (`position-sizing`/circuit breaker).

---

## 🔧 Tool cheatsheet (detalhe em `skills/_references/tv-tools.md`)

- Ler chart: `chart_get_state` (1× no início) → `data_get_study_values` → `quote_get`.
- `data_get_ohlcv` **sempre** `summary: true` (cap `count`: 20 rápida / 100 profunda / 500 máx).
- Pine drawings (indicador visível): `data_get_pine_lines/_labels/_tables/_boxes` com `study_filter`.
- ⚠️ `quote_get(symbol=…)` **ignora** o parâmetro → no macro **DEVE** `chart_set_symbol` por ticker.
- Trocar layout: `ui_evaluate` navegando `/chart/{slug}/` (`layout_switch` não recarrega o Desktop);
  navegar **reseta o símbolo** → re-setar `chart_set_symbol` depois.
- `chart_manage_indicator` exige nome completo ("Relative Strength Index", não "RSI").

---

## 📚 Wiki + Brain

> Padrão LLM Wiki com **brain ativo**: o LLM lê o brain ANTES e escreve DEPOIS de cada interação.

- `wiki/` compilada · `wiki/brain/` cérebro ativo (gitignored — dados pessoais) ·
  `wiki/brain/_templates/` (comitado) · `raw/` dados brutos **imutáveis** · `wiki/log.md` append-only.
- Brain file inexistente → copiar de `wiki/brain/_templates/{nome}.md`. Locais ausentes → criar do
  seed `.initial.md` (`index.md`, `log.md`, `setups/index.md`, `watchlist.md`, `library.md`).
- Recall otimizado: `brain-read` lê `insights-hot.md` (Top 8) + busca por relevância; **não** despeja
  `insights.md`/`predictions-log.md` inteiros.

---

## ⛔ Regras Críticas

1. NUNCA modificar arquivos em `raw/` — imutáveis.
2. SEMPRE `brain-read` antes e `brain-write` depois de qualquer análise.
3. SEMPRE atualizar `wiki/log.md` após qualquer operação.
4. SEMPRE atualizar `wiki/index.md` ao criar nova página.
5. SEMPRE preencher "Setups Identificados" e "Resultado" (`⏳ aberta`) em cada sessão.
6. SEMPRE atualizar `wiki/setups/index.md` + recalcular Estatísticas após criar/fechar setup.
7. Screenshots → `raw/screenshots/`; OHLCV exportado → `raw/ohlcv/`.
8. Previsões abertas > 48h → `⚪ expirada` no próximo LINT.
9. Cripto contradiz macro → rótulo `contra-macro` (−2). Fim de semana → `macro-parcial (dados sex)`.

## Convenções
- Backlinks `[[nome-do-arquivo]]` (sem extensão/path); toda página nova com `## Backlinks` bidirecionais.
- Nomes: sessões `YYYY-MM-DD-SYMBOL-TF.md` · setups `kebab-case` · analysis `YYYY-MM-DD-slug.md` · lint `YYYY-MM-DD.md`.

---

> **Espelhamento:** este arquivo é a fonte. `GEMINI.md` e `AGENTS.md` são gerados por
> `python3 scripts/tools/sync_agent_md.py` (idênticos exceto título + "invoque a skill X" → "leia
> skills/X/SKILL.md"). Editou o CLAUDE.md → rode o script.
