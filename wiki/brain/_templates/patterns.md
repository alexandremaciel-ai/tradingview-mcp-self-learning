# Brain — Padrões Recorrentes

> Padrões que o LLM identifica ao cruzar múltiplas sessões.
> Diferente de setups (que são regras de entrada), padrões são observações comportamentais.

## Sistema de Confiança
- **OBSERVAÇÃO** — 1 confirmação (baixa confiança, ainda não replicado)
- **VALIDADO** — 2–3 confirmações (média confiança, aplicar com cautela)
- **CONSOLIDADO** — 4+ confirmações (alta confiança, aplicar ativamente)

Ao atingir 2, 3 ou 4 confirmações → promover o Status automaticamente.

## Formato

```markdown
### {Nome do Padrão}
- **Status:** OBSERVAÇÃO | VALIDADO | CONSOLIDADO
  _(OBSERVAÇÃO = 1 conf | VALIDADO = 2–3 conf | CONSOLIDADO = 4+ conf)_
- **Observado:** N vezes
- **Última confirmação:** YYYY-MM-DD
- **Contexto:** _(quando aparece)_
- **O que acontece depois:** _(resultado típico)_
- **Falhou em:** _(sessões onde não se confirmou — ou "nenhuma falha registrada")_
- **Confiança:** alta | média | baixa
- **Sessões de referência:** [links]
```

---

## Padrões Identificados

_(serão adicionados automaticamente após análises que revelem padrões recorrentes)_
