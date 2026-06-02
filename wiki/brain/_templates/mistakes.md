# Brain — Registro de Erros e Correções

> Append-only. Cada erro vira uma lição que o LLM consulta antes de analisar.
> Formato: `### [YYYY-MM-DD] {tipo de erro}`

## Como Usar
O LLM lê os **últimos 10 erros** antes de cada análise para não repeti-los.
Para cada erro, verificar: "Este cenário pode se repetir nesta análise?" → declarar prevenção ativa.

## Categorias de Erro
- **falso-sinal** — setup identificado que não se concretizou
- **bias-errado** — direção prevista incorreta
- **timing** — análise correta mas momento errado
- **indicador** — leitura errada de indicador
- **htf-ignorado** — ignorou conflito de higher timeframe
- **overtrading** — muitas entradas sem confirmação adequada
- **sl-apertado** — stop loss muito próximo, estopado antes do movimento
- **psicologico** — revenge trade, FOMO, medo, quebra de disciplina (ver [[trading-psychology]])

---

## Formato de Entrada

```markdown
### [YYYY-MM-DD] {tipo}
- **O que aconteceu:** 
- **Por quê falhou:**
- **Lição:**
- **Prevenção:** _(check a executar antes de entrar em setup similar)_
- **Sessão:** [[link]]
```

---

## Registro de Erros

_(serão adicionados automaticamente quando feedback de mercado confirmar erro)_
