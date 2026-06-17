---
name: btc-macro-briefing
description: Briefing macro global do mercado financeiro com foco em TUDO que pode mover o preço do Bitcoin — calendário econômico (FOMC/CPI/PCE/NFP), liquidez & renda fixa (DXY/yields/net liquidity/M2), mercado tradicional (SPX/VIX/ouro/petróleo + correlações), eventos cripto (ETF flows, opções Deribit, funding/OI, liquidações, unlocks, stablecoins), on-chain, regulação/geopolítica, sentimento e black-swan watch, terminando num Veredito de Risco Macro 24h/7d. Dirigida por WEB SEARCH (dados reais, nunca inventados). Use quando o usuário pedir "briefing macro", "briefing do mercado", "o que pode afetar o bitcoin", "calendário econômico", "agenda da semana", "macro do dia", "macro briefing", "economic calendar", "what can move bitcoin". NÃO é leitura de chart — para análise técnica de um ativo use `analyze`; para o scan macro de tickers do TradingView use `macro-scan`.
---

# BTC Macro Briefing — Panorama macro global via Web Search

> Esta skill **NÃO lê o chart do TradingView**. Ela coleta dados macro reais via **WebSearch/
> WebFetch** e produz um briefing estruturado em PT-BR, tom técnico e direto. **Não depende** de
> `brain-read`/`brain-write` (para não recursar quando chamada pelo gate de `brain-read`), mas
> **persiste** seu resultado no briefing do dia (ver "Persistência" no fim). Saída final: bloco
> `=== VEREDITO DE RISCO MACRO ===`.

## Parâmetros (reconhecer em linguagem natural)

| Parâmetro | Valores | Default | Gatilhos |
|---|---|---|---|
| **Horizonte** | `hoje` (24h) · `semana` (1-7d) | `semana` | "só hoje", "macro do dia" → `hoje`; "agenda da semana" → `semana` |
| **Detalhe** | `resumido` · `completo` | `completo` | "briefing resumido", "rápido" → `resumido` |

- `completo`: cabeçalho 🔴 + os 8 blocos detalhados + Veredito.
- `resumido`: cabeçalho 🔴 + Veredito apenas (blocos 1-8 omitidos ou condensados em 1 linha cada).

## Step 0 — Contexto temporal & gating (SEMPRE PRIMEIRO)

1. **Datar o briefing:** dia/hora atual em **BRT (GMT-3)** + dia da semana. Todo horário citado no
   briefing é BRT — converter eventos publicados em ET/UTC.
2. **Estado de mercado** (espelha `skills/macro-scan/SKILL.md` Step 0):
   - **NYSE:** Seg-Sex 10:30–17:00 BRT (verão) / 11:30–18:00 (inverno).
   - **CME:** quase 24h; fecha Sex 18h BRT → reabre Dom 19h BRT.
   - **Forex/DXY:** Seg 00h – Sex ~22h BRT; congelado no fim de semana.
3. **Adaptação obrigatória de foco:**
   - **Fim de semana (Sex 18h → Dom 19h BRT):** TradFi fechado → SPX/DXY/yields/ouro/petróleo
     **congelados** (fechamento de sexta). Declarar `⚠️ TradFi fechado — dados de sexta. Cripto =
     único mercado ao vivo.` Pesar mais os blocos cripto-nativos (4, 5, 7) e fazer **preparação da
     semana** (eventos agendados Seg-Sex no bloco 1).
   - **Reabertura Dom 19h+:** notar que ES1!/DXY voltaram ao vivo.
   - **Véspera de FOMC / CPI / NFP / PCE:** destacar o evento no topo do bloco 🔴 e na seção de
     "datas críticas" do Veredito; a postura sugerida deve refletir o evento iminente.
4. **Cache de feeds:** ler `raw/feeds/latest.md` (apenas leitura — `raw/` é imutável, NÃO rodar o
   script). Se `status` ≠ indisponível e a idade do snapshot < 2h, usar funding rate / open
   interest / Fear & Greed de lá no bloco 4 e 7 (citar "fonte: feeds local"). Caso contrário,
   buscar via web ou marcar `não disponível`.

## Estratégia de coleta (WebSearch / WebFetch)

