# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Email:** Open a private security advisory via [GitHub Security Advisories](https://github.com/tradesdontlie/tradingview-mcp/security/advisories/new).

**Do not** open a public issue for security vulnerabilities.

## Scope

This project connects to a locally running TradingView Desktop instance via Chrome DevTools Protocol on `localhost:9222`. Security concerns in scope include:

- Code injection via crafted tool inputs
- Unintended data exposure through tool outputs
- Credential or session token leakage
- Vulnerabilities in the MCP server or CLI that could be exploited locally

## Out of Scope

- TradingView's own security (report to TradingView directly)
- Chrome DevTools Protocol security (report to Google/Chromium)
- Claude Code or MCP SDK security (report to Anthropic)

## Best Practices for Users

- Only run TradingView with `--remote-debugging-port=9222` on localhost
- Do not expose port 9222 to your network or the internet
- Do not pipe `tv stream` output to external services without reviewing the data
- Keep your TradingView Desktop and Node.js installations up to date

## Data Model — Shared vs Local (privacy)

This repo is **public** and intentionally separates two kinds of content. Personal
analysis data must never be committed; see `.gitignore` for the enforced rules.

**Tracked (shared framework — safe to publish):**
- Source code (`src/`, `scripts/`, `tests/`), CLI, MCP server
- Reference knowledge: `wiki/concepts/`, `wiki/strategies/` (qualitative — **no real
  performance numbers**), `wiki/overview.md`, `wiki/dashboard.md`
- Templates and seeds: `wiki/**/_template.md`, `wiki/brain/_templates/`, and the
  `*.initial.md` seeds (`index`, `log`, `setups/index`, `watchlist`, `library`)

**Local-only (gitignored — your personal data, never published):**
- `wiki/brain/*` (insights, mistakes, predictions-log, indicators, patterns, metrics)
- `wiki/sessions/`, `wiki/analysis/`, `wiki/lint/`, `wiki/assets/`, `wiki/research/`, `wiki/outputs/`
- `wiki/setups/*` (incl. live `index.md`), `wiki/watchlist.md`, `wiki/library.md`,
  `wiki/log.md`, `wiki/index.md`, `wiki/search-index.md`
- `raw/` captures (screenshots, OHLCV, clippings, pine exports), `.env`, secrets

On first use, `scripts/setup.sh` copies each `*.initial.md` seed into its live
local file, so a fresh clone bootstraps an empty personal wiki/brain without
carrying anyone else's data. Real performance metrics live only in the gitignored
`brain/metrics.md` and `wiki/setups/index.md` — never in tracked strategy files.
