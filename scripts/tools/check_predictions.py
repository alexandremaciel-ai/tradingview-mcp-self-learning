#!/usr/bin/env python3
"""
check_predictions.py — Gate determinístico do loop de previsões.

O AUTO-PILOT precisa saber, no início de TODA análise (passo 2c do `brain-read`),
QUAIS previsões `⏳ aberta` já deveriam ter sido graduadas (TP vs SL) e nunca foram.
Essa é uma pergunta de FILESYSTEM, não de memória do LLM — então este script a
responde de forma determinística, espelhando o `check_briefing.py`.

Uma previsão "precisa graduar" quando está `⏳ aberta` E:
  - a linha Status contém "Supersedida" (resolvida-por-substituição mas nunca
    convertida em win/loss — o vazamento que deixa criteria_stats em N=0), OU
  - a data do header tem >= 2 dias (vencida por idade, sem update).

Responsabilidade ÚNICA (read-only): listar o worklist e refletir o estado no exit
code. NÃO gradua (grading exige OHLCV/MCP, feito pela skill `prediction-feedback`)
nem grava nada. NÃO toca raw/.

Uso:
  python scripts/tools/check_predictions.py              # backlog inteiro
  python scripts/tools/check_predictions.py --symbol BTC # só previsões do símbolo

Saída (stdout):
  loop: SUJO | pendentes: 12 | supersedidas: 11 | vencidas: 1
  - 2026-06-27 | BTC+ETH 4H — SHORT continuação... | supersedida
  - 2026-06-25 | BTC CYCLE — BEAR... | vencida (3d)
  ...
  loop: LIMPO | pendentes: 0

Exit code: 0 = LIMPO · 1 = SUJO (há pendências) · 2 = erro de uso.
Sem dependências externas (stdlib: importa os parsers de metrics_engine).
"""

import sys
from datetime import datetime, timedelta, timezone

from metrics_engine import HEADER_RE, PRED_FILE, detect_status

BRT = timezone(timedelta(hours=-3))  # America/Sao_Paulo, sem DST desde 2019
OVERDUE_DAYS = 2  # >= 48h sem update => vencida


def parse_args(argv):
    """Retorna o filtro de símbolo (str maiúscula) ou None."""
    if '--symbol' in argv:
        i = argv.index('--symbol')
        try:
            return argv[i + 1].upper()
        except IndexError:
            print('uso: check_predictions.py [--symbol BTC]', file=sys.stderr)
            sys.exit(2)
    return None


def status_line(block):
    """Texto bruto da linha '- **Status:** ...' (para detectar 'Supersedida')."""
    for line in block.splitlines():
        if line.startswith('- **Status:**'):
            return line
    return ''


def pending_predictions(symbol=None):
    """Lista (date_str, title, motivo) das ⏳ que precisam graduar."""
    try:
        with open(PRED_FILE, encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []

    headers = []
    for i, line in enumerate(lines):
        hm = HEADER_RE.match(line.rstrip('\n'))
        if hm:
            headers.append((i, hm.group(1), hm.group(2).strip()))

    today = datetime.now(BRT).date()
    out = []
    for idx, (start, date_str, title) in enumerate(headers):
        end = headers[idx + 1][0] if idx + 1 < len(headers) else len(lines)
        block = ''.join(lines[start:end])
        if detect_status(block) != 'open':
            continue
        if symbol and symbol not in title.upper():
            continue
        sline = status_line(block)
        if 'Supersedida' in sline or 'supersedida' in sline:
            out.append((date_str, title, 'supersedida'))
            continue
        try:
            age = (today - datetime.strptime(date_str, '%Y-%m-%d').date()).days
        except ValueError:
            continue
        if age >= OVERDUE_DAYS:
            out.append((date_str, title, f'vencida ({age}d)'))
    return out


def main():
    symbol = parse_args(sys.argv[1:])
    pend = pending_predictions(symbol)
    if not pend:
        print('loop: LIMPO | pendentes: 0')
        sys.exit(0)

    sup = sum(1 for _, _, m in pend if m == 'supersedida')
    venc = len(pend) - sup
    print(f'loop: SUJO | pendentes: {len(pend)} | supersedidas: {sup} | vencidas: {venc}')
    for date_str, title, motivo in pend:
        short = title if len(title) <= 70 else title[:67] + '...'
        print(f'- {date_str} | {short} | {motivo}')
    sys.exit(1)


if __name__ == '__main__':
    main()
