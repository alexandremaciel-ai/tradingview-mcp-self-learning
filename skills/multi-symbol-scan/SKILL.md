---
name: multi-symbol-scan
description: Scan multiple symbols for setups, patterns, or strategy performance. Use when comparing across instruments or screening for opportunities.
---

# Multi-Symbol Scanner

You are scanning multiple symbols for trading setups or comparing performance.

## Step 0: Preâmbulo (classe WATCHLIST — análise de mercado)

Se o scan for de **análise de mercado** (não só comparar backtests), rode 1× no início:
- **`brain-read`** — conexão, feeds, brain por relevância, classe `WATCHLIST`, fechar previsões.
- **`macro-scan`** — macro completo **1×** (Risk-On/Off/Misto) — vale para todos os ativos do scan.
  Inclui o **Step 1.5: a Fase de rotação de liquidez é SISTÊMICA → ler 1× só** (Migração BTC /
  Rotação ETH / Altseason / Fuga Stablecoins). Por ativo, o veredito é por **target-type**: ETH usa
  `TOTAL2ES`, altcoins usam `TOTAL3ES` — **não** re-puxar os índices por ativo ([[liquidity-rotation-cycle]]).
- Output por ativo: tabela `Ativo | Preço | Bias | Confiança | Rot.Liq | Setup? | Nota` + Top 3
  (`Rot.Liq` = ✅ a-favor / ⚠️ bull-trap / — neutro vs. a Fase). Em Altseason as alts ganham peso; em
  Fuga Stablecoins **rebaixar** os longs de alt. Ao final, **`brain-write`** (1 sessão `YYYY-MM-DD-WATCHLIST.md`).

> Para puro screening técnico/backtest (sem brain), siga direto do Step 1.

## Step 1: Define the Scan

Determine:
- **Symbols**: Which instruments to scan (user-provided or watchlist via `watchlist_get`)
- **Timeframe**: Which timeframe to analyze
- **Criteria**: What to look for (indicator values, strategy results, visual patterns)

## Step 2: Run the Scan

### For Strategy Performance Comparison
Use `batch_run` with action `get_strategy_results`:
```
symbols: ["ES1!", "NQ1!", "YM1!", "RTY1!"]
timeframes: ["15"]
action: "get_strategy_results"
```

### For Screenshot Comparison
Use `batch_run` with action `screenshot`:
```
symbols: ["AAPL", "MSFT", "GOOGL", "AMZN"]
timeframes: ["D"]
action: "screenshot"
```

### For Custom Analysis (per-symbol)
Loop through symbols manually:
1. `chart_set_symbol` + `chart_set_timeframe`
2. `chart_manage_indicator` — add the study
3. `data_get_ohlcv` — pull price data
4. `data_get_indicator` — read indicator values
5. Analyze and record findings

## Step 3: Compile Results

Build a comparison table:
| Symbol | Key Metric 1 | Key Metric 2 | Signal |
|--------|-------------|-------------|--------|

Sort by the most relevant metric.

## Step 4: Report

Present findings:
- Ranked list of symbols by the scan criteria
- Highlight the strongest setups
- Note any divergences or anomalies
- Screenshot the top 1-2 charts for visual confirmation

## Watchlist Integration

To scan the user's watchlist:
1. `watchlist_get` — read all symbols
2. Use the symbol list for the scan
3. `watchlist_add` — add new finds to the watchlist
