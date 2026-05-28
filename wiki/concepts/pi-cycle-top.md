# Pi Cycle Top Indicator

> Indicador on-chain/técnico de topos de ciclo Bitcoin — precisão histórica de dias.
> Criador: Philip Swift | Compilado: 2026-05-28

## Definição

O **Pi Cycle Top Indicator** usa dois múltiplos da média móvel diária para identificar topos de ciclo do Bitcoin:
- **111DMA** (Média Móvel de 111 Dias)
- **350DMA × 2** (Média Móvel de 350 Dias multiplicada por 2)

## Sinal de Topo

**Quando a 111DMA cruza ACIMA da 350DMA×2 → TOPO DE CICLO**

## Histórico de Precisão

| Ciclo | Data do Topo Real | Data do Cruzamento | Precisão |
|-------|-------------------|--------------------|----------|
| 2013 | 29 Nov 2013 | 29 Nov 2013 | ± 0 dias |
| 2017 | 17 Dez 2017 | 17 Dez 2017 | ± 0 dias |
| 2021 | 10 Nov 2021 | 12 Abr 2021* | ~7 meses antes |

*Em 2021 o indicador deu sinal antecipado — houve double top ($64K em abril, $69K em novembro).

## Uso Operacional

**Para determinar se topo de ciclo ocorreu:**
1. Verificar se 111DMA cruzou 350DMA×2 neste ciclo
2. Se **SIM** → topo provavelmente ocorreu → bear market pode ter começado
3. Se **NÃO** → topo pode não ter sido atingido ainda

**Como monitorar no TradingView:**
1. Adicionar indicador comunitário "Pi Cycle Top" (buscar nos indicadores)
2. Ou manualmente: adicionar 2 SMAs (111 e 350) + multiplicar a 350 por 2

**Limitações:**
- Amostra pequena (apenas 3 ciclos com dados)
- Em 2021 deu sinal antecipado (double top distorceu)
- Não dá sinal de FUNDO, apenas de TOPO
- Pode ser distorcido por novos fluxos institucionais (ETFs)

## Backlinks
- [[btc-cycle-analysis]] — framework de ciclo que usa Pi Cycle como indicador de topo
- [[mvrv-z-score]] — indicador complementar de topo (Z-Score > 7)
- [[nupl]] — indicador complementar de topo (NUPL > 0.75)
