# Referência — Classes de Pedido + Regras Especiais

> Carregada por `brain-read`/`analyze`/`macro-scan` para classificar o pedido e ajustar o pipeline.

## Tabela de Classificação (escolher a classe → seguir o pipeline)

| Classe | Quando | Macro Scan | Checklist | Extras |
|--------|--------|------------|-----------|--------|
| `BTC` | Análise solo de Bitcoin | **Completo** (10 passos) | Fases 1-9 completas | BTCUSDLONGS/SHORTS obrigatório |
| `BTC+ETH` | BTC e ETH juntos | Completo **1×** | BTC completo → ETH relativo (+ ETH/BTC pair) | Declarar ETH outperform/underperform |
| `BTC+ALTCOIN` | BTC + altcoin específica (BTC+SOL, BTC+ADA) | **Parcial** (7 passos): USDT.D + BTC.D + TOTAL3 + BTC + Longs/Shorts + par | BTC: Fases 1-6,8-9 → Altcoin: Fases 1-6,8-9 | ALTCOIN/BTC pair obrigatório. Wyckoff só se vol > $50M |
| `ALTCOIN` | SOL, ADA, DOGE, etc. | **Reduzido** (5 passos): USDT.D + BTC.D + TOTAL3 + BTC bias + par | Fases 1-6, 8-9. Wyckoff só se vol > $50M | Tag obrigatória: `scalp/swing/holder` |
| `EQUITIES` | AAPL, TSLA, SPX, ações | **TradFi**: DXY + SPX + VIX + setor (XLK/XLF) | Fases 1-6, 9. Sem USDT.D/Longs/Shorts | Checar earnings/eventos. Sem Funding Rate |
| `WATCHLIST` | "scan da lista", vários ativos | Completo **1×** no início | Compacto por ativo: quote + indicators + bias | Output: tabela resumo. 1 sessão total |
| `DAILY` | "daily", "morning scan" | Completo **1×** | Macro → BTC rápido (D+4H) → Watchlist → Previsões | Dashboard compacto |
| `CYCLE` | "ciclo do BTC", "topo/fundo" | Completo + on-chain | Ver skill `btc-cycle` | Score Topo/Fundo |

## Regras Especiais por Classe

**BTC:** Macro vence micro — não confiar em rompimento sem fechamento + volume + USDT.D confirmando.

**ALTCOIN:** Se BTC em risco macro → altcoins só como scalp/day trade. Wyckoff: só se vol diário > $50M.
Compra de altcoin (swing) **só com o BTC dando sustentação técnica** (gatilho/estrutura de alta) — sem
gatilho claro no ativo primário, long em secundárias é alto risco. Ver `[[institutional-flow-poi]]`.

**EQUITIES:** Checar earnings iminentes (7 dias) → alertar risco de gap. Horário: pré-market (05h–10:30h BRT), regular (10:30–17:00h), after-hours — sinais em regular = mais confiáveis. Playbook 4 (squeeze crypto) **não se aplica** — usar Playbooks 1-3.

**WATCHLIST:** Macro 1× no início. Output: tabela `Ativo | Preço | Bias | Confiança | Setup? | Nota`. Destacar "Top 3". 1 sessão: `YYYY-MM-DD-WATCHLIST.md`.

**DAILY:** Macro 1× completo. BTC rápido (D+4H). Fechar previsões expiradas (>48h). Output: dashboard `Macro | BTC Bias | Alertas | Watchlist | Previsões`.

## Como escrever na sessão (adaptar por classe)

**Todas as classes:**
- `Layout: [nome] | Indicadores ativos: [lista do layout]` (passo 0c)
- `Classe: BTC | BTC+ETH | ALTCOIN | EQUITIES | WATCHLIST | DAILY`
- `MTF: M/W/D/4H/1H → [resumo]` (DAILY: D+4H, mas citar o M no contexto de ciclo)
- `Indicadores: RSI [M/W/D/4H/1H/15M valores+direção+divergências] | StochRSI [W/1H/15M %K/%D+cross] | MACD [M/W/D/4H vs zero+cross+hist] | ADX [valor]`
- `Bias: LONG/SHORT/NEUTRO | Confiança: alta/média/baixa`

**BTC / BTC+ETH — adicionar:**
- `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega`
- `Div RSI USDT.D: [TF:tipo ou —] | BTC↔USDT.D: alinhado/divergente`
- `Derivativos: BTC FR [valor] OI [valor] | ETH FR [valor] OI [valor] | F&G [valor]` (de raw/feeds/latest.md)
- `Longs/Shorts: BTCUSDLONGS [valor] | BTCUSDSHORTS [valor] | Ratio [X.X] | Squeeze Risk: [nível]`
- (BTC+ETH) `ETH/BTC: [valor] [outperform/underperform] [%]`

**BTC+ALTCOIN — adicionar:**
- `Liquidez: acima/abaixo/neutra | USDT.D: confirma/nega`
- `Div RSI USDT.D: [TF:tipo ou —] | BTC↔USDT.D: alinhado/divergente`
- `Derivativos: BTC FR [valor] OI [valor] | F&G [valor]` (de raw/feeds/latest.md)
- `Longs/Shorts: Ratio [X.X] | Squeeze Risk: [nível]`
- `{ALT}/BTC: [valor] [outperform/underperform] [%]`
- `Tipo: scalp | swing`

**ALTCOIN — adicionar:**
- `Setor: DeFi/AI/L2/meme/infra | Par/BTC: [subindo/caindo] | BTC.D: [valor] [tendência]`
- `Sentimento: F&G [valor]` (de raw/feeds/latest.md; funding default cobre BTC/ETH)
- `Tipo: scalp | swing | holder`

**EQUITIES — adicionar:**
- `VIX: [valor] [tendência] | Setor ETF: [ticker] [tendência] | Earnings: [data ou N/A]`

**WATCHLIST — usar tabela:** `| Ativo | Preço | Bias | Confiança | Setup? | Nota |`

**DAILY — usar dashboard:** `Macro: Risk-On/Off/Misto | BTC: [bias] | Alertas: [N] | Previsões abertas: [N]`
