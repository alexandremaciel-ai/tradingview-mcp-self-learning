#!/bin/bash
# ──────────────────────────────────────────────────────────────
# TradingView MCP Self-Learning — One-Line Installer
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/alexandremaciel-ai/tradingview-mcp-self-learning/main/scripts/setup.sh | bash
#
# Or after cloning:
#   ./scripts/setup.sh
#
# What this script does:
#   1. Clones the repo (if not already cloned)
#   2. Installs npm dependencies
#   3. Registers the MCP server in Claude Code (via `claude mcp add`)
#   4. Optionally launches TradingView with CDP debug port
#   5. Prints verification instructions
# ──────────────────────────────────────────────────────────────

set -euo pipefail

# ── Colors ───────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
DIM='\033[2m'
RESET='\033[0m'

# ── Config ───────────────────────────────────────────────────
REPO_URL="https://github.com/alexandremaciel-ai/tradingview-mcp-self-learning.git"
DEFAULT_INSTALL_DIR="$HOME/.tradingview-mcp-self-learning"
MCP_SERVER_NAME="tradingview"
CDP_PORT=9222

# ── Helpers ──────────────────────────────────────────────────
info()    { echo -e "${BLUE}ℹ${RESET}  $1"; }
success() { echo -e "${GREEN}✔${RESET}  $1"; }
warn()    { echo -e "${YELLOW}⚠${RESET}  $1"; }
error()   { echo -e "${RED}✖${RESET}  $1" >&2; }
step()    { echo -e "\n${CYAN}${BOLD}[$1/5]${RESET} ${BOLD}$2${RESET}"; }

# ── Banner ───────────────────────────────────────────────────
echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║  TradingView MCP — Self-Learning Edition                ║${RESET}"
echo -e "${BOLD}║  ${DIM}Installer v1.0${RESET}${BOLD}                                         ║${RESET}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
echo ""

# ── Detect OS ────────────────────────────────────────────────
OS="$(uname -s)"
case "$OS" in
  Darwin) PLATFORM="mac" ;;
  Linux)  PLATFORM="linux" ;;
  *)
    error "Unsupported OS: $OS"
    error "This installer supports macOS and Linux only."
    error "For Windows, see README.md for manual setup."
    exit 1
    ;;
esac
info "Detected platform: ${BOLD}$PLATFORM${RESET}"

# ── Detect install dir ───────────────────────────────────────
# If running from inside the repo (after clone), use current dir
INSTALL_DIR="$DEFAULT_INSTALL_DIR"
if [ -f "./src/server.js" ] && [ -f "./package.json" ]; then
  INSTALL_DIR="$(pwd)"
  info "Running from existing clone: ${BOLD}$INSTALL_DIR${RESET}"
fi

# ── Step 1: Prerequisites ───────────────────────────────────
step 1 "Checking prerequisites"

# Check Node.js
if ! command -v node &> /dev/null; then
  error "Node.js not found. Install Node.js 18+ from https://nodejs.org"
  exit 1
fi
NODE_VERSION=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
  error "Node.js $NODE_VERSION found but 18+ is required."
  exit 1
fi
success "Node.js $(node -v)"

# Check npm
if ! command -v npm &> /dev/null; then
  error "npm not found."
  exit 1
fi
success "npm $(npm -v)"

# Check git (only if we need to clone)
if [ "$INSTALL_DIR" = "$DEFAULT_INSTALL_DIR" ] && [ ! -d "$INSTALL_DIR" ]; then
  if ! command -v git &> /dev/null; then
    error "git not found. Install git to clone the repository."
    exit 1
  fi
  success "git $(git --version | awk '{print $3}')"
fi

# Check claude CLI
HAS_CLAUDE=false
if command -v claude &> /dev/null; then
  HAS_CLAUDE=true
  success "Claude Code CLI found"
else
  warn "Claude Code CLI not found — will skip MCP auto-registration"
  warn "You can register manually later or use the project .mcp.json"
fi

# ── Step 2: Clone & Install ─────────────────────────────────
step 2 "Setting up repository"

if [ ! -d "$INSTALL_DIR" ]; then
  info "Cloning to $INSTALL_DIR ..."
  git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
  success "Cloned successfully"
elif [ ! -f "$INSTALL_DIR/package.json" ]; then
  error "$INSTALL_DIR exists but doesn't look like the project."
  exit 1
else
  success "Repository already exists at $INSTALL_DIR"
fi

info "Installing dependencies..."
cd "$INSTALL_DIR"
npm install --silent 2>/dev/null
success "Dependencies installed"

# Initialize wiki working files from templates (gitignored, local only)
if [ -d "$INSTALL_DIR/wiki/brain/_templates" ]; then
  info "Initializing wiki brain..."
  for tmpl in "$INSTALL_DIR/wiki/brain/_templates/"*.md; do
    target="$INSTALL_DIR/wiki/brain/$(basename "$tmpl")"
    if [ ! -f "$target" ]; then
      cp "$tmpl" "$target"
    fi
  done
  # Copy initial index and log if not present
  [ ! -f "$INSTALL_DIR/wiki/index.md" ] && [ -f "$INSTALL_DIR/wiki/index.initial.md" ] && \
    cp "$INSTALL_DIR/wiki/index.initial.md" "$INSTALL_DIR/wiki/index.md"
  [ ! -f "$INSTALL_DIR/wiki/log.md" ] && [ -f "$INSTALL_DIR/wiki/log.initial.md" ] && \
    cp "$INSTALL_DIR/wiki/log.initial.md" "$INSTALL_DIR/wiki/log.md"
  success "Wiki brain initialized (local only — not tracked by git)"
