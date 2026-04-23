# Liquidation HeatMap (Mapa de Calor de Liquidações)

> Ferramenta preditiva para identificar zonas de liquidação e liquidez.
> Fonte original: CoinGlass | Compilado: 2026-04-23

## Definição

Ferramenta que **estima os níveis de preço onde grandes ondas de liquidação provavelmente ocorrerão**, com base em dados de mercado e diferentes alavancagens.

## Como Funciona

- Calcula níveis de liquidação forçada para múltiplos tamanhos de posição e alavancagens
- Quanto mais níveis estimados em determinado preço, mais quente a cor
- Escala de cores: **roxo → amarelo** (amarelo = alta concentração de liquidações previstas)
- Threshold padrão CoinGlass: **0,85** (filtro de liquidez mínima)

## Dois Usos Principais

### 1. Magnet Zone (Zona Ímã)

Concentração de liquidações em um nível de preço **atrai o preço** naquela direção.

**Por quê:** Exchanges e market makers sabem onde estão os stops. O preço se move para capturar essa liquidez antes de reverter.

**Como usar:** Zona amarela próxima = probabilidade aumentada de o preço ir até lá no curto prazo.

### 2. Support/Resistance Zone (Zona de Reversão)

Após o preço atingir a zona de alta liquidação, grandes traders executam ordens rapidamente na liquidez disponível — depois o preço **reverte**.

**Por quê:** A cascata de liquidações cria pressão brusca em um lado do order book. Quando a liquidez se esgota, o preço inverte (pós-sweep).

**Como usar:** Zona amarela = potencial fundo (se for zona de liquidação de longs) ou topo (se for zona de liquidação de shorts) após o sweep.

## Limitações Importantes

1. Prevê onde liquidações **iniciam**, não onde param
2. A quantidade real de liquidações será **menor** que a prevista (modelo é conservador)
3. Deve ser interpretado **relativamente** (não em valores absolutos) — comparar zonas entre si

## Conexão com SMC

Zonas amarelas de liquidação frequentemente coincidem com:
- **FVGs** (Fair Value Gaps) — desequilíbrios de ordem que também atraem preço
- **EQLs** (Equal Lows/Highs) — pool de liquidez óbvio que o mercado vai buscar
- **BOS anteriores** — níveis de estrutura que acumularam stops

Quando uma zona amarela e um FVG/EQL coincidem = **confluência alta** para entrada pós-sweep.

## Dados Técnicos

- Binance: atualização limitada a 1x/segundo desde abril 2021
- OKX: mesma limitação desde setembro 2021
- Durante extrema volatilidade → dados podem ter defasagem de segundos

## Vocabulário Associado

- **Rekt** (de *wrecked*): gíria cripto para quem foi liquidado
- **Cascata de liquidações** = evento em que liquidações geram mais liquidações (efeito dominó)
- **Fundo de liquidação** = Spring Wyckoff = London Raid = sweep de EQL + reversão

## Backlinks
- [[SMC]] — FVGs e EQLs como zonas de confluência
- [[Wyckoff]] — Spring = fundo de liquidação = preço varre stops e reverte
- [[open-interest]] — OI alto + zona amarela = risco elevado de cascata
- [[funding-rate]] — FR extrema precede cascatas de liquidação
- [[research/2026-04-23-derivatives-onchain-concepts-batch6]]
