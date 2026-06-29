---
name: multi-layout-scan
description: Varredura completa dos layouts do TradingView com dedup de indicadores — pergunta o ativo em linguagem natural e roda o pipeline AUTO-PILOT completo. Use quando o usuário quer "scan multi-layout", "varredura de todos os layouts", "passe por todos os layouts" ou uma análise consolidada que combine ciclo (MVRV), estrutura (SMC), RSI MTF e volume.
---

# Varredura Multi-Layout com Dedup

Você vai percorrer **todos os layouts ativos** do TradingView, capturar a leitura de **cada
indicador uma única vez** (os que se repetem entre layouts são lidos só na 1ª aparição) e
entregar **uma análise consolidada** que nenhum layout sozinho oferece — combinando ciclo
on-chain (MVRV), estrutura/liquidez (SMC), RSI multi-TF e volume institucional.

Fonte de verdade dos perfis de layout: `wiki/brain/layouts.md`. Se os slugs/indicadores
abaixo divergirem desse arquivo, **o `layouts.md` vence** (rode RECALIBRATE LAYOUTS antes).

---

## Passo 1 — Obter o ativo (linguagem natural)

1. **Se o ativo veio nos argumentos da invocação**, use-o direto.
2. **Senão, PERGUNTE ao usuário:** "Qual ativo você quer na varredura multi-layout? (pode
   escrever em linguagem natural — ex.: *Bitcoin e Ethereum*, *Solana*, *AAPL*)". Aceite
   texto livre, inclusive **múltiplos ativos**.
3. **Mapeie nome → ticker** (interprete a linguagem natural):

   | Disse | Ticker | | Disse | Ticker |
   |-------|--------|-|-------|--------|
   | Bitcoin / BTC | `BTCUSDT` | | Cardano / ADA | `ADAUSDT` |
   | Ethereum / ETH | `ETHUSDT` | | Dogecoin / DOGE | `DOGEUSDT` |
   | Solana / SOL | `SOLUSDT` | | XRP / Ripple | `XRPUSDT` |
   | BNB | `BNBUSDT` | | Avalanche / AVAX | `AVAXUSDT` |

   - Ticker **não mapeado** (cripto ou ação) → `symbol_search` para resolver o símbolo real.
   - Ações/índices (AAPL, TSLA, SPX…) → tratar como classe `EQUITIES`.
4. **TF default:** 4H, salvo se o usuário pedir outro.
5. **Classifique o pedido** pela tabela de `skills/_references/class-rules.md` → define o macro scan do Passo 2:
   - 1 ativo BTC → `BTC` · BTC+ETH → `BTC+ETH` · BTC+altcoin → `BTC+ALTCOIN` ·
     altcoin solo → `ALTCOIN` · ação/índice → `EQUITIES`.
6. **Múltiplos ativos:** faça o macro scan **1× no início**, depois repita o sweep dos
   layouts (Passos 3–5) **por ativo**, e ao final compare força relativa (ETH/BTC, ALT/BTC).

---

## Passo 2 — Preâmbulo AUTO-PILOT (uma vez, antes do sweep)

Delegue às camadas reutilizáveis (não reimplemente aqui):
1. **`brain-read`** — conexão TV, feeds, layout ativo, classe do pedido, leitura do brain por
   relevância, prevenções/insights/padrões, fechar previsões abertas. → Brain Read Summary.
   - ⚠️ **Calibração cross-layout (específico do multi-layout):** o `brain-read` lê o Hit Rate "só do
     layout ativo", mas aqui o sweep cobre **os 5 layouts** → puxar em `wiki/brain/indicators.md` a
     calibração de **TODOS os indicadores que serão varridos** (V.V.I.R./StochRSI/MACD/SMC/EMA-Cross/
     ADX/MVRV/Bollinger/VRVP/Whale/Mxwll/Supertrend/EMA200), não só os do home. É esse Cartão de
     Calibração ampliado + as **Prevenções ativas** e **Insights aplicados** do Brain Read Summary que
     o Passo 5 consome (carregar para a consolidação, não deixar órfãos).
2. **`macro-scan`** — Step 0 (contexto/horário, NYSE/CME/Forex, reabertura Dom 19h) + Workflow da
   classe (A/B/C/D) + Regras de Leitura Macro. Faça-o **1× no início** (multi-ativo: 1× só).
   - ⚠️ Lembrete: **`quote_get(symbol=...)` IGNORA o parâmetro** → `chart_set_symbol` por ticker.
     Priorize **USDT.D MACD ao vivo** (filtro-mestre) + **BTCUSDLONGS/SHORTS**; índice que não
     carrega (`chart loading`) → repetir 1×, persistindo use o último valor rotulado (lento).

---

## Passo 3 — Sweep dos layouts com DEDUP (núcleo da skill)

