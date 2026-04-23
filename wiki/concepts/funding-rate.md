# Funding Rate (Taxa de Financiamento)

> Conceito core para análise de mercados de futuros perpétuos.
> Fonte original: CoinGlass | Compilado: 2026-04-23

## Definição

Taxa periódica trocada entre traders em **posições long e short** de contratos perpétuos, sem envolvimento da exchange. Seu objetivo é manter o preço do contrato alinhado ao preço spot do ativo.

## Mecânica

- **Taxa positiva** → longs pagam para shorts (mercado sobreaquecido, muita compra especulativa)
- **Taxa negativa** → shorts pagam para longs (mercado sobrevendido, muita venda especulativa)
- **Taxa = 0,00%** → sem pagamentos, equilíbrio perfeito entre as forças
- Liquidada a cada **8 horas** na maioria das exchanges
- Limite máximo/mínimo BTC: ±0,375% (varia por exchange)

## Leitura Visual (CoinGlass)

| Cor | Taxa | Significado |
|-----|------|------------|
| Preto | = 0,01% | Taxa base neutra |
| Vermelho | > 0,01% | Bullish — longs pagando |
| Verde | < 0,005% | Bearish — shorts pagando |
| Mais escuro | Maior desvio | Sentimento mais extremo |

## Uso Operacional

**Sinais de cautela:**
- FR persistentemente alta (>0,1%) = mercado com muitos longs alavancados → risco de long squeeze
- FR persistentemente negativa (<-0,05%) = muito short alavancado → risco de short squeeze

**Sinais de oportunidade:**
- FR voltando a zero após extremo = normalização, possível squeeze na direção do excesso
- FR negativa em suporte técnico = combustível para bounce (shorts vão ser comprados)

**Combinação com OI:**
- FR alta + OI subindo = novos longs abrindo com custo crescente → tendência insustentável
- FR alta + OI caindo = longs fechando, pagamentos reduzindo → normalização saudável

## Notas Técnicas

- dYdX publica taxa horária (CoinGlass multiplica por 8 para padronizar)
- Dados suavizados no front-end do CoinGlass — usar API para dados brutos
- Binance e OKX limitam atualizações a 1x/segundo desde 2021

## Backlinks
- [[open-interest]] — sempre analisar FR junto com OI
- [[liquidation-heatmap]] — FR extrema precede cascatas de liquidação
- [[long-short-ratio]] — trio completo: FR + OI + LSR
- [[research/2026-04-23-derivatives-onchain-concepts-batch6]]
