# RSI + StochRSI — Estratégia Combinada para BTC

> Estratégia de uso conjunto do RSI clássico e RSI Estocástico para maximizar precisão de entrada.
> Princípio: RSI define a tendência, StochRSI define o timing. Nunca usar isolados.
> Compilado: 2026-05-29

---

## Filosofia Core

| Indicador | Papel | Timeframe Ideal | Força | Fraqueza |
|-----------|-------|-----------------|-------|----------|
| **RSI (14)** | Confirmar tendência de ciclo/regime + divergências macro | M / W / D / 4H | Suave, confiável, filtra ruído (M/W = ciclo/regime, D/4H = operacional) | Lento, fica "preso" em sobrecompra/venda por tempo prolongado |
| **StochRSI** | Gatilho de entrada/saída + timing preciso | 1H / 15M | Ultra-rápido, marca topos/fundos locais | Ruidoso, gera sinais falsos em alta volatilidade. _Mensal é lento demais — não usar como gatilho_ |

> **Regra de ouro:** O RSI diz **"para onde"**. O StochRSI diz **"quando"**.
> Nunca entrar apenas com StochRSI sem confirmação direcional do RSI.

---

## Workflow Operacional — Passo a Passo

### Passo 1: RSI no Timeframe Maior (M / W / D / 4H) — Direção

> **Hierarquia de direção:** o RSI **Mensal** define a direção de **ciclo** e o **Semanal** o regime — ambos prevalecem sobre o D/4H. Operar contra o RSI M/W é counter-trend e exige R:R ≥ 2 e gestão apertada. M/W são obrigatórios no macro (CYCLE/swing/classes).

Verificar primeiro M/W (ciclo/regime), depois descer para o diário ou 4H (direção operacional):

| Leitura RSI | Direção | Interpretação | Operações Permitidas |
|-------------|---------|---------------|---------------------|
| RSI > 50 + subindo | Bullish | Momentum comprador ativo | ✅ Longs apenas |
| RSI > 70 + subindo | Bullish forte | Tendência forte, mas sobrecompra | ✅ Longs com cautela (trailing stop) |
| RSI > 70 + divergência bearish | Alerta de reversão | Preço HH + RSI LH = exaustão | ⚠️ Nenhum long novo, preparar short |
| RSI < 50 + descendo | Bearish | Momentum vendedor ativo | ✅ Shorts apenas |
| RSI < 30 + descendo | Bearish forte | Tendência forte, mas sobrevenda | ✅ Shorts com cautela |
| RSI < 30 + divergência bullish | Alerta de reversão | Preço LL + RSI HL = exaustão | ⚠️ Nenhum short novo, preparar long |
| RSI 40-60 + achatando | Neutro | Sem direção clara | ⛔ Sem operação — aguardar resolução |

**Checklist RSI HTF:**
```
□ RSI está acima ou abaixo de 50? → Define o lado (long/short)
□ RSI está em zona extrema (>70 / <30)? → Ajustar gestão de risco
□ Existe divergência clássica? → Sinal de exaustão iminente
□ RSI × SMA(RSI): cruza acima = bullish / abaixo = bearish
□ Direção da inclinação do RSI: subindo/descendo/plano
```

### Passo 2: StochRSI no Timeframe Menor (1H / 15M) — Timing

**Somente após o RSI HTF definir a direção**, descer para o StochRSI:

#### Para Longs (RSI HTF > 50 confirma tendência de alta):
| Condição StochRSI | Zona | Ação |
|-------------------|------|------|
| %K cruza %D para cima | Sobrevenda (<20) | 🟢 **ENTRADA LONG** — máxima confluência |
| %K cruza %D para cima | Neutro (20-80) | 🟡 Entrada possível se preço em suporte (FVG/OB) |
| %K cruza %D para baixo | Sobrecompra (>80) | 🔴 Fechar parcial / trailing stop — NÃO shortear |
| %K e %D ambos < 20 | Oversold extremo | 🟢🟢 Zona de acumulação — DCA agressivo se HTF bullish |

#### Para Shorts (RSI HTF < 50 confirma tendência de baixa):
| Condição StochRSI | Zona | Ação |
|-------------------|------|------|
| %K cruza %D para baixo | Sobrecompra (>80) | 🟢 **ENTRADA SHORT** — máxima confluência |
| %K cruza %D para baixo | Neutro (20-80) | 🟡 Entrada possível se preço em resistência (FVG/OB) |
| %K cruza %D para cima | Sobrevenda (<20) | 🔴 Fechar parcial / trailing stop — NÃO longear |
| %K e %D ambos > 80 | Overbought extremo | 🟢🟢 Zona de distribuição — short agressivo se HTF bearish |

### Passo 3: Confirmação de Confluência

A entrada de **máxima convicção** combina:
1. ✅ RSI HTF (D/4H) confirmando direção (acima/abaixo de 50)
2. ✅ StochRSI LTF (1H/15M) dando gatilho de cruzamento em zona extrema
3. ✅ Preço em zona de confluência técnica (FVG + OB + Fibonacci Golden Zone)
4. ✅ Volume acima da média (confirma força do movimento)

**Mínimo para entrar:** 3 de 4. Todos os 4 = alta convicção.

