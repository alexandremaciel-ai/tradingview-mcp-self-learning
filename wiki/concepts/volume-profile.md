# Volume Profile — POC, VWAP e Estrutura de Volume

> Análise de onde o volume se distribuiu historicamente — atua como mapa de suporte/resistência.
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Conceitos Fundamentais

### POC — Point of Control
- Faixa de preço com **maior volume transacionado** no período
- Age como suporte/resistência magnético — o preço é "atraído" de volta ao POC
- Em tendências: POC marca o "preço justo" de equilíbrio da consolidação anterior
- **Uso operacional:** zona de reteste após rompimento

### HVN — High Volume Node
- Zonas de alto volume = **zonas de consolidação**
- O preço **desacelera** nelas (resistência/suporte moderada)
- Boa zona para TP parcial em tendência que se aproxima de um HVN

### LVN — Low Volume Node
- Zonas de baixo volume = **zonas de passagem rápida**
- O preço **atravessa rapidamente** (pouca resistência)
- LVN entre o preço atual e o alvo = movimento rápido esperado

---

## 2. VWAP — Volume Weighted Average Price

- Preço médio ponderado por volume — **referência institucional**
- Abaixo do VWAP = pressão vendedora. Acima = pressão compradora.
- **Ancoragem:** usar VWAP ancorado na **abertura semanal** para crypto (24/7)
- VWAP diário é comum em ações mas menos relevante em crypto que opera 24h
- Preço retestando VWAP semanal após rompimento = confluência de entrada

---

## 3. OBV — On-Balance Volume

- Acumula volume na direção de cada fechamento de candle
- OBV subindo + preço lateral = **acumulação** (próximo movimento bullish)
- OBV caindo + preço lateral = **distribuição** (próximo movimento bearish)
- Divergência OBV/preço = antecipa reversão antes do candle confirmar
- Parâmetros: padrão (sem ajuste)

---

## 4. Leitura Rápida

| Zona | Comportamento Esperado |
|------|------------------------|
| **POC** | Suporte/resistência magnético — preço tende a retornar |
| **HVN** | Desaceleração — bom para TP parcial |
| **LVN** | Passagem rápida — não colocar alvos nela |
| **Acima do VWAP semanal** | Pressão compradora institucional |
| **Abaixo do VWAP semanal** | Pressão vendedora institucional |

---

## 5. Confluências Importantes

- POC + Golden Zone Fibonacci = suporte/resistência de máxima convicção
- POC + FVG = zona de entrada sniper em reteste
- LVN entre preço e alvo = extensão rápida esperada após BOS
- HVN como TP2 em playbooks (LVN = passagem, HVN = alvo)

---

## Backlinks
- [[fibonacci-structural]] — POC + Golden Zone
- [[SMC]] — FVG + POC = confluência
- [[vvir-framework]] — OBV é parte do componente "Volume" do V.V.I.R.
- [[trade-playbooks]]
- [[position-sizing]] — HVN como zona de TP
