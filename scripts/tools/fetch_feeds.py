#!/usr/bin/env python3
"""
fetch_feeds.py — Ingestão de dados externos que o TradingView/CDP não entrega.

A Fase 8 do checklist EXIGE funding rate / OI / long-short ratio, e o CYCLE exige
sentimento on-chain. Mas o MCP só lê o que está visível no chart. Este script puxa
esses dados de APIs gratuitas e grava um cache que o brain lê na análise:

  - Coinalyze (free, requer COINALYZE_API_KEY): funding rate, open interest,
    predicted funding e (best-effort) long/short ratio para BTC e ETH perps.
  - alternative.me (sem key): Fear & Greed Index.

Saída:
  - raw/feeds/AAAA-MM-DD-HHMM.json   (snapshot bruto, imutável)
  - raw/feeds/latest.md              (digest legível que o AUTO-PILOT lê na Fase 8)

DEGRADAÇÃO GRACIOSA (regra de ouro): SEM key, SEM rede ou com erro de API, o script
NUNCA quebra — escreve `latest.md` com `status: indisponível`. A Fase 9 do checklist
então aplica a penalidade `dados-parciais` (−1 no Confluence Score) em vez de estimar.

Uso:
  COINALYZE_API_KEY=xxxx python scripts/tools/fetch_feeds.py
  python scripts/tools/fetch_feeds.py              # sem key → só Fear&Greed + status

Config opcional por env:
  COINALYZE_API_KEY   — chave grátis (https://coinalyze.net/account/api)
  COINALYZE_SYMBOLS   — símbolos perp (default "BTCUSDT_PERP.A,ETHUSDT_PERP.A")

Sem dependências externas (stdlib: urllib, json).
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FEEDS_DIR = os.path.join(BASE_DIR, 'raw', 'feeds')
LATEST = os.path.join(FEEDS_DIR, 'latest.md')

COINALYZE_BASE = 'https://api.coinalyze.net/v1'
FNG_URL = 'https://api.alternative.me/fng/?limit=1'
TIMEOUT = 12

API_KEY = os.environ.get('COINALYZE_API_KEY', '').strip()
SYMBOLS = os.environ.get('COINALYZE_SYMBOLS', 'BTCUSDT_PERP.A,ETHUSDT_PERP.A').strip()


def http_get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode('utf-8'))


def fetch_coinalyze():
    """Funding/OI/predicted/LSR da Coinalyze. Retorna dict com 'status' sempre presente."""
    if not API_KEY:
        return {'status': 'sem API key (COINALYZE_API_KEY não definida)'}
    headers = {'api_key': API_KEY}
    out = {'status': 'ok', 'symbols': SYMBOLS}
    try:
        out['funding_rate'] = http_get_json(
            f'{COINALYZE_BASE}/funding-rate?symbols={SYMBOLS}', headers)
        out['open_interest'] = http_get_json(
            f'{COINALYZE_BASE}/open-interest?symbols={SYMBOLS}&convert_to_usd=true', headers)
        out['predicted_funding'] = http_get_json(
            f'{COINALYZE_BASE}/predicted-funding-rate?symbols={SYMBOLS}', headers)
    except urllib.error.HTTPError as e:
        return {'status': f'erro HTTP {e.code} (verifique a key/símbolos)'}
    except (urllib.error.URLError, TimeoutError) as e:
        return {'status': f'sem rede ({e})'}
    except (ValueError, KeyError) as e:
        return {'status': f'resposta inesperada ({e})'}
    return out


def fetch_fear_greed():
    """Fear & Greed Index (alternative.me, sem key)."""
    try:
        data = http_get_json(FNG_URL)
        item = data['data'][0]
        return {'status': 'ok', 'value': int(item['value']),
                'classification': item.get('value_classification', '—')}
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            ValueError, KeyError, IndexError) as e:
        return {'status': f'indisponível ({e})'}


def _by_symbol(arr, field):
    """Extrai {symbol: valor} de uma resposta array da Coinalyze, tolerante a formatos."""
    out = {}
    if not isinstance(arr, list):
        return out
    for it in arr:
        if isinstance(it, dict) and 'symbol' in it and field in it:
            out[it['symbol']] = it[field]
    return out


def build_digest(now, coinalyze, fng):
    lines = []
    lines.append('# Feeds Externos — Cache')
    lines.append('')
    lines.append(f'> Gerado por `scripts/tools/fetch_feeds.py` em {now.strftime("%Y-%m-%d %H:%M UTC")}.')
    lines.append('> Lido pelo AUTO-PILOT na **Fase 8**. Se este arquivo estiver ausente, com')
    lines.append('> `status: indisponível` ou desatualizado → aplicar penalidade `dados-parciais` (Fase 9).')
    lines.append('')
    lines.append(f'- **Timestamp:** {now.isoformat()}')
    lines.append(f'- **Coinalyze:** {coinalyze.get("status")}')
    lines.append(f'- **Fear & Greed:** {fng.get("status")}')
    lines.append('')

    # Fear & Greed
    lines.append('## Sentimento')
    lines.append('')
    if fng.get('status') == 'ok':
        v = fng['value']
        leitura = 'medo extremo' if v < 25 else 'medo' if v < 45 else \
                  'neutro' if v < 55 else 'ganância' if v < 75 else 'ganância extrema'
        lines.append('| Métrica | Valor | Leitura |')
        lines.append('|---|---|---|')
        lines.append(f'| Fear & Greed | {v} | {fng["classification"]} ({leitura}) |')
    else:
        lines.append(f'_Fear & Greed indisponível: {fng.get("status")}_')
    lines.append('')

    # Derivativos
    lines.append('## Derivativos (Coinalyze)')
    lines.append('')
    if coinalyze.get('status') == 'ok':
        fr = _by_symbol(coinalyze.get('funding_rate'), 'value')
        oi = _by_symbol(coinalyze.get('open_interest'), 'value')
        pf = _by_symbol(coinalyze.get('predicted_funding'), 'value')
        syms = sorted(set(fr) | set(oi) | set(pf))
        if syms:
            lines.append('| Símbolo | Funding | Predicted | Open Interest (USD) |')
            lines.append('|---|---|---|---|')
            for s in syms:
                lines.append(f'| {s} | {fr.get(s, "—")} | {pf.get(s, "—")} | {oi.get(s, "—")} |')
            lines.append('')
            lines.append('> Funding muito positivo + OI alto = mercado esticado em long (risco de long squeeze).')
            lines.append('> Funding negativo + OI subindo = pressão short (combustível para short squeeze).')
        else:
            lines.append('_Sem dados parseáveis — revisar COINALYZE_SYMBOLS._')
    else:
        lines.append(f'_Derivativos indisponíveis: {coinalyze.get("status")}_')
        lines.append('')
        lines.append('⚠️ **status: indisponível** — a Fase 9 deve aplicar `dados-parciais` (−1 no score).')
    lines.append('')
    return '\n'.join(lines) + '\n'


def main():
    dry_run = '--dry-run' in sys.argv[1:]
    now = datetime.now(timezone.utc)

    coinalyze = fetch_coinalyze()
    fng = fetch_fear_greed()
    digest = build_digest(now, coinalyze, fng)

    available = coinalyze.get('status') == 'ok' or fng.get('status') == 'ok'

    if dry_run:
        print(digest)
        print('--- [DRY-RUN] nada gravado ---')
        return

    os.makedirs(FEEDS_DIR, exist_ok=True)
    snapshot = {'timestamp': now.isoformat(), 'coinalyze': coinalyze, 'fear_greed': fng}
    snap_path = os.path.join(FEEDS_DIR, now.strftime('%Y-%m-%d-%H%M') + '.json')
    with open(snap_path, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)
    with open(LATEST, 'w', encoding='utf-8') as f:
        f.write(digest)

    print('Feeds atualizados:')
    print(f'  Coinalyze:    {coinalyze.get("status")}')
    print(f'  Fear & Greed: {fng.get("status")}')
    print(f'  Snapshot:     {os.path.relpath(snap_path, BASE_DIR)}')
    print(f'  Digest:       {os.path.relpath(LATEST, BASE_DIR)}')
    if not available:
        print('  ⚠️ Tudo indisponível — brain deve aplicar penalidade dados-parciais.')


if __name__ == '__main__':
    main()
