# RSI — Divergências e Sobreextensão

> Conceito crítico para identificar exaustão de tendência antes da reversão de candle.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Tipos de Divergência

### Divergência Bearish (Clássica)
- Preço faz **topo mais alto** (HH)
- RSI faz **topo mais baixo**
- Significado: força compradora exaurida, o movimento de alta perdeu momentum real
- **Ação:** Sinal de Short (confirmar com zona de resistência/FVG/OB)

### Divergência Bullish (Clássica)
- Preço faz **fundo mais baixo** (LL)
- RSI faz **fundo mais alto**
- Significado: força vendedora exaurida, a queda perdeu momentum real
- **Ação:** Sinal de Long (confirmar com zona de suporte/FVG/OB)

---

## 2. Divergências Ocultas (Continuação de Tendência)

### RSI Oculto Bearish
- Retração **menor** no RSI + retração **maior** no preço
- Significado: continuação da **baixa** — o RSI não caiu tanto mas o preço caiu mais
- **Ação:** Short na continuação da tendência

### RSI Oculto Bullish
- Retração **maior** no RSI + retração **menor** no preço
- Significado: continuação da **alta** — o RSI sofreu mais que o preço
- **Ação:** Long na continuação da tendência

---

## 3. Zonas de Alta Convicção

| Cenário | RSI | Preço | Ação |
|---------|-----|-------|------|
| Sobrecompra + div. bearish | > 70 | Em resistência | Short de alta convicção |
| Sobrevenda + div. bullish | < 30 | Em suporte | Long de alta convicção |
| Sobrecompra sem div. | > 70 | Em resistência | Aguardar — pode andar na banda |
| Sobrevenda sem div. | < 30 | Em suporte | Aguardar — pode andar na banda |

> **Regra:** Divergência sozinha não é suficiente. Sempre confirmar com zona de preço (FVG, OB, Fibonacci Golden Zone, EQH/EQL).

---

## 4. Parâmetros Operacionais

- **Período padrão:** RSI(14)
- **Timeframes para divergências:** 1H e 4H (gatilho e confirmação)
- **Timeframes para sobrecompra/venda macro:** Diário e Semanal
- **Sobrecompra limita retração:** RSI sobrecomprado no Diário = limite da retração do Mensal

---

## 5. Integração com MTF

- Divergência no **4H** + confirmação no **1H** = setup de entrada de alta confiança
- Divergência no **Diário** + confirmação no **4H** = swing trade de alta confiança
- Divergência no **1H** contra tendência 4H = baixa convicção, evitar

---

## Backlinks
- [[SMC]] — FVG + divergência RSI = confluência máxima
- [[multi-timeframe-analysis]]
- [[trade-playbooks]]
- [[fibonacci-structural]] — Golden Zone + divergência = entrada sniper
