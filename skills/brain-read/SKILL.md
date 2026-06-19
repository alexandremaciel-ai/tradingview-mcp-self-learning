---
name: brain-read
description: Ciclo READ obrigatório do AUTO-PILOT antes de QUALQUER análise de mercado — testa a conexão TradingView, atualiza feeds, casa o layout ativo, lê o brain (insights/mistakes/patterns/predictions/metrics) por RELEVÂNCIA e declara prevenções/insights/padrões ativos + fecha previsões abertas. Use no início de toda análise (BTC, altcoin, equities, watchlist, daily, ciclo, multi-layout). Saída: "Brain Read Summary".
---

# Brain READ — Pré-flight obrigatório

> Aplica-se a TODA análise. É a 1ª coisa a rodar. Saída final: um bloco **Brain Read Summary**.
> Leitura por **relevância** (não despejo): use `wiki_search`/grep, não leia arquivos gigantes inteiros.

## 0 — Conexão + contexto

1. **🔌 Conexão:** `tv_health_check()` → se falhar → `tv_launch()` → 3 tentativas max.
2. **📡 Feeds (cripto):** se `raw/feeds/latest.md` `indisponível` **ou** timestamp > 2h → rodar
   `python3 scripts/tools/fetch_feeds.py` (carrega o `.env`) e reler. Rede falhou → cache + rótulo
   `dados-parciais`. EQUITIES pula feeds.
2b. **🗞️ Briefing macro do dia (gate matinal):** rodar `python3 scripts/tools/check_briefing.py`.
   Garante 1 briefing por dia, lido por toda análise. Decisão por estado:
   - **`AUSENTE`** → invocar a skill **`btc-macro-briefing`** (horizonte default `semana`) **antes
     de prosseguir**; ela persiste `wiki/briefings/{hoje}.md`. Depois ler o Veredito.
   - **`PRESENTE`** e **sem** evento de ALTO impacto (FOMC/CPI/NFP/PCE/Powell) dentro da janela da
     análise → **NÃO re-rodar**; só ler `wiki/briefings/{hoje}.md` (o `🔴 EVENTOS` + o
     `=== VEREDITO ===`) e passar adiante.
   - **`PRESENTE`** **mas** há evento 🔴 agendado dentro da janela → re-rodar `btc-macro-briefing`
     (refresh por evento 🔴; sobrescreve o arquivo do dia).
   - Aplica-se a **todas as classes** (o briefing é macro-global; FOMC/CPI/DXY também movem
     EQUITIES). O `macro-scan` (Step 0.5) consome o Veredito daqui.
2c. **🔁 Gate de feedback (fecha o loop ANTES de analisar):** garante que a análise leia métricas
   frescas. Espelha o gate matinal:
   - `grep -n "⏳" wiki/brain/predictions-log.md` filtrando o símbolo → para cada previsão aberta
     **vencida** (horizonte/prazo passou, ou > 48h sem update), rodar o grading do `prediction-feedback`
     (regra objetiva com `data_get_ohlcv`): TP antes SL = ✅ / SL antes TP = ❌ / nenhum = ⚪ + `Pós-fecho`.
   - Depois de fechar o que venceu, rodar **`python3 scripts/tools/metrics_engine.py`** → atualiza
     `metrics.md` (WR, circuit breaker) + `indicators.md` (Hit Rate por critério) a partir dos `Critérios:`.
   - Só então prosseguir: o Cartão de Calibração (passo 3) lerá números atuais, não defasados.
3. **🖼️ Layout ativo (0c):** `chart_get_state()` → casar os studies (fingerprint) com um perfil em
   `wiki/brain/layouts.md`; ele define QUAIS indicadores a Fase 6 aplica + a recipe do layout. Sem
   match → `layout-adhoc`. **Híbrido:** trocar de layout (navegar `/chart/{slug}/`) só se o
   pedido/classe exigir (ex: SMC → "Liquidity e SMC").

## 1 — Classificar o pedido

