"""Helpers compartilhados pelos scripts de ingestão de feeds (fetch_feeds / fetch_onchain).

Stdlib puro, sem deps — preserva a mesma regra de degradação graciosa dos scripts:
sem .env, sem rede ou com erro de leitura, nada quebra.
"""
import json
import os
import urllib.request


def load_dotenv(base_dir, path=None):
    """Carrega base_dir/.env em os.environ (stdlib puro, sem deps).

    NÃO sobrescreve variáveis já presentes no ambiente — env real vence o .env.
    Degradação graciosa: sem .env (ou erro de leitura) segue sem alterar nada.
    """
    path = path or os.path.join(base_dir, '.env')
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


def http_get_json(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode('utf-8'))
