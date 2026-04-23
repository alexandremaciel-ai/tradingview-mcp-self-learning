# MVRV-Z Score (Market Value to Realized Value Z-Score)

> Métrica on-chain de ciclo Bitcoin — identifica topos e fundos históricos.
> Fonte: bitbo.io / CoinGlass | Compilado: 2026-04-23

## Definição

Ferramenta de análise on-chain desenvolvida por **Murad Mahmudov e David Puell** que avalia o preço do Bitcoin em relação ao seu "valor justo" (Realized Value), adicionando análise estatística por desvio padrão.

## Componentes

| Componente | Definição |
|-----------|-----------|
| **Market Value** | Preço atual × oferta circulante (= Market Cap) |
| **Realized Value** | Preço no último movimento de cada BTC × qtd. de moedas (ignora moedas perdidas/HODLadas) |
| **MVRV Ratio** | Market Cap / Realized Cap |
| **MVRV-Z Score** | Desvios padrão que o MVRV atual está acima/abaixo da média histórica |

## MVRV vs MVRV-Z

- **MVRV** = razão simples → `Market Cap / Realized Cap`
- **MVRV-Z** = normalização estatística → mede quantos σ o MVRV está da média histórica
- MVRV-Z é **mais útil para comparar ciclos diferentes** (elimina viés de época)

## Leitura do MVRV-Z Score

| Zona | Z-Score | Interpretação |
|------|---------|--------------|
| **Zona Vermelha** | Alto positivo (>7) | Bitcoin extremamente sobrevalorizado — topos históricos |
| **Neutro** | Próximo a 0 | Mercado em "valor justo" |
| **Zona Verde** | Baixo/negativo (<1) | Bitcoin subvalorizado — fundos históricos, oportunidade macro |

## Uso Operacional

**Para entrada macro:**
- Z-Score na zona verde = oportunidade de acumulação de longo prazo (DCA)
- Z-Score subindo rapidamente = momentum bullish, mas cautela com topos

**Para saída macro:**
- Z-Score acima de 7 = histórico de topos de ciclo (2017, 2021)
- Z-Score voltando de extremo positivo = início de distribuição macro

**Limitações:**
- Indicador de longo prazo (ciclos) — não use para timing de curto prazo
- Não prevê o momento exato do topo/fundo, apenas a zona de risco

## Relação com Realized Price

O Realized Price é a base do MVRV: quando o preço está muito acima da Realized Price, o Z-Score sobe. [[realized-price]]

## Backlinks
- [[realized-price]] — Realized Price é o denominador do MVRV
- [[nupl]] — indicador complementar de ciclo (mede lucro não realizado)
- [[sopr]] — métrica de curto prazo (lucro realizado em transações)
- [[research/2026-04-23-onchain-metrics-batch7]]
