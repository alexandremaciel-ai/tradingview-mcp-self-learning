---
name: analyze
description: Análise técnica completa de um ativo (operação INGEST) — orquestra o pipeline AUTO-PILOT inteiro: classifica o pedido, roda brain-read → macro-scan → technical-checklist → bias com Confluence Score → brain-write + arquivo de sessão. Use como DEFAULT sempre que o usuário pede para analisar um ativo (BTC, ETH, SOL, AAPL…), pedir bias/setup, ou "analise X". Para varredura de todos os layouts use multi-layout-scan; para vários ativos use multi-symbol-scan.
---

# Analyze — Pipeline de análise (INGEST)

> Orquestra as camadas reutilizáveis. Cada uma é uma skill própria — invoque-as em ordem.
> Não reimplemente a lógica delas aqui; carregue-as sob demanda.

## Pipeline

1. **`brain-read`** — conexão, feeds, layout ativo, classe do pedido, leitura do brain por
   relevância, prevenções/insights/padrões, fechar previsões abertas. → Brain Read Summary.
2. **`macro-scan`** — Step 0 (contexto/horário) + Workflow da classe (A/B/C/D) + Regras de Leitura
   Macro. Declarar regime (Risk-On/Off/Misto). Classes e fallbacks em
   `skills/_references/class-rules.md` + `skills/_references/tv-tools.md`.
3. **`technical-checklist`** — Fases 1-9 (MTF, SMC, Wyckoff, Fib, Indicadores dirigidos pelo layout,
   Playbook, Liquidez/USDT.D/Longs-Shorts, Bias). Pular framework = PROIBIDO (N/A justificado).
4. **Bias final** — Confluence Score (0–10) + confiança derivada + score→ação, conforme
   `skills/_references/confluence-score.md`.
5. **`brain-write`** — insight + previsão (se bias) + indicators/patterns + arquivo de sessão
   `wiki/sessions/YYYY-MM-DD-SYMBOL-TF.md` + append `wiki/log.md` (`ingest | {SYMBOL} {TF}`).

## Saída
Análise consolidada com header temporal, contexto macro, MTF, indicadores do layout, liquidez/
posicionamento, bias + score + confiança, e o plano de operação (entrada/stop/TP/R:R). Adaptar o
formato à classe (ver `class-rules.md`).

## Atalhos de classe
- WATCHLIST → use `multi-symbol-scan`. DAILY → use `daily-scan`. CYCLE → use `btc-cycle`.
- "varredura de todos os layouts" / "scan multi-layout" → use `multi-layout-scan`.
