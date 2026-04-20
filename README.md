# TradingView MCP — Self-Learning Edition

> 🧠 Fork with a persistent **LLM Wiki** that turns every chart analysis into compounding knowledge.

Personal AI assistant for your TradingView Desktop charts — now with a **self-learning second brain**. Built on the [TradingView MCP Bridge](https://github.com/tradesdontlie/tradingview-mcp) by [@tradesdontlie](https://github.com/tradesdontlie), this fork adds a structured wiki system inspired by [Andrej Karpathy's LLM Wiki pattern](https://x.com/karpathy) where the LLM writes and maintains the knowledge base automatically.

> [!WARNING]
> **This tool is not affiliated with, endorsed by, or associated with TradingView Inc.** It interacts with your locally running TradingView Desktop application via Chrome DevTools Protocol. Review the [Disclaimer](#disclaimer) before use.

> [!IMPORTANT]
> **Requires a valid TradingView subscription.** This tool does not bypass or circumvent any TradingView paywall or access control. It reads from and controls the TradingView Desktop app already running on your machine.

> [!NOTE]
> **All data processing occurs locally on your machine.** No TradingView data is transmitted, stored, or redistributed externally by this tool.

---

## What This Fork Adds

The upstream project gives Claude **eyes and hands** on your chart. This fork gives it a **memory**.

| Feature | Upstream | This Fork |
|---------|----------|-----------|
| Chart reading & control | ✅ | ✅ |
| Pine Script dev workflow | ✅ | ✅ |
| Replay, drawings, alerts | ✅ | ✅ |
| **Persistent wiki (second brain)** | ❌ | ✅ |
| **Session-by-session learning** | ❌ | ✅ |
| **Setup tracking with statistics** | ❌ | ✅ |
| **Strategy versioning & review** | ❌ | ✅ |
| **Concept library (SMC, Wyckoff…)** | ❌ | ✅ |
| **Automated wiki maintenance** | ❌ | ✅ |

### The Wiki System

Every chart analysis feeds a structured markdown wiki that the LLM maintains automatically:

```
wiki/
├── index.md                          # Master index (auto-updated)
├── log.md                            # Append-only operation log
├── overview.md                       # Trading thesis & system rules
├── assets/BTCUSD.md                  # Per-asset pages with live status
├── setups/                           # Trade patterns with win-rate stats
├── strategies/                       # Versioned strategies with performance
├── concepts/SMC.md, Wyckoff.md...    # Technical analysis knowledge base
├── sessions/                         # Every analysis session archived
├── analysis/                         # Q&A and insights preserved
└── lint/                             # Wiki health-check reports
```

### Four Wiki Operations

| Command | Trigger | What Happens |
|---------|---------|-------------|
| **INGEST** | _"Analise o gráfico e registre na wiki"_ | Captures chart state → creates session → updates asset page → logs |
| **QUERY** | _"Baseado na wiki, [pergunta]"_ | Reads relevant pages → synthesizes answer → archives if valuable |
| **LINT** | _"Health-check da wiki"_ | Checks broken links, stale data, missing fields → generates report |
| **UPDATE** | _"Atualize a estratégia"_ | Reviews recent sessions → recalculates stats → proposes adjustments |

### The Self-Learning Loop

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  TradingView │────▶│  MCP Bridge  │────▶│  Wiki (markdown) │
│  (live chart)│     │  (68 tools)  │     │  (persistent)    │
└─────────────┘     └──────────────┘     └────────┬────────┘
                                                   │
                    ┌──────────────┐                │
                    │   LLM Agent  │◀───────────────┘
                    │  (reads wiki │
                    │   before     │─── better analysis ──▶ next session
                    │   analyzing) │
                    └──────────────┘
```

Each session compounds on previous knowledge. The wiki grows. The analysis improves.

---

## Prerequisites

- **TradingView Desktop app** (paid subscription required for real-time data)
- **Node.js 18+**
- **Claude Code** with MCP support (or any MCP-compatible agent)
- **macOS, Windows, or Linux**

## Quick Start

### Option A — One-Line Install (recommended)

Clones, installs dependencies, registers the MCP server in Claude Code, and optionally launches TradingView — all in one command:

```bash
curl -fsSL https://raw.githubusercontent.com/alexandremaciel-ai/tradingview-mcp-self-learning/main/scripts/setup.sh | bash
```

Or if you already cloned the repo:

```bash
./scripts/setup.sh
```

That's it. Open Claude Code and start using.

### Option B — Project Auto-Config (zero setup)

If you just want to clone and go:

```bash
git clone https://github.com/alexandremaciel-ai/tradingview-mcp-self-learning.git
cd tradingview-mcp-self-learning
npm install
```

Then open Claude Code **inside the project directory**. The `.mcp.json` at the root auto-registers the MCP server — no manual JSON editing needed.

> [!NOTE]
> With Option B the MCP server is only active when Claude Code is opened inside this project directory. Use Option A for global access from any directory.

### Option C — Manual Setup

If you prefer full control:

```bash
git clone https://github.com/alexandremaciel-ai/tradingview-mcp-self-learning.git
cd tradingview-mcp-self-learning
npm install

# Register globally via Claude Code CLI
claude mcp add --scope user tradingview -- node "$(pwd)/src/server.js"
```

Or add to `~/.claude/.mcp.json` manually:

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

### Launch TradingView

TradingView Desktop must be running with Chrome DevTools Protocol enabled:

| Platform | Command |
|----------|---------|
| **Mac** | `./scripts/launch_tv_debug_mac.sh` |
| **Windows** | `scripts\launch_tv_debug.bat` |
| **Linux** | `./scripts/launch_tv_debug_linux.sh` |
| **Manual** | `/path/to/TradingView --remote-debugging-port=9222` |
| **Via MCP** | Ask Claude: *"Use tv_launch to start TradingView"* |

### Verify & Start

```
1. Ask Claude: "Use tv_health_check to verify TradingView is connected"
2. Ask Claude: "Analyze the current graph and record it on the wiki."
```

The wiki will grow from here.

---

## Running the Application — Complete Step-by-Step Guide

Follow these steps every time you want to use the TradingView MCP Self-Learning system.

### Prerequisites Checklist

Before starting, make sure you have:

- [ ] **TradingView Desktop** installed (paid subscription required)
- [ ] **Node.js 18+** — verify with `node --version`
- [ ] **Claude Code** with MCP support — verify with `claude --version`
- [ ] This repository cloned and dependencies installed (see Step 1)

---

### Step 1 — Install Dependencies

Clone the repository (if you haven't already) and install Node.js dependencies:

```bash
git clone https://github.com/alexandremaciel-ai/tradingview-mcp-self-learning.git
cd tradingview-mcp-self-learning
npm install
```

If you already cloned it, just make sure dependencies are up to date:

```bash
npm install
```

> [!NOTE]
> The project has no heavy dependencies — only `@modelcontextprotocol/sdk` and `chrome-remote-interface`. Installation is fast.

---

### Step 2 — Launch TradingView with CDP Enabled

> [!IMPORTANT]
> TradingView **must be launched via this script** (not from your Dock or Applications folder). The Chrome DevTools Protocol (CDP) debug port must be explicitly enabled for the MCP bridge to connect.

Run the platform-specific launch script:

**macOS:**
```bash
./scripts/launch_tv_debug_mac.sh
```

**Windows:**
```cmd
scripts\launch_tv_debug.bat
```

**Linux:**
```bash
./scripts/launch_tv_debug_linux.sh
```

**What the script does:**
1. Auto-detects your TradingView installation path
2. Kills any existing TradingView process
3. Relaunches TradingView with `--remote-debugging-port=9222`
4. Waits up to 15 seconds for the CDP endpoint to become available
5. Confirms readiness with a `CDP ready at http://localhost:9222` message

**Expected output:**
```
Found TradingView at: /Applications/TradingView.app/Contents/MacOS/TradingView
Launching with --remote-debugging-port=9222 ...
PID: 12345
Waiting for CDP...
CDP ready at http://localhost:9222
{
  "Browser": "Chrome/...",
  "webSocketDebuggerUrl": "ws://localhost:9222/..."
}
```

**If TradingView is installed in a custom path**, run it manually:
```bash
/path/to/TradingView.app/Contents/MacOS/TradingView --remote-debugging-port=9222 &
```

**Verify CDP is responding:**
```bash
curl http://localhost:9222/json/version
```

---

### Step 3 — Register the MCP Server in Claude Code

This step only needs to be done **once**. Skip to Step 4 if you've already registered it.

#### Option A — Global registration (recommended)

Registers the MCP server globally so it's available from any directory in Claude Code:

```bash
claude mcp add --scope user tradingview -- node "$(pwd)/src/server.js"
```

> [!TIP]
> Use `$(pwd)/src/server.js` to automatically insert the absolute path. Run this command from inside the project directory.

#### Option B — Project-local auto-registration (zero config)

The repository already includes a `.mcp.json` at the root. When you open Claude Code **inside the project directory**, the MCP server is registered automatically — no command needed.

```bash
# Just open Claude Code from within the project folder
cd tradingview-mcp-self-learning
claude  # MCP server auto-activates
```

> [!NOTE]
> With Option B, the MCP server is only active when Claude Code is opened inside this project directory. Use Option A for global access.

#### Option C — Manual JSON config

Edit `~/.claude/.mcp.json` (create if it doesn't exist):

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

---

### Step 4 — Verify the Connection

With TradingView running (Step 2) and the MCP server registered (Step 3), open Claude Code and ask:

```
Use tv_health_check to verify TradingView is connected
```

**Expected response:** Claude will confirm the CDP connection is active, report the TradingView version, and list available tools.

**If the connection fails:**

| Symptom | Fix |
|---------|-----|
| `CDP connection refused` | TradingView was not launched with the debug script — repeat Step 2 |
| `Port 9222 already in use` | Run `lsof -i :9222` and kill the conflicting process |
| `MCP server not found` | Re-run Step 3; restart Claude Code after registering |
| `TradingView not found` in script | Install TradingView Desktop or pass a custom path manually |

You can also verify via CLI without Claude Code:
```bash
tv status          # check CDP connection
curl http://localhost:9222/json/version  # raw CDP check
```

---

### Step 5 — Start Using the System

Everything is connected. Here are the key commands to get started:

#### First analysis (triggers wiki creation)
```
Analyze the current chart and record it in the wiki
```

#### Wiki operations
| What you want | What to say |
|---------------|-------------|
| Analyze & save | *"Analyze the current graph and record it on the wiki"* |
| Query the wiki | *"Based on the wiki, what is the current bias for BTC?"* |
| Run a health check | *"Run a wiki health-check"* |
| Update strategy | *"Update the strategy based on recent sessions"* |

#### CLI commands (for power users)
```bash
tv status                     # verify CDP connection
tv quote                      # get current price
tv symbol AAPL                # switch chart symbol
tv ohlcv --summary            # price summary
tv screenshot -r chart        # capture the chart
tv stream quote | jq '.close' # monitor price live
tv pine compile               # compile Pine Script
```

#### Run tests (no TradingView needed)
```bash
npm test          # runs 29 offline unit tests
```

---

### Typical Session Flow

```
1. Run ./scripts/launch_tv_debug_mac.sh
2. Open Claude Code in the project directory
3. Ask: "Use tv_health_check to verify TradingView is connected"
4. Ask: "Analyze the current chart and record it in the wiki"
5. Review the new session file created in wiki/sessions/
6. Continue your analysis — the wiki compounds automatically
```

> [!TIP]
> The wiki grows with every session. The more you use it, the better the analysis becomes as the LLM reads accumulated insights before every new session.

---

## Wiki Structure

### Concepts (pre-populated)

The wiki ships with foundational technical analysis concepts:

| Concept | Description |
|---------|-------------|
| [SMC](wiki/concepts/SMC.md) | Smart Money Concepts — CHoCH, BoS, FVG, Order Blocks |
| [Wyckoff](wiki/concepts/Wyckoff.md) | Accumulation, Distribution, Spring, UTAD |
| [ADX](wiki/concepts/ADX.md) | Trend strength filter with interpretation table |
| [ATR](wiki/concepts/ATR.md) | Volatility-based position sizing and stop-loss |
| [MTF Analysis](wiki/concepts/multi-timeframe-analysis.md) | 1D→4H→1H→15m→5m hierarchy and conflict rules |

### Strategy

The default strategy — [Conservative Trend Follower v2.0](wiki/strategies/conservative-trend-follower-v2.md) — documents:
- Entry/exit rules with 4-layer filter system
- Trailing stop progression (breakeven at +10%, stepped)
- HTF conflict resolution (4H bearish + ADX > 25 = hard block)
- Performance tracking table (populated after sessions)

### How the Wiki Grows

1. **You analyze a chart** → a session file is created in `wiki/sessions/`
2. **A setup is identified** → tracked in `wiki/setups/` with occurrence history
3. **Statistics accumulate** → win rates, R:R ratios auto-calculated
4. **Strategy evolves** → `wiki/strategies/` updated with evidence-based changes
5. **Lint catches gaps** → missing data, stale pages, broken links flagged

---

## MCP Tools (68 tools)

All 68 tools from the upstream project are fully available. See [`CLAUDE.md`](CLAUDE.md) for the complete decision tree and tool reference.

### Chart Reading
`chart_get_state` · `data_get_study_values` · `quote_get` · `data_get_ohlcv`

### Pine Script Data
`data_get_pine_lines` · `data_get_pine_labels` · `data_get_pine_tables` · `data_get_pine_boxes`

### Chart Control
`chart_set_symbol` · `chart_set_timeframe` · `chart_set_type` · `chart_manage_indicator` · `chart_scroll_to_date`

### Pine Script Development
`pine_set_source` · `pine_smart_compile` · `pine_get_errors` · `pine_save` · `pine_new` · `pine_open`

### Replay, Drawing, Alerts
`replay_start` · `replay_step` · `replay_trade` · `draw_shape` · `alert_create` · `capture_screenshot`

### Multi-Pane & Batch
`pane_set_layout` · `pane_set_symbol` · `batch_run` · `tab_list` · `tab_new`

## CLI

Every MCP tool is also a `tv` CLI command with JSON output:

```bash
tv status                          # check connection
tv quote                           # current price
tv symbol AAPL                     # change symbol
tv ohlcv --summary                 # price summary
tv screenshot -r chart             # capture chart
tv pine compile                    # compile Pine Script
tv stream quote | jq '.close'      # monitor price
```

---

## Architecture

```
Claude Code  ←→  MCP Server (stdio)  ←→  CDP (port 9222)  ←→  TradingView Desktop (Electron)
                      │
                      ▼
              wiki/ (persistent markdown knowledge base)
              raw/  (immutable screenshots, OHLCV, Pine exports)
```

- **Transport**: MCP over stdio (68 tools) + CLI (`tv` command)
- **Connection**: Chrome DevTools Protocol on localhost:9222
- **Wiki**: Markdown files maintained by LLM, human-readable, git-trackable
- **No dependencies** beyond `@modelcontextprotocol/sdk` and `chrome-remote-interface`

## Testing

```bash
npm test          # 29 offline tests (no TradingView needed)
tv status         # verify CDP connection (TradingView must be running)
```

---

## Upstream Project

This is a fork of **[tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp)** by **[@tradesdontlie](https://github.com/tradesdontlie)**, licensed under the [MIT License](https://github.com/tradesdontlie/tradingview-mcp/blob/main/LICENSE).

The upstream project provides the complete MCP bridge (68 tools, CLI, streaming) that connects Claude Code to TradingView Desktop via CDP. All original functionality is preserved in this fork.

### What this fork changes

- **Added**: `wiki/` — persistent LLM-maintained knowledge base
- **Added**: `raw/` — immutable data storage (screenshots, OHLCV, Pine exports)
- **Modified**: `CLAUDE.md` — added Wiki Maintenance Protocol section
- **Modified**: `README.md` — updated for self-learning edition
- **Modified**: `.gitignore` — added security rules for wiki raw data

No upstream source code (`src/`, `scripts/`, `tests/`) was modified.

---

## Attributions

- **Upstream project**: [tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) by [@tradesdontlie](https://github.com/tradesdontlie) — MIT License
- **Wiki pattern**: Inspired by [Andrej Karpathy's LLM Wiki concept](https://x.com/karpathy)
- **Fork maintainer**: [@alexandremaciel-ai](https://github.com/alexandremaciel-ai)

This project is not affiliated with, endorsed by, or associated with:
- **TradingView Inc.** — TradingView is a trademark of TradingView Inc.
- **Anthropic** — Claude and Claude Code are trademarks of Anthropic, PBC.

## Disclaimer

This project is provided **for personal, educational, and research purposes only**.

**How this tool works:** This tool uses the Chrome DevTools Protocol (CDP), a standard debugging interface built into all Chromium-based applications by Google. It does not reverse engineer any proprietary TradingView protocol, connect to TradingView's servers, or bypass any access controls. The debug port must be explicitly enabled by the user via a standard Chromium command-line flag (`--remote-debugging-port=9222`).

By using this software, you acknowledge and agree that:

1. **You are solely responsible** for ensuring your use of this tool complies with [TradingView's Terms of Use](https://www.tradingview.com/policies/) and all applicable laws.
2. TradingView's Terms of Use **restrict automated data collection, scraping, and non-display usage** of their platform and data. This tool uses Chrome DevTools Protocol to programmatically interact with the TradingView Desktop app, which may conflict with those terms.
3. **You assume all risk** associated with using this tool. The authors are not responsible for any account bans, suspensions, legal actions, or other consequences resulting from its use.
4. This tool **must not be used** for, including but not limited to:
   - Redistributing, reselling, or commercially exploiting TradingView's market data
   - Circumventing TradingView's access controls or subscription restrictions
   - Performing automated trading or algorithmic decision-making using extracted data
   - Violating the intellectual property rights of Pine Script indicator authors
   - Connecting to TradingView's servers or infrastructure (all access is via the locally running Desktop app)
5. The streaming functionality monitors your locally running TradingView Desktop instance only. It does not connect to TradingView's servers or extract data from TradingView's infrastructure.
6. Market data accessed through this tool remains subject to exchange and data provider licensing terms. **Do not redistribute, store, or commercially exploit any data obtained through this tool.**
7. This tool accesses internal, undocumented TradingView application interfaces that may change or break at any time without notice.
8. **The wiki system** stores analysis notes and observations locally in markdown files. It does not store raw market data. Screenshots in `raw/screenshots/` are for personal reference only and must not be redistributed.

**Use at your own risk.** If you are unsure whether your intended use complies with TradingView's terms, do not use this tool.

## License

MIT — see [LICENSE](LICENSE) for details.

The MIT license applies to the source code of this project only. It does not grant any rights to TradingView's software, data, trademarks, or intellectual property.

Original upstream code: Copyright (c) 2026 [@tradesdontlie](https://github.com/tradesdontlie).
Wiki system additions: Copyright (c) 2026 [@alexandremaciel-ai](https://github.com/alexandremaciel-ai).
