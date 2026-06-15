---
name: prediction-feedback
description: Fecha o loop de aprendizado avaliando previsões abertas — grading objetivo por regra (TP antes do SL = acertou / SL antes do TP = errou / nenhum no prazo = expirou). Use quando o usuário pergunta "como foi minha previsão?", "o mercado confirmou?", ou ao analisar um ativo com previsão ⏳ aberta. Atualiza a sessão original, setups, indicators, mistakes e metrics.
---

# FEEDBACK — Fechar previsões + métricas

1. Ler `wiki/brain/predictions-log.md` → buscar previsões abertas (⏳) do símbolo (grep, não o arquivo todo).
2. **Grading objetivo (regra, não opinião):** com `data_get_ohlcv` buscar o range real desde a data
   da previsão e comparar com `Entrada/SL/TPs`.
3. Marcar pela regra: **TP antes do SL = ✅ | SL antes do TP = ❌ | nenhum no prazo = ⚪**. Se ⚪,
   preencher `Pós-fecho:` pela direção na expiração (a favor=certa / contra=errada / neutra).
4. **Atualizar a sessão original** (`wiki/sessions/`): seção "Resultado" (outcome, entrada/saída
   real, R:R, P&L, tempo) + "Setup utilizado" (link).
5. **Se setup usado no trade:** atualizar "Histórico de Ocorrências" + recalcular "Estatísticas" +
   atualizar `wiki/setups/index.md`.
6. **Se ❌ errou:** causa raiz → append `brain/mistakes.md` (categoria + lição + **Prevenção**) +
   `brain/indicators.md` (incrementar Falhas + recalcular Hit Rate do indicador que falhou).
7. **Se ✅ acertou:** reforçar insight em `brain/insights.md` + `brain/indicators.md` (Acertos + Hit Rate).
8. Atualizar `brain/patterns.md` se padrão confirmou/negou → promover Status se atingiu threshold.
9. Preencher "Aprendizados desta Sessão" se ainda vazio.
10. Append `wiki/log.md`: `## [YYYY-MM-DD] feedback | {SYMBOL} {resultado}`.
