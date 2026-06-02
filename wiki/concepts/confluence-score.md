# Confluence Score — Pontuação Objetiva de Entrada

> Converte "parece um bom setup" em um número auditável de 0 a 10.
> O score determina o TAMANHO da posição e deriva a CONFIANÇA registrada na previsão.
> Os pesos começam heurísticos e são **recalibrados** pelos dados reais (ver [[metrics]] / `metrics_engine.py`).

## Por que existe
O checklist dos [[trade-playbooks]] (6/8) responde "entro ou não". O Confluence Score responde **"com quanta convicção e qual tamanho"** — e cria um campo numérico que o brain mede ao longo do tempo, ligando faixa de score → win rate histórico. Sem isso, a confiança é palpite e não pode ser calibrada.

## Rubrica (máximo 10 pontos)

Some os pontos de cada critério ATENDIDO. Critério parcial não conta (binário).

| # | Critério | Pts | Como verificar |
|---|----------|-----|----------------|
| 1 | **MTF alinhado** | +2 | Mensal/Semanal e Diário apontam a mesma direção do trade ([[multi-timeframe-analysis]]) |
| 2 | **EMA 200 (4H) confirma** | +1 | Preço acima → só long / abaixo → só short |
| 3 | **Zona institucional** | +2 | Entrada em FVG, Order Block ou POC ([[SMC]] / [[volume-profile]]) |
| 4 | **Golden Zone Fibonacci** | +1 | Entrada em 0.618–0.786 do impulso ([[fibonacci-structural]]) |
| 5 | **Divergência confirmando** | +1 | RSI ou MACD divergente a favor ([[rsi-divergences]] / [[macd]]) |
| 6 | **BOS no gatilho** | +1 | Fechamento além do pivô no TF de execução ([[SMC]]) |
| 7 | **Volume / ATR validam** | +1 | Vol > SMA(20)×1.5 **e** \|O−C\| > ATR×1.5 ([[ATR]]) |
| 8 | **Posicionamento a favor** | +1 | Funding/OI ou Longs-Shorts a favor ([[btcusdlongs-btcusdshorts]] / [[funding-rate]]) |

> StochRSI como TIMING não soma ponto isolado — ele só libera o gatilho dentro da direção do RSI HTF ([[rsi-stochrsi-combined]]).

## Penalidades (subtrair)

| Condição | Pts |
|----------|-----|
| Trade **contra o macro** (contra-macro) | −2 |
| **Fim de semana** / liquidez baixa (vol < 40% avg) | −1 |
| Evento macro de alto impacto < 24h (FOMC/CPI/NFP) | −1 |
| ADX < 20 num playbook de tendência (1 ou 2) | −1 |

## Tabela Score → Ação

| Score | Ação | Tamanho | Confiança registrada |
|-------|------|---------|----------------------|
| **≥ 8** | Operar | posição cheia (1–2% risco) | alta |
| **6–7** | Operar | posição reduzida (0.5–1%) | média-alta / média |
| **4–5** | Só observar / paper | — | baixa |
| **< 4** | Não operar | — | — (declarar "sem confluência") |

> Limiares iniciais. Quando `metrics.md` mostrar win rate por faixa de score com ≥20 amostras, ajustar os cortes para o ponto onde o win rate justifica o risco.

## Como registrar
- Na **Fase 9** (Declaração de Bias), calcular o score e escrever na previsão:
  `- **Confluence Score:** N/10` e derivar a `Confiança` pela tabela acima.
- Listar quais critérios pontuaram (ex: `Score 7/10 = 1,3,5,6,7,8 ✓ | 2,4 ✗ | −2 contra-macro... = 7`).
- O `metrics_engine.py` lê o campo `Confluence Score` para cruzar score × resultado.

## Exemplo
> BTC short em repique, regime risk-off, 4H abaixo da EMA200, entrada em OB bearish + Fib 0.705, MACD 1H divergente, BOS 15M, volume 110% avg, Ratio L/S extremo.
> Critérios: 1(+2) 2(+1) 3(+2) 4(+1) 5(+1) 6(+1) 7(+1) 8(+1) = **10**; sem penalidade → **Score 10/10 = posição cheia, confiança alta**.

## Backlinks
- [[trade-playbooks]] — checklist 6/8 (entra ou não) complementado pelo score (quanto)
- [[position-sizing]] — o score define o tamanho
- [[multi-timeframe-analysis]] · [[SMC]] · [[fibonacci-structural]] · [[volume-profile]]
- [[rsi-divergences]] · [[macd]] · [[ADX]] · [[ATR]] · [[rsi-stochrsi-combined]]
- [[btcusdlongs-btcusdshorts]] · [[funding-rate]]
- [[metrics]] — calibração score × win rate
