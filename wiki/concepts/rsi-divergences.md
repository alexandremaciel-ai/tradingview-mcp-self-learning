# RSI — Divergências e Sobreextensão

> Conceito crítico para identificar exaustão de tendência antes da reversão de candle.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

> 🔴 **Como LER a divergência (Invariante 0 — fonte, não inferência):** os padrões abaixo descrevem o que
> o indicador (`RSI Divergences Pro` / V.V.I.R.) **já computa e plota**. Preferir SEMPRE a marca lida da
> fonte — `data_get_pine_lines(study_filter="RSI Div", verbose=true)` (cor=bull/bear) e, se decisivo,
> `capture_screenshot` do pane. `data_get_study_values` dá só o valor atual e **não** revela divergência.
> A comparação manual de pivôs (preço HH/LL vs RSI HH/LL) só vale com a **série puxada de fonte real**;
> nunca afirmar presença/ausência por estimativa → senão `DADO_INDISPONIVEL`. (Erro de ref.: CYCLE 28/06.)

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
- **Timeframes para divergências:** **5M, 15M, 1H, 4H, Diário, Semanal, Quinzenal (2W) e Mensal** — varrer TODOS quando o RSI está no layout (ordem HTF→LTF). 1H/15M/5M = gatilho; D/4H = swing; **1W/2W e 1M são PRIMORDIAIS para marcar topo/fundo de movimento (peso máximo)**. Peso por TF + quórum de confirmação na §6.5.
- **Timeframes para sobrecompra/venda macro:** Diário, Semanal e **Mensal**
- **Timeframe de ciclo:** RSI **Mensal** define teto/piso de ciclo e alvos mensais. Cruzamento mensal de 50 = virada macro. Divergência mensal = reversão de **CICLO** (peso máximo, acima da semanal) — confirmar com a semanal.
- **Sobrecompra limita retração:** RSI sobrecomprado no Semanal = limite da retração do Mensal; RSI mensal em extremo = teto/piso de ciclo que limita TODOS os TFs abaixo

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

### Divergências StochRSI
> StochRSI divergências são mais rápidas e ruidosas que RSI — usar apenas como gatilho em TF baixos (1H/15M), nunca como sinal isolado.

- **Divergência Bullish:** Preço LL + StochRSI %K HL em zona <20 → gatilho de compra rápido
- **Divergência Bearish:** Preço HH + StochRSI %K LH em zona >80 → gatilho de venda rápido
- **Oculta Bullish:** Preço HL + StochRSI LL → continuação de alta
- **Oculta Bearish:** Preço LH + StochRSI HH → continuação de baixa
- **⚠️ Regra:** StochRSI divergência SÓ vale se RSI HTF confirma a direção. Divergência StochRSI contra o RSI diário = ignorar.

> ⚠️ **Regular e Oculta dão sinais OPOSTOS no mesmo gráfico** (Regular = reversão · Oculta =
> continuação) — NUNCA tratar como equivalentes. Classificar o tipo ANTES de pontuar.

---

## 6.5 Divergência MTF — peso por TF e confirmação (obrigatório)

> Varredura **sempre do maior para o menor**: `1M → 2W → 1W → 1D` (HTF, definem o viés) ·
> `4H → 1H → 15m → 5m` (LTF, definem timing/gatilho). Separar SEMPRE Regular (reversão) de Oculta
> (continuação) por TF.

### Peso por timeframe (sub-score de FORÇA da divergência)
| TF | Peso | Papel |
|----|------|-------|
| 1M | 5 | Viés macro / topo-fundo de ciclo |
| 2W | 4 | Viés macro |
| 1W | 4 | Viés primário |
| 1D | 3 | Viés primário |
| 4H | 2 | Estrutura operacional |
| 1H | 1 | Timing |
| 15m/5m | 0.5 | Gatilho de entrada |

- **Sinal FORTE:** divergências do **mesmo lado** em ≥2 TFs com **peso somado ≥6** (ex.: 1W+1D=7).
- **Sinal FRACO / não-gatilho:** só em LTF com **peso somado <3** (sem suporte de HTF).
- **`DIV_CONTRA_HTF`:** divergência LTF **contra** o viés HTF = **não opera** (provável armadilha) —
  registrar o rótulo, não pontuar.

> Este é um **sub-score de força** que alimenta o critério `divergencia` (e `rsi`) do
> **[[confluence-score]]** — **não** é um segundo sistema 0–10 paralelo.

### Confirmação obrigatória — quórum ≥2-de-3 (divergência NUNCA opera sozinha)
Para promover qualquer divergência a sinal acionável, exigir **≥2 dos 3**:
1. **Volume/Delta confirmando** — nos layouts atuais = **Crypto Smart Volume** (Smart Score/Z
   climático/virando) + **VRVP** (delta/OBV clássico não está nos layouts).
