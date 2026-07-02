#!/usr/bin/env python3
"""Self-check do parser de frontmatter das notas atômicas de previsão.
Roda offline (sem filesystem do brain): python3 scripts/tools/test_metrics_frontmatter.py"""

from metrics_engine import read_frontmatter, record_from_frontmatter, criteria_stats

SAMPLE = '''---
type: prediction
symbol: SOL
tf: 4H
date: 2026-07-01
side: long
kind: swing
setup: asian-session-liquidity-sweep-long
playbook: 2
confluence: 6
confidence: média
regime: misto
price: 76.72
entry: 74.5
sl: 71.0
tps: [76.7, 79.2]
rr_plan: 2.1
rr_real: null
criteria: ["ema200+", "macd+", "rsi+", "-stochrsi"]
status: win
postclose: null
tags: [side/long, setup/liquidity-sweep]
---

## Tese
Sweep de EQH asiático + reclaim. Corpo em prosa livre.
'''


def main():
    fm, body = read_frontmatter(SAMPLE)
    assert fm['symbol'] == 'SOL', fm.get('symbol')
    assert fm['tf'] == '4H'
    assert fm['criteria'] == ['ema200+', 'macd+', 'rsi+', '-stochrsi'], fm['criteria']
    assert fm['rr_real'] is None
    assert '## Tese' in body

    rec = record_from_frontmatter(fm, body)
    assert rec is not None
    assert rec['status'] == 'win'
    assert rec['side'] == 'long'
    assert rec['type'] == 'swing'
    assert rec['confidence'] == 'média'
    assert rec['regime'] == 'misto'
    assert rec['playbook'] == 'Playbook 2'
    assert rec['setup'] == 'asian-session-liquidity-sweep-long'
    assert rec['rr_plan'] == 2.1
    # criteria: 3 sinais '+' e 1 '-'
    assert ('ema200', '+') in rec['criteria'], rec['criteria']
    assert ('stochrsi', '-') in rec['criteria'], rec['criteria']

    # win credita os '+' como acerto; o '-' (stochrsi) é ignorado por criteria_stats
    stats = criteria_stats([rec])
    assert stats['ema200']['acertos'] == 1
    assert stats['macd']['acertos'] == 1
    assert 'stochrsi' not in stats, stats

    # arquivo sem status válido → ignorado (não vira record)
    bad, _ = read_frontmatter('---\ndate: 2026-01-01\nstatus: rascunho\n---\n')
    assert record_from_frontmatter(bad, '') is None

    print('OK — frontmatter parser + record + criteria_stats')


if __name__ == '__main__':
    main()
