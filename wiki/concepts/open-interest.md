# Open Interest (Interesse Aberto)

> Conceito core para análise de mercados de derivativos.
> Fonte original: CoinGlass | Compilado: 2026-04-23

## Definição

**Total de contratos futuros ou de opções que permanecem abertos** — não liquidados, não expirados. Mede o volume total de capital comprometido em derivativos de um ativo em determinado momento.

## Os Três Resultados Possíveis

| Cenário | Resultado no OI |
|---------|----------------|
| Comprador abre posição nova + vendedor abre posição nova | OI **aumenta** |
| Comprador fecha posição + vendedor fecha posição | OI **diminui** |
| Comprador abre posição + vendedor fecha posição (ou vice-versa) | OI **fica igual** |

**Implicação importante:** Sempre há um comprador para cada vendedor. "Mais compradores que vendedores" é incorreto — o OI mede se *capital novo está entrando* no mercado, não quem tem mais.

## Interpretação Combinada: OI + Preço

| OI | Preço | Interpretação |
|----|-------|--------------|
| ↑ subindo | ↑ subindo | Capital novo entrando long — **bullish confirmado** |
| ↑ subindo | ↓ caindo | Capital novo entrando short — **bearish confirmado** |
| ↓ caindo | ↑ subindo | Shorts fechando (short squeeze) — momentum sem convicção nova |
| ↓ caindo | ↓ caindo | Longs capitulando — pressão de venda mas sem novos shorts |

## Por que o Preço se Move?

Participantes **delta-neutros** (market makers, hedgers, arbitrageurs) não têm viés direcional mas afetam o equilíbrio entre oferta e demanda instantaneamente — isso move preço mesmo sem variação de OI.

## Uso Operacional

**Risco alto:**
- OI em máximos históricos + preço em resistência = mercado sobreexposto → qualquer lado pode explodir
- OI crescente + Funding Rate crescendo = posições se acumulando com custo — insustentável por longo período

**Oportunidades:**
- OI caindo bruscamente = desalavancagem rápida → volatilidade reduzindo, possível consolidação antes do próximo movimento
- OI subindo + preço quebrando resistência = confirmação de rompimento real (não fakeout)

**Sinal fraco (evitar):**
- OI caindo + FR extrema = posições fechando, sem convicção nova — sinal de baixa qualidade

## Dados por Exchange

CoinGlass monitora OI em todas as principais exchanges globais em tempo real. APIs disponíveis para dados históricos.

## Backlinks
- [[funding-rate]] — FR e OI são inseparáveis na análise de derivativos
- [[long-short-ratio]] — OI valida (ou invalida) a leitura do LSR
- [[liquidation-heatmap]] — OI alto + zonas amarelas = risco elevado de cascata
- [[research/2026-04-23-derivatives-onchain-concepts-batch6]]
