---
type: session
symbol: {SYMBOL}
tf: {TF}
date: {YYYY-MM-DD}
class: {BTC|BTC+ETH|BTC+ALTCOIN|ALTCOIN|EQUITIES|WATCHLIST|DAILY|CYCLE}
layout: {layout ativo}
bias: {LONG|SHORT|NEUTRO}
price: {preço}
confluence: {N}
regime: {risk-on|risk-off|misto}
setup: {slug-do-setup|null}
result: open
tags: [class/{ALTCOIN}, bias/{LONG}, regime/{misto}]
---

# Sessão: {SYMBOL} {TIMEFRAME} — {YYYY-MM-DD HH:MM}

> Gerado automaticamente pelo MCP. Não editar manualmente.
> O **frontmatter acima** é a camada estruturada (Dataview/Bases/Graph). `result` passa a
> ✅/❌/⚪ quando a previsão é graduada.

## Contexto
- **Ativo:** {SYMBOL}
- **Timeframe principal:** {TF}
- **Hora:** {HH:MM} BRT

## Brain Read Summary (OBRIGATÓRIO — preencher antes de iniciar análise técnica)
- **Erros prevenidos:** _(erros de mistakes.md aplicáveis a este setup)_
  - ⚠️ [categoria] [YYYY-MM-DD]: [resumo do erro] → Prevenção: [ação tomada]
  - _(ou "Nenhum erro relevante nos últimos 10 registros")_
- **Insights ativados:** _(insights de insights.md aplicados nesta análise)_
  - 💡 [resumo do insight aplicado]
  - _(ou "Nenhum insight diretamente aplicável")_
- **Padrões monitorados:** _(padrões de patterns.md potencialmente ativos)_
  - 🔄 [nome do padrão] (Status: OBSERVAÇÃO/VALIDADO/CONSOLIDADO)
  - _(ou "Nenhum padrão ativo identificado")_
- **Previsão anterior fechada:** _(link para sessão anterior ou "nenhuma aberta para este ativo")_

## Contexto Macro (preenchido pelo MACRO SCAN)
<!-- OBRIGATÓRIO para BTC/ETH/Altcoins. Preenchido automaticamente antes da análise do ativo. -->
- **Regime:** Risk-On | Risk-Off | Misto

| Ativo | Preço | Tendência D | Sinal | Correlação BTC |
|-------|-------|-------------|-------|----------------|
| USDT.D | | | | inversa |
| S&P 500 / ES1! | | | | positiva |
| Ouro | | | | contextual |
| DXY | | | | inversa |
| TOTAL | | | | direta |
| TOTAL2 | | | | direta |
| TOTAL3 | | | | direta |
| Petróleo | | | | inversa (inflação) |

**Leitura macro:** _{Risk-On/Risk-Off/Misto — justificativa em 1-2 linhas}_

## Dados Capturados
### Quote
- Open: | High: | Low: | Close: | Volume:

### Indicadores
| Indicador | Valor |
|-----------|-------|

### Níveis (Pine Lines/Labels)
| Nível | Tipo | Valor |
|-------|------|-------|

## Análise Técnica (OBRIGATÓRIO — preencher cada item)

### MTF (Multi-Timeframe)
- **Mensal (M):** _{tendência de ciclo HH/HL ou LH/LL, RSI/MACD mensal, alvo mensal, teto/piso de ciclo}_ ← obrigatório no macro (CYCLE/swing/classes); recomendado em scalp
- **Semanal:** _{regime, tendência HH/HL ou LH/LL}_
- **Diário:** _{ciclo, sobrecompra/venda}_
- **4H:** _{EMA 200 acima/abaixo, estrutura}_
- **1H:** _{zona de entrada, FVG, OB}_

### SMC (Smart Money Concepts)
- **Estrutura:** BOS/CHoCH _{direção}_ no _{TF}_
- **FVG:** _{zona ou N/A}_
- **Order Block:** _{zona ou N/A}_
- **Liquidez:** EQH/EQL/PDH/PDL _{zonas}_
- **Traps:** _{Bull Trap/Bear Trap/Stop Hunt ou N/A}_

### Wyckoff
- **Fase:** _{Acumulação/Markup/Distribuição/Markdown ou N/A}_
- **Evento:** _{Spring/UT/LPS/LPSY ou N/A}_
- **Esforço × Resultado:** _{absorção detectada? sim/não}_

