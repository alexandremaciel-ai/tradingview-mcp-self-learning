# Brain — Log de Previsões

> Cada análise que gera um bias (LONG/SHORT/SPOT) é registrada aqui.
> O LLM verifica previsões anteriores ao analisar o mesmo ativo.
> Os **campos parseáveis** abaixo são lidos por `scripts/tools/metrics_engine.py` — manter os nomes exatos.

## Formato (campos parseáveis obrigatórios)

```markdown
### [YYYY-MM-DD HH:MM BRT] SYMBOL TF — BIAS
- **Preço na análise:** $XX,XXX
- **Contexto:** _(1-2 linhas de macro/estrutura)_
- **Tese:** _(o racional do trade)_
- **Lado:** long | short | spot
- **Tipo:** scalp | swing | holder
- **Setup:** [[nome-do-setup]] | —
- **Playbook:** 1 | 2 | 3 | 4 | —
- **Confluence Score:** N/10        ← ver [[confluence-score]]
- **Confiança:** alta | média | baixa
- **Regime:** risk-on | risk-off | misto
- **Entrada:** $XX,XXX (zona) | **SL:** $XX,XXX | **TPs:** $A / $B / $C
- **R:R plan:** X.X
- **R:R real:** _(preenchido no feedback)_
- **Invalidação:** _(condição que mata a tese)_
- **Indicadores base:** [lista livre, leitura humana]
- **Critérios:** ema200+, macd+, rsi+, smc-ob+, macro+ | -adx   ← slugs parseáveis de [[criteria-keys]] (alimenta a calibração)
- **Status:** ⏳ aberta | ✅ acertou | ❌ errou | ⚪ expirou
- **Pós-fecho:** _(só p/ ⚪: errada | certa | neutra — direção do preço na expiração vs a tese)_
- **Resultado:** _(preenchido no feedback)_
- **Lição:** _(preenchida no feedback)_
```

### Convenções de parsing
- **Status** é detectado pelo emoji (⏳/✅/❌/⚪) — o texto após o emoji é livre.
- **Lado** ausente → inferido do header (LONG/BULLISH = long; SHORT/BEARISH = short).
- Toda previsão ❌ DEVE gerar entrada em [[mistakes]] com `Categoria` + `Prevenção`.
- Previsão ⏳ há mais de 48h sem atualização → marcar ⚪ expirou (o `wiki_lint.py` sinaliza).
- Ao marcar ⚪, preencher `Pós-fecho` (errada/certa/neutra) — `metrics_engine.py` conta as **erradas** como loss no **WR ajustado** (evita esconder perda como "expirada").
- **Critérios** usa os slugs de [[criteria-keys]] — quando a previsão fecha, cada `slug+` é creditado/debitado e o Hit Rate é reescrito em [[indicators]]. Liste todos os critérios que entraram no Confluence Score.

---

## Previsões

_(serão adicionadas automaticamente após cada análise com bias definido)_