fi

# ── Step 3: Register MCP Server ──────────────────────────────
step 3 "Registering MCP server in Claude Code"

SERVER_PATH="$INSTALL_DIR/src/server.js"

if [ "$HAS_CLAUDE" = true ]; then
  # Remove existing entry if present (idempotent)
  claude mcp remove "$MCP_SERVER_NAME" 2>/dev/null || true

  # Register with user scope (available in all projects)
  claude mcp add --scope user "$MCP_SERVER_NAME" -- node "$SERVER_PATH"
  success "MCP server registered globally: ${BOLD}$MCP_SERVER_NAME${RESET}"
  info "Server path: $SERVER_PATH"
else
  warn "Skipping MCP auto-registration (claude CLI not found)"
  echo ""
  info "Option 1 — Open Claude Code inside the project directory:"
  echo -e "  ${DIM}cd $INSTALL_DIR && claude${RESET}"
  echo -e "  ${DIM}(the .mcp.json in the project auto-configures the server)${RESET}"
  echo ""
  info "Option 2 — Register manually later:"
  echo -e "  ${DIM}claude mcp add --scope user $MCP_SERVER_NAME -- node $SERVER_PATH${RESET}"
  echo ""
  info "Option 3 — Add to ~/.claude/.mcp.json manually:"
  cat <<EOF
  {
    "mcpServers": {
      "tradingview": {
        "command": "node",
        "args": ["$SERVER_PATH"]
      }
    }
  }
EOF
fi

# ── Step 4: Launch TradingView ───────────────────────────────
step 4 "TradingView Desktop"

LAUNCH_TV=false

# Check if TradingView is already running with CDP
if curl -s "http://localhost:$CDP_PORT/json/version" > /dev/null 2>&1; then
  success "TradingView already running with CDP on port $CDP_PORT"
else
  echo ""
  echo -e "  TradingView Desktop needs to run with debug mode enabled."
  echo -e "  ${DIM}(--remote-debugging-port=$CDP_PORT)${RESET}"
  echo ""

  # Try to auto-detect and offer to launch
  if [ "$PLATFORM" = "mac" ] && [ -f "$INSTALL_DIR/scripts/launch_tv_debug_mac.sh" ]; then
    read -p "  Launch TradingView now? [Y/n] " -n 1 -r REPLY
    echo ""
    if [[ $REPLY =~ ^[Yy]?$ ]]; then
      LAUNCH_TV=true
    fi
  elif [ "$PLATFORM" = "linux" ] && [ -f "$INSTALL_DIR/scripts/launch_tv_debug_linux.sh" ]; then
    read -p "  Launch TradingView now? [Y/n] " -n 1 -r REPLY
    echo ""
    if [[ $REPLY =~ ^[Yy]?$ ]]; then
      LAUNCH_TV=true
    fi
  fi

  if [ "$LAUNCH_TV" = true ]; then
    info "Launching TradingView..."
    if [ "$PLATFORM" = "mac" ]; then
      bash "$INSTALL_DIR/scripts/launch_tv_debug_mac.sh" "$CDP_PORT"
    else
      bash "$INSTALL_DIR/scripts/launch_tv_debug_linux.sh" "$CDP_PORT"
    fi
  else
    warn "Skipped — launch TradingView manually before using MCP tools:"
    echo -e "  ${DIM}$INSTALL_DIR/scripts/launch_tv_debug_mac.sh${RESET}  (Mac)"
    echo -e "  ${DIM}$INSTALL_DIR/scripts/launch_tv_debug_linux.sh${RESET}  (Linux)"
    echo -e "  ${DIM}Or: /path/to/TradingView --remote-debugging-port=$CDP_PORT${RESET}"
  fi
fi

# ── Step 5: Summary ─────────────────────────────────────────
step 5 "Setup complete"

echo ""
echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}${BOLD}║  ✔ Installation complete!                               ║${RESET}"
echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════════════╝${RESET}"
echo ""
echo -e "  ${BOLD}Install path:${RESET}  $INSTALL_DIR"
if [ "$HAS_CLAUDE" = true ]; then
  echo -e "  ${BOLD}MCP server:${RESET}    registered as '${CYAN}$MCP_SERVER_NAME${RESET}' (user scope)"
fi
echo -e "  ${BOLD}Wiki:${RESET}          $INSTALL_DIR/wiki/"
echo ""
echo -e "  ${BOLD}Next steps:${RESET}"
echo -e "  1. Open Claude Code:  ${DIM}claude${RESET}"
echo -e "  2. Verify connection: ${DIM}\"Use tv_health_check to verify TradingView is connected\"${RESET}"
echo -e "  3. Start learning:    ${DIM}\"Analise o gráfico atual e registre na wiki\"${RESET}"
echo ""
echo -e "  ${DIM}Wiki:     $INSTALL_DIR/wiki/index.md${RESET}"
echo -e "  ${DIM}Docs:     $INSTALL_DIR/CLAUDE.md${RESET}"
echo -e "  ${DIM}CLI:      cd $INSTALL_DIR && npm link && tv status${RESET}"
echo ""
