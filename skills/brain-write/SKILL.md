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
2. **Bias definido →** previsão em `wiki/brain/predictions-log.md` (Status `⏳ aberta`).
3. **Indicador surpreendeu →** atualizar `wiki/brain/indicators.md` (campos Sessões/Acertos/Falhas + Hit Rate).
4. **Padrão repetido (2ª+ vez) →** atualizar `wiki/brain/patterns.md`; promover Status quando
   atingir threshold: OBSERVAÇÃO →(2)→ VALIDADO →(3)→ CONSOLIDADO.
5. **Erro confirmado →** append em `wiki/brain/mistakes.md` (categoria + lição + **Prevenção**).
6. **Previsões > 48h sem update →** marcar `⚪ expirada` em `predictions-log.md`.

## Arquivo de sessão (operação INGEST)
Criar `wiki/sessions/YYYY-MM-DD-SYMBOL-TF.md` usando o template, com TODAS as seções obrigatórias:
- **Brain Read Summary** (erros prevenidos, insights ativados, padrões monitorados)
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
