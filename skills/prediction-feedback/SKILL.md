---
name: prediction-feedback
description: Fecha o loop de aprendizado avaliando previsões abertas — grading objetivo por regra (TP antes do SL = acertou / SL antes do TP = errou / nenhum no prazo = expirou). Use quando o usuário pergunta "como foi minha previsão?", "o mercado confirmou?", ou ao analisar um ativo com previsão ⏳ aberta. Atualiza a sessão original, setups, indicators, mistakes e metrics.
---

# FEEDBACK — Fechar previsões + métricas

1. Localizar as previsões abertas do símbolo nas **notas atômicas**:
   `grep -l "status: open" wiki/brain/predictions/*.md | xargs grep -l "symbol: {SÍMBOLO}"`
   (histórico só se preciso: `grep "⏳" wiki/brain/predictions-log.md`). Ler o frontmatter (`entry/sl/
   tps/date/criteria`), não o arquivo inteiro.
2. **Grading objetivo (regra, não opinião):** com `data_get_ohlcv` buscar o range real desde `date`
   e comparar com `entry/sl/tps` do frontmatter.
3. Marcar pela regra **editando o frontmatter** da nota: `status: win` (TP antes do SL) | `status: loss`
   (SL antes do TP) | `status: expired` (nenhum no prazo) + preencher `rr_real:`. Se `expired`,
   preencher `postclose:` pela direção na expiração (a favor=certa / contra=errada / neutra).
   _(No monolito congelado, ainda vale a convenção de emoji `- **Status:**`.)_
4. **Atualizar a sessão original** (`wiki/sessions/`): seção "Resultado" (outcome, entrada/saída
   real, R:R, P&L, tempo) + "Setup utilizado" (link).
5. **Se setup usado no trade:** atualizar "Histórico de Ocorrências" + recalcular "Estatísticas" +
   atualizar `wiki/setups/index.md`.
6. **Se ❌ errou OU ⚪-errada (direção contra na expiração):** causa raiz → append `brain/mistakes.md`
   um stub estruturado (categoria `falso-sinal|bias-errado|timing|indicador|htf-ignorado|...` +
   **O que aconteceu** + **Por que errou** + **Lição** + **Prevenção**). Matéria-prima: reaproveitar
   os campos `Penalidades:`/`Confiança` da própria previsão (já listam o que pesou contra). Isto é o
   que mantém `mistakes.md` vivo — todo erro graduado vira aprendizado acionável, não só um ❌ no log.
7. **Se ✅ acertou:** reforçar insight em `brain/insights.md`.
8. Atualizar `brain/patterns.md` se padrão confirmou/negou → promover Status se atingiu threshold.
9. Preencher "Aprendizados desta Sessão" se ainda vazio.
10. **Recalcular calibração:** rodar `python3 scripts/tools/metrics_engine.py` — ele lê o campo
    `Critérios:` da previsão fechada e reescreve Acertos/Falhas/Hit Rate por critério em
    `brain/indicators.md` + a seção "Calibração por Critério" de `brain/metrics.md`. **Não editar os
    números de `indicators.md` à mão** (o Hit Rate é derivado dos `Critérios:`, não digitado).
11. Append `wiki/log.md`: `## [YYYY-MM-DD] feedback | {SYMBOL} {resultado}`.
