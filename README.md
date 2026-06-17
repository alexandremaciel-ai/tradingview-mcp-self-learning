# TradingView MCP — Self-Learning Edition

> 🧠 A persistent **LLM Wiki** that turns every chart analysis into compounding knowledge.
> ⚡ A **skill-first architecture** that keeps the base context tiny and loads analysis logic on demand.
> 🔌 Works with **Claude Code**, **Gemini CLI**, and **Codex CLI** — same brain, any agent.

A personal AI assistant for your TradingView Desktop charts, with a **self-learning second brain** and **multi-CLI support**. Built on the [TradingView MCP Bridge](https://github.com/tradesdontlie/tradingview-mcp) by [@tradesdontlie](https://github.com/tradesdontlie), this fork adds a structured wiki system — inspired by [Andrej Karpathy's LLM Wiki pattern](https://x.com/karpathy) — that the LLM writes and maintains automatically.

Run the same 79 MCP tools and the autonomous learning protocol from Claude Code, Google Gemini CLI, or OpenAI Codex CLI — all sharing a single `wiki/brain/` knowledge base.

> [!WARNING]
> **This tool is not affiliated with, endorsed by, or associated with TradingView Inc.** It interacts with your locally running TradingView Desktop application via Chrome DevTools Protocol. Review the [Disclaimer](#disclaimer) before use.

> [!IMPORTANT]
> **Requires a valid TradingView subscription.** This tool does not bypass or circumvent any TradingView paywall or access control. It reads from and controls the TradingView Desktop app already running on your machine.

> [!NOTE]
> **All data processing occurs locally on your machine.** No TradingView data is transmitted, stored, or redistributed externally by this tool.

---

## Table of Contents

- [What This Fork Adds](#what-this-fork-adds)
- [Skill-First Architecture](#skill-first-architecture)
- [The Self-Learning Brain](#the-self-learning-brain)
- [The Obsidian Interface](#the-obsidian-interface)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Daily Usage](#daily-usage)
- [Skills Reference](#skills-reference)
- [Wiki Structure](#wiki-structure)
- [MCP Tools & CLI](#mcp-tools--cli)
- [Architecture](#architecture)
- [Testing](#testing)
- [Upstream Project](#upstream-project)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## What This Fork Adds

The upstream project gives the LLM **eyes and hands** on your chart. This fork gives it a **memory** — and a **skill-first runtime** that makes that memory cheap to use.

| Capability | Upstream | This Fork |
|---|---|---|
| Chart reading & control | ✅ | ✅ |
| Pine Script dev workflow | ✅ | ✅ |
| Replay, drawings, alerts | ✅ | ✅ |
| **Persistent wiki (second brain)** | ❌ | ✅ |
| **Session-by-session learning** | ❌ | ✅ |
| **Setup tracking with statistics** | ❌ | ✅ |
| **Strategy versioning & review** | ❌ | ✅ |
| **Concept library (SMC, Wyckoff…)** | ❌ | ✅ |
| **Daily macro briefing gate (event-aware analysis)** | ❌ | ✅ |
| **Automated wiki maintenance** | ❌ | ✅ |
| **Skill-first architecture (on-demand logic)** | ❌ | ✅ |
| **Relevance-based brain recall** | ❌ | ✅ |
| **Multi-CLI support (Claude + Gemini + Codex)** | ❌ | ✅ |

---

## Skill-First Architecture

Earlier versions packed the entire analysis protocol — pre-flight checks, macro workflows, a 9-phase technical checklist, and ten wiki operations — into a single **619-line `CLAUDE.md`** that loaded into **every** session. Most of it went unused on any given request, yet it was paid for in tokens every time.

This edition refactors that monolith into a **thin router plus on-demand skills**:

```
CLAUDE.md  (≈95-line router: invariants + dispatch table + tool cheatsheet)
   │  request → skill
   ▼
Reusable layers (loaded only when a request needs them)
   brain-read ──┐
   macro-scan ──┼──►  analyze  (default dispatcher / INGEST)  ◄── multi-layout-scan
   technical-checklist┤        btc-cycle · prediction-feedback · wiki-maintenance · …
   brain-write ─┘
Shared references (markdown, loaded by path): class-rules · confluence-score · tv-tools
```

**Result:** the always-loaded context dropped **~85%** (619 → 95 lines). A Pine task or a feedback request no longer pays for the full analysis pipeline — each request loads only the skills it actually uses. Quality is preserved (the same frameworks, now modular) and recall is sharper (see [The Self-Learning Brain](#the-self-learning-brain)).

### Request Dispatch

`CLAUDE.md` is now a router that maps each request to a skill:

| You ask for… | Skill invoked |
|---|---|
| Analyze a single asset, get a bias/setup (default) | `analyze` |
| A consolidated scan across every chart layout | `multi-layout-scan` |
| A scan/screen across multiple symbols or a watchlist | `multi-symbol-scan` |
| A daily / morning dashboard | `daily-scan` |
| A macro briefing — economic calendar, what can move BTC (web search) | `btc-macro-briefing` |
| BTC cycle, top/bottom projection | `btc-cycle` |
| "How did my prediction do?" | `prediction-feedback` |
| Wiki lint, strategy update, compile, review, search | `wiki-maintenance` |
| Recalibrate TradingView layout profiles | `recalibrate-layouts` |
| Build a Pine indicator/strategy | `pine-develop` |
| Practice in replay / manual backtest | `replay-practice` |
| Backtest performance report | `strategy-report` |

The `analyze` dispatcher and the scan skills compose four **reusable layers** — `brain-read`, `macro-scan`, `technical-checklist`, `brain-write` — so the AUTO-PILOT read/write discipline stays intact without duplicating logic. Portability is handled by `scripts/tools/sync_agent_md.py`, which regenerates `GEMINI.md` and `AGENTS.md` from `CLAUDE.md` so all three agents stay in lockstep.

---

## The Self-Learning Brain

Every chart analysis feeds a structured markdown wiki that the LLM maintains automatically. The core of the system is `wiki/brain/` — the active memory the agent reads **before** analyzing and writes **after**.

```
wiki/
├── index.md                          # Master index (auto-updated)
├── log.md                            # Append-only operation log
├── brain/                            # Active second brain
│   ├── insights-hot.md               #   Top-8 rolling digest (cheap, always read)
│   ├── insights.md                   #   Full insight history (searched by relevance)
│   ├── insights-archive/             #   Cold storage pruned by archive_brain.py
│   ├── mistakes.md                   #   Logged errors + prevention notes
│   ├── predictions-log.md            #   Predictions with objective grading
│   ├── patterns.md                   #   Recurring patterns with confirmation counts
│   ├── indicators.md                 #   Per-indicator hit-rate calibration
│   ├── metrics.md                    #   Win rate, Brier score, circuit breaker
│   └── layouts.md                    #   TradingView layout fingerprints
├── assets/BTCUSD.md                  # Per-asset pages with live status
├── setups/                           # Trade patterns with win-rate stats
├── strategies/                       # Versioned strategies with performance
├── concepts/SMC.md, Wyckoff.md...    # Technical analysis knowledge base
├── sessions/                         # Every analysis session archived
├── briefings/                        # Daily macro briefings (YYYY-MM-DD.md)
├── analysis/                         # Q&A and insights preserved
└── lint/                             # Wiki health-check reports
```

### Relevance-Based Recall

The brain no longer dumps entire files into context. On each analysis, `brain-read`:

- reads `insights-hot.md` (a Top-8 rolling digest) for cheap, always-on context;
- searches `insights.md` by **relevance** (`wiki_search` / grep on the asset & timeframe) instead of reading it whole;
- greps `predictions-log.md` for **open predictions of the current symbol** rather than the full log.

`archive_brain.py` keeps `insights.md` lean by moving older entries to `insights-archive/`, and `brain-write` keeps `insights-hot.md` trimmed to the Top 8. The effect is both fewer tokens and a more **relevant** recall than chronological dumping.

### Daily Macro Briefing Gate

Chart indicators show the *structural* macro (USDT.D, DXY, S&P, longs/shorts) but are blind to *event* macro — an FOMC meeting today, a CPI print tomorrow, ETF flows, a stablecoin depeg. The `btc-macro-briefing` skill gathers that via live web search, but on its own it was ephemeral: nothing recorded whether it had already run, and `macro-scan` never consumed it.

This edition turns the briefing into a **deterministic daily artifact** wired into the mandatory pre-flight:

- **Persistence** — the briefing now writes `wiki/briefings/YYYY-MM-DD.md` (one file per day, BRT) and appends to the log.
- **The gate** — `brain-read` (step 2b) runs `check_briefing.py`, a read-only filesystem check. On the **first analysis of the day** with no briefing yet, it runs `btc-macro-briefing` *before* proceeding; later analyses the same day reuse the file (no re-run) unless a high-impact event (FOMC/CPI/NFP/PCE) falls inside the analysis window, which forces a refresh.
- **Consumption** — `macro-scan` (step 0.5) folds the briefing's *Macro Risk Verdict* (suggested stance, critical dates, imminent event) into the regime call and the confluence score; an imminent 🔴 event downgrades confidence and tags the read `pre-event`.

The decision to run still lives with the LLM, but the *evidence* (does today's briefing exist?) is a filesystem fact — not a memory guess.

### The Self-Learning Loop

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│  TradingView │────▶│  MCP Bridge  │────▶│  Wiki (markdown)  │
│ (live chart) │     │  (79 tools)  │     │  (persistent)     │
└──────────────┘     └──────────────┘     └────────┬─────────┘
                                                    │
                     ┌──────────────┐               │
                     │   LLM Agent  │◀──────────────┘
                     │ (brain-read  │
                     │  before, ────│── better analysis ──▶ next session
                     │  brain-write │
                     │  after)      │
                     └──────────────┘
```

Each session compounds on previous knowledge. The wiki grows. The analysis improves.

### How the Wiki Grows

1. **You analyze a chart** → a session file is created in `wiki/sessions/`.
2. **A setup is identified** → tracked in `wiki/setups/` with occurrence history.
3. **Statistics accumulate** → win rates and R:R ratios auto-calculated by `metrics_engine.py`.
4. **Strategy evolves** → `wiki/strategies/` updated with evidence-based changes.
5. **Lint catches gaps** → missing data, stale pages, and broken links flagged by `wiki_lint.py`.

---

## The Obsidian Interface

The entire repository is designed to be opened as an **Obsidian Vault**. The LLM writes the markdown; you visualize it in Obsidian using:

- **Graph View** — an interconnected map of assets, setups, and sessions
- **Dataview Dashboards** — live tables of win rates and open predictions
- **Web Clipper** — save articles directly to `raw/clippings/` for the LLM to process
- **Marp Slides** — weekly performance reviews generated as presentations

<details>
<summary><strong>Obsidian step-by-step configuration</strong></summary>

1. **Open the Vault:** install [Obsidian](https://obsidian.md/), click "Open Folder as Vault", and select this repository folder.
2. **Trust Author:** if prompted, click "Trust Author" so the pre-configured workspace settings load safely.
3. **Enable Community Plugins:** Settings ⚙️ → Community Plugins → disable Safe Mode to allow the pre-configured plugins (Dataview, Templater, Calendar).
4. **View the Dashboard:** open `wiki/dashboard.md` to see your learning stats rendered natively.
5. **Web Clipper:**
   - install the official [Obsidian Web Clipper](https://obsidian.md/clipper) browser extension and select your vault;
   - set **Behavior → Folder location** to `raw/clippings`;
   - in **Properties**, add `source_url: {{url}}` and `date_captured: {{date}}`;
   - in **Note Content**, paste:
     ```markdown
     # Clipping: {{title}}

     ## Key Takeaways
     -

     ## Concepts Mentioned
     -

     ## Original Content
     {{content}}
     ```
   - **Usage:** clip any trading article, then ask your agent: *"Compile recent clippings in the wiki."*

</details>

---

## Prerequisites

- **TradingView Desktop app** (paid subscription required for real-time data)
- **Node.js 18+**
- **Python 3** (for the offline brain/wiki maintenance scripts)
- **At least one MCP-compatible CLI agent:**
  - [Claude Code](https://claude.ai/code) — uses `CLAUDE.md` + `.mcp.json`
  - [Gemini CLI](https://geminicli.com) — uses `GEMINI.md` + `.gemini/settings.json`
  - [Codex CLI](https://developers.openai.com/codex/cli) — uses `AGENTS.md` + `.codex/config.toml`
- **macOS, Windows, or Linux**

---

## Installation & Setup

### 1. Install

**One-line install (recommended).** Clones, installs dependencies, registers the MCP server in Claude Code, and optionally launches TradingView:

```bash
curl -fsSL https://raw.githubusercontent.com/alexandremaciel-ai/tradingview-mcp-self-learning/main/scripts/setup.sh | bash
```

**Manual clone:**

```bash
git clone https://github.com/alexandremaciel-ai/tradingview-mcp-self-learning.git
cd tradingview-mcp-self-learning
npm install
```

> [!NOTE]
> The project has no heavy dependencies — only `@modelcontextprotocol/sdk` and `chrome-remote-interface`. Installation is fast.

### 2. Register the MCP server (once per CLI)

<details open>
<summary><strong>Claude Code</strong></summary>

**Global registration (recommended):**

```bash
claude mcp add --scope user tradingview -- node "$(pwd)/src/server.js"
```

**Project-local auto-registration (zero config):** the repo ships a root `.mcp.json`. Open Claude Code **inside the project directory** and the server registers automatically.

**Manual JSON** in `~/.claude/.mcp.json`:

```json
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["/absolute/path/to/tradingview-mcp-self-learning/src/server.js"]
    }
  }
}
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

`GEMINI.md` is auto-loaded by Gemini CLI. Create the project-scoped MCP config (gitignored):

```bash
mkdir -p .gemini
cat > .gemini/settings.json << 'EOF'
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["./src/server.js"],
      "cwd": "/absolute/path/to/tradingview-mcp-self-learning"
    }
  }
}
EOF
```

> [!IMPORTANT]
> Replace `/absolute/path/to/tradingview-mcp-self-learning` with the output of `pwd` inside the project directory.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

`AGENTS.md` is auto-loaded by Codex CLI. Create the project-scoped MCP config (gitignored) and trust the project:

```bash
mkdir -p .codex
cat > .codex/config.toml << 'EOF'
[mcp_servers.tradingview]
command = "node"
args = ["./src/server.js"]
cwd = "/absolute/path/to/tradingview-mcp-self-learning"
startup_timeout_sec = 15
tool_timeout_sec = 120
required = true
EOF

cat >> ~/.codex/config.toml << EOF

[projects."/absolute/path/to/tradingview-mcp-self-learning"]
trust_level = "trusted"
EOF
```

> [!IMPORTANT]
> Replace the absolute path in **both** `.codex/config.toml` and the `~/.codex/config.toml` trust entry.

</details>

### 3. Launch TradingView with CDP enabled

> [!IMPORTANT]
> TradingView **must be launched via this script** (not from the Dock or Applications folder). The Chrome DevTools Protocol debug port must be explicitly enabled for the MCP bridge to connect.

| Platform | Command |
|---|---|
| **macOS** | `./scripts/launch_tv_debug_mac.sh` |
| **Windows** | `scripts\launch_tv_debug.bat` |
| **Linux** | `./scripts/launch_tv_debug_linux.sh` |
| **Manual** | `/path/to/TradingView --remote-debugging-port=9222` |
| **Via MCP** | Ask your agent: *"Use tv_launch to start TradingView"* |

The script auto-detects the install path, relaunches with `--remote-debugging-port=9222`, and waits for `CDP ready at http://localhost:9222`. Verify the port directly with:

```bash
curl http://localhost:9222/json/version
```

### 4. Verify the connection

Open your CLI from the project directory and ask:

```
Use tv_health_check to verify TradingView is connected
```

The agent confirms the CDP connection, reports the TradingView version, and lists available tools.

<details>
<summary><strong>Troubleshooting</strong></summary>

| Symptom | Fix |
|---|---|
| `CDP connection refused` | TradingView wasn't launched with the debug script — repeat step 3 |
| `Port 9222 already in use` | Run `lsof -i :9222` and kill the conflicting process |
| `MCP server not found` | Re-run step 2; restart your CLI after registering |
| `TradingView not found` in script | Install TradingView Desktop or pass a custom path manually |

You can also check connectivity with `tv status` or `curl http://localhost:9222/json/version`.

</details>

---

## Daily Usage

```
1. Launch TradingView:  ./scripts/launch_tv_debug_mac.sh
2. Open your agent in the project directory:  claude | gemini | codex
3. "Use tv_health_check to verify TradingView is connected"
4. "Analyze the current chart and record it in the wiki"   → runs the analyze pipeline
5. Review the new session file in wiki/sessions/
6. Keep going — the wiki compounds automatically
```

Common requests (the router picks the right skill automatically):

| What you want | What to say |
|---|---|
| Analyze & record an asset | *"Analyze BTC and record it in the wiki"* |
| Consolidated multi-layout scan | *"Run a multi-layout scan on Bitcoin and Ethereum"* |
| Macro briefing / economic calendar | *"Give me a macro briefing — what can move BTC this week?"* |
| Query the brain | *"Based on the wiki, what is the current bias for BTC?"* |
| Close a prediction | *"How did my last BTC prediction do?"* |
| Health check | *"Run a wiki health-check"* |
| Strategy review | *"Update the strategy based on recent sessions"* |

> [!TIP]
> All three CLIs share the same `wiki/brain/` — insights compound across platforms.

---

## Skills Reference

Skills live in `skills/<name>/SKILL.md` and load on demand. Claude Code invokes them via the Skill tool; Gemini/Codex read the same files by path (kept in sync by `sync_agent_md.py`).

### Reusable layers
| Skill | Role |
|---|---|
| `brain-read` | AUTO-PILOT READ — connection, feeds, layout fingerprint, relevance-based brain recall, declare preventions/insights, close open predictions |
| `macro-scan` | Market-context detector + class workflow (A/B/C/D) + macro reading rules (Risk-On/Off, squeeze, weekend) |
| `technical-checklist` | The 9-phase checklist — MTF, SMC, Wyckoff, Fibonacci, layout-driven indicators, playbook, liquidity/USDT.D, bias + confluence score |
| `brain-write` | AUTO-PILOT WRITE — insight, prediction, indicator/pattern updates, session file, log |

### Dispatchers & operations
| Skill | Role |
|---|---|
| `analyze` | Default pipeline (INGEST): classify → brain-read → macro-scan → technical-checklist → bias → brain-write |
| `multi-layout-scan` | Sweep every TradingView layout with indicator dedup → consolidated cross-axis analysis |
| `multi-symbol-scan` | Screen/compare multiple symbols or a watchlist |
| `daily-scan` | Morning dashboard (macro 1× + quick BTC + watchlist + predictions) |
| `btc-macro-briefing` | Web-search macro briefing (economic calendar, liquidity, ETF flows, sentiment, black-swan) → daily verdict; persists `wiki/briefings/`. Gated by `brain-read` step 2b |
| `btc-cycle` | Cycle phase, top/bottom scoring, 200W SMA, on-chain, Fibonacci-log projection |
| `prediction-feedback` | Objective grading of open predictions + setup/indicator/metric updates |
| `wiki-maintenance` | LINT / UPDATE STRATEGY / COMPILE / REVIEW / SEARCH — runs the Python tools |
| `recalibrate-layouts` | Re-fingerprint TradingView layouts into `wiki/brain/layouts.md` |
| `chart-analysis`, `pine-develop`, `replay-practice`, `strategy-report` | Focused tactical workflows |

### Shared references
`skills/_references/class-rules.md` · `confluence-score.md` · `tv-tools.md` — loaded by path when a skill needs the full detail, so the logic is never duplicated.

### Maintenance scripts (`scripts/tools/`)
| Script | Purpose |
|---|---|
| `fetch_feeds.py` | Pull funding/OI (Coinalyze) + Fear & Greed → `raw/feeds/latest.md` |
| `check_briefing.py` | Read-only gate — report whether today's macro briefing exists (date/age/horizon) |
| `archive_brain.py` | Prune `insights.md` to the Top N, archive the rest |
| `wiki_lint.py` | Broken links, expired predictions, statless setups; updates index counters |
| `metrics_engine.py` | Win rate, Brier score, drawdown, circuit breaker → `brain/metrics.md` |
| `plot_accuracy.py` / `plot_metrics.py` | Accuracy curve + calibration charts |
| `sync_agent_md.py` | Regenerate `GEMINI.md` / `AGENTS.md` from `CLAUDE.md` |

---

## Wiki Structure

### Concepts (pre-populated)

| Concept | Description |
|---|---|
| [SMC](wiki/concepts/SMC.md) | Smart Money Concepts — CHoCH, BoS, FVG, Order Blocks |
| [Wyckoff](wiki/concepts/Wyckoff.md) | Accumulation, Distribution, Spring, UTAD |
| [ADX](wiki/concepts/ADX.md) | Trend-strength filter with interpretation table |
| [ATR](wiki/concepts/ATR.md) | Volatility-based position sizing and stop-loss |
| [MTF Analysis](wiki/concepts/multi-timeframe-analysis.md) | 1D→4H→1H→15m→5m hierarchy and conflict rules |
| [BTCUSDLONGS/SHORTS](wiki/concepts/btcusdlongs-btcusdshorts.md) | Bitfinex margin positioning for squeeze detection |
| [Short/Long Squeeze](wiki/concepts/short-long-squeeze.md) | Cascade liquidation mechanics and setup conditions |
| [BTC Cycle Analysis](wiki/concepts/btc-cycle-analysis.md) | Macro cycle framework — tops, bottoms, scoring system |
| [Puell Multiple](wiki/concepts/puell-multiple.md) | Miner-revenue metric for cycle phase identification |
| [Pi Cycle Top](wiki/concepts/pi-cycle-top.md) | 111DMA vs 350DMA×2 crossover for cycle-top detection |
| [Hash Ribbons](wiki/concepts/hash-ribbons.md) | Mining-capitulation indicator for cycle-bottom signals |

### Strategies

The default strategy — [Conservative Trend Follower v2.0](wiki/strategies/conservative-trend-follower-v2.md) — documents entry/exit rules with a 4-layer filter, a stepped trailing stop, HTF conflict resolution, and a performance-tracking table. Additional strategies:

| Strategy | Description |
|---|---|
| [Liquidity Wicks + USDT.D](wiki/strategies/liquidity-wicks-trap-short-usdtd.md) | HTF wick mapping, trap detection, USDT.D correlation |
| [RSI + StochRSI Combined](wiki/strategies/rsi-stochrsi-combined.md) | RSI (D/4H) for direction, StochRSI (1H/15M) for entry timing |

> [!NOTE]
> Personal performance numbers live only in `wiki/brain/metrics.md` and `wiki/setups/index.md` (both gitignored). The public `wiki/strategies/*.md` files keep qualitative placeholders.

---

## MCP Tools & CLI

All 79 upstream tools are available. Each CLI has its own context file with the dispatch table and a tool cheatsheet; the full tool decision tree lives in `skills/_references/tv-tools.md`.

| CLI | Context File | MCP Config |
|---|---|---|
| Claude Code | [`CLAUDE.md`](CLAUDE.md) | `.mcp.json` (tracked) |
| Gemini CLI | [`GEMINI.md`](GEMINI.md) | `.gemini/settings.json` (gitignored) |
| Codex CLI | [`AGENTS.md`](AGENTS.md) | `.codex/config.toml` (gitignored) |

**Chart reading:** `chart_get_state` · `data_get_study_values` · `quote_get` · `data_get_ohlcv`
**Pine drawings:** `data_get_pine_lines` · `data_get_pine_labels` · `data_get_pine_tables` · `data_get_pine_boxes`
**Chart control:** `chart_set_symbol` · `chart_set_timeframe` · `chart_set_type` · `chart_manage_indicator` · `chart_scroll_to_date`
**Pine development:** `pine_set_source` · `pine_smart_compile` · `pine_get_errors` · `pine_save` · `pine_new` · `pine_open`
**Replay / drawing / alerts:** `replay_start` · `replay_step` · `replay_trade` · `draw_shape` · `alert_create` · `capture_screenshot`
**Multi-pane & batch:** `pane_set_layout` · `pane_set_symbol` · `batch_run` · `tab_list` · `tab_new`

Every MCP tool is also a `tv` CLI command with JSON output:

```bash
tv status                          # check CDP connection
tv quote                           # current price
tv symbol AAPL                     # change symbol
tv ohlcv --summary                 # price summary
tv screenshot -r chart             # capture chart
tv pine compile                    # compile Pine Script
tv stream quote | jq '.close'      # monitor price live
```

---

## Architecture

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Claude Code  │   │ Gemini CLI   │   │ Codex CLI    │
│ CLAUDE.md    │   │ GEMINI.md    │   │ AGENTS.md    │   ← thin routers (kept in
│ .mcp.json    │   │ .gemini/     │   │ .codex/      │     sync by sync_agent_md.py)
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       └──────────────┬───┴──────────────────┘
                      │  request → skill (loaded on demand)
              ┌───────▼────────┐
              │ skills/         │  brain-read · macro-scan · technical-checklist
              │ (on-demand SOP) │  brain-write · analyze · btc-cycle · …
              └───────┬────────┘
              ┌───────▼────────┐
              │  MCP Server     │  node stdio · 79 tools
              └───────┬────────┘
                      │ CDP (port 9222)
              ┌───────▼────────┐
              │  TradingView    │
              │  Desktop        │
              └───────┬────────┘
              ┌───────▼────────┐
              │  wiki/brain/    │  ← shared state (insights, predictions,
              │  wiki/sessions/ │     mistakes compound across all CLIs)
              │  raw/           │
              └─────────────────┘
```

- **Transport:** MCP over stdio (79 tools) + a `tv` CLI command.
- **Connection:** Chrome DevTools Protocol on `localhost:9222`.
- **Runtime:** thin per-CLI router → on-demand skills → MCP server.
- **Wiki:** markdown maintained by the LLM, human-readable, git-trackable.
- **Multi-CLI:** all agents share the same MCP server and `wiki/brain/` knowledge base.
- **Dependencies:** only `@modelcontextprotocol/sdk` and `chrome-remote-interface` (Node) + Python 3 stdlib for the maintenance scripts.

---

## Testing

```bash
npm test          # offline e2e + Pine-analysis tests (no TradingView needed)
tv status         # verify CDP connection (TradingView must be running)
```

---

## Upstream Project

This is a fork of **[tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** by **[@tradesdontlie](https://github.com/tradesdontlie)**, licensed under the [MIT License](https://github.com/tradesdontlie/tradingview-mcp/blob/main/LICENSE). The upstream project provides the complete MCP bridge (79 tools, CLI, streaming) that connects agents to TradingView Desktop via CDP. All original functionality is preserved.

### What this fork changes

- **Added** `wiki/` — a persistent, LLM-maintained knowledge base (the second brain).
- **Added** `skills/` — the skill-first runtime (reusable layers, dispatchers, operations, shared references).
- **Added** `raw/` — immutable data storage (screenshots, OHLCV, feeds, Pine exports).
- **Added** `scripts/tools/` — Python maintenance scripts (feeds, archiving, lint, metrics, plots, agent-file sync).
- **Added** `GEMINI.md` / `AGENTS.md` — Gemini and Codex context files, generated from `CLAUDE.md`.
- **Refactored** `CLAUDE.md` — from a 619-line monolith into a ~95-line skill-first router.
- **Updated** `.gitignore` — security rules for personal brain data and local CLI configs (`.gemini/`, `.codex/`, `.claude/`).

No upstream source code (`src/`, `tests/`) was modified.

> [!NOTE]
> CLI config directories (`.gemini/`, `.codex/`, `.claude/`) are **gitignored** because they contain absolute local paths. The context files (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`) **are** tracked — they hold only the shared protocol, no personal data.

---

## Attributions

- **Upstream project:** [tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) by [@tradesdontlie](https://github.com/tradesdontlie) — MIT License
- **Wiki pattern:** inspired by [Andrej Karpathy's LLM Wiki concept](https://x.com/karpathy)
- **Fork maintainer:** [@alexandremaciel-ai](https://github.com/alexandremaciel-ai)

This project is not affiliated with, endorsed by, or associated with:
- **TradingView Inc.** — TradingView is a trademark of TradingView Inc.
- **Anthropic** — Claude and Claude Code are trademarks of Anthropic, PBC.

---

## Disclaimer

This project is provided **for personal, educational, and research purposes only**.

**How this tool works:** it uses the Chrome DevTools Protocol (CDP), a standard debugging interface built into all Chromium-based applications. It does not reverse engineer any proprietary TradingView protocol, connect to TradingView's servers, or bypass any access controls. The debug port must be explicitly enabled by the user via a standard Chromium command-line flag (`--remote-debugging-port=9222`).

By using this software, you acknowledge and agree that:

1. **You are solely responsible** for ensuring your use complies with [TradingView's Terms of Use](https://www.tradingview.com/policies/) and all applicable laws.
2. TradingView's Terms of Use **restrict automated data collection, scraping, and non-display usage** of their platform and data. This tool uses CDP to programmatically interact with the TradingView Desktop app, which may conflict with those terms.
3. **You assume all risk** associated with using this tool. The authors are not responsible for any account bans, suspensions, legal actions, or other consequences.
4. This tool **must not be used** for, including but not limited to:
   - redistributing, reselling, or commercially exploiting TradingView's market data;
   - circumventing TradingView's access controls or subscription restrictions;
   - performing automated trading or algorithmic decision-making using extracted data;
   - violating the intellectual property rights of Pine Script indicator authors;
   - connecting to TradingView's servers or infrastructure (all access is via the locally running Desktop app).
5. The streaming functionality monitors your locally running TradingView Desktop instance only. It does not connect to TradingView's servers.
6. Market data accessed through this tool remains subject to exchange and data-provider licensing terms. **Do not redistribute, store, or commercially exploit any data obtained through this tool.**
7. This tool accesses internal, undocumented TradingView application interfaces that may change or break at any time without notice.
8. **The wiki system** stores analysis notes locally in markdown. It does not store raw market data. Screenshots in `raw/screenshots/` are for personal reference only and must not be redistributed.

**Use at your own risk.** If you are unsure whether your intended use complies with TradingView's terms, do not use this tool.

---

## License

MIT — see [LICENSE](LICENSE) for details. The MIT license applies to the source code of this project only. It does not grant any rights to TradingView's software, data, trademarks, or intellectual property.

- Original upstream code: Copyright (c) 2026 [@tradesdontlie](https://github.com/tradesdontlie).
- Wiki system & skill-first additions: Copyright (c) 2026 [@alexandremaciel-ai](https://github.com/alexandremaciel-ai).
