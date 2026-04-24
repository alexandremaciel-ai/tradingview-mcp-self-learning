# V.V.I.R. — Framework de Validação de Movimento

> Volume, Velocidade, Intensidade, Rompimento.
> Valida se um movimento de preço é real ou armadilha institucional antes de entrar.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## O Framework

O V.V.I.R. é uma grade de 4 perguntas que filtra falsos rompimentos antes de executar a entrada.

### V — Volume
- Rompimento de topo **SEM** aumento expressivo de volume de compra = **falso (Bull Trap)**
- Perda de suporte **COM** pico de volume vendedor = **confirmado** (tendência de queda)
- Volume financeiro (não apenas quantidade de contratos) deve confirmar a direção
- **OBV Divergência:** OBV divergindo do preço antecipa reversões antes do candle confirmar

### V — Velocidade
- Compare o tempo de subida com o tempo de descida
- Subida lenta (15 dias) + queda rápida (3 dias) = **pressão vendedora dominante**
- Velocidade assimétrica indica alinhamento de fluxo para o lado da queda rápida
- Queda devolveu 100% do movimento ascendente em < 30% do tempo = **alta probabilidade de rompimento de suporte**

### I — Intensidade (Candle de Gatilho)
- O corpo do candle de rompimento deve superar `ATR(14) × 1.5`
- Candle com corpo pequeno + pavio longo = rejeição, não rompimento

### R — Rompimento
- O volume do candle deve superar `SMA(Volume, 20) × 1.5`
- Fechamento ALÉM do nível (não apenas pavio) = rompimento válido
- Reteste do nível rompido após fechamento = confirmação adicional

---

## Checklist V.V.I.R.

```
□ [V] Volume alinhado com a direção do rompimento?
□ [V] Velocidade do movimento confirma a tendência (assimetria)?
□ [I] Corpo do candle de gatilho > ATR(14) × 1.5?
□ [R] Volume do candle > SMA(Volume, 20) × 1.5?
```

**Aprovação mínima:** 3 de 4 critérios. Todos os 4 = alta convicção.

---

## OBV — On-Balance Volume

Indicador complementar ao V.V.I.R.:
- OBV subindo + preço lateral = acumulação → próximo movimento bullish
- OBV caindo + preço lateral = distribuição → próximo movimento bearish
- OBV divergindo do preço = **antecipa reversão antes do candle confirmar**
- Parâmetros: padrão (sem ajuste necessário)

---

## Integração com Outros Conceitos

| Sinal V.V.I.R. | Combinação Ideal |
|----------------|-----------------|
| Volume alto em rompimento bearish | FVG Bearish + RSI divergência bearish |
| Velocidade assimétrica (queda rápida) | LH/LL estrutura confirmada no 4H |
| Intensidade (ATR × 1.5) | Candle fecha além de EQH/EQL |
| Rompimento com volume | BOS confirmado no 15M |

---

## Backlinks
- [[SMC]] — BOS com V.V.I.R. = confirmação de estrutura
- [[rsi-divergences]] — divergência de OBV + RSI = sinal combinado
- [[trade-playbooks]]
- [[position-sizing]]
