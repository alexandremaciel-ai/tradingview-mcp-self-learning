#!/usr/bin/env python3
"""
fetch_onchain.py — Ingestão de métricas on-chain de CICLO que o chart não entrega.

A skill `btc-cycle` precisa de NUPL, Puell Multiple, Pi Cycle Top e Hash Ribbons
(peso 40% no score de fundo). Nenhum está nos layouts atuais e o MCP só lê o chart.
Este script puxa/computa esses dados de fontes gratuitas e grava um cache que o
CYCLE lê na análise.

FONTES (todas KEYLESS — confirmado contra a doc OpenAPI da BGeometrics):
  - bitcoin-data.com / BGeometrics  (base https://api.bitcoin-data.com/v1):
      endpoints `/<slug>/last` retornam o último valor SEM exigir API key. Métricas:
      NUPL, MVRV Z-Score (confirmação do chart), Puell Multiple, Realized Price,
      Reserve Risk. Resposta: {"d":"YYYY-MM-DD","unixTs":..., "<campoCamelCase>":valor}.
  - blockchain.com/charts  (sem key):
      * hash-rate     → Hash Ribbons (MA30 vs MA60 do hash rate)
      * market-price  → Pi Cycle Top (SMA 111 vs 2×SMA 350) — matemática de preço pura
      * miners-revenue → Puell proxy (fallback se a BGeometrics falhar)

API KEY OPCIONAL (BGEO_API_KEY no .env): NÃO é necessária para o valor `/last`. Serve só
para elevar limites/bulk no tier free (8 req/h, 15/dia). Quando presente é enviada no
header `x-api-key`. Sem ela, tudo aqui ainda funciona.

Saída:
  - raw/feeds/onchain-AAAA-MM-DD.json   (snapshot bruto, imutável)
  - raw/feeds/onchain-latest.md         (digest que o CYCLE lê no passo 5)

DEGRADAÇÃO GRACIOSA (regra de ouro): SEM rede ou erro de API, o script NUNCA quebra —
escreve o digest com `status: indisponível` na métrica afetada (não estima).

Uso:
  python3 scripts/tools/fetch_onchain.py            # carrega o .env do projeto
  python3 scripts/tools/fetch_onchain.py --dry-run  # imprime o digest, não grava

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
LATEST = os.path.join(FEEDS_DIR, 'onchain-latest.md')

BLOCKCHAIN_BASE = 'https://api.blockchain.info/charts'
BGEO_BASE = 'https://api.bitcoin-data.com/v1'
TIMEOUT = 20


def load_dotenv(path=None):
    """Carrega BASE_DIR/.env em os.environ (stdlib puro). Env real vence o .env."""
    path = path or os.path.join(BASE_DIR, '.env')
    if not os.path.isfile(path):
        return
    try:
        with open(path, encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, val = line.partition('=')
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = val
    except OSError:
        return


load_dotenv()

BGEO_API_KEY = os.environ.get('BGEO_API_KEY', '').strip()


def http_get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode('utf-8'))


# ---------------------------------------------------------------------------
# Helpers de série / médias (blockchain.com)
# ---------------------------------------------------------------------------

def _sma(values, length):
    """Média simples dos últimos `length` pontos. None se não houver dados suficientes."""
    if len(values) < length or length <= 0:
        return None
    window = values[-length:]
    return sum(window) / len(window)


def fetch_chart_series(chart):
    """Puxa uma série diária da blockchain.com/charts. Retorna lista de y (floats) ou None."""
    url = f'{BLOCKCHAIN_BASE}/{chart}?timespan=3years&sampled=false&format=json'
    try:
        data = http_get_json(url)
        pts = data.get('values') if isinstance(data, dict) else None
        if not isinstance(pts, list) or not pts:
            return None
        ys = [float(p['y']) for p in pts if isinstance(p, dict) and 'y' in p]
        return ys or None
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            ValueError, KeyError, TypeError):
        return None


# ---------------------------------------------------------------------------
# Métricas computadas (blockchain.com)
# ---------------------------------------------------------------------------

def compute_hash_ribbons():
    """MA30 vs MA60 do hash rate → estado de ciclo (capitulação / recuperação / normal)."""
    hr = fetch_chart_series('hash-rate')
    if not hr:
        return {'status': 'indisponível'}
    ma30, ma60 = _sma(hr, 30), _sma(hr, 60)
    if ma30 is None or ma60 is None:
        return {'status': 'dados insuficientes'}
    prev30, prev60 = _sma(hr[:-1], 30), _sma(hr[:-1], 60)
    if ma30 < ma60:
        state = 'capitulação de mineradores (MA30<MA60) — fundo histórico se reverter'
    elif prev30 is not None and prev60 is not None and prev30 <= prev60 and ma30 > ma60:
        state = 'RECUPERAÇÃO (cruz↑ recente = sinal de compra histórico)'
    else:
        state = 'normal/recuperado (MA30>MA60)'
    return {'status': 'ok', 'ma30': ma30, 'ma60': ma60, 'state': state,
            'spread_pct': (ma30 / ma60 - 1) * 100}


def compute_pi_cycle():
    """Pi Cycle Top: SMA111 vs 2×SMA350 do preço. Topo iminente quando 111 cruza↑ 2×350."""
    px = fetch_chart_series('market-price')
    if not px:
        return {'status': 'indisponível'}
    sma111 = _sma(px, 111)
    sma350 = _sma(px, 350)
    if sma111 is None or sma350 is None:
        return {'status': 'dados insuficientes'}
    sma350x2 = sma350 * 2
    dist = (sma111 / sma350x2 - 1) * 100
    if sma111 >= sma350x2:
        zona = '🔴 TOPO sinalizado (111DMA ≥ 2×350DMA)'
    elif dist > -10:
        zona = '🟠 aproximando do topo (<10% abaixo)'
    else:
        zona = '🟢 longe do topo'
    return {'status': 'ok', 'sma111': sma111, 'sma350x2': sma350x2,
            'dist_pct': dist, 'zona': zona}


def compute_puell_proxy():
    """Puell ≈ receita de mineradores de hoje / MA-365 (blockchain.com). Fallback da BGeometrics."""
    rev = fetch_chart_series('miners-revenue')
    if not rev:
        return None
    ma365 = _sma(rev, 365)
    if ma365 is None or ma365 == 0:
        return None
    return rev[-1] / ma365


# ---------------------------------------------------------------------------
# Métricas BGeometrics (api.bitcoin-data.com — KEYLESS para o valor /last)
# ---------------------------------------------------------------------------

# slug do endpoint → (rótulo, campo JSON camelCase na resposta)
BGEO_METRICS = {
    'nupl':           ('NUPL',           'nupl'),
    'mvrv-zscore':    ('MVRV Z-Score',   'mvrvZscore'),
    'puell-multiple': ('Puell Multiple', 'puellMultiple'),
    'realized-price': ('Realized Price', 'realizedPrice'),
    'reserve-risk':   ('Reserve Risk',   'reserveRisk'),
}


def fetch_bgeometrics():
    """Último valor de cada métrica via /v1/<slug>/last. KEYLESS; key (se houver) eleva limites."""
    headers = {'x-api-key': BGEO_API_KEY} if BGEO_API_KEY else {}
    out = {'status': 'ok', 'date': None, 'values': {}, 'keyed': bool(BGEO_API_KEY)}
    any_ok = False
    for slug, (label, field) in BGEO_METRICS.items():
        try:
            resp = http_get_json(f'{BGEO_BASE}/{slug}/last', headers)
            if isinstance(resp, list) and resp:
                resp = resp[-1]
            val = float(resp[field]) if isinstance(resp, dict) and field in resp else None
            out['values'][slug] = val
            if isinstance(resp, dict) and resp.get('d'):
                out['date'] = resp['d']
            if val is not None:
                any_ok = True
        except urllib.error.HTTPError as e:
            out['values'][slug] = f'erro HTTP {e.code}'
        except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError) as e:
            out['values'][slug] = f'indisponível ({type(e).__name__})'
    if not any_ok:
        out['status'] = 'indisponível'
    return out


def bgeo_zone(slug, v):
    """Classifica o valor BGeometrics na zona de ciclo (ref. btc-cycle-analysis.md)."""
    if not isinstance(v, (int, float)):
        return '—'
    if slug == 'nupl':
        return ('🟢🟢 capitulação (<0)' if v < 0 else '🟢 acumulação/esperança (0-0.25)' if v < 0.25
                else '🟡 otimismo (0.25-0.5)' if v < 0.5 else '🟠 crença/negação (0.5-0.75)'
                if v < 0.75 else '🔴 euforia/ganância (>0.75)')
    if slug == 'mvrv-zscore':
        return ('🟢🟢 FUNDO (<0)' if v < 0 else '🟢 acumulação (0-1)' if v < 1
                else '🟡 neutro (1-3)' if v < 3 else '🟠 bull maduro (3-7)' if v < 7
                else '🔴 TOPO (>7)')
    if slug == 'puell-multiple':
        return ('🟢🟢 FUNDO (<0.5)' if v < 0.5 else '🟢 acumulação (0.5-1)' if v < 1
                else '🟡 neutro (1-4)' if v < 4 else '🔴 TOPO (>4)')
    if slug == 'reserve-risk':
        return '🟢 atrativo p/ acumular (baixo)' if v < 0.002 else '🟡/🔴 conferir vs histórico'
    return '(ref. btc-cycle-analysis.md)'  # realized-price: comparar vs preço spot


# ---------------------------------------------------------------------------
# Digest
# ---------------------------------------------------------------------------

def build_digest(now, ribbons, pi, bgeo, puell_proxy):
    L = []
    L.append('# Feeds On-Chain (Ciclo) — Cache')
    L.append('')
    L.append(f'> Gerado por `scripts/tools/fetch_onchain.py` em {now.strftime("%Y-%m-%d %H:%M UTC")}.')
    L.append('> Lido pela skill `btc-cycle` (passo 5). Métrica `indisponível` → não pontua no')
    L.append('> Score de Fundo (não estimar). Refresh ~1×/dia (dado on-chain é diário).')
    L.append('')
    L.append(f'- **Timestamp:** {now.isoformat()}')
    L.append(f'- **BGeometrics (keyless):** {bgeo.get("status")}'
             + (f' · dado de {bgeo.get("date")}' if bgeo.get('date') else '')
             + (' · com API key' if bgeo.get('keyed') else ' · sem key (não necessária)'))
    L.append(f'- **blockchain.com (keyless):** Hash Ribbons {ribbons.get("status")} · Pi Cycle {pi.get("status")}')
    L.append('')

    L.append('## Métricas de Ciclo')
    L.append('')
    L.append('| Métrica | Valor | Zona / Estado | Fonte |')
    L.append('|---|---|---|---|')

    bvals = bgeo.get('values', {})

    # NUPL
    nupl = bvals.get('nupl')
    if isinstance(nupl, (int, float)):
        L.append(f'| NUPL | {nupl:.4f} | {bgeo_zone("nupl", nupl)} | BGeometrics |')
    else:
        L.append(f'| NUPL | {nupl if nupl is not None else "indisponível"} | — | BGeometrics |')

    # MVRV Z (confirmação do chart)
    mvrv = bvals.get('mvrv-zscore')
    if isinstance(mvrv, (int, float)):
        L.append(f'| MVRV Z-Score (confirma chart) | {mvrv:.4f} | {bgeo_zone("mvrv-zscore", mvrv)} | BGeometrics |')
    else:
        L.append(f'| MVRV Z-Score | {mvrv if mvrv is not None else "indisponível"} | — | BGeometrics |')

    # Puell — BGeometrics primário, blockchain.com proxy como fallback
    puell = bvals.get('puell-multiple')
    if isinstance(puell, (int, float)):
        L.append(f'| Puell Multiple | {puell:.4f} | {bgeo_zone("puell-multiple", puell)} | BGeometrics |')
    elif isinstance(puell_proxy, (int, float)):
        L.append(f'| Puell Multiple | {puell_proxy:.3f} | {bgeo_zone("puell-multiple", puell_proxy)} | blockchain.com (proxy, fallback) |')
    else:
        L.append('| Puell Multiple | indisponível | — | BGeometrics/blockchain.com |')

    # Pi Cycle (preço)
    if pi.get('status') == 'ok':
        L.append(f'| Pi Cycle Top | 111DMA ${pi["sma111"]:,.0f} vs 2×350DMA ${pi["sma350x2"]:,.0f} '
                 f'({pi["dist_pct"]:+.1f}%) | {pi["zona"]} | preço (blockchain.com) |')
    else:
        L.append(f'| Pi Cycle Top | {pi.get("status")} | — | preço |')

    # Hash Ribbons (hash rate)
    if ribbons.get('status') == 'ok':
        L.append(f'| Hash Ribbons | MA30/MA60 spread {ribbons["spread_pct"]:+.1f}% | '
                 f'{ribbons["state"]} | blockchain.com |')
    else:
        L.append(f'| Hash Ribbons | {ribbons.get("status")} | — | blockchain.com |')

    # Realized Price + Reserve Risk
    rp = bvals.get('realized-price')
    if isinstance(rp, (int, float)):
        L.append(f'| Realized Price | ${rp:,.0f} | preço<RP = capitulação / preço>RP = lucro | BGeometrics |')
    else:
        L.append(f'| Realized Price | {rp if rp is not None else "indisponível"} | — | BGeometrics |')
    rr = bvals.get('reserve-risk')
    if isinstance(rr, (int, float)):
        L.append(f'| Reserve Risk | {rr:.5f} | {bgeo_zone("reserve-risk", rr)} | BGeometrics |')
    else:
        L.append(f'| Reserve Risk | {rr if rr is not None else "indisponível"} | — | BGeometrics |')

    L.append('')
    L.append('> Limiares (ref. `wiki/concepts/btc-cycle-analysis.md`): Puell >4 topo / <0.5 fundo · '
             'Pi Cycle 111DMA≥2×350DMA = topo · Hash Ribbons MA30<MA60 = capitulação, cruz↑ = compra · '
             'NUPL >0.75 euforia / <0 capitulação · MVRV-Z >7 topo / <0 fundo.')
    L.append('> MVRV-Z primário vem do **chart** (layout Emas); a linha BGeometrics é confirmação cruzada.')
    L.append('')
    return '\n'.join(L) + '\n'


def main():
    dry_run = '--dry-run' in sys.argv[1:]
    now = datetime.now(timezone.utc)

    bgeo = fetch_bgeometrics()
    ribbons = compute_hash_ribbons()
    pi = compute_pi_cycle()
    # proxy só se a BGeometrics não trouxe o Puell
    puell_proxy = None
    if not isinstance(bgeo.get('values', {}).get('puell-multiple'), (int, float)):
        puell_proxy = compute_puell_proxy()

    digest = build_digest(now, ribbons, pi, bgeo, puell_proxy)

    if dry_run:
        print(digest)
        print('--- [DRY-RUN] nada gravado ---')
        return

    os.makedirs(FEEDS_DIR, exist_ok=True)
    snapshot = {'timestamp': now.isoformat(), 'bgeometrics': bgeo,
                'hash_ribbons': ribbons, 'pi_cycle': pi, 'puell_proxy': puell_proxy}
    snap_path = os.path.join(FEEDS_DIR, 'onchain-' + now.strftime('%Y-%m-%d') + '.json')
    with open(snap_path, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)
    with open(LATEST, 'w', encoding='utf-8') as f:
        f.write(digest)

    print('On-chain atualizado:')
    print(f'  BGeometrics:  {bgeo.get("status")} (dado de {bgeo.get("date")})')
    print(f'  Hash Ribbons: {ribbons.get("status")}')
    print(f'  Pi Cycle:     {pi.get("status")}')
    print(f'  Snapshot:     {os.path.relpath(snap_path, BASE_DIR)}')
    print(f'  Digest:       {os.path.relpath(LATEST, BASE_DIR)}')


if __name__ == '__main__':
    main()
