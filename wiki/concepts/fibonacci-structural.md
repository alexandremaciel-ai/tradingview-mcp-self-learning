# Fibonacci Estrutural — Golden Zone, Extensões e Tempo

> Ferramenta de confluência para entradas e alvos de saída.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Retração — Zonas de Entrada

### Golden Zone (Zona Primária)
- **0.618 – 0.786** = zona primária de retração
- Em tendência de alta: aguardar pullback para essa zona → Long
- Em tendência de baixa: aguardar repique para essa zona → Short
- Golden Zone + FVG ou Order Block = **zona de Sniper de máxima convicção**

### Nível de Equilíbrio
- **0.5** = referência de equilíbrio — frequentemente testado antes da continuação
- Menos preciso que 0.618, mas útil como alerta de aproximação da Golden Zone

### Outros Níveis Relevantes
- **0.382** = retração rasa (tendência muito forte)
- **0.886** = retração profunda (tendência potencialmente virando)

---

## 2. Extensões — Alvos de Take Profit

| Extensão | TP Recomendado | Contexto |
|----------|---------------|---------|
| **1.272** | TP3 (15% da posição) | Pós-rompimento de estrutura |
| **1.618** | TP4 (15% da posição) | Extensão máxima normal |
| **2.0** | Opcional (runner) | Tendências muito fortes |

> Integração com distribuição de posição: Seção 7 do KB → TP3 = Fib 1.272 | TP4 = Fib 1.618

---

## 3. Fibonacci de Tempo

- Retratamentos em **8, 13, 21 velas** são as mais comuns (números Fibonacci)
- Contar velas desde o início do movimento para antecipar quando o pullback pode terminar
- Confluência de Fibonacci de Tempo + Golden Zone = entrada de timing preciso

---

## 4. Como Desenhar Corretamente

- **Para Long:** draw do fundo do impulso até o topo (âncora baixo → alto)
- **Para Short:** draw do topo do impulso até o fundo (âncora alto → baixo)
- Usar swing highs/lows estruturais (não micronfundos intraday)
- No TradingView: `draw_shape` com ferramenta "Fibonacci Retracement"

---

## 5. Confluências de Alta Convicção

| Combinação | Convicção |
|-----------|----------|
| Golden Zone + FVG | Alta |
| Golden Zone + Order Block | Alta |
| Golden Zone + EMA 200 (1H ou 4H) | Alta |
| Golden Zone + POC (Volume Profile) | Alta |
| Golden Zone + EQH/EQL (pool de liquidez) | Altíssima |
| Golden Zone + RSI divergência | Altíssima |

---

## Backlinks
- [[SMC]] — Golden Zone + OB = sniper entry
- [[rsi-divergences]] — Fibonacci + divergência
- [[volume-profile]] — Golden Zone + POC
- [[trade-playbooks]] — Playbooks 1 e 2 usam Golden Zone como zona de entrada
- [[position-sizing]] — TP3/TP4 em extensões Fibonacci
