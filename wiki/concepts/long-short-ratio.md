# Long/Short Ratio (Razão L/S)

> Indicador de sentimento de mercado para futuros perpétuos.
> Fontes: CoinGlass, Binance Academy | Compilado: 2026-04-23

## Definição

Razão entre o **número de posições longas e curtas abertas** por traders em contratos perpétuos. Mede o sentimento especulativo coletivo do mercado.

**Fórmula:** LSR = posições longas / posições curtas

## Leitura Básica

| LSR | Significado |
|-----|------------|
| > 1,0 | Mais longs que shorts — sentimento bullish |
| = 1,0 | Equilíbrio perfeito |
| < 1,0 | Mais shorts que longs — sentimento bearish |

## Zonas Extremas (Interpretação Contrária)

| Zona | LSR | Interpretação |
|------|-----|--------------|
| Extremo bullish | > 1,5 | Muito otimismo — possível **topo** (posições compradas em excesso) |
| Extremo bearish | < 0,5 | Muito pessimismo — possível **fundo** (posições vendidas em excesso) |

**Lógica contrária:** Quando "todo mundo" está comprado (LSR > 1,5), há poucos compradores novos para empurrar o preço. O mercado está vulnerável a short squeeze que vira long squeeze.

## REGRA DE OURO: LSR + OI são inseparáveis

| LSR | OI | Interpretação |
|-----|-----|--------------|
| Alto (>1,5) | ↑ subindo | Novos longs abrindo → **momentum bullish** OU **armadilha** |
| Alto (>1,5) | ↓ caindo | Longs fechando → **sinal fraco — evitar** |
| Baixo (<0,5) | ↑ subindo | Novos shorts abrindo → **momentum bearish** OU **long squeeze iminente** |
| Baixo (<0,5) | ↓ caindo | Shorts fechando → **sinal fraco — evitar** |
| Extremo qualquer | Estável | Sem posições novas → **aguardar confirmação** |

**Regra de ouro:** Rising OI = sinal forte | Falling OI = sinal fraco

## Divergências de Alta Convicção

| Condição | Divergência | Expectativa |
|----------|------------|------------|
| Preço HH + LSR caindo + OI subindo | Bearish | Shorts acumulando contra o rally |
| Preço LL + LSR subindo + OI subindo | Bullish | Longs acumulando na queda |

## Estratégias

**Contrariana (zonas extremas):**
- LSR >1,5 + OI subindo → possível reversão down ou short squeeze exagerado
- LSR <0,5 + OI subindo → possível reversão up ou long squeeze exagerado

**Confirmação de tendência:**
- LSR subindo + preço subindo + OI subindo = tendência bullish com novas posições
- LSR caindo + preço caindo + OI subindo = tendência bearish com novas posições

## Indicadores TradingView

### ⭐⭐⭐ Aggregated Long Short Ratio (Binance + Bybit)
**Autor:** carlosbucci | **Atualizado:** Out 2025

Combina LSR das duas maiores exchanges + média agregada em tempo real.

**Alertas integrados:**
- LSR cruzou acima de 1,0 (virou bullish)
- LSR cruzou abaixo de 1,0 (virou bearish)
- LSR muito alto (>1,5, possível topo)
- LSR muito baixo (<0,5, possível fundo)

**Requisitos:** TradingView Premium+. Usar em pares perpétuos (BTCUSDT.P, ETHUSDT.P).

**Melhor uso:** 4H e 1D para sinais mais confiáveis. Sempre combinar com OI no mesmo gráfico.

## Dados por Exchange

- Binance e Bybit = as duas maiores fontes de LSR
- CoinGlass agrega múltiplas exchanges para LSR global
- Dados com defasagem durante extrema volatilidade (limitação de API)

## Backlinks
- [[open-interest]] — LSR sem OI = análise incompleta
- [[funding-rate]] — trio completo: LSR + OI + FR
- [[liquidation-heatmap]] — LSR extremo + zonas amarelas = squeeze iminente
- [[research/2026-04-23-derivatives-onchain-concepts-batch6]]
- [[research/2026-04-21-tv-community-indicators-batch4]] — primeiro registro do indicador Aggregated LSR
