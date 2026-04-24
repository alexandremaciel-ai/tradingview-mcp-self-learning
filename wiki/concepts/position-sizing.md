# Gestão de Posição — Sizing, TP e Anti-Loss Framework

> Regras matemáticas de risco, distribuição de saída e proteção de capital.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Matemática de Posição

```
Tamanho da Posição = (Risco em $) ÷ (Distância % até o Stop Loss)
```

**Exemplo:** Capital R$10,000 | Risco 1% = R$100 em risco | Stop 2% abaixo da entrada
→ Tamanho = R$100 ÷ 0.02 = R$5,000 em posição

### Limites de Risco
- **Risco máximo por trade:** 1–2% do capital total
- **Risco máximo simultâneo:** máximo 5% do capital em operações abertas
- **Squeeze de alavancagem (Playbook 4):** reduzir para 0.5% do capital em risco

---

## 2. Posicionamento do Stop Loss

- **Stop Loss:** 1 tick além do pavio do candle que armou a armadilha
- Nunca mover o stop para longe da entrada após sofrer pressão — **Stop Loss é sagrado**
- **Breakeven (BE):** mover stop para entrada ao atingir 40–50% do alvo
- Jamais adicionar posição em trade perdedor (proibido Martingale)

---

## 3. Distribuição de Take Profit (35/35/15/15)

| Parcela | % da Posição | Alvo | R:R Mínimo |
|---------|-------------|------|------------|
| **TP1** | 35% | Primeiro FVG ou resistência imediata | 1.5:1 |
| **TP2** | 35% | Próxima zona de liquidez (PDH/PDL, EQH/EQL) | 2.5:1+ |
| **TP3** | 15% | Extensão Fibonacci 1.272 ou OB de TF maior | 3.5:1+ |
| **TP4** | 15% | Extensão Fibonacci 1.618 ou próximo FVG de TF maior | 5:1+ |

> **Compatibilidade com Conservative Trend Follower v2:** R:R mínimo de entrada permanece ≥ 1:3 (refere-se ao TP2/TP3 como referência principal). TP1 em 1.5:1 é a saída parcial de proteção — não o alvo principal da operação.

---

## 4. Trailing Stop e Gestão Dinâmica

- Após **TP1**: mover stop para breakeven (entrada)
- Após **TP2**: mover stop para TP1 (travar parcial)
- Em tendências fortes: usar `ATR × 2` como trailing stop para deixar a posição rodar
- Se o mercado rejeitar fortemente em zona de liquidez sem atingir TP parcial → fechar 50% manualmente

---

## 5. Anti-Loss Framework — Regras de Ouro

### Proibições Absolutas
- ❌ **NUNCA** entrar contra a EMA 200 no 4H sem confluência extrema (mínimo 4 fatores alinhados)
- ❌ **NUNCA** mover o stop para longe da entrada após sofrer pressão
- ❌ **NUNCA** adicionar posição em trade perdedor (sem Martingale)
- ❌ **NUNCA** operar durante FOMC, CPI, NFP sem reduzir posição em 50%
- ❌ **NUNCA** arriscar mais de 2% do capital em um único trade

### Obrigações
- ✅ **SEMPRE** aguardar o fechamento do candle de confirmação — nunca entrar no candle aberto
- ✅ **SEMPRE** registrar setup, entrada, SL, TP e resultado na wiki/sessions/
- ✅ **SEMPRE** revisar os últimos 3 trades antes de abrir uma nova posição
- ✅ **SEMPRE** verificar ausência de eventos macro de alto impacto (FOMC, CPI, NFP) antes de entrar

### Circuit Breakers
- 🛑 Atingiu drawdown de **5% no dia** → parar. Retomar no dia seguinte.
- 🛑 Atingiu **3 stops consecutivos** → pausa de 24h para revisar contexto de mercado.

---

## 6. Trailing Stop Progressive (Conservative Trend Follower v2)

| Momento | Ação |
|---------|------|
| Entrada | Stop no setup |
| +10% do alvo | Stop move para breakeven |
| +20% do alvo | Stop move para +10% |
| +30% do alvo | Stop move para +20% |
| Após TP2 | Stop move para TP1 |

---

## Backlinks
- [[trade-playbooks]] — todos os playbooks referenciam esta página para gestão
- [[conservative-trend-follower-v2]]
- [[fibonacci-structural]] — TP3/TP4 em extensões Fibonacci
- [[volume-profile]] — TP2 em HVN
- [[SMC]] — TP2 em PDH/PDL, EQH/EQL
