---
name: brain-write
description: Ciclo WRITE obrigatório do AUTO-PILOT depois de QUALQUER análise — grava insight, previsão (se bias definido), atualiza indicators/patterns, cria/atualiza o arquivo de sessão e faz append no log. Use ao final de toda análise para fechar o loop de auto-aprendizado. Usa os templates de wiki/brain/_templates/.
---

# Brain WRITE — Pós-análise obrigatório

> Fecha o loop de auto-aprendizado. Formatos: usar templates em `wiki/brain/_templates/`.
> Categorias de erro: `falso-sinal | bias-errado | timing | indicador | htf-ignorado | overtrading | sl-apertado | psicologico`.

## Sempre
1. **Insight →** append em `wiki/brain/insights.md` + atualizar `wiki/brain/insights-hot.md`
   (manter Top 5–8; remover o mais antigo) + append `wiki/log.md`
   (`## [YYYY-MM-DD HH:MM] {op} | {SYMBOL} {TF}`).

## Condicional
2. **Bias definido →** criar **nota atômica** de previsão em
   `wiki/brain/predictions/YYYY-MM-DD-HHMM-SYMBOL-TF.md` a partir de
   `wiki/brain/_templates/prediction-note.md` (`status: open`). **O frontmatter YAML é a fonte
   única** (lido por Dataview/Bases e por `metrics_engine.py`) — preencher `criteria:` com os slugs
   de `skills/_references/criteria-keys.md` (os MESMOS que pontuaram no Confluence Score / Fase 9;
   sinal `-` entre aspas: `"-stochrsi"`). NÃO reescrever campos como prosa `- **Campo:**`.
   - `predictions-log.md` está **congelado** (histórico cold, ainda somado pelo `metrics_engine.py`);
     não fazer mais append nele.
   - **Graduar-antes-de-supersedir (regra dura):** se esta previsão substitui uma anterior do mesmo
     ativo, a anterior **já deve ter sido graduada** pelo gate 2c do `brain-read` (`status: win/loss/
     expired`) ANTES de marcar a antiga com `superseded: true`. NUNCA setar `superseded` sobre uma
     `open` ainda não graduada — **supersedir ≠ resolver**; toda previsão sai de `open` por grading
     objetivo (TP vs SL), não por substituição. Era esse vazamento que deixava `criteria_stats` em N=0.
3. **Indicador surpreendeu →** registrar a observação qualitativa em `wiki/brain/indicators.md`
   ("Confiabilidade observada" / "Falhas comuns"). Os campos numéricos (Sessões/Acertos/Falhas/Hit Rate)
   são reescritos por `metrics_engine.py` a partir dos `Critérios:` — **não editar à mão**.
4. **Padrão repetido (2ª+ vez) →** atualizar `wiki/brain/patterns.md`; promover Status quando
   atingir threshold: OBSERVAÇÃO →(2)→ VALIDADO →(3)→ CONSOLIDADO.
5. **Erro confirmado →** append em `wiki/brain/mistakes.md` (categoria + lição + **Prevenção**).
6. **Previsões pendentes (supersedidas/vencidas) →** NÃO marcar `⚪` à mão por idade. O gate 2c do
   `brain-read` (via `check_predictions.py` + `prediction-feedback`) gradua pela regra objetiva
   (TP/SL com OHLCV) e roda o `metrics_engine.py`. Aqui só confirmar que o worklist foi zerado.

## Arquivo de sessão (operação INGEST)
Criar `wiki/sessions/YYYY-MM-DD-SYMBOL-TF.md` usando o template. **Preencher o frontmatter YAML no
topo** (symbol/tf/date/class/layout/bias/price/confluence/regime/setup/result/tags) — é o que
alimenta o `wiki/dashboard.md`, os `.base` e o Graph. Depois, TODAS as seções obrigatórias:
- **Brain Read Summary** (erros prevenidos, insights ativados, padrões monitorados)
- **Alertas disparados hoje** (Dados Capturados) — copiar os alertas lidos no `brain-read` (item 2d):
  `SYMBOL cond @nível (TF) → confirma/avisa`, ou `— nenhum` / `alertas-parciais` (TV offline)
- **Contexto Macro** (se BTC/ETH/Altcoin)
- **Setups Identificados** (mesmo que "Nenhum setup reconhecido")
- **Plano de Operação** (entrada/stop/TP/R:R)
- **Comparação com Sessão Anterior**
- **Resultado** inicializado com `⏳ aberta`
- **Aprendizados desta Sessão**

## Setup Match Check
- Conferir `wiki/setups/index.md` → corresponde a setup existente? Sim → linkar + atualizar
  "Histórico de Ocorrências". Não, mas 2+ sessões anteriores → criar `wiki/setups/{nome}.md`.
  Primeira ocorrência → registrar como "candidato" no index sem criar arquivo.
- Se setup criado/atualizado → recalcular "Estatísticas" (Total/Win/Loss/Win Rate/R:R) + atualizar ranking no index.

> Métricas numéricas de performance pessoal vão SOMENTE em `brain/metrics.md` + `setups/index.md`
> (gitignored). NÃO escrever números em `wiki/strategies/*.md` (públicos).
