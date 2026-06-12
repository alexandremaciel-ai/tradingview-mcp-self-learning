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
5. **Classifique o pedido** pela tabela do CLAUDE.md → define o macro scan do Passo 2:
   - 1 ativo BTC → `BTC` · BTC+ETH → `BTC+ETH` · BTC+altcoin → `BTC+ALTCOIN` ·
     altcoin solo → `ALTCOIN` · ação/índice → `EQUITIES`.
6. **Múltiplos ativos:** faça o macro scan **1× no início**, depois repita o sweep dos
   layouts (Passos 3–5) **por ativo**, e ao final compare força relativa (ETH/BTC, ALT/BTC).

---

## Passo 2 — Preâmbulo AUTO-PILOT (uma vez, antes do sweep)

Siga o ciclo READ obrigatório do CLAUDE.md:
1. `tv_health_check` → se falhar, `tv_launch` (3 tentativas).
2. **Feeds (cripto):** se `raw/feeds/latest.md` estiver `indisponível` ou timestamp > 2h →
   `python3 scripts/tools/fetch_feeds.py` e reler. EQUITIES pula feeds.
3. **Brain READ:** `wiki/brain/insights.md` (Top N) + `mistakes.md` (últimos 10) +
   `wiki/assets/{SYMBOL}.md` + `predictions-log.md` (fechar previsões abertas) +
   `brain/metrics.md` (circuit breaker). Declarar prevenções/insights ativos.
4. **Macro scan da classe** (Workflow A/B/C/D do CLAUDE.md):
   - `BTC`/`BTC+ETH` → completo (10 passos) · `BTC+ALTCOIN` → parcial (7) ·
     `ALTCOIN` → reduzido (5) · `EQUITIES` → TradFi (DXY/SPX/VIX/setor/GOLD).
   - Respeite os fallbacks de horário (Step 0 do CLAUDE.md: NYSE/CME/Forex, reabertura Dom 19h).
   - ⚠️ **`quote_get(symbol=...)` IGNORA o parâmetro** e retorna o chart ativo (bug confirmado
     12/06). Para cada ticker do macro: `chart_set_symbol` → `data_get_study_values`/`quote_get`
     (NÃO tente "quotes paralelos por símbolo"). Priorize o **USDT.D MACD ao vivo** (filtro-mestre)
     + **BTCUSDLONGS/SHORTS**; se um índice não carregar (`chart loading`), repita 1× e, se
     persistir, use o último valor conhecido rotulando-o (lento) — não trave a varredura.

---

## Passo 3 — Sweep dos layouts com DEDUP (núcleo da skill)

### Mapa de duplicatas — capturar SÓ na 1ª aparição, pular depois
| Indicador | Aparece em | Capturar em |
|-----------|-----------|-------------|
| RSI Divergences Pro (V.V.I.R.) | 4/4 layouts | Trade Diario (1º) |
| Stoch RSI Div Pro | 3/4 | Trade Diario (1º) |
| MACD (qualquer variante) | 3/4 | Trade Diario (1º) |
| Crypto Smart Volume | 2/4 | Trade Diario (1º) |

Todos os **demais** indicadores são exclusivos de um layout → sempre capturar.

### Procedimento por layout (repetir nesta ordem)
Para cada layout: navegue, confirme, leia, aplique a dedup.

1. **Navegar:** `ui_evaluate("location.href = location.origin + '/chart/{SLUG}/'")`
   (navegação real recarrega o layout salvo — `layout_switch` sozinho **não** recarrega).
2. **Confirmar:** `tv_health_check` (símbolo/TF) + opcional ler "Layout ativo: X" no toolbar.
3. **Ajustar:** se o símbolo/TF não for o do pedido → `chart_set_symbol` + `chart_set_timeframe`.
4. **Ler estado:** `chart_get_state` (1× por layout) → lista os studies presentes.
5. **Valores nativos:** `data_get_study_values`.
6. **Custom (Pine drawings)** — usar a tool certa com `study_filter`:
   - Tabela RSI Dinâmica - Maciel → `data_get_pine_tables(study_filter="Tabela RSI")`
   - Smart Money Concepts [LuxAlgo] → `data_get_pine_labels` (CHoCH/BOS/EQH/EQL) +
     `data_get_pine_boxes` (Order Blocks) + `data_get_pine_lines` (níveis de estrutura)
   - Whale Liquidity and Absorption → `data_get_pine_boxes` (**filtrar zonas dentro de ±5%
     do preço** para poupar contexto)
   - Visible Range Volume Profile → `data_get_study_values` (POC/HVN/Up/Down/Total)