**Priorizar fontes primárias e agregadores rastreáveis:**
- Macro/Fed: `federalreserve.gov` (decisões, atas, dot plot, discursos), CME **FedWatch** (prob. de
  juros), BLS (CPI, NFP), BEA (PCE, PIB), ISM (PMI).
- Calendário: ForexFactory, Investing.com economic calendar, TradingEconomics.
- Renda fixa/liquidez: US Treasury / FRED (DXY, US10Y, US02Y, M2, Fed balance sheet, RRP, TGA).
- ETF flows: **Farside Investors**, **SoSoValue**.
- Derivativos cripto: **Coinglass** (funding, OI, liquidações), **Deribit** (opções, max pain, OI).
- On-chain: Glassnode, CryptoQuant, DefiLlama (stablecoins/TVL).
- Sentimento: alternative.me (**Fear & Greed Index**).

**Evitar:** previsões de preço de blogs, conteúdo promocional/"shill", influencers, agregadores
sem fonte, e qualquer número **sem data**. Quando a busca retornar um agregador, usar WebFetch para
abrir a fonte primária e confirmar o número + a data.

**Eficiência:** uma query de WebSearch por bloco temático (8 queries no modo `completo`); no modo
`hoje`/`resumido` priorizar blocos 1, 2, 3, 4 e 7.

## Regra de honestidade (INVARIANTE)

> NUNCA inventar números. Dado que não conseguiu confirmar → marcar **`não disponível`** (não
> estimar). Fontes que **conflitam** → declarar a divergência explicitamente e **não forçar
> conclusão**. Valor defasado/de fechamento anterior → marcar `(defasado: fechamento de DD/MM)`.
> Probabilidade ≠ certeza: reportar consenso/probabilidade como tal.

## Selo de impacto no BTC (cada item recebe um)

| Selo | Critério |
|---|---|
| 🔴 **ALTO** | FOMC/decisão de juros, CPI/Core CPI, PCE, NFP, discurso de Powell; grandes ETF flows (entrada/saída > ~$500M/dia); depeg de stablecoin; evento de crédito/falência bancária; vencimento grande de opções. |
| 🟡 **MÉDIO** | PPI, jobless claims, JOLTS, retail sales, ISM/PMI principal, GDP revisão; movimento relevante de DXY/yields; funding/OI em extremo; unlock de token grande; ação regulatória em curso. |
| ⚪ **BAIXO** | Indicadores secundários, discursos de membros não-Powell, dados confirmatórios sem surpresa, ruído de sentimento. |

## Blocos do briefing (1-8)

Para cada item buscar: **valor atual, consenso (se evento), valor anterior, data/hora BRT, e o selo
de impacto**. Quando faltar qualquer campo → `não disponível`.

**1. Calendário Econômico (próximos 1-7 dias / 24h conforme horizonte)**
FOMC (decisão de juros, atas, dot plot); discursos do Fed (em especial **Powell**); CPI, Core CPI,
**PCE** (métrica preferida do Fed), PPI; NFP, jobless claims, taxa de desemprego, JOLTS; PIB, retail
sales, ISM/PMI (manufatura e serviços), consumer confidence. Tabela: Evento | Data/Hora BRT |
Consenso | Anterior | Selo.

**2. Liquidez Global & Renda Fixa**
DXY (nível + direção + nível-chave); US10Y e US02Y (curva, inversão 2s10s); net liquidity (Fed
balance sheet, RRP, TGA — tendência); M2 global (expansão/contração); decisões de BCE/BoJ/PBoC se
relevantes na janela.

**3. Mercado Tradicional (correlações)**
S&P 500 e Nasdaq (risk-on/risk-off); VIX (nível de medo); ouro e petróleo (safe haven / inflação);
**correlação atual BTC×SPX e BTC×DXY** (direção e força — citar a fonte/janela).

**4. Eventos Específicos de Cripto**
ETF spot de BTC: fluxos (entradas/saídas — IBIT/BlackRock, FBTC/Fidelity etc.); vencimento de
opções Deribit (datas, **max pain**, OI); **funding rates e OI agregado** BTC e ETH (preferir feeds
local se fresco); liquidações recentes (clusters long/short); posição no ciclo de halving;
unlocks de tokens relevantes na semana; market cap de stablecoins USDT/USDC (capital entrando/saindo).

