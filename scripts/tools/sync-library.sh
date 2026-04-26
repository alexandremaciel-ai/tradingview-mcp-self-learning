#!/bin/bash
# sync-library.sh — Regenerates wiki/library.md with all clippings from raw/clippings/
# This ensures every clipping is linked in the Obsidian Graph View automatically.
# Can be run manually, via git pre-commit hook, or by the LLM during COMPILE/LINT.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
CLIPPINGS_DIR="$ROOT_DIR/raw/clippings"
LIBRARY_FILE="$ROOT_DIR/wiki/library.md"

if [ ! -d "$CLIPPINGS_DIR" ]; then
  echo "⚠️  Clippings directory not found: $CLIPPINGS_DIR"
  exit 0
fi

# Count clippings
COUNT=$(find "$CLIPPINGS_DIR" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')

# Write header
cat > "$LIBRARY_FILE" << 'HEADER'
# Biblioteca de Recortes (Clippings) Mestre

> Auto-gerado por `scripts/tools/sync-library.sh`.
> **Não edite manualmente** — este arquivo é regenerado automaticamente.

HEADER

echo "- **Total:** $COUNT artigos indexados" >> "$LIBRARY_FILE"
echo "" >> "$LIBRARY_FILE"
echo "## Índice Completo" >> "$LIBRARY_FILE"
echo "" >> "$LIBRARY_FILE"

# List all clippings as wikilinks, sorted
find "$CLIPPINGS_DIR" -maxdepth 1 -name '*.md' -exec basename {} .md \; | sort | while read -r clip; do
  echo "- [[$clip]]" >> "$LIBRARY_FILE"
done

echo "" >> "$LIBRARY_FILE"
echo "## Backlinks" >> "$LIBRARY_FILE"
echo "- [[index]]" >> "$LIBRARY_FILE"

echo "✅ wiki/library.md synced — $COUNT clippings indexed."
