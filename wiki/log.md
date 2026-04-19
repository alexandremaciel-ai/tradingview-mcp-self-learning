# Wiki Log

> Append-only. Cada entrada: `## [YYYY-MM-DD] tipo | descrição`
> Tipos: `ingest` | `analyze` | `lint` | `query` | `update` | `feedback`

## Como parsear
```bash
grep "^## \[" wiki/log.md | tail -10
grep "^## \[" wiki/log.md | grep "ingest"
```

---

## [2026-04-19] init | Wiki criada a partir do padrão Karpathy
- Estrutura base gerada
- Arquivos template criados
- CLAUDE.md expandido com seção WikiMaintenance

## [2026-04-19] update | Brain system adicionado — autoaprendizado ativo
- wiki/brain/ criado com 5 arquivos (insights, mistakes, predictions-log, indicators, patterns)
- CLAUDE.md reescrito com REGRA ZERO: ciclo READ → ANALYZE → WRITE automático
- Operação FEEDBACK adicionada para fechar loop de aprendizado
- Prioridade de contexto definida para carregamento eficiente

