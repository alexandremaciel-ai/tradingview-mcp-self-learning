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

## 5. Cruzamento RSI × SMA(RSI)

> **Não basta ler o valor do RSI. A direção e o cruzamento com sua SMA definem o momentum.**

- **RSI cruza SMA para cima:** momentum comprando força → bullish
- **RSI cruza SMA para baixo:** momentum perdendo força → bearish
- **RSI acima da SMA + subindo:** tendência de momentum saudável
- **RSI abaixo da SMA + descendo:** momentum em deterioração
- **RSI achatando na SMA:** indecisão, aguardar resolução

### Uso Operacional
- Em zona de sobrevenda (<30): RSI cruza SMA para cima = gatilho de Long
- Em zona de sobrecompra (>70): RSI cruza SMA para baixo = gatilho de Short
- Na zona neutra (40-60): cruzamento confirma direção do momentum, não é gatilho isolado

---

## 6. RSI Estocástico (Stochastic RSI)

> Mede a posição do RSI dentro do seu próprio range. Mais sensível que o RSI clássico.

### Componentes
- **%K:** linha rápida do Stoch RSI
- **%D:** SMA do %K (linha lenta, sinal)

### Sinais
| Cenário | %K vs %D | Zona | Ação |
|---------|----------|------|------|
| %K cruza %D para cima | Cross up | Sobrevenda (<20) | **Long de alta convicção** |
| %K cruza %D para baixo | Cross down | Sobrecompra (>80) | **Short de alta convicção** |
| %K cruza %D para cima | Cross up | Zona neutra | Confirmação de momentum, não gatilho |
| %K cruza %D para baixo | Cross down | Zona neutra | Alerta de perda de momentum |

### Direção das Linhas
- **Ambas subindo:** momentum bullish ativo
- **Ambas descendo:** momentum bearish ativo
- **%K girando, %D ainda plano:** sinal prematuro, aguardar confirmação
- **Reset de oversold em tendência de alta:** continuação bullish (comprar o dip)
- **Reset de overbought em tendência de baixa:** continuação bearish (vender o rally)

---

## 5. Integração com MTF

- Divergência no **4H** + confirmação no **1H** = setup de entrada de alta confiança
- Divergência no **Diário** + confirmação no **4H** = swing trade de alta confiança
- Divergência no **1H** contra tendência 4H = baixa convicção, evitar

---

## 7. Estratégia Combinada RSI + StochRSI

> **O RSI diz "para onde". O StochRSI diz "quando".**

A abordagem profissional para BTC combina ambos:

1. **RSI (D/4H) → Direção:** RSI > 50 = Long only. RSI < 50 = Short only. Divergência = alerta de reversão.
2. **StochRSI (1H/15M) → Timing:** %K cruza %D em zona extrema (<20 ou >80) = gatilho de entrada.
3. **Nunca operar StochRSI isolado** — em tendência forte, StochRSI fica "preso" em zona extrema por horas.

**Armadilhas críticas:**
- StochRSI overbought + RSI HTF bullish = **continuação**, não reversão
- StochRSI oversold + RSI HTF bearish = **continuação bearish**, não fundo

Ver estratégia completa: [[rsi-stochrsi-combined]]

---

## Backlinks
- [[rsi-stochrsi-combined]] — estratégia combinada RSI + StochRSI para BTC
- [[SMC]] — FVG + divergência RSI = confluência máxima
- [[multi-timeframe-analysis]]
- [[trade-playbooks]]
- [[fibonacci-structural]] — Golden Zone + divergência = entrada sniper
- [[btc-cycle-analysis]] — RSI semanal divergências em topos/fundos de ciclo