Casar com a tabela de `skills/_references/class-rules.md` → define o macro scan e o checklist.
Classes: `BTC | BTC+ETH | BTC+ALTCOIN | ALTCOIN | EQUITIES | WATCHLIST | DAILY | CYCLE`.

## 2 — Ler o brain POR RELEVÂNCIA (recall otimizado)

> ⚠️ NÃO ler `insights.md` (centenas de linhas) nem `predictions-log.md` inteiros. Buscar o que importa.

- **insights:** ler `wiki/brain/insights-hot.md` (Top 5–8, barato, sempre). Para profundidade no
  ativo/TF, `wiki_search` ou `grep` no `insights.md` pelos termos do pedido (símbolo, TF, setup).
- **mistakes:** ler os **últimos 10** de `wiki/brain/mistakes.md` (arquivo curto).
- **asset:** se envolve ativo → `wiki/assets/{SYMBOL}.md`.
- **predictions:** `grep -n "⏳" wiki/brain/predictions-log.md` filtrando o **símbolo do pedido** →
  ler só as abertas relevantes. Fechar/atualizar antes de continuar; > 48h sem update → ⚪ expirada.
- **metrics:** ler `wiki/brain/metrics.md` (curto) → circuit breaker + WR (usar o **ajustado** como
  número principal) + segmentação (melhor/pior lado e regime).
- **indicators (calibração por sinal):** ler em `wiki/brain/indicators.md` o Hit Rate **só dos
  indicadores do layout ativo** (não o arquivo todo) → define o peso data-driven de cada critério no
  Confluence Score (ver `[[confluence-score]]` / `[[criteria-keys]]`).
- **setups:** se houver setup candidato, ler seu Win Rate em `wiki/setups/index.md` → trava
  `setup-fraco` (WR < 50%, N ≥ 10) ou bônus (WR ≥ 70%, N ≥ 10).

## 3 — Protocolo de aplicação (declarar explicitamente)

- **mistakes:** p/ cada um dos últimos 5 erros: "pode repetir aqui?" → se sim,
  `⚠️ Prevenção ativa: [erro] → [ação]`.
- **insights:** os 3 mais aplicáveis ao ativo/TF → `💡 Aplicando: [insight]`.
- **patterns:** algum padrão VALIDADO/CONSOLIDADO ativo? → `🔄 Padrão monitorado: [nome] (N confirmações)`.
- **predictions:** previsão ⏳ aberta → FECHAR/ATUALIZAR; > 48h → ⚪ expirada.
- **metrics:** 🔴 ativo (3 losses seguidos / DD 5% no dia) → rebaixar p/ "observação/paper" +
  `⛔ Disciplina: [estado]`. Ref: `[[trading-psychology]]`.
- **calibração (Cartão de Calibração):** para os indicadores do layout, declarar o ajuste de peso que
  valerá neste score → `📊 Calibração: ema200 cheio (78%, n=12) | -adx sinal-fraco (32%, n=11) → não
  pontua | macd meio-peso (52%, n=9) | setup X WR 44% (n=10) → trava em média`. Critério com N < 8 →
  declarar `(amostra baixa, peso atual)`. É consumido na Fase 9 do `technical-checklist`.
- **lente sempre ativa:** os 4 Pilares + POIs + gatilhos de sobrevenda (D/W) e CHoCH são doutrina de
  toda análise — `[[institutional-flow-poi]]` (aplicada nas Fases do `technical-checklist`).

## Saída — Brain Read Summary

Bloco com: classe detectada, layout ativo + indicadores, prevenções ativas, insights aplicados,
padrões monitorados, previsões abertas fechadas/atualizadas (gate de feedback), estado de disciplina,
e o **📊 Cartão de Calibração** (ajustes de peso data-driven por critério + trava de setup).
Incluir também:
`🗞️ Briefing do dia: [presente | recém-gerado | refresh por evento] | Postura: [risk-on/off/cautela/aguardar evento] | 🔴 hoje: [evento ou —]`.

> Brain files inexistentes → copiar de `wiki/brain/_templates/`. Próximo passo do pipeline:
> `macro-scan` (pelo Workflow da classe), depois `technical-checklist`.