---

## Armadilhas Comuns — O Que NÃO Fazer

### ❌ Erro 1: Shortear porque StochRSI está overbought com RSI HTF bullish
> Em tendência de alta forte, o StochRSI pode ficar >80 por horas/dias.
> StochRSI overbought + RSI diário >50 e subindo = **continuação**, não reversão.
> **Correção:** Use o reset de StochRSI overbought como sinal de **comprar o pullback**, não de shortear.

### ❌ Erro 2: Longear porque StochRSI está oversold com RSI HTF bearish
> Em tendência de baixa forte, o StochRSI pode ficar <20 por horas/dias.
> StochRSI oversold + RSI diário <50 e descendo = **continuação bearish**, não fundo.
> **Correção:** Aguardar RSI diário reverter acima de 50 antes de considerar longs.

### ❌ Erro 3: Usar StochRSI no gráfico diário como gatilho
> StochRSI no diário é lento demais e perde sua vantagem de sensibilidade.
> **Correção:** StochRSI só no 1H ou 15M para timing. RSI no D/4H para direção.

### ❌ Erro 4: Ignorar divergência RSI porque StochRSI ainda não cruzou
> Divergência RSI no diário = sinal de exaustão macro com semanas de antecedência.
> StochRSI pode demorar para confirmar. Não ignorar a divergência — ajustar posição.

---

## Cenários Práticos — BTC

### Cenário 1: Bull Pullback (comprar a retração)
```
RSI Diário: 58, subindo, acima da SMA → BULLISH confirmado
RSI 4H: 45, tocou zona neutra → pullback saudável
StochRSI 1H: %K cruza %D para cima em zona <20 → GATILHO DE COMPRA
Preço: em FVG bullish do 4H + Fibonacci 0.618

→ LONG com alta convicção. Stop abaixo do FVG.
```

### Cenário 2: Bear Rally (vender o repique)
```
RSI Diário: 38, descendo, abaixo da SMA → BEARISH confirmado
RSI 4H: 55, repicando para zona neutra → bounce técnico
StochRSI 1H: %K cruza %D para baixo em zona >80 → GATILHO DE VENDA
Preço: em FVG bearish do 4H + Fibonacci 0.618

→ SHORT com alta convicção. Stop acima do FVG.
```

### Cenário 3: RSI Divergência Macro + StochRSI Timing
```
RSI Diário: 72, divergência bearish (preço ATH, RSI topo menor)
RSI 4H: 65, achatando → perda de momentum
StochRSI 1H: %K cruza %D para baixo em >80 → GATILHO

→ SHORT ou fechar longs. A divergência diária + StochRSI timing = setup de reversão.
```

### Cenário 4: Falso sinal StochRSI (armadilha)
```
RSI Diário: 62, subindo → tendência de alta intacta
StochRSI 15M: %K cruza %D para baixo em >80

→ NÃO shortear! RSI HTF é bullish. O StochRSI está apenas resetando.
→ AGUARDAR: StochRSI voltar para <20 e cruzar para cima = próxima compra.
```

---

## Parâmetros Recomendados

| Indicador | Período | Timeframe Ideal | Configuração TV |
|-----------|---------|-----------------|----------------|
| RSI | 14 | M, W, D, 4H | Padrão + SMA(14) sobreposta (M/W = ciclo/regime, obrigatórios no macro) |
| StochRSI | 14, 14, 3, 3 | 1H, 15M | %K=3, %D=3, RSI Length=14, Stoch Length=14 (sem M — lento demais como gatilho) |

**Configuração no TradingView:**
- RSI: Adicionar "Relative Strength Index" → marcar "RSI-based MA" para ver o cruzamento RSI×SMA
- StochRSI: Adicionar "Stochastic RSI" → usar K=3, D=3 para suavizar (reduz ruído)

---

## Integração com o Checklist de Análise

Na Fase 6 do checklist obrigatório, a leitura combinada deve ser:

```
RSI (14) M/W/D/4H: [valores] [direção: subindo/descendo/plano] [RSI×SMA: acima/abaixo]
  → Ciclo (M) e regime (W) + direção operacional (D/4H)
  → Direção confirmada: LONG ONLY / SHORT ONLY / NEUTRO
StochRSI 1H/15M: %K=[valor] %D=[valor] [cross: bull/bear/neutro] [zona: OB/OS/neutro]
  → Gatilho: SIM (cruzamento em zona extrema) / NÃO (aguardar)
Confluência RSI+StochRSI: [alta/média/baixa]
```

---

## Backlinks
- [[rsi-divergences]] — RSI clássico: divergências, sobreextensão, cruzamento RSI×SMA
- [[multi-timeframe-analysis]] — RSI HTF define direção, StochRSI LTF executa
- [[trade-playbooks]] — Playbook 1 e 2 usam RSI+StochRSI para timing
- [[fibonacci-structural]] — Golden Zone + StochRSI oversold cross = entrada sniper
- [[SMC]] — FVG/OB como zona + StochRSI como gatilho temporal
- [[macd]] — MACD confirma tendência que RSI e StochRSI temporizam
- [[btc-cycle-analysis]] — RSI semanal divergências marcam topos/fundos de ciclo
