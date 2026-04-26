# Bull Trap e Bear Trap — Identificação e Filtros

> Criado: 2026-04-26
> Categoria: Price Action / Confluências de Confirmação

## Definição

**Bull Trap:** rompimento falso de resistência que engana compradores breakout — preço entra acima, liquida stops, reverte abaixo.  
**Bear Trap:** rompimento falso de suporte que engana vendedores breakout — preço entra abaixo, liquida stops, reverte acima.

Ambos são engineered: criados por smart money para capturar a liquidez dos traders de varejo que entram em rompimentos sem confirmação.

---

## Framework 1 — Divergência RSI + MACD

### Regra Operacional
> **NUNCA comprar rompimento de resistência se o RSI está divergindo negativamente (preço faz high mais alto mas RSI faz high mais baixo).**  
> **NUNCA vender rompimento de suporte se o RSI está divergindo positivamente (preço faz low mais baixo mas RSI faz low mais alto).**

### Como Identificar
- **Bull Trap via RSI:** Preço rompe resistência → novo high → RSI lower high = momentum fraquejando → rompimento não tem força real
- **Bear Trap via RSI:** Preço rompe suporte → novo low → RSI higher low = pressão vendedora fraquejando → breakdown fabricado

### Filtro MACD
O MACD reforça quando confirma a divergência:
- Bull Trap: preço faz higher high + histograma MACD declinando + linha MACD curva para baixo
- Bear Trap: preço faz lower low + histograma MACD subindo (menos negativo) + linha MACD curva para cima

### Regra de Aplicação
| Condição | RSI | MACD | Conclusão |
|----------|-----|------|-----------|
| Rompimento de resistência | Higher high | Lower high | BULL TRAP — aguardar reversão |
| Rompimento de resistência | Higher high | Higher high | Rompimento válido — pode entrar |
| Rompimento de suporte | Lower low | Higher low | BEAR TRAP — aguardar reversão |
| Rompimento de suporte | Lower low | Lower low | Breakdown válido — pode entrar |

---

## Framework 2 — Ichimoku Chikou Span

### Regra Operacional
> **Um rompimento só é válido quando TODOS os 4 elementos estão do mesmo lado do Kumo (nuvem):**
> 1. Preço
> 2. Tenkan-sen (linha de conversão)
> 3. Kijun-sen (linha base)
> 4. Chikou Span (span atrasado)

### Como Identificar a Armadilha
- Preço rompe acima do Kumo, mas o **Chikou Span ainda está dentro ou abaixo** = Kumo ainda segura como resistência defasada = bull trap potencial
- Preço cai abaixo do Kumo, mas o **Chikou Span ainda está acima ou dentro** = suporte defasado ainda ativo = bear trap potencial

### Por que o Chikou Span é o Filtro Mais Importante
O Chikou Span é o preço atual plotado 26 períodos atrás. Se ele está no lado contrário do Kumo, significa que o preço atual está tentando romper onde o preço esteve 26 períodos atrás ainda não confirmou a tendência. É o componente de "segunda verificação" do sistema Ichimoku.

### Aplicação Prática
```
Bull Trap evitado: Preço > Kumo ✅ | Tenkan > Kijun ✅ | Chikou < Kumo (26p atrás) ❌ → aguardar
Rompimento válido: Todos 4 componentes acima do Kumo ✅✅✅✅ → pode operar
```

---

## Framework 3 — Fibonacci 1.272 — A Armadilha de Extensão

### Regra Operacional
> **Candle que ultrapassa o nível 1.0 de Fibonacci (rompimento aparente) mas fecha abaixo de 1.272 e depois reverte de volta à faixa = armadilha clássica.**

### Estrutura da Armadilha
```
1.272 ──── [topo da armadilha / sweep máximo]
             ↑ wick/corpo da vela de trap
1.000 ──── [nível de rompimento "esperado"]
             ↓ fechamento de volta à faixa
0.786 ──── [zona de golden pocket]
0.618 ──── [zona OTE / alvo de retorno]
```

### Identificação Passo a Passo
1. Identificar pernada de alta (para bull trap) ou de baixa (para bear trap)
2. Traçar Fibonacci da pernada completa (0 → 1.0)
3. Verificar extensões: 1.272, 1.414, 1.618
4. Se vela rompe o 1.0 (novo high/low aparente) mas o fechamento fica **abaixo/acima do 1.272** e volta para dentro da faixa → é a trap

