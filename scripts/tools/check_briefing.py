#!/usr/bin/env python3
"""
check_briefing.py — Gate determinístico do briefing macro do dia.

O AUTO-PILOT precisa saber, no início de TODA análise (passo 2b do `brain-read`),
se o briefing macro de HOJE já existe. Esta é uma pergunta de FILESYSTEM, não de
memória do LLM — então este script a responde de forma determinística.

Responsabilidade ÚNICA (read-only): reportar o estado do briefing do dia.
  - Calcula a data de hoje em BRT (GMT-3).
  - Verifica wiki/briefings/{AAAA-MM-DD}.md: existe? idade (mtime)? horizonte?
  - Imprime UMA linha de status parseável + sai com código que reflete o estado.

Este script NÃO roda o briefing (isso é web-search/LLM, feito pela skill
`btc-macro-briefing`). Quem decide invocar a skill é o `brain-read`, com base
neste status. NÃO toca em raw/ (imutável) nem grava nada.

Uso:
  python scripts/tools/check_briefing.py            # estado do briefing de hoje
  python scripts/tools/check_briefing.py --date 2026-06-17   # estado de uma data específica

Saída (stdout, 1 linha):
  briefing: PRESENTE | data: 2026-06-17 | idade: 2h13 | horizonte: semana | arquivo: wiki/briefings/2026-06-17.md
  briefing: AUSENTE  | data: 2026-06-17 | arquivo esperado: wiki/briefings/2026-06-17.md

Exit code: 0 = PRESENTE · 1 = AUSENTE · 2 = erro de uso.
Sem dependências externas (stdlib: os, sys, datetime).
"""

import os
import sys
from datetime import datetime, timedelta, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BRIEFINGS_DIR = os.path.join(BASE_DIR, 'wiki', 'briefings')
BRT = timezone(timedelta(hours=-3))  # America/Sao_Paulo, sem DST desde 2019


def parse_args(argv):
    """Retorna a data-alvo (str AAAA-MM-DD). Default: hoje em BRT."""
    if '--date' in argv:
        i = argv.index('--date')
        try:
            val = argv[i + 1]
            datetime.strptime(val, '%Y-%m-%d')  # valida
            return val
        except (IndexError, ValueError):
            print('uso: check_briefing.py [--date AAAA-MM-DD]', file=sys.stderr)
            sys.exit(2)
    return datetime.now(BRT).strftime('%Y-%m-%d')


def read_horizon(path):
    """Extrai o horizonte (hoje|semana) do header do briefing. '?' se ausente."""
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                low = line.lower()
                if 'horizonte' in low:
                    if 'semana' in low:
                        return 'semana'
                    if 'hoje' in low:
                        return 'hoje'
        return '?'
    except OSError:
        return '?'


def humanize_age(seconds):
    """Idade legível: '2h13', '45min', '1d3h'."""
    s = int(seconds)
    days, rem = divmod(s, 86400)
    hours, rem = divmod(rem, 3600)
    mins = rem // 60
    if days:
        return f'{days}d{hours}h'
    if hours:
        return f'{hours}h{mins:02d}'
    return f'{mins}min'


def main():
    date = parse_args(sys.argv[1:])
    rel = os.path.join('wiki', 'briefings', f'{date}.md')
    path = os.path.join(BRIEFINGS_DIR, f'{date}.md')

    if not os.path.isfile(path):
        print(f'briefing: AUSENTE  | data: {date} | arquivo esperado: {rel}')
        sys.exit(1)

    age_s = datetime.now(timezone.utc).timestamp() - os.path.getmtime(path)
    horizon = read_horizon(path)
    print(f'briefing: PRESENTE | data: {date} | idade: {humanize_age(age_s)} '
          f'| horizonte: {horizon} | arquivo: {rel}')
    sys.exit(0)


if __name__ == '__main__':
    main()
