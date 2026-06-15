---
name: wiki-maintenance
description: Manutenção e operações da wiki — LINT (health-check), UPDATE STRATEGY (revisão com métricas), COMPILE (ingestão de clippings), REVIEW/VISUALIZE (gráficos + apresentação), SEARCH (pesquisa indexada). Use quando o usuário pede "faça o lint da wiki", "health-check", "atualize a estratégia", "compile os clippings", "gere a revisão semanal", "ache na wiki…". Roda os scripts de scripts/tools/.
---

# Wiki Maintenance — Operações periódicas

## LINT — Health-check (trigger: "lint da wiki" / "health-check")
1. Ler `wiki/index.md`. 2. `wiki_search` p/ cruzar conceitos soltos → sugerir páginas em
`wiki/research/`. 3. Cruzar `wiki/setups/` com `wiki/sessions/` p/ atualizar estatísticas.
4. Verificar previsões expiradas (>48h) em `brain/predictions-log.md`. 5. Rodar
`python scripts/tools/archive_brain.py` (Top N insights → `insights-archive/YYYY-MM.md`).
6. Conceitos em `raw/clippings/` sem página própria. 7. Regenerar `wiki/library.md` (Graph View).
8. Rodar `python scripts/tools/wiki_lint.py` (gera `wiki/lint/YYYY-MM-DD.md` + contadores do index).
9. Rodar `python scripts/tools/metrics_engine.py` (recalcula `brain/metrics.md` + `setups/index.md`).
10. Append `wiki/log.md`: `## [YYYY-MM-DD] lint | {N} issues`.

## UPDATE STRATEGY — Revisão com métricas (trigger: "atualize a estratégia")
1. `wiki/setups/index.md` ranking. 2. Sessões com Resultado (✅/❌/⚪). 3. Métricas globais (win rate,
R:R, drawdown, Sharpe simplificado). 4. Ler `brain/mistakes.md` + `indicators.md`. 5. `brain/patterns.md`.
6. Propor ajustes com evidência: setups <40% candidato a remoção; >60% aumento de posição;
indicadores que falham → reduzir peso; padrões validados → virar filtro. 7. Números reais SOMENTE em
`brain/metrics.md` + `setups/index.md` (NÃO em `wiki/strategies/*.md` públicos — manter placeholder
qualitativo apontando `[[metrics]]`). 8. Atualizar "Métricas Globais" no index. 9. Incrementar data
de "Última revisão". 10. Append `wiki/log.md`: `update-strategy | {ajustes}`.

## COMPILE — Clippings (trigger: "compile os clippings")
1. `.md` novos em `raw/clippings/` e `raw/papers/`. 2. Extrair conceitos/dados/insights. 3. Atualizar
`wiki/concepts/` ou criar em `wiki/research/`. 4. Backlinks bidirecionais. 5. Atualizar `index.md` +
`search-index.md`. 6. Regenerar `wiki/library.md`. 7. Append `wiki/log.md`: `compile | {N} artigos`.

## REVIEW / VISUALIZE (trigger: "revisão semanal" / "visualize os resultados")
1. Sessões do período. 2. Extrair métricas. 3. `scripts/tools/plot_accuracy.py` +
`scripts/tools/plot_metrics.py` → `wiki/outputs/charts/`. 4. Apresentação Marp
`wiki/outputs/YYYY-MM-DD-review.md`. 5. Append `wiki/log.md`.

## SEARCH (trigger: "ache na wiki…")
1. `wiki_search` com a query. 2. Analisar ranking + ler snippets. 3. Sintetizar com backlinks.
