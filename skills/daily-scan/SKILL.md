---
name: daily-scan
description: Dashboard diário / morning scan — macro completo 1×, BTC rápido (D+4H), watchlist e fechamento de previsões expiradas. Use quando o usuário pede "daily", "morning scan", "resumo do dia" ou um panorama compacto de abertura.
---

# DAILY — Dashboard de abertura

Classe `DAILY` (ver `skills/_references/class-rules.md`).

1. **`brain-read`** — incluir fechamento de previsões expiradas (>48h → ⚪).
2. **`macro-scan`** — Workflow A completo **1×** (Risk-On/Off/Misto).
3. **BTC rápido** — D + 4H (citar o M no contexto de ciclo). Fases-chave do `technical-checklist`.
4. **Watchlist** — varredura compacta (ou chamar `multi-symbol-scan`).
5. **Previsões** — listar abertas + expiradas fechadas.
6. **`brain-write`** — insight + append `wiki/log.md`.

## Output — dashboard compacto
`Macro: Risk-On/Off/Misto | BTC: [bias] | Alertas: [N] | Previsões abertas: [N]`
