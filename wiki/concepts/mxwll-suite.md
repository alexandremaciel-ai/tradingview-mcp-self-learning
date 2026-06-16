# Mxwll Suite

> Criado: 2026-06-16
> Categoria: Indicador / All-in-One (Estrutura + Fibonacci + Sessões + Liquidez)

## Definição
**Mxwll Suite** é um indicador "tudo-em-um" sobreposto ao gráfico, presente no layout **Emas**. Combina, num único study, quatro camadas de leitura que normalmente exigiriam vários indicadores:

1. **Estrutura de mercado (SMC-style):** marca automaticamente `BoS`/`CHoCH` (swing) e `I-BoS`/`I-CHoCH` (internos), além de pivôs `HH`/`HL`/`LH`/`LL` — a mesma gramática do [[smc-luxalgo]]/[[SMC]].
2. **Fibonacci automático:** plota os níveis `0.236 / 0.382 / 0.5 / 0.618 / 0.786` da última perna de estrutura (Golden Zone embutida).
3. **Dashboard de sessões (table):** sessão atual, contagem para o fechamento, próxima sessão e abertura, e classificação de **volume 4h e 24h** (Very High / High / Average / Low).
4. **Níveis de liquidez / S-R:** centenas de linhas horizontais (S/R + liquidez histórica) ao longo de todo o range.

## Como ler (MCP / pine tools)
- `data_get_pine_tables(study_filter="Mxwll")` → dashboard de sessão (ex.: `Session: New York`, `Session Close: 3h8m`, `Next Session: Asia`, `4-Hr Volume: Very High`).
- `data_get_pine_labels(study_filter="Mxwll")` → estrutura (`BoS`/`CHoCH`/`I-BoS`/`I-CHoCH`/`HH`/`HL`/`LH`/`LL`) **e** os níveis de Fibonacci com seus preços.
- `data_get_pine_lines(study_filter="Mxwll")` → níveis horizontais de S/R e liquidez. **São centenas** (≈500) → sempre **filtrar dentro de ±5% do preço** para poupar contexto.

## Leituras práticas
- **BoS** = continuação da tendência (entrar a favor); **CHoCH** = primeiro sinal de reversão (aguardar confirmação no TF inferior). Internos (`I-`) são ruído de TF baixo — cruzar sempre com o swing.
- **Golden Zone (0.5–0.618)** da última perna + um nível S/R denso no mesmo preço = zona de entrada de alta convicção.
- O **dashboard de sessão** dá contexto de liquidez (NY/Londres/Ásia) e a classificação de volume confirma se o movimento atual tem força — confluência com [[market-hours-traditional-finance]].
- Clusters densos de linhas horizontais = ímãs de preço / zonas de defesa (leitura semelhante à do [[whale-liquidity-absorption]]).

## Uso no contexto deste wiki
- No layout **Emas**, o Mxwll Suite cobre a **Fase 3 (SMC)** e parte da **Fase 4 (Fibonacci + S/R)** do [[technical-checklist]] — junto com [[supertrend]] (tendência) e EMA Cross ([[sma-cross]]).
- É o **eixo de estrutura/liquidez** desse layout (não há LuxAlgo SMC nem Whale aqui).

## Limitações
- Excesso de níveis de liquidez → ruído se não filtrar perto do preço.
- Estrutura interna (`I-CHoCH`/`I-BoS`) gera muitos sinais de TF baixo — usar só o swing para tese direcional.
- Não substitui o on-chain/ciclo: é price-action puro.

## Backlinks
- [[SMC]] — mesma gramática BoS/CHoCH/HH/HL/LH/LL
- [[smc-luxalgo]] — alternativa de SMC no layout Liquidity e SMC
- [[fibonacci-structural]] — Golden Zone automática
- [[supertrend]] — par de tendência no layout Emas
- [[sma-cross]] — EMA Cross (ribbon) como filtro de tendência no mesmo layout
- [[market-hours-traditional-finance]] — dashboard de sessões
- [[layouts]]
- [[indicators]]
