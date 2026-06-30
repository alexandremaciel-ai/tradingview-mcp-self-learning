# ADX — Average Directional Index

## O que mede
Força da tendência (NÃO a direção). Escala 0–100. Composto por três linhas:
- **ADX (linha branca):** intensidade da tendência (qualquer direção)
- **DI+ / DMI+ (linha verde):** pressão compradora
- **DI- / DMI- (linha vermelha):** pressão vendedora

## Interpretação da Força
| Valor | Interpretação |
|-------|---------------|
| < 20 | Sem tendência — range (evitar entradas de tendência) |
| 20–25 | Tendência fraca emergindo |
| > 25 | Tendência confirmada |
| > 40 | Tendência forte |
| > 60 | Tendência extrema (raro — risco de exaustão) |

## Interpretação da Direção (DI+ vs DI-)
- **DI+ > DI- e ADX subindo:** tendência de alta ganhando força → favorece LONG
- **DI- > DI+ e ADX subindo:** tendência de baixa ganhando força → favorece SHORT
- **Cruzamento DI+ × DI-:** primeiro alerta de mudança de pressão direcional (confirmar com BOS/CHoCH)
- **ADX caindo de >40:** tendência madura/exaurindo → cuidado com reversão ou range

## Uso no Sistema (filtro do checklist)
- **ADX > 25 = filtro de entrada de tendência habilitado.** Respeitar a direção dominante (DI+/DI-).
- **ADX > 25 + estrutura bearish 4H = hard block em LONG** (e vice-versa).
- **ADX < 20 = range:** desabilitar playbooks de tendência (1 e 2). Favorecer Playbook 3 (Stop Hunt Reversal) nas extremidades do range.
- **ADX subindo + cruzando 25 = confirmação de início de perna** — bom para entrada a favor da tendência recém-confirmada.

## Integração Multi-Timeframe
- ADX deve ser lido no MESMO TF do filtro direcional (4H para swing, 1H para gatilho).
- **Conflito:** ADX 4H > 25 bearish mas ADX 1H < 20 = perna maior vendedora com micro-range → repique para short, não reversão.
- Ref: [[multi-timeframe-analysis]] — ADX confirma se o TF de filtro está em tendência ou range antes de escolher o playbook.

## Combinação com outros indicadores
- **ADX > 25 + MACD a favor + EMA 200 confirmando = tripla confirmação de tendência** (peso alto).
- **ADX < 20 + Bollinger Bands estreitando = squeeze de volatilidade** → aguardar expansão (ADX cruzar 25 define a direção do breakout).
- **ADX alto + RSI divergente = tendência forte mas exaurindo** → apertar stops, não abrir nova posição.

## Falhas comuns
- Usar ADX como sinal de direção (ele só mede força — a direção vem de DI+/DI- e da estrutura).
- Entrar em tendência com ADX < 20 (whipsaw garantido).
- Ignorar ADX caindo após >40 (tendência exaurindo, não acelerando).

## Backlinks
- [[conservative-trend-follower-v2]]
- [[ATR]]
- [[multi-timeframe-analysis]]
- [[trade-playbooks]]
- [[confluence-score]]
