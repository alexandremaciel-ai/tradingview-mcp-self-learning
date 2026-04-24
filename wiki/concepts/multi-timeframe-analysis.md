# Multi-Timeframe Analysis (MTF)

> O mercado é fractal — a tendência de tempo maior sempre domina os tempos menores.
> Toda decisão começa pelo macro e desce até o gatilho de entrada.
> Atualizado: 2026-04-23 com KB v1.0 (hierarquia completa + filtros direcionais)

---

## 1. Hierarquia de Timeframes

| Timeframe | Função |
|---|---|
| **Mensal / Semanal** | Tendência primária — define viés macro (Bull / Bear) |
| **Diário / 12H** | Tendência secundária — ciclos médio prazo, sobrecompra/venda estrutural |
| **4H / 2H** | Tendência intermediária — filtro direcional (EMA 200), estrutura SMC |
| **1H / 30M** | Confirmação de setup — BOS, CHoCH, FVG de entrada |
| **15M / 5M** | Gatilho de execução — candle de confirmação, volume, ATR |

---

## 2. Regras Direcionais (Top-Down)

- **Tendência Primária:** Mensal formando LH/LL com indicadores bearish = macro bearish. Qualquer alta nos TFs menores é retração.
- **Regra da Retração:**
  - Em macro bearish → altas no Diário/4H são oportunidades de **Short** (não reversões)
  - Em macro bullish → correções no Diário/4H são oportunidades de **Long**
- **RSI Primário:** RSI Semanal < 50 = tendência primária bearish. Qualquer long é counter-trend e exige R:R ≥ 2x e gestão apertada.

---

## 3. EMA 200 como Filtro Direcional Absoluto

- Preço **abaixo** da EMA 200 no **4H** → Modo **APENAS SHORT**
- Preço **acima** da EMA 200 no **4H** → Modo **APENAS LONG**
- Em dúvida ou preço na EMA → aguardar reteste e fechamento de candle além da EMA
- EMA 200 no 1H como filtro secundário para setups de curto prazo

---

## 4. Conflito de Timeframes

- Se 4H contradiz 1D → **aguardar resolução** antes de entrar
- Se 4H bearish + ADX > 25 → **hard block em LONG** independente do 1H
- Se 1H bullish mas 4H abaixo da EMA 200 → **apenas scalp de alta confiança**, não swing

---

## 5. Sequência de Análise (Operacional)

1. **Mensal/Semanal:** Viés macro, RSI primário, EMA 200 semanal, estrutura LH/LL ou HH/HL
2. **Diário/12H:** Ciclo secundário, zonas chave, sobrecompra/venda estrutural
3. **4H:** Confirmar bias, detectar CHoCH/BoS, verificar ADX, EMA 200
4. **1H:** Identificar zona de entrada, FVG, OB, RSI divergência
5. **15M:** Refinamento de entrada, BOS de gatilho
6. **5M:** Timing de execução (opcional)

---

## 6. Teto/Piso Magnético de RSI entre Timeframes

- RSI sobrecomprado no **Diário** = limita a retração do **Mensal** (resistência de RSI)
- RSI sobrecomprado no **12H** = limita a retração do **Quinzenal**
- RSI sobressaturado nos TFs maiores = setups no TF menor têm upside limitado

---

## Backlinks
- [[ADX]]
- [[SMC]]
- [[conservative-trend-follower-v2]]
- [[BTCUSD]]
- [[rsi-divergences]]
- [[trade-playbooks]]
- [[fibonacci-structural]]
