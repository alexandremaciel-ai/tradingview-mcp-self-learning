# Wiki Log

> Append-only. Cada entrada: `## [YYYY-MM-DD] tipo | descrição`
> Tipos: `ingest` | `analyze` | `lint` | `query` | `update`

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