7. **Aplicar dedup:** pular qualquer indicador da tabela de duplicatas já capturado antes.

### Sequência dos layouts (otimizada — os compartilhados caem no 1º)
| # | Layout | Slug | Capturar aqui |
|---|--------|------|---------------|
| 1 | **Trade Diario** ⭐home | `Fbl7OmwZ` | V.V.I.R. RSI · Stoch RSI · MACD · Crypto Smart Volume · **Triple Smoothed Signals** (exclusivo) |
| 2 | **RSI's e MACD** | `CtPFiwLf` | **Tabela RSI Maciel** (MTF 5m→1M + preços P.RSI 30/50/70) · **Visible Range Volume Profile** · **RSI&EMA Reverse Calculator** |
| 3 | **EMA Cross e MVRV** | `HQ98e9nf` | **Bollinger Awesome Alert** · **EMA200** (filtro de tendência 4H) · **ADX** (força/range). _MVRV removido pelo usuário 12/06 — não é mais layout de ciclo._ |
| 4 | **Liquidity e SMC** | `71Oqhxgm` | **SMC LuxAlgo** (CHoCH/BOS/EQH/EQL/OBs) · **Whale Liquidity Absorption** |

> O layout **Padrão 3** é legado/sem URL acessível → **ignorar**.
>
> **Nota L3:** o "EMA Cross e MVRV" foi reconfigurado pelo usuário (12/06) — **MVRV/SMA Cross
> removidos, EMA200/ADX adicionados**. Não há mais layout de **ciclo on-chain**: para CYCLE,
> adicionar o MVRV ad-hoc (`chart_manage_indicator`) ou usar [[btc-cycle-analysis]]. Sempre
> capture o que o `chart_get_state` retornar ao vivo (símbolo INDEX:BTCUSD).

---

## Passo 4 — Consolidar por eixo

Reúna tudo (cada indicador uma vez) numa visão única, organizada por eixo:

- **Momentum / Osciladores:** RSI (V.V.I.R. + Tabela Maciel MTF 5m→1M) · StochRSI · MACD
- **Tendência:** Triple Smoothed Signals · SMA Cross · EMA do RSI
- **Volume / Liquidez:** Crypto Smart Volume · Visible Range Volume Profile · Whale Absorption
- **Ciclo on-chain:** MVRV Z-Score
- **Estrutura SMC:** CHoCH/BOS · EQH/EQL · Order Blocks
- **Volatilidade:** Bollinger squeeze
- **Níveis-chave:** P.RSI50/70 (Tabela Maciel) · POC (VRVP) · OBs (SMC) · clusters Whale

---

## Passo 5 — Bias final (Fase 9 do CLAUDE.md)

1. Sintetize todos os eixos num bias claro: **LONG / SHORT / NEUTRO**.
2. **Confluence Score (0–10)** — listar critérios que pontuaram + penalidades
   (`−2 contra-macro`, `−1 dados-parciais` se feeds falharam).
3. **Confiança derivada do score:** ≥8 alta · 6–7 média · 4–5 baixa · <4 NEUTRO.
4. **Multi-ativo:** adicionar força relativa (ETH/BTC, ALT/BTC: outperform/underperform).
5. Disciplina: se `brain/metrics.md` indicar circuit breaker 🔴 → rebaixar para observação/paper.

---

## Passo 6 — Brain WRITE + cleanup

1. Insight → `wiki/brain/insights.md` + append `wiki/log.md`
   (`## [YYYY-MM-DD HH:MM] multi-layout-scan | {SYMBOL(s)} {TF}`).
2. Se bias definido → previsão em `brain/predictions-log.md`.
3. Indicador que surpreendeu → `brain/indicators.md` · padrão repetido → `brain/patterns.md`.
4. **Restaurar o layout home** (Trade Diario, `Fbl7OmwZ`) ao final, deixando o chart no estado padrão.

---

## Saída esperada (resumo)
- Cabeçalho temporal (data/hora BRT, sessão, fechamentos) + `Classe` + `Layout home`.
- Tabela/bloco por **eixo** (Passo 4) com cada indicador aparecendo **uma só vez**.
- **Confluence Score + bias + confiança** por ativo; comparação relativa se multi-ativo.
- Confirmação do brain WRITE e da restauração do layout home.
