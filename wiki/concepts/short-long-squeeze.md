# Short Squeeze e Long Squeeze

> Criado: 2026-04-26
> Categoria: Market Microstructure / Liquidações em Cascata

## Definição

**Short Squeeze:** quando muitos traders estão vendidos a descoberto e o preço sobe — forçando os shorts a recomprar (fechar posições) → pressão de compra adicional → preço sobe ainda mais em cascata.

**Long Squeeze:** quando muitos traders estão comprados e o preço cai — forçando os longs a vender (fechar posições) → pressão de venda adicional → preço despenca em cascata.

Ambos criam movimentos rápidos e violentos sem necessidade de notícias — são puramente mecânicos, derivados da posição agregada do mercado.

---

## Mecanismo

### Short Squeeze — Passo a Passo
1. Alta concentração de posições short (visível via Open Interest + Funding Rate negativa)
2. Preço inicia movimento de alta (pode ser engenhado por smart money)
3. Shorts começam a perder → margin calls → forçados a recomprar
4. Compras forçadas elevam o preço ainda mais → novos shorts são stoppados
5. Cascata de liquidações → move violento de alta em velas grandes

### Long Squeeze — Passo a Passo
1. Alta concentração de posições long (OI alto + Funding Rate muito positiva)
2. Preço cai abaixo de suporte chave
3. Longs entram em stop → vendem → preço cai mais
4. Novos longs são stoppados → cascata de liquidações baixistas
5. Candle de queda violenta ("dump")

---

## Como Identificar Antes de Acontecer

### Condições de Setup para Short Squeeze
- [ ] Funding Rate fortemente negativa (shorts pagando fundos para longs)
- [ ] Open Interest alto com preço lateral ou levemente em queda
- [ ] Long/Short Ratio < 0.4 (muito mais shorts que longs)
- [ ] HeatMap de liquidação mostra cluster de liquidações de shorts acima do preço atual
- [ ] Preço próximo de resistência chave com volume seco (sem sellers)

### Condições de Setup para Long Squeeze
- [ ] Funding Rate fortemente positiva (longs pagando fundos para shorts)
- [ ] Open Interest alto com preço em alta estendida
- [ ] Long/Short Ratio > 3.0 (muito mais longs que shorts)
- [ ] HeatMap mostra cluster de liquidações de longs abaixo do preço
- [ ] Preço em resistência histórica + RSI sobrecomprado + volume declinando

---

## Dica Operacional (Phoenixion Trader)
> "Não persiga grandes velas verdes/vermelhas. Esses squeezes punem entradas tardias. Observe o mercado acumular pressão, então negocie o **efeito posterior** assim que as coisas se acalmarem."

O trade mais seguro não é durante o squeeze, mas **após** a cascata se esgotar:
- Após short squeeze: aguardar reteste do nível de onde partiu → long com stop abaixo
- Após long squeeze: aguardar reteste da resistência quebrada → short com stop acima

---

## Diferença para Bull Trap / Bear Trap

| Conceito | Gatilho | Movimento | Quem perde |
|----------|---------|-----------|-----------|
| Short Squeeze | Compras forçadas de shorts | Violento para cima | Traders que estavam short |
| Long Squeeze | Vendas forçadas de longs | Violento para baixo | Traders que estavam long |
| Bull Trap | Rompimento falso de resistência | Sobe e reverte | Traders que compraram o breakout |
| Bear Trap | Rompimento falso de suporte | Cai e reverte | Traders que venderam o breakout |

Short Squeeze → muitas vezes resulta em Bull Trap subsequente (preço subiu por squeeze, não por demanda real → reverte).

---

## Integração com Derivativos

Para analisar probabilidade de squeeze, usar o trio:
1. **Open Interest** — tamanho das posições abertas (ver [[open-interest]])
2. **Funding Rate** — quem está pagando quem (ver [[funding-rate]])
3. **Long/Short Ratio** — proporção das posições (ver [[long-short-ratio]])
4. **Liquidation HeatMap** — onde estão os stops (ver [[liquidation-heatmap]])

---

## Backlinks
- [[open-interest]] — monitorar OI para detectar condições de squeeze
- [[funding-rate]] — FR extrema = mercado sobreexposto = squeeze iminente
- [[long-short-ratio]] — desequilíbrio extremo = combustível para squeeze
- [[liquidation-heatmap]] — localizar os clusters de liquidação alvo
- [[bull-bear-traps]] — squeeze pode criar ou amplificar armadilhas
- [[Wyckoff]] — Spring e UTAD frequentemente coincidem com squeezes
