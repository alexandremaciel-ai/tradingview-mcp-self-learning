# BTCUSDLONGS e BTCUSDSHORTS — Posicionamento de Margem Bitfinex

> Criado: 2026-05-27
> Categoria: Market Microstructure / Posicionamento / Squeeze Detection

## Definição

`BTCUSDLONGS` e `BTCUSDSHORTS` são tickers disponíveis no TradingView que mostram o **volume total de posições de margem** (long e short, respectivamente) abertas na exchange **Bitfinex** para o par BTC/USD.

- **BTCUSDLONGS:** Número total de contratos de margem comprados (long) abertos na Bitfinex
- **BTCUSDSHORTS:** Número total de contratos de margem vendidos (short) abertos na Bitfinex

Apesar de representarem apenas a Bitfinex, esses dados são considerados um **proxy confiável do sentimento institucional** porque a Bitfinex historicamente concentra traders de maior porte e market makers.

---

## Por que usar na análise de BTC

1. **Dados reais de posicionamento:** Diferente de indicadores de sentimento baseados em surveys ou social media, BTCUSDLONGS/SHORTS mostram dinheiro real em risco.
2. **Detecção precoce de squeeze:** Desequilíbrios extremos entre longs e shorts precedem frequentemente movimentos violentos de preço.
3. **Divergências preço × posições:** Quando o preço sobe mas as posições long diminuem (ou vice-versa), isso revela a ação real do smart money.
4. **Disponíveis diretamente no TradingView:** Não requer APIs externas — basta `chart_set_symbol({symbol: "BTCUSDLONGS"})`.

---

## Ratio L/S (Long/Short Ratio via Margem)

**Fórmula:** `Ratio = BTCUSDLONGS / BTCUSDSHORTS`

| Ratio | Significado | Risco |
|-------|-------------|-------|
| > 10.0 | Extremamente mais longs que shorts | 🔴 Long Squeeze Risk muito alto |
| 5.0–10.0 | Fortemente skewed para longs | 🟠 Long Squeeze Risk alto |
| 2.0–5.0 | Moderadamente mais longs | 🟡 Normal-bullish |
| 1.0–2.0 | Equilíbrio saudável | 🟢 Neutro |
| 0.5–1.0 | Mais shorts que longs | 🟡 Short Squeeze Risk moderado |
| < 0.5 | Extremamente mais shorts | 🔴 Short Squeeze Risk muito alto |

---

## Sinais de Squeeze

### Condições para Short Squeeze
- [ ] BTCUSDSHORTS subindo rapidamente (>20% em 7 dias)
- [ ] BTCUSDLONGS estável ou caindo
- [ ] Ratio L/S < 1.0
- [ ] Preço próximo de resistência chave
- [ ] Funding Rate negativa (shorts pagando)
- [ ] USDT.D caindo (risk-on)

**Mecânica:** Shorts acumulados são "combustível". Quando o preço rompe resistência, shorts são forçados a recomprar → cascata de compras → short squeeze.

### Condições para Long Squeeze
- [ ] BTCUSDLONGS em máxima histórica ou extremo relativo
- [ ] BTCUSDSHORTS em mínima ou muito baixo
- [ ] Ratio L/S > 5.0
- [ ] Preço esticado após rally prolongado
- [ ] Funding Rate muito positiva (longs pagando)
- [ ] RSI diário > 70 (sobrecompra)

**Mecânica:** Longs excessivos sem novos compradores. Quando o preço cai, longs são forçados a vender → cascata de vendas → long squeeze.

---

## Divergências de Alta Convicção

| Condição | Tipo | Interpretação |
|----------|------|--------------|
| Preço ↑ + Longs ↓ | Bearish Divergence | Smart money está saindo. Rally sem convicção. |
| Preço ↓ + Longs ↑ | Bullish Divergence | Smart money está acumulando na queda. |
| Preço ↑ + Shorts ↑ | Squeeze Setup | Shorts estão apostando contra — combustível para mais alta. |
| Preço ↓ + Shorts ↓ | Capitulação Short | Vendedores desistindo. Fundo pode estar próximo. |
| Preço → lateral + Longs ↑↑ | ⚠️ Armadilha | Acumulação unilateral = vulnerável a dump. |

---

## Workflow MCP (passos exatos)

```
chart_set_symbol({symbol: "BTCUSDLONGS"})
chart_set_timeframe({timeframe: "D"})
quote_get()
data_get_study_values()
```

```
chart_set_symbol({symbol: "BTCUSDSHORTS"})
chart_set_timeframe({timeframe: "D"})
quote_get()
data_get_study_values()
```

**Depois:** Calcular Ratio L/S manualmente = valor_longs / valor_shorts

---

## Integração com Outros Indicadores

### Trio de Derivativos Completo
1. **BTCUSDLONGS/SHORTS** → posicionamento real de margem (Bitfinex)
2. **Funding Rate** → custo de manter posições alavancadas (ver [[funding-rate]])
3. **Open Interest** → volume total de contratos abertos (ver [[open-interest]])
4. **Long/Short Ratio (Perpétuos)** → LSR de futuros perpétuos (ver [[long-short-ratio]])

### Confluência máxima para squeeze
- BTCUSDLONGS em extremo + FR muito positiva + OI alto + LSR > 1.5 → **Long Squeeze iminente**
- BTCUSDSHORTS em extremo + FR negativa + OI alto + LSR < 0.5 → **Short Squeeze iminente**

### Cruzamento com USDT.D
- BTCUSDSHORTS subindo + USDT.D caindo → contradição (shorts abrindo mas capital saindo de stablecoins) → provável short squeeze
- BTCUSDLONGS caindo + USDT.D subindo → dupla confirmação bearish → longs reduzindo + capital voltando para stablecoins

---

## Limitações

1. **Apenas Bitfinex:** Não inclui dados de Binance, Bybit, OKX, etc. É um proxy, não o quadro completo.
2. **Margem vs Futuros:** BTCUSDLONGS/SHORTS medem margem spot, não futuros perpétuos. São complementares ao LSR de perpétuos, não substitutos.
3. **Delays possíveis:** Dados podem ter atraso de alguns minutos dependendo do feed do TradingView.
4. **Tamanho absoluto vs relativo:** O número absoluto importa menos que a tendência e o nível relativo (comparado com histórico recente de 30-90 dias).

---

## Backlinks
- [[short-long-squeeze]] — contexto teórico de squeezes
- [[long-short-ratio]] — LSR de futuros perpétuos (complementar)
- [[open-interest]] — OI como confirmação de squeeze
- [[funding-rate]] — FR como confirmação de desequilíbrio
- [[liquidation-heatmap]] — onde estão os stops que serão acionados
- [[liquidity-wicks-trap-short-usdtd]] — estratégia de pavios e USDT.D
- [[btc-macro-correlations]] — contexto macro para BTC
- [[bull-bear-traps]] — squeezes frequentemente criam traps
