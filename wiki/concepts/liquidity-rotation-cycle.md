# Ciclo de Rotação de Liquidez (BTC.D + índices ES)

> Doutrina de **roteamento de liquidez sistêmica**: antes de validar o bias de um ativo, mapear ONDE
> o capital está dentro do ecossistema cripto. Lente sempre ativa para ETH e altcoins (camada de
> confirmação macro, ao lado de [[institutional-flow-poi]]). Operada pelo `macro-scan` Step 1.5;
> alimenta o Confluence Score via o critério `liq-rotacao` ([[confluence-score]] / [[criteria-keys]]).

## Por que índices ES (Excluding Stablecoins)

Os índices clássicos `TOTAL2` (cap total ex-BTC) e `TOTAL3` (ex-BTC, ex-ETH) **incluem stablecoins**
na sua massa — o que polui a leitura de "para onde foi o capital de risco". Os índices **ES** removem
as stablecoins, isolando o capital efetivamente alocado em risco:

- `CRYPTOCAP:TOTAL2ES` — cap total **ex-BTC e ex-stablecoins** → veículo de confirmação para **ETH**.
- `CRYPTOCAP:TOTAL3ES` — cap total **ex-BTC, ex-ETH e ex-stablecoins** → confirmação para **altcoins menores**.
- `CRYPTOCAP:TOTAL3ESBTC` — razão TOTAL3ES/BTC (força relativa das small-caps vs BTC), opcional.

Por isso o roteamento usa **ES**; os `TOTAL/TOTAL2/TOTAL3` clássicos seguem só no scan amplo do
Workflow A (Regra 5: TOTAL vs TOTAL3, dinheiro em BTC/ETH vs alts).

## Roteamento por target (CORE LOGIC)

| Target | Índice base | Índice de confirmação | Regra de validação de FORÇA |
|--------|-------------|-----------------------|------------------------------|
| **ETH** | `BTC.D` | `TOTAL2ES` | BTC.D falhando suporte / em baixa **E** TOTAL2ES ganhando momentum de alta. BTC.D subindo junto = força do ETH é só beta de BTC → rebaixar. |
| **Altcoin menor** | `BTC.D` | `TOTAL3ES` | BTC.D em queda **+** ETH lateral/subindo com menos força **+** TOTAL3ES rompendo resistência ou expansão de volatilidade. |
| **BTC-solo** | `BTC.D` + `USDT.D` | — | Só o classificador de fase; **não** forçar TOTAL2ES/3ES (anti-alucinação — BTC é a própria base). |
| **EQUITIES** | — | **N/A** | Sem índices cripto; declarar `Rotação liq: N/A`. |

> ETH **permanece** classe `BTC+ETH` (Workflow A, mantém Longs/Shorts + macro TradFi). O roteamento é
> **camada de confirmação**, NÃO reclassifica ETH como altcoin.

## Fases do Ciclo de Liquidez (classificador)

1. **Migração para BTC:** `BTC.D`↑ + `USDT.D` estável/baixo → capital concentra em BTC; alts sangram.
2. **Rotação para ETH:** `BTC.D`↓ + `TOTAL2ES`↑ com `TOTAL3ES` lateral → dinheiro sai de BTC para ETH.
3. **Altseason (TOTAL3ES):** `BTC.D`↓ + `TOTAL3ES`↑ + `OTHERS`↑ → risco se espalha para small-caps.
4. **Fuga para Stablecoins:** `USDT.D`↑ domina (risk-off) → liquidez sai de tudo para stables.

Cruza com (NÃO repete): Regra 5 (TOTAL vs TOTAL3), Regra 9 (acum/distrib cíclica — [[institutional-flow-poi]]),
Regra 10 (força dupla ALT/BTC). A fase é o **classificador que consome** essas leituras.

## Confluência técnica anti-bull-trap (rodar TA NO índice ES)

Para evitar validar rompimentos falsos (bull traps), aplicar ao **gráfico do índice de liquidez**
(não só ao ativo):

- **RSI:** nível de exaustão macro do capital — **não validar compra** se o índice ES estiver em
  sobrecompra forte. Simétrico: índice ES em sobrevenda profunda = risco de bear-trap/capitulação
  (não chase short). Preserva a intenção original: filtro primário de entrada **LONG**.
- **MACD:** cruzamento das médias + momentum do histograma no índice = entrada/saída real de capital.
- **Bandas de Bollinger:** compressão (squeeze) antecede explosão de liquidez; rompimento da banda
  superior do índice = forte fluxo direcional.
- **Fibonacci:** retrações/extensões no índice mapeiam alvos macro onde a liquidez tende a secar/reverter.

## Veredito Estratégico → Confluence Score

O `macro-scan` emite um bloco compacto de 4 linhas (Fase / Índices / Confluência técnica / Veredito):
- **Cenário Otimizado** (rota + fase + índice-TA alinhados ao bias) → critério `liq-rotacao+`.
- **Neutro** → não pontua.
- **Alto Risco de Bull Trap** (rota contradiz o bias, ou índice ES em sobrecompra macro contra um
  LONG) → **−1 + `bull-trap-liquidez`** (`-liq-rotacao`).

É um **input ao Confluence Score**, nunca um veredito paralelo — a Fase 9 do [[confluence-score]]
segue como única fonte de bias.

## Backlinks
- [[institutional-flow-poi]] — lente de fluxo institucional (4 Pilares/POIs) que esta doutrina complementa.
- [[long-short-ratio]] — posicionamento de margem (cruza com a fase de rotação).
- [[liquidity-wicks-trap-short-usdtd]] — USDT.D como confirmador inverso + a fase Fuga para Stablecoins.
- [[confluence-score]] — consome o Veredito de Rotação via `liq-rotacao` / `bull-trap-liquidez`.
- [[criteria-keys]] — define o slug `liq-rotacao` (critério de contexto).
- `macro-scan` (Step 1.5) — operacionaliza o roteamento e emite o Veredito.