2. **Zona SMC coincidente** — Order Block, FVG, liquidity sweep, EQH/EQL varridos.
3. **Gatilho de price action** — engolfo, pin bar, BOS/CHoCH no LTF.

> Este quórum ≥2-de-3 **substitui** (endurece) o antigo "confirmar com cruzamento RSI×SMA, CHoCH/BOS
> **ou** candle" (1-de-N). Uma fonte de verdade.

---

## 5. Integração com MTF

- Divergência no **Mensal** = reversão de **CICLO** (peso máximo) — confirma com Semanal; marca topos/fundos de ciclo
- Divergência no **4H** + confirmação no **1H** = setup de entrada de alta confiança
- Divergência no **Diário** + confirmação no **4H** = swing trade de alta confiança
- Divergência no **1H** contra tendência 4H = baixa convicção, evitar

---

## 7. Estratégia Combinada RSI + StochRSI

> **O RSI diz "para onde". O StochRSI diz "quando".**

A abordagem profissional para BTC combina ambos:

1. **RSI (M/W/D/4H) → Direção:** RSI > 50 = Long only. RSI < 50 = Short only (M = direção de ciclo, W = regime, ambos acima do D/4H). Divergência = alerta de reversão.
2. **StochRSI (1H/15M) → Timing:** %K cruza %D em zona extrema (<20 ou >80) = gatilho de entrada.
3. **Nunca operar StochRSI isolado** — em tendência forte, StochRSI fica "preso" em zona extrema por horas.

**Armadilhas críticas:**
- StochRSI overbought + RSI HTF bullish = **continuação**, não reversão
- StochRSI oversold + RSI HTF bearish = **continuação bearish**, não fundo

Ver estratégia completa: [[rsi-stochrsi-combined]]

---

## 8. Divergência de RSI no USDT.D — sinal inverso do BTC

> Em análise de BTC/ETH, varrer divergência de RSI **também no USDT.D é OBRIGATÓRIO**. O USDT.D
> (dominância do Tether) é **inversamente correlacionado** ao BTC — a divergência nele antecipa a
> reversão do BTC pelo lado oposto.

### Leitura inversa
| USDT.D (RSI / alvo projetado) | BTC | Significado |
|-------------------------------|-----|-------------|
| Div. **bullish** / RSI subindo / alvo de **alta** | **Baixista** | Capital indo p/ stable → BTC perde combustível |
| Div. **bearish** / RSI caindo / alvo de **baixa** | **Altista** | Capital saindo de stable p/ risco → BTC ganha combustível |
| Sem divergência / lateral | Neutro | Sem confirmação inversa — reduzir convicção |

- **Mesmos TFs do BTC:** W/D/4H/1H/15M, com **1W primordial** para topo/fundo de movimento.
- **Alvo projetado:** o V.V.I.R. exibe os preços onde o RSI do USDT.D bate 30/80 — alvo de alta do
  USDT.D = pressão baixista no BTC.

### Divergência cruzada BTC ↔ USDT.D
Como são inversos, em um topo saudável do BTC o USDT.D deveria fazer um **fundo mais baixo (LL)**
correspondente. Quando o BTC faz **HH** mas o USDT.D **não** faz LL (faz HL / fundo mais alto), o
combustível baixista do USDT.D está se formando = **topo provável do BTC**. O espelho vale no fundo:
BTC **LL** sem o USDT.D fazer **HH** = exaustão da dominância = **fundo provável do BTC**.

### Enforcement
Obrigatório em BTC/ETH (Fase 8). Impacto no [[confluence-score]]: divergência do USDT.D (ou cruzada)
que **contradiz** o bias → **−1 + rótulo `usdtd-diverge`**; que **confirma** → conta no critério 5.
Mecânica do USDT.D como confirmador/negador macro em [[liquidity-wicks-trap-short-usdtd]].

---

## Backlinks
- [[rsi-stochrsi-combined]] — estratégia combinada RSI + StochRSI para BTC
- [[liquidity-wicks-trap-short-usdtd]] — USDT.D como confirmador inverso; divergência de RSI no USDT.D
- [[confluence-score]] — score da divergência do USDT.D (critério 5 / `usdtd-diverge`)
- [[SMC]] — FVG + divergência RSI = confluência máxima
- [[multi-timeframe-analysis]]
- [[trade-playbooks]]
- [[fibonacci-structural]] — Golden Zone + divergência = entrada sniper
- [[btc-cycle-analysis]] — RSI semanal divergências em topos/fundos de ciclo

