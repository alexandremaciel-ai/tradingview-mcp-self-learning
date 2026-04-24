# Trade Playbooks — Setups Padronizados

> 4 playbooks com critérios de entrada, stop e gestão definidos.
> Todos os playbooks exigem aprovação do checklist de entrada obrigatório (abaixo).
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## Checklist de Entrada Obrigatório

Todos os critérios devem ser atendidos antes de executar qualquer playbook:

```
□ [1] Viés macro alinhado (Mensal/Semanal confirma a direção do trade)
□ [2] EMA 200 no 4H/1H confirma a direção (acima → Long | abaixo → Short)
□ [3] Zona de entrada identificada (FVG, Order Block, Fibonacci, POC)
□ [4] Armadilha de liquidez detectada (Stop Hunt, Bull/Bear Trap) se aplicável
□ [5] BOS confirmado no timeframe de gatilho (fechamento de candle além do pivô)
□ [6] ATR Filter: |Abertura - Fechamento| > ATR(14) × 1.5
□ [7] Volume Filter: Volume > SMA(Volume, 20) × 1.5
□ [8] Ausência de eventos macro de alto impacto iminentes (FOMC, CPI, NFP)
```

**Mínimo para entrar:** 6 de 8. Todos os 8 = alta convicção.

---

## Playbook 1 — Long em Retração de Tendência de Alta

**Contexto:** macro bullish, preço puxando para reteste de zona de suporte.

1. Macro bullish (Mensal/Semanal HH/HL) + 4H acima da EMA 200
2. Aguardar retração para **Golden Zone Fibonacci 0.618–0.786** do último impulso
3. Confirmar: FVG Bullish ou Bullish OB na zona + divergência bullish no RSI do 1H
4. Gatilho: BOS bullish no 15M (fechamento acima do último HH do 15M)
5. Stop: 1 tick abaixo do pavio do fundo da retração
6. TP: distribuição 35/35/15/15 → ver [[position-sizing]]

---

## Playbook 2 — Short em Repique de Tendência de Baixa

**Contexto:** macro bearish, preço repicando para reteste de zona de resistência.

1. Macro bearish (Mensal/Semanal LH/LL) + 4H abaixo da EMA 200
2. Aguardar repique para **Golden Zone Fibonacci 0.618–0.786** do último impulso de queda
3. Confirmar: FVG Bearish ou Bearish OB na zona + divergência bearish no RSI do 1H
4. Gatilho: BOS bearish no 15M (fechamento abaixo do último LL do 15M)
5. Stop: 1 tick acima do pavio do topo do repique
6. TP: distribuição 35/35/15/15 → ver [[position-sizing]]

---

## Playbook 3 — Stop Hunt Reversal

**Contexto:** spike de liquidez além de EQH/EQL ou PDH/PDL sem volume, seguido de retorno à range.

1. Preço faz spike além de EQH/EQL ou PDH/PDL → retorna para a range
2. Aguardar **Engulfing** ou **Pin Bar** de reversão após o spike
3. Confirmar: volume do spike < SMA(20) | candle de reversão com volume > SMA(20) × 1.5
4. Gatilho: fechamento de candle dentro da range anterior (cancela o rompimento)
5. Stop: além da extremidade do spike
6. TP1: 50% da range. TP2: extremo oposto da range

---

## Playbook 4 — Squeeze de Alavancagem

**Contexto:** Funding Rate em extremo + preço comprimido em zona de liquidez.

1. Funding Rate extremo: > 0.07%/8h (squeeze long) ou < -0.04%/8h (squeeze short)
2. Preço comprimido em zona de liquidez (EQH/EQL ou HVN)
3. Alta probabilidade de movimento explosivo **contra** o lado mais alavancado
4. Direção: funding alto → squeeze Long → operar **Short**. Funding negativo extremo → squeeze Short → operar **Long**
5. Confirmar: Open Interest elevado + BOS no 15M na direção do squeeze
6. Stop apertado: 1–1.5% do preço de entrada
7. Posição reduzida: 0.5% do capital em risco (trade de maior risco)

---

## Janelas de Ataque (BRT)

| Janela | Horário BRT | Observação |
|--------|-------------|------------|
| Abertura NY | 09h30 – 11h30 | Alta liquidez, movimentos direcionais fortes |
| Overlap London/NY | 09h00 – 12h00 | Maior volume do dia — FVGs frequentes |
| Tarde Europa/NY | 14h00 – 16h00 | Boas extensões de movimento |
| Asian Session | 23h00 – 00h30 | Baixa liquidez — Stop Hunts antes de NY (Playbook 3) |
| ⛔ Bloqueio | 20h30 – 21h30 | Virada diária — manipulação elevada, evitar entradas |
| London Kill Zone | 04h00 – 07h00 | Sweeps agressivos de liquidez (Playbook 3 frequente) |

---

## Backlinks
- [[SMC]] — BOS, FVG, OB, EQH/EQL
- [[rsi-divergences]] — divergência como confirmação
- [[fibonacci-structural]] — Golden Zone como zona de entrada
- [[volume-profile]] — POC e HVN como alvos
- [[position-sizing]] — regras de TP e gestão
- [[vvir-framework]] — validação de volume e intensidade
- [[conservative-trend-follower-v2]]