### Fibonacci + Price Action
- **Fibonacci:** Golden Zone _{zona}_ do impulso _{de→para}_
- **Confluência:** _{Golden Zone + FVG + OB = sim/não}_
- **Padrão de candle:** _{Engulfing/Pin Bar/Doji ou N/A}_

### Indicadores (valor por TF + direção + cruzamento)
<!-- RSI e MACD: ler M/W/D/4H/1H (M obrigatório no macro). StochRSI: W/1H/15M (sem M — lento demais como gatilho). -->
| Indicador | Valor por TF | Direção | Cruzamento | Sinal |
|-----------|--------------|---------|------------|-------|
| RSI (14) | _{M:__ / W:__ / D:__ / 4H:__ / 1H:__}_ | _{subindo/descendo/achatando}_ | _{RSI × SMA: acima/abaixo · RSI × 50 no M}_ | _{divergência mensal?}_ |
| Stoch RSI %K/%D | _{W:__ / 1H:__ / 15M:__}_ | _{subindo/descendo}_ | _{%K × %D: bullish/bearish}_ | |
| MACD | _{M:__ / W:__ / D:__ / 4H:__}_ | _{convergindo/divergindo}_ | _{MACD × Signal: cross up/down · vs zero no M}_ | _{acima/abaixo de zero}_ |
| MACD Histograma | _{M / W / D / 4H}_ | _{crescente/decrescente}_ | | |
| ADX | | _{DI+ vs DI-}_ | | |
| EMA 50/200 | _{+ EMA mensal / 200W como ref. de ciclo}_ | _{inclinação}_ | _{Golden/Death Cross}_ | |

### Bias
_{LONG / SHORT / NEUTRO}_
- Liquidez por pavios: acima/abaixo/neutra
- USDT.D: confirma/nega/indisponível
- Macro: Risk-On/Risk-Off/Misto
- Confiança: alta/média/baixa

### Playbook Match
- **Playbook:** _{1/2/3/4 ou Nenhum}_
- **Checklist de entrada:** _{X/8 critérios atendidos}_

### Setups Identificados
<!-- OBRIGATÓRIO: sempre preencher, mesmo que "Nenhum setup reconhecido nesta sessão" -->
_{links para wiki/setups/ ou "Nenhum setup reconhecido nesta sessão"}_

## Plano de Operação
- **Entrada:** $___
- **Stop Loss:** $___
- **TP1:** $___
- **TP2:** $___
- **R:R planejado:** ___:1

## Comparação com Sessão Anterior
- **Sessão anterior:** [[YYYY-MM-DD-SYMBOL-TF]] ou "primeira sessão deste ativo"
- **Previsão anterior:** _(o que foi previsto na sessão anterior)_
- **O que mudou:** _(diferença estrutural, de indicadores ou de contexto macro)_
- **Previsão anterior acertou?** ✅ / ❌ / ⚪ / ⏳

## Ação
- [ ] Setup válido para entrada
- [ ] Aguardar confirmação
- [ ] Sem oportunidade

## Resultado (preenchido no FEEDBACK)
<!-- Este bloco é atualizado quando o mercado confirma/nega a tese -->
- **Outcome:** ⏳ aberta
- **Entrada real:** $___
- **Saída real:** $___
- **R:R alcançado:** ___:1
- **P&L estimado:** ___% do capital
- **Tempo na operação:** ___ horas
- **Setup utilizado:** [[nome-do-setup]] ou _nenhum_

## Aprendizados desta Sessão (OBRIGATÓRIO — preencher ao escrever o brain)
- **Insight gerado:** _(o que aprendi nesta sessão que ainda não estava em insights.md — ou "nenhum novo")_
- **Padrão confirmado/negado:** _(nome do padrão + resultado — ou "nenhum padrão testado")_
- **Indicador que surpreendeu:** _(indicador + como se comportou diferente do esperado — ou "nenhum")_
- **Setup promovido para wiki/setups/?** _(sim → [[link]] | candidato → motivo | não → motivo)_

## Screenshot
<!-- screenshot: {YYYY-MM-DD}-{SYMBOL}-{TF}.png -->

## Backlinks
- `{SYMBOL}` — replace with actual asset wikilink
- `{SETUP}` — replace with actual setup wikilink