### Mapa de duplicatas — capturar SÓ na 1ª aparição, pular depois
| Indicador | Aparece em | Capturar em |
|-----------|-----------|-------------|
| RSI Divergences Pro (V.V.I.R.) | 4/5 layouts (**não** no Emas) | Trade Diario (1º) |
| Tabela RSI Dinâmica - Maciel | 2/5 (Trade Diario + RSI's e MACD) | Trade Diario (1º) |
| Stoch RSI Div Pro | 3/5 | Trade Diario (1º) |
| MACD (qualquer variante) | 3/5 | Trade Diario (1º) |
| Crypto Smart Volume | 2/5 | Trade Diario (1º) |
| Volume (nativo) | 3/5 | Trade Diario (1º) |

Todos os **demais** indicadores são exclusivos de um layout → sempre capturar.
⚠️ O **Emas** é o único layout **sem RSI/StochRSI/MACD/ADX** (price-action puro) → ele não contribui osciladores; capture nele só os exclusivos (Mxwll Suite, Supertrend, EMA Cross ribbon).

### Procedimento por layout (repetir nesta ordem)
Para cada layout: navegue, confirme, leia, aplique a dedup.

1. **Navegar:** `ui_evaluate("location.href = location.origin + '/chart/{SLUG}/'")`
   (navegação real recarrega o layout salvo — `layout_switch` sozinho **não** recarrega).
2. **Confirmar:** `tv_health_check` (símbolo/TF) + opcional ler "Layout ativo: X" no toolbar.
3. **Ajustar:** se o símbolo/TF não for o do pedido → `chart_set_symbol` + `chart_set_timeframe`.
4. **Ler estado:** `chart_get_state` (1× por layout) → lista os studies presentes.
5. **Valores nativos:** `data_get_study_values`.
6. **Custom (Pine drawings)** — usar a tool certa com `study_filter`:
   - RSI Divergences Pro (V.V.I.R.) / MACD Divergences Pro / Stoch RSI Div Pro → **divergência (Bull/Bear)
     só sai por SCREENSHOT.** ⚠️ Confirmado 28/06: os marcadores são `plotshape()` → **nenhuma** tool de
     dados os lê (`data_get_study_values` = só valor; `data_get_pine_labels` = só projeções RSI78/30, K90/10;
     `data_get_pine_lines("RSI Div")` = ~5.400 linhas do filtro MTF = ruído). Se a divergência for **decisiva**
     ao bias → `capture_screenshot(region="full")` (region `chart` corta o sub-painel!) e ler o marcador no
     candle atual. Não-decisiva → pular sem custo. Nunca inferir de price action; sem chart → `DADO_INDISPONIVEL`.
   - Tabela RSI Dinâmica - Maciel → `data_get_pine_tables(study_filter="Tabela RSI")`
   - Smart Money Concepts [LuxAlgo] → `data_get_pine_labels` (CHoCH/BOS/EQH/EQL) +
     `data_get_pine_boxes` (Order Blocks) + `data_get_pine_lines` (níveis de estrutura)
   - Whale Liquidity and Absorption → `data_get_pine_boxes` (**filtrar zonas dentro de ±5%
     do preço** para poupar contexto)
   - Visible Range Volume Profile → `data_get_study_values` (POC/HVN/Up/Down/Total)
   - Mxwll Suite (layout Emas) → `data_get_pine_labels` (estrutura BoS/CHoCH/HH/HL/LH/LL + Fib) +
     `data_get_pine_tables(study_filter="Mxwll")` (sessões/volume) + `data_get_pine_lines(study_filter="Mxwll")`
     (S/R/liquidez — **filtrar ±5% do preço**, são ≈500 linhas)
7. **Aplicar dedup:** pular qualquer indicador da tabela de duplicatas já capturado antes.

### Sequência dos layouts (otimizada — os compartilhados caem no 1º)
| # | Layout | Slug | Capturar aqui |
|---|--------|------|---------------|
| 1 | **Trade Diario** ⭐home | `Fbl7OmwZ` | V.V.I.R. RSI · Stoch RSI · MACD Div · Crypto Smart Volume · **Tabela RSI Maciel** (MTF 5m→1M + preços P.RSI 30/50/70). _Triple Smoothed Signals saiu — substituído pela Tabela Maciel (16/06)._ |
| 2 | **Emas** 🆕 | `f8sPhMo9` | **Mxwll Suite** (estrutura BoS/CHoCH/HH/HL/LH/LL + Fib + sessões + S/R/liquidez) · **Supertrend** (tendência ATR) · **EMA Cross** (ribbon de 4 EMAs). _Sem osciladores — price-action puro._ |
| 3 | **RSI's e MACD** | `CtPFiwLf` | **Visible Range Volume Profile** · **RSI&EMA Reverse Calculator** (Tabela Maciel já capturada no #1) |
| 4 | **EMA Cross e MVRV** | `HQ98e9nf` | **Bollinger Awesome Alert** · **EMA200** (filtro de tendência 4H) · **ADX** (força/range). _MVRV removido pelo usuário 12/06 — não é mais layout de ciclo._ |
| 5 | **Liquidity e SMC** | `71Oqhxgm` | **SMC LuxAlgo** (CHoCH/BOS/EQH/EQL/OBs) · **Whale Liquidity Absorption** |

> O layout **Padrão 3** foi **removido pelo usuário** (não consta mais no `layout_list`, 16/06) → ignorar.
>
> **Nota Emas (#2):** layout novo, **price-action puro sem osciladores** (não tem RSI/StochRSI/MACD/ADX).
> Não contribui momentum à consolidação — capture nele só os exclusivos (Mxwll/Supertrend/EMA ribbon).
> Se o pedido exigir RSI/MACD, eles já vêm do Trade Diario / RSI's e MACD.
>
> **Nota L4:** o "EMA Cross e MVRV" foi reconfigurado pelo usuário (12/06) — **MVRV/SMA Cross
> removidos, EMA200/ADX adicionados**. Não há mais layout de **ciclo on-chain**: para CYCLE,
> adicionar o MVRV ad-hoc (`chart_manage_indicator`) ou usar [[btc-cycle-analysis]]. Sempre
> capture o que o `chart_get_state` retornar ao vivo (símbolo INDEX:BTCUSD).

---

## Passo 4 — Consolidar por eixo

Reúna tudo (cada indicador uma vez) numa visão única, organizada por eixo:

- **Momentum / Osciladores:** RSI (V.V.I.R. + Tabela Maciel MTF 5m→1M) · StochRSI · MACD
- **Tendência:** Supertrend (ATR) · EMA Cross ribbon · EMA200 · EMA do RSI
- **Volume / Liquidez:** Crypto Smart Volume · Visible Range Volume Profile · Whale Absorption · Mxwll S/R
- **Ciclo on-chain:** MVRV Z-Score (ad-hoc — sem layout dedicado)
- **Estrutura SMC:** CHoCH/BOS · EQH/EQL · Order Blocks (LuxAlgo) · BoS/CHoCH/HH/HL/LH/LL (Mxwll)
- **Volatilidade:** Bollinger squeeze
- **Rotação de liquidez:** Veredito do `macro-scan` Step 1.5 ([[liquidity-rotation-cycle]]) — **Fase**
  (Migração BTC / Rotação ETH / Altseason / Fuga Stablecoins) + `BTC.D` + índice ES (`TOTAL2ES` p/ ETH,
  `TOTAL3ES` p/ alt) + índice-TA anti-bull-trap. **Consumir** o veredito (não re-puxar os índices).
- **Níveis-chave:** P.RSI50/70 (Tabela Maciel) · POC (VRVP) · OBs (SMC) · clusters Whale · Fib + S/R (Mxwll)

---

## Passo 5 — Bias final (Fase 9)

1. Sintetize todos os eixos num bias claro: **LONG / SHORT / NEUTRO**.
2. **Aplicar os aprendizados do brain (obrigatório — fecha o elo do Passo 2):**
   - **Cartão de Calibração** sobre os indicadores varridos: `sinal-fraco` (<40%, N≥8) **não pontua**
     (e considerar inverter a leitura); `meio-peso` (40–55%) conta 0.5; `setup-fraco` (WR<50%, N≥10)
     **trava** a confiança em "média" −1. Critério N<8 = peso atual (declarar).
   - **Prevenções ativas** (dos `mistakes`) e **Padrões monitorados** do Brain Read Summary → aplicar
     como gate/desconto no bias (ex.: "Melt-up ≠ reclaim", "OB subindo ≠ gatilho", "não confirmar
     swing em FDS"); **Insights aplicados** → reforço quando alinhados.
3. **Confluence Score (0–10)** + penalidades + confiança derivada → seguir
   `skills/_references/confluence-score.md`. **Incluir o critério `liq-rotacao`** (ou a penalidade
   `bull-trap-liquidez` se o índice ES/rota contradiz o bias).
4. **Multi-ativo:** força relativa (ETH/BTC, ALT/BTC: outperform/underperform) **interpretada pela
   Fase de rotação** — ex.: ETH outperform + Fase "Rotação ETH" (BTC.D↓ + TOTAL2ES↑) = força
   confirmada pela liquidez; ETH outperform mas Fase "Fuga Stablecoins" = força frágil/contra-fluxo.

---

## Passo 6 — Brain WRITE + cleanup

1. Rodar **`brain-write`** — insight (+ `insights-hot.md`), previsão (se bias), indicators/patterns,
   append `wiki/log.md` (`## [YYYY-MM-DD HH:MM] multi-layout-scan | {SYMBOL(s)} {TF}`).
2. **Restaurar o layout home** (Trade Diario, `Fbl7OmwZ`) ao final, deixando o chart no estado padrão.

---

## Saída esperada (resumo)
- Cabeçalho temporal (data/hora BRT, sessão, fechamentos) + `Classe` + `Layout home`.
- Tabela/bloco por **eixo** (Passo 4) com cada indicador aparecendo **uma só vez**.
- **Veredito de Rotação de Liquidez** (Fase + índices ES + veredito Otimizado/Neutro/Bull-Trap).
- **Confluence Score + bias + confiança** por ativo; comparação relativa **lida pela Fase** se multi-ativo.
- Confirmação do brain WRITE e da restauração do layout home.
