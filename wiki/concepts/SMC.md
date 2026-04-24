# Smart Money Concepts (SMC)

> Conceito central de leitura de estrutura de mercado e zonas institucionais.
> Atualizado: 2026-04-23 com KB v1.0 (EQH/EQL traps, MSS, Fibonacci confluence)

---

## 1. Estrutura de Mercado

| Conceito | Definição |
|---|---|
| **BOS** (Break of Structure) | Rompimento de um pivô anterior na direção da tendência. Confirma continuação. |
| **CHoCH** (Change of Character) | Primeiro sinal de reversão — preço quebra a última estrutura contrária à tendência. |
| **MSS** (Market Structure Shift) | Mudança definitiva de caráter após CHoCH confirmado em timeframe relevante. |
| **LH / LL** | Lower High / Lower Low — sequência bearish: topos e fundos descendentes. |
| **HH / HL** | Higher High / Higher Low — sequência bullish: topos e fundos ascendentes. |

### Uso Operacional
- CHoCH no 4H = gatilho para mudar bias
- BOS no 15M = gatilho de entrada (após confirmação no 4H/1H)
- MSS = confirma reversão estrutural, não apenas pullback

---

## 2. Fair Value Gaps (FVG)

"Buracos" de liquidez deixados por impulsos violentos onde os pavios dos candles vizinhos não se tocam.
O preço tende a retornar para preencher o FVG antes de continuar.

- **FVG Bearish** (gap de queda): zona de Short quando o preço retorna para preenchê-lo
- **FVG Bullish** (gap de alta): zona de Long quando o preço retorna para preenchê-lo
- FVG em confluência com EMA 200, Golden Zone Fibonacci ou Order Block = **zona Sniper de alta convicção**
- FVG como alvo de TP e como zona de entrada

---

## 3. Order Blocks (OB)

Último candle de impulso antes de um movimento explosivo. Representa acumulação/distribuição institucional.

- **Bullish OB:** último candle bearish antes de um impulso de alta → zona de Long em reteste
- **Bearish OB:** último candle bullish antes de um impulso de baixa → zona de Short em reteste
- Order Block + FVG na mesma região = **zona de confluência máxima**

---

## 4. Zonas de Liquidez e Traps

### Definições
- **PDH / PDL** (Previous Day High/Low): o mercado frequentemente caça liquidez acima/abaixo antes de reverter
- **EQH / EQL** (Equal Highs/Lows): múltiplos toques no mesmo nível = pool de liquidez (BSL/SSL). O mercado vai buscar esses stops
- **BSL** (Buy Side Liquidity): acima de swing highs — stop hunts de shorts
- **SSL** (Sell Side Liquidity): abaixo de swing lows — stop hunts de longs

### Armadilhas
- **Bull Trap:** rompimento acima de EQH/PDH **sem volume**, seguido de reversão. Sinal de Short.
- **Bear Trap:** rompimento abaixo de EQL/PDL **sem volume**, seguido de reversão. Sinal de Long.
- **BSL Grab:** spike mínimo acima de EQH → close abaixo = smart money capturou liquidez antes de queda
- **Stop Hunt:** movimento brusco que atinge zonas de stop antes de reverter para a direção real

### Confluência de Alta Convicção
- EQH varrido + weekly close abaixo = BSL grab confirmado → Playbook 3 (Stop Hunt Reversal)
- EQH + Golden Zone Fibonacci + FVG = entrada sniper de máxima convicção

---

## 5. Confluências com Outros Conceitos

| Combinação | Convicção |
|-----------|----------|
| FVG + OB na mesma zona | Alta |
| FVG + Golden Zone Fibonacci (0.618-0.786) | Alta |
| FVG + EMA 200 (1H ou 4H) | Alta |
| OB + RSI divergência (1H) | Alta |
| EQH swept + close abaixo + RSI divergência bearish | Altíssima |
| FVG + POC (Volume Profile) | Alta |

---

## 6. Como Usar na Estratégia (Fluxo Top-Down)

1. 4H: identificar tendência, BOS/CHoCH, zonas de FVG e OB relevantes
2. 1H: identificar zona de entrada sniper (FVG + OB + Fibonacci)
3. 15M: gatilho de entrada — BOS bullish/bearish com volume
4. 5M: timing de execução (opcional)

---

## Backlinks
- [[conservative-trend-follower-v2]]
- [[Wyckoff]]
- [[multi-timeframe-analysis]]
- [[fibonacci-structural]] — Golden Zone + OB/FVG
- [[volume-profile]] — POC + FVG
- [[rsi-divergences]] — RSI divergência + OB
- [[trade-playbooks]] — Playbooks 1, 2 e 3 usam SMC
- [[vvir-framework]] — V.V.I.R. valida rompimentos de BOS
