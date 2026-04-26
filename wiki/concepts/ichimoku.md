# Ichimoku Kinko Hyo — Nuvem de Ichimoku

> Criado: 2026-04-26
> Categoria: Indicador Multi-componente / Tendência + Momentum + S&R

## Definição

O Ichimoku Kinko Hyo ("equilíbrio à primeira vista") é um sistema completo de análise técnica que combina tendência, suporte/resistência, momentum e timing em um único indicador. Criado por Goichi Hosoda no final dos anos 1960, é amplamente usado por traders profissionais.

---

## Os 5 Componentes

| Componente | Nome técnico | Cálculo | Defasagem |
|------------|-------------|---------|-----------|
| Tenkan-sen | Linha de conversão | (Máx 9 + Mín 9) / 2 | 0 |
| Kijun-sen | Linha base | (Máx 26 + Mín 26) / 2 | 0 |
| Senkou Span A | Leading Span A | (Tenkan + Kijun) / 2 | +26 períodos à frente |
| Senkou Span B | Leading Span B | (Máx 52 + Mín 52) / 2 | +26 períodos à frente |
| Chikou Span | Lagging Span | Preço de fechamento atual | -26 períodos no passado |

A **Kumo (nuvem)** é a área entre o Senkou Span A e B — verde quando SpanA > SpanB, vermelha quando SpanB > SpanA.

---

## Leituras Primárias

### Tendência pelo Preço vs Kumo
- Preço **acima** da Kumo = tendência de **alta**
- Preço **dentro** da Kumo = zona de **transição / indecisão**
- Preço **abaixo** da Kumo = tendência de **baixa**
- Nuvem espessa = suporte/resistência mais forte
- Nuvem fina = suporte/resistência mais fraco

### Força da Tendência pela Kumo
- Kumo verde à frente do preço = projeção bullish
- Kumo vermelha à frente do preço = projeção bearish
- Kumo twisting (mudança de cor) à frente = possível reversão nos próximos 26 períodos

### Cruzamento Tenkan × Kijun
- Tenkan cruza **acima** do Kijun = sinal de compra (mais forte se preço acima da Kumo)
- Tenkan cruza **abaixo** do Kijun = sinal de venda (mais forte se preço abaixo da Kumo)

---

## Chikou Span — O Filtro Mais Poderoso

O Chikou Span é o preço de fechamento atual plotado **26 períodos no passado**. Ele responde à pergunta: "onde estava o preço 26 períodos atrás em relação ao que existe hoje?"

### Por que é o filtro mais importante
- Chikou **acima** do preço histórico e **acima** da Kumo histórica = confirmação bullish forte
- Chikou **abaixo** do preço histórico e **abaixo** da Kumo histórica = confirmação bearish forte
- Chikou **dentro** da Kumo = ambiguidade — rompimento ainda não confirmado

### Regra Anti-Trap (integração com [[bull-bear-traps]])
> Um rompimento de alta é válido **somente** se o Chikou Span também estiver acima da Kumo 26 períodos atrás. Se o preço rompeu a resistência mas o Chikou ainda está na Kumo ou abaixo dela, o breakout é prematuro = bull trap potencial.

---

## Checklist Ichimoku Completo — Setup de Alta

Para uma entrada long com máxima confiança Ichimoku:
- [ ] Preço acima da Kumo
- [ ] Tenkan-sen acima do Kijun-sen
- [ ] Chikou Span acima do preço histórico (26 períodos atrás)
- [ ] Chikou Span acima da Kumo histórica
- [ ] Kumo à frente é verde (projeção bullish)

Se 4+ condições = setup forte. Se 3 = moderado. Se < 3 = não operar.

---

## Configurações Recomendadas

### Padrão (Japonês)
- Tenkan: 9 | Kijun: 26 | Senkou B: 52

### Cripto / 24h (ajuste comum)
- Tenkan: 20 | Kijun: 60 | Senkou B: 120
*(Porque cripto opera 7 dias, enquanto mercados japoneses usavam 6 dias úteis/semana)*

---

## Limitações

1. Em mercados laterais (consolidação) as linhas se cruzam frequentemente gerando falsos sinais
2. A Kumo pode tornar-se irrelevante quando o preço está distante por muito tempo
3. Muitas linhas no gráfico podem dificultar a leitura → ocultar Tenkan/Kijun se necessário e focar na Kumo + Chikou
4. Não é preditivo — é baseado em dados históricos apesar da projeção da Kumo

---

## Uso Combinado com Outros Indicadores

| Indicador | Como combinar |
|-----------|---------------|
| RSI | Confirmar momentum quando preço rompeu a Kumo |
| Volume | Volume alto no rompimento da Kumo = sinal mais forte |
| Fibonacci | Nívels 0.618/0.786 que coincidem com Kijun-sen = confluência máxima de S/R |
| Supertrend | Usar Supertrend para trailing stop quando Ichimoku confirma tendência |

---

## Backlinks
- [[bull-bear-traps]] — Chikou Span é o filtro principal no Framework 2 (regra anti-trap)
- [[multi-timeframe-analysis]] — Ichimoku no D1 define o macro, H4 define o swing
- [[fibonacci-structural]] — confluência Kijun + Fib = zonas de S/R máximas
- [[rsi-divergences]] — RSI confirma/nega momentum quando preço está na Kumo
