# Hash Ribbons

> Indicador on-chain de capitulação de mineradores — sinal histórico de fundo de ciclo BTC.
> Criador: Charles Edwards | Compilado: 2026-05-28

## Definição

**Hash Ribbons** usa o cruzamento entre a média móvel de 30 dias e 60 dias do hash rate do Bitcoin para detectar períodos de **capitulação de mineradores** e subsequentes **sinais de compra**.

## Componentes

- **Hash Rate 30DMA:** Média móvel de 30 dias do hash rate da rede
- **Hash Rate 60DMA:** Média móvel de 60 dias do hash rate da rede

## Fases

| Fase | Condição | Significado |
|------|----------|-------------|
| **Capitulação** 🔴 | 30DMA < 60DMA | Mineradores desligando máquinas → hash rate caindo → estresse financeiro |
| **Recuperação** 🟢 | 30DMA cruza acima de 60DMA | Hash rate se recuperando → mineradores voltando → pior já passou |
| **Expansão** 🟡 | 30DMA >> 60DMA | Hash rate saudável e crescente → rede em expansão |

## Sinal de Compra

O **sinal de compra** do Hash Ribbons ocorre quando:
1. Capitulação termina (30DMA volta acima de 60DMA)
2. Preço fecha acima da 10DMA e 20DMA

## Histórico

| Data do Sinal | Preço no Sinal | Retorno 12 meses |
|---------------|----------------|-------------------|
| Out 2015 | ~$300 | +350% |
| Jan 2019 | ~$3,500 | +160% |
| Ago 2020 | ~$11,500 | +400% |
| Ago 2022 | ~$21,000 | +165% |

**Fato:** Nenhum sinal de compra do Hash Ribbons resultou em perda no horizonte de 12 meses.

## Uso Operacional

**Para fundos de ciclo:**
- Hash Ribbons em capitulação = mineradores em estresse = fase final do bear market
- Sinal de recuperação = compra macro de alta convicção (historicamente infalível)
- Combinar com Puell Multiple < 0.5 para confirmação dupla

**Para topos de ciclo:**
- Hash Ribbons em expansão prolongada ≠ sinal de venda (apenas contexto)
- Hash Ribbons não é indicador de topo

**Disponibilidade no TradingView:**
- Indicador comunitário: buscar "Hash Ribbons" (Charles Edwards)
- Mostra as fitas coloridas no gráfico diário

**Limitações:**
- Halvings causam capitulação artificial (receita cai 50% → mineradores menos eficientes saem)
- Em 2022, evento FTX coincidiu com capitulação natural, amplificando o sinal
- Não funciona como timing de curto prazo — é indicador de ciclo (meses)

## Backlinks
- [[btc-cycle-analysis]] — framework de ciclo que usa Hash Ribbons como indicador de fundo
- [[puell-multiple]] — indicador complementar de estresse de mineradores
- [[mvrv-z-score]] — confirma zona de fundo quando Hash Ribbons sinaliza
- [[realized-price]] — preço abaixo do Realized Price + Hash Ribbons em capitulação = máxima convicção
