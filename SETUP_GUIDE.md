# Setup Guide for Claude Code

This file is a step-by-step guide for Claude Code (or any LLM agent) to install and configure the TradingView MCP Self-Learning server. If a user asks you to install or set up this project, follow these steps.

## Automatic Setup (Preferred)

If the user is already inside the project directory, the `.mcp.json` at the root should auto-configure the MCP server. Just verify:

1. Check that `src/server.js` exists in the current directory
2. Run `tv_health_check` to verify the connection
3. If it fails, TradingView needs to launch with CDP — use `tv_launch`

## One-Line Setup Script

If the user wants a global install:

```bash
./scripts/setup.sh
```

This handles: npm install, `claude mcp add --scope user`, and optionally launches TradingView.

## Manual Setup

### Step 1: Install Dependencies

```bash
npm install
```

### Step 2: Register MCP Server

**Option A — Via Claude Code CLI (recommended):**
```bash
claude mcp add --scope user tradingview -- node "<INSTALL_PATH>/src/server.js"
```

**Option B — Via config file:**
Add the server to `~/.claude/.mcp.json` (global) or `.mcp.json` (project-level):

```json
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["<INSTALL_PATH>/src/server.js"]
    }
  }
}
```

Replace `<INSTALL_PATH>` with the actual path (e.g., `/Users/username/tradingview-mcp-self-learning`).

If the config file already exists and has other servers, merge the `tradingview` entry into the existing `mcpServers` object. Do not overwrite other servers.

### Step 3: Launch TradingView Desktop

TradingView Desktop must be running with Chrome DevTools Protocol enabled.

**Auto-detect and launch (recommended):**
After the MCP server is connected, use the `tv_launch` tool — it auto-detects TradingView on Mac, Windows, and Linux.

**Manual launch by platform:**

Mac:
```bash
/Applications/TradingView.app/Contents/MacOS/TradingView --remote-debugging-port=9222
```

Windows:
```bash
%LOCALAPPDATA%\TradingView\TradingView.exe --remote-debugging-port=9222
```

Linux:
```bash
/opt/TradingView/tradingview --remote-debugging-port=9222
```

### Step 4: Restart Claude Code

The MCP server only loads when Claude Code starts. After adding the config:

1. Exit Claude Code (Ctrl+C)
2. Relaunch Claude Code
3. The tradingview MCP server should connect automatically

> **Note:** If using the project `.mcp.json` (already included in this repo), no restart is needed — just open Claude Code inside the project directory.

### Step 5: Verify Connection

Use the `tv_health_check` tool. Expected response:

```json
{
  "success": true,
  "cdp_connected": true,
  "chart_symbol": "...",
  "api_available": true
}
```

If `cdp_connected: false`, TradingView is not running with `--remote-debugging-port=9222`.

### Step 6: Install CLI (Optional)

To use the `tv` CLI command globally:

```bash
npm link
```

Then `tv status`, `tv quote`, `tv pine compile`, etc. work from anywhere.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `cdp_connected: false` | Launch TradingView with `--remote-debugging-port=9222` |
| `ECONNREFUSED` | TradingView isn't running or port 9222 is blocked |
| MCP server not showing in Claude Code | Check `~/.claude/.mcp.json` syntax, restart Claude Code |
| `tv` command not found | Run `npm link` from the project directory |
| Tools return stale data | TradingView may still be loading — wait a few seconds |
| Pine Editor tools fail | Open the Pine Editor panel first (`ui_open_panel pine-editor open`) |

## What to Read Next

- `CLAUDE.md` — Decision tree for which tool to use when (auto-loaded by Claude Code)
- `README.md` — Full tool reference and wiki documentation
- `wiki/index.md` — The self-learning wiki index

---

## Obsidian Web Clipper Configuration

To fully leverage the LLM compilation capabilities, you should use the [Obsidian Web Clipper](https://obsidian.md/clipper) extension to ingest external articles into the `raw/clippings/` folder.

1. Install the official Obsidian Web Clipper extension in your browser.
2. In the clipper settings, choose the Vault corresponding to this repository.
3. In **Behavior**, set the "Folder location" to: `raw/clippings`
4. In the **Properties** section, add (by clicking `+ Add property`):
   - Property: `source_url` | Value: `{{url}}`
   - Property: `date_captured` | Value: `{{date}}`
5. In the **Note content** section, paste exactly this text (removing any `---` block):

```markdown
# Clipping: {{title}}

## Key Takeaways
- 

## Concepts Mentioned
- 

## Original Content
{{content}}
```

**Workflow:** After clipping an article, go to Claude Code and say: *"Compile recent clippings in the wiki"* to have the LLM automatically extract insights, connect concepts, and create backlinks for your trading wiki!
