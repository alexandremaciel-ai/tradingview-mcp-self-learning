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
2c. **🔁 Gate de feedback (DURO — fecha o loop ANTES de analisar):** uma previsão sai de `⏳`
   por **grading objetivo**, nunca por substituição. Sem isto, `criteria_stats` fica em N=0 e o
   Cartão de Calibração (passo 3) lê pesos de template. **Bloqueante:**
   - Rodar **`python3 scripts/tools/check_predictions.py --symbol {SÍMBOLO}`** (gate determinístico).
     Exit `0` (`loop: LIMPO`) → seguir. Exit `1` (`loop: SUJO`) → o stdout traz o **worklist** das
     `⏳` pendentes (status `supersedida` OU `vencida`).
   - Para CADA item do worklist (inclui as **supersedidas** — antes ignoradas), rodar o grading do
     `prediction-feedback` com `data_get_ohlcv`: TP antes SL = ✅ / SL antes TP = ❌ / nenhum no prazo =
     ⚪ + `Pós-fecho`. Erro (❌/⚪-errada) também gera stub em `mistakes.md` (ver `prediction-feedback`).
   - Depois de zerar o worklist, rodar **`python3 scripts/tools/metrics_engine.py`** → reescreve
     `metrics.md` (WR, circuit breaker) + `indicators.md` (Hit Rate por critério) a partir dos `Critérios:`.
   - **NÃO avançar ao macro-scan com `loop: SUJO`.** Só então o Cartão de Calibração lê números atuais.
   - Sem conexão TradingView (OHLCV indisponível) → não inventar grading: declarar `loop-pendente:N`
     no Summary e usar pesos atuais com a ressalva (degradação explícita, não silenciosa).
2d. **🚨 Alertas disparados hoje:** chamar a tool `alert_list` (usa a conexão viva; NÃO há script
   offline — a auth é CDP). Filtrar os alertas cujo `last_fired` cai na data de HOJE (BRT). Para
   cada um, ler `symbol`, `condition`, `resolution` (= TF de origem), `message`, `last_fired`.
   Escopo: priorizar os do símbolo do pedido; os de OUTROS símbolos disparados hoje entram como
   contexto macro. TradingView offline / `alert_list` falhou → `DADO_INDISPONIVEL` + rótulo
   `alertas-parciais` (degradação explícita, não inventar). **Limitação da fonte (declarar):**
   `last_fire_time` é só o ÚLTIMO disparo — múltiplos disparos no dia colapsam; one-time disparado
   e deletado não aparece.
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
Incluir também (obrigatórias):
`🔁 Loop: [N graduadas | LIMPO] · metrics @ HH:MM · calibração [N≥8: sim/não]` (do gate 2c).
`🗞️ Briefing do dia: [presente | recém-gerado | refresh por evento] | Postura: [risk-on/off/cautela/aguardar evento] | 🔴 hoje: [evento ou —]`.
`🚨 Alertas hoje: [SYMBOL cond @nível (TF, HH:MM) · … | — | alertas-parciais]`.

> Brain files inexistentes → copiar de `wiki/brain/_templates/`. Próximo passo do pipeline:
> `macro-scan` (pelo Workflow da classe), depois `technical-checklist`.