**5. On-Chain (resumo)**
Exchange reserves de BTC (acumulação/distribuição); movimentos de whales / OTC relevantes; métricas
de ciclo (MVRV, NUPL) **apenas se houver sinal** no momento — senão omitir.

**6. Regulação & Geopolítica**
Ações da SEC/CFTC, legislação cripto em andamento; eventos geopolíticos com impacto em risk assets;
eleições / política monetária relevantes.

**7. Sentimento**
Fear & Greed Index (valor + tendência vs. dias anteriores); narrativa social/dominante do momento.

**8. Black Swan Watch**
Riscos de cauda monitorados: falências bancárias, problemas em exchanges, depegs de stablecoin,
eventos de crédito; qualquer sinal de estresse sistêmico. Se nada relevante → `Sem sinais de
estresse sistêmico no momento.`

## Formato de saída (seguir à risca)

```
=== BRIEFING MACRO — BITCOIN ===
Data/Hora: [DD/MM/AAAA HH:MM BRT] | [dia da semana] | Horizonte: [hoje|semana] | Detalhe: [resumido|completo]
Contexto de mercado: NYSE [aberta/fechada] · CME [aberto/fechado] · Forex [disponível/congelado]
[⚠️ avisos de fim de semana / véspera de evento, se aplicável]

🔴 EVENTOS DE ALTO IMPACTO (próximas 24h-7d)
- [item priorizado 1 — data/hora BRT]
- [item priorizado 2 — data/hora BRT]
- ...

— BLOCO 1 · Calendário Econômico —
[itens com selo 🔴/🟡/⚪]

— BLOCO 2 · Liquidez & Renda Fixa —
...

— BLOCO 3 · Mercado Tradicional —
— BLOCO 4 · Eventos Cripto —
— BLOCO 5 · On-Chain —
— BLOCO 6 · Regulação & Geopolítica —
— BLOCO 7 · Sentimento —
— BLOCO 8 · Black Swan Watch —

=== VEREDITO DE RISCO MACRO ===
Risco direcional 24h: [ALTA pressão compradora / ALTA pressão vendedora / neutro] — [justificativa curta]
Risco direcional 7d:  [...] — [justificativa curta]
Principais catalisadores da semana: [top 3]
Datas/horários críticos a monitorar (BRT): [lista com data/hora]
Cenário de maior risco para o BTC: [descrever o tail risk mais provável]
Postura sugerida: [risk-on / risk-off / cautela / aguardar evento X]
```

> No modo `resumido`: emitir apenas o cabeçalho, o bloco `🔴 EVENTOS DE ALTO IMPACTO` e o
> `=== VEREDITO DE RISCO MACRO ===` (cada bloco 1-8 pode virar uma única linha-resumo ou ser omitido).

## Persistência (OBRIGATÓRIA ao final)

> Sem este passo o gate de `brain-read` não sabe que o briefing "já rodou hoje". É o que torna a
> verificação determinística (filesystem) em vez de depender da memória do LLM.

1. **Gravar o briefing do dia** em `wiki/briefings/{AAAA-MM-DD}.md` (data em **BRT**), partindo de
   `wiki/briefings/_template.md`. Se o arquivo do dia já existir, **sobrescrever** (é o refresh do
   dia, ex.: re-execução por evento 🔴). Preencher no header: Data/Hora BRT, dia da semana,
   `Horizonte` (`hoje`/`semana` — o gate lê este campo), `Detalhe` e o contexto de mercado.
2. **Append em `wiki/log.md`** (mesma linha que as demais operações):
   `## [AAAA-MM-DD HH:MM] briefing | {horizonte} | Veredito: {postura sugerida} | 🔴: {top eventos do dia}`.
3. **Backlinks:** manter `## Backlinks` com `[[log]]` e, se houver sessão de análise do dia,
   adicionar o backlink bidirecional.

> ⚠️ `raw/` é imutável — NÃO gravar lá. O cache de feeds (`raw/feeds/latest.md`) é só leitura aqui.
