#!/usr/bin/env python3
"""Regenera GEMINI.md e AGENTS.md a partir do CLAUDE.md (fonte única).

O CLAUDE.md é o router. GEMINI.md/AGENTS.md são idênticos exceto:
  - o título (Claude → Gemini → Codex);
  - o primeiro ator do diagrama de arquitetura;
  - uma linha-adaptador no topo dizendo como carregar skills por path
    (Claude Code usa o Skill tool; os demais leem skills/<nome>/SKILL.md).

Uso:  python3 scripts/tools/sync_agent_md.py
Rode SEMPRE que editar o CLAUDE.md (regra de espelhamento).
"""
from __future__ import annotations

import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parents[2]
SOURCE = BASE / "CLAUDE.md"

# nome do agente, ator do diagrama, arquivo de saída
TARGETS = [
    ("Gemini", "Gemini CLI", "GEMINI.md"),
    ("Codex", "Codex", "AGENTS.md"),
]

ADAPTER = (
    "> **Skills (não-Claude):** onde este documento diz “invocar/invoque a skill `X`” ou "
    "cita uma skill na tabela de dispatch, **leia e siga `skills/X/SKILL.md`** (o conteúdo é o "
    "mesmo; só a forma de carregar muda).\n\n"
)


def render(agent: str, actor: str, body: str) -> str:
    out = body
    # 1) título
    out = out.replace(
        "# TradingView MCP — Claude Instructions",
        f"# TradingView MCP — {agent} Instructions",
        1,
    )
    # 2) ator do diagrama
    out = out.replace("Claude Code ←→ MCP Server", f"{actor} ←→ MCP Server", 1)
    # 3) linha-adaptador logo após o blockquote "Arquitetura skill-first"
    anchor = "não reimplemente.\n\n"
    if anchor in out:
        out = out.replace(anchor, "não reimplemente.\n\n" + ADAPTER, 1)
    return out


def main() -> int:
    if not SOURCE.exists():
        print(f"ERRO: {SOURCE} não encontrado", file=sys.stderr)
        return 1
    body = SOURCE.read_text(encoding="utf-8")
    for agent, actor, fname in TARGETS:
        (BASE / fname).write_text(render(agent, actor, body), encoding="utf-8")
        print(f"  {fname:12s} regenerado ({agent})")
    print("Espelhamento concluído a partir de CLAUDE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
