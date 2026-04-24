# Conservative Trend Follower v2.0

> Estratégia principal. Última revisão: 2026-04-23 (KB v1.0 integrado)

---

## Parâmetros Core

- **Alavancagem padrão:** 3x–5x
- **Alavancagem máxima:** 10x (alta convicção)
- **R:R mínimo de entrada:** 1:3 (referência ao TP2/TP3)
- **Time stop:** 48 horas
- **Risco máximo por trade:** 1–2% do capital
- **Risco máximo simultâneo:** 5% do capital total

---

## Filtros HTF — Bloqueios Absolutos

- **Hard block LONG:** EMA 200 no 4H acima do preço (preço abaixo da EMA 200) + estrutura 4H bearish
- **Hard block SHORT:** EMA 200 no 4H abaixo do preço (preço acima da EMA 200) + estrutura 4H bullish
- **Aguardar:** CHoCH no 4H para re-habilitar bias
- Se RSI Semanal < 50 → qualquer long é counter-trend → exige R:R ≥ 2x e posição reduzida

---

## Filtros de Entrada — 4 Camadas

1. ADX > 20 (tendência presente)
2. ATR normalizado (volatilidade adequada)
3. EMA 50/200 alinhadas com direção
4. MACD + RSI confirmando momentum

---

## Checklist de Entrada Obrigatório (V.V.I.R. + SMC)

```
□ [1] Viés macro alinhado (Mensal/Semanal confirma a direção)
□ [2] EMA 200 no 4H confirma a direção
□ [3] Zona de entrada identificada (FVG, OB, Fibonacci Golden Zone, POC)
□ [4] Armadilha de liquidez detectada se aplicável (EQH/EQL, PDH/PDL)
□ [5] BOS confirmado no timeframe de gatilho (fechamento além do pivô)
□ [6] ATR Filter: corpo do candle > ATR(14) × 1.5
□ [7] Volume Filter: volume > SMA(Volume, 20) × 1.5
□ [8] Sem eventos macro de alto impacto iminentes (FOMC, CPI, NFP)
```

Mínimo para entrar: 6 de 8. Todos os 8 = alta convicção.

---

## Gestão de Take Profit (35/35/15/15)

| Parcela | % da Posição | Alvo | R:R Típico |
|---------|-------------|------|------------|
| **TP1** | 35% | Primeiro FVG ou resistência imediata | ≥ 1.5:1 |
| **TP2** | 35% | Próxima zona de liquidez (PDH/PDL, EQH/EQL) | ≥ 2.5:1 |
| **TP3** | 15% | Extensão Fibonacci 1.272 ou OB maior TF | ≥ 3.5:1 |
| **TP4** | 15% | Extensão Fibonacci 1.618 ou FVG maior TF | ≥ 5:1 |

---

## Progressão do Trailing Stop

| Momento | Ação |
|---------|------|
| Entrada | Stop no setup (1 tick além do pavio) |
| 40–50% do alvo | Move stop para breakeven |
| Após TP1 | Stop move para breakeven |
| Após TP2 | Stop move para TP1 |
| Tendência forte | Trailing = ATR × 2 |

---

## Playbooks Ativos

- **Playbook 1** — Long em Retração de Alta
- **Playbook 2** — Short em Repique de Baixa
- **Playbook 3** — Stop Hunt Reversal
- **Playbook 4** — Squeeze de Alavancagem

→ Ver [[trade-playbooks]] para checklists completos de cada playbook.

---

## Anti-Loss Framework

- ❌ Nunca entrar contra EMA 200 no 4H sem 4+ fatores alinhados
- ❌ Nunca mover stop para longe da entrada
- ❌ Nunca adicionar posição perdedora (sem Martingale)
- ❌ Nunca operar em FOMC/CPI/NFP sem reduzir posição em 50%
- 🛑 Drawdown 5% no dia → parar
- 🛑 3 stops consecutivos → pausa 24h

---

## Performance Histórica

| Período | Trades | Win Rate | Drawdown | Sharpe |
|---------|--------|----------|----------|--------|
| _(vazio)_ | | | | |

---

## Indicadores Utilizados

| Indicador | Parâmetro | Uso |
|-----------|-----------|-----|
| EMA 200 | Padrão | Filtro direcional absoluto (4H/1H) |
| EMA 50 / 21 | Padrão | Suporte/resistência dinâmico, Golden/Death Cross |
| RSI | 14 | Divergências (1H/4H), sobrecompra macro (Diário/Semanal) |
| MACD | 12/26/9 | Momentum, Linha Zero, histograma |
| StochRSI | 3/3/14/14 | Gatilho fino em 15M e 1H |
| Bollinger Bands | 20, 2σ | Squeeze, riding the band, reversões |
| ATR | 14 | Filtro de intensidade do candle de gatilho |
| ADX | Padrão | Confirma presença de tendência |
| Volume / OBV | Padrão | Validação de rompimentos (V.V.I.R.) |
| Volume Profile | Variável | POC, HVN, LVN, VWAP semanal |

---

## Backlinks
- [[BTCUSD]]
- [[ADX]]
- [[ATR]]
- [[multi-timeframe-analysis]]
- [[SMC]]
- [[trade-playbooks]]
- [[position-sizing]]
- [[rsi-divergences]]
- [[fibonacci-structural]]
- [[volume-profile]]
- [[vvir-framework]]