### Confirmação
- Volume na vela de trap: pode ser alto (engineered) ou baixo (falta de buyers/sellers)
- A reversão subsequente costuma mirar 0.618–0.786 da pernada original (OTE)
- Se RSI diverge simultaneamente com a candle trap = confluência máxima (ver Framework 1)

---

## Framework 4 — Regra do Fechamento H4/D1

### Regra Operacional
> **Um rompimento só existe APÓS o fechamento da vela no timeframe relevante. Velas abertas não confirmam rompimento.**

### Cenários Críticos

**Bull Trap clássico por wick:**
- Vela D1 ou H4 empurra preço acima da resistência durante a formação
- Wick longo acima da resistência = preço foi testado lá mas não houve buyers suficientes
- Candle fecha ABAIXO da resistência = Shooting Star ou equivalente = bull trap confirmado
- Nunca entrar no "rompimento" de uma vela ainda aberta

**Bear Trap clássico por wick:**
- Vela H4 ou D1 cai abaixo do suporte com wick
- Candle fecha ACIMA do suporte = Hammer ou equivalente = bear trap confirmado
- O fechamento de volta acima nega o breakdown

### Regras de Espera
| Timeframe do setup | Aguardar |
|--------------------|----------|
| Scalp M15 | Fechamento da vela M15 acima/abaixo do nível |
| Intraday H1 | Fechamento da vela H1 |
| Swing H4 | Fechamento da vela H4 (prioridade máxima) |
| Swing/Posição D1 | Fechamento da vela D1 |

### Aplicação com Shooting Star (Bull Trap)
```
Resistência em $80,000
Vela H4 abre $79,500 → sobe a $80,420 (wick) → fecha $79,650
Conclusão: BULL TRAP. Wick tocou a zona mas sem compradores = Shooting Star.
Ação: aguardar reteste da resistência de baixo para short, ou ignorar.
```

---

## Combinação dos 4 Frameworks — Setup Anti-Trap Completo

Para máxima confiança de identificar uma armadilha **antes** de ser capturado:

### Checklist Pré-Entrada em Rompimento
- [ ] **RSI/MACD:** sem divergência negativa (bull) / positiva (bear) no TF do trade
- [ ] **Ichimoku:** Chikou Span do mesmo lado do Kumo que o preço
- [ ] **Fibonacci:** preço não está na zona de extensão 1.0–1.272 apenas via wick sem fechamento
- [ ] **Candle Close:** vela do TF relevante FECHOU além do nível (não apenas wick)

Se 2 ou mais condições falham → probabilidade de trap > 70% → não entrar.

---

## Impacto nos Setups da Wiki

### Interação com SMC (BOS / CHoCH)
- Um BOS só é válido se a vela H4/D1 fecha além do swing high/low (regra 4)
- CHoCH + divergência RSI = mais fraco → requer confluência adicional
- Veja: [[SMC]]

### Interação com Wyckoff
- O "Upthrust After Distribution" (UTAD) é um bull trap de manual
- O "Spring" no final da acumulação é um bear trap de manual
- Aplicar Fib 1.272 nesses momentos potencializa o sinal
- Veja: [[Wyckoff]]

### Interação com RSI Divergências
- Este framework é a principal fonte dos filtros de divergência
- Veja: [[rsi-divergences]]

### Interação com Fibonacci Estrutural
- Extensões 1.272/1.414/1.618 como níveis de armadilha são centrais aqui
- Veja: [[fibonacci-structural]]

---

## Backlinks
- [[SMC]] — BOS/CHoCH precisam do filtro de fechamento de vela
- [[Wyckoff]] — UTAD = bull trap / Spring = bear trap estrutural
- [[rsi-divergences]] — Framework 1 baseia-se na leitura de divergências
- [[fibonacci-structural]] — extensões 1.272 para identificar zonas de trap
- [[macd]] — filtro secundário no Framework 1
- [[vvir-framework]] — V.V.I.R. ajuda confirmar se rompimento tem volume real
- [[trade-playbooks]] — regras anti-trap se aplicam a todos os playbooks
