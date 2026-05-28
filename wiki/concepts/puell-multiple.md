# Puell Multiple

> Métrica on-chain de ciclo Bitcoin — mede a receita dos mineradores vs média histórica.
> Fonte: LookIntoBitcoin / Glassnode | Compilado: 2026-05-28

## Definição

O **Puell Multiple** é a razão entre a receita diária dos mineradores (em USD) e a média móvel de 365 dias dessa receita. Criado por **David Puell**.

## Fórmula

```
Puell Multiple = Receita Diária dos Mineradores (USD) / MA365(Receita Diária)
```

## Interpretação

| Zona | Puell | Significado | Fase do Ciclo |
|------|-------|-------------|---------------|
| 🔴 Sobrevalorizado | >4 | Mineradores com receita extrema, vendem agressivamente | TOPO |
| 🟡 Neutro | 1-4 | Receita saudável | MARKUP / MARKDOWN |
| 🟢 Subvalorizado | 0.5-1 | Receita abaixo da média | ACUMULAÇÃO |
| 🟢🟢 Fundo | <0.5 | Mineradores em estresse financeiro | CAPITULAÇÃO / FUNDO |

## Uso Operacional

**Identificação de fundos:**
- Puell < 0.5 = mineradores vendendo para cobrir custos operacionais = capitulação de mineradores
- Historicamente, Puell < 0.5 precedeu os maiores ralis de ciclo
- Combinar com Hash Ribbons para confirmação de fundo

**Identificação de topos:**
- Puell > 4 = mineradores com lucro extremo = pressão vendedora institucional
- Historicamente, Puell > 4 precedeu correções significativas

**Limitações:**
- Afetado por halvings (cada halving corta a receita pela metade, criando reset artificial)
- Custo de mineração varia geograficamente — Puell não captura margem real
- Melhor usado em conjunto com MVRV e NUPL para visão completa do ciclo

## Backlinks
- [[btc-cycle-analysis]] — framework completo de ciclo que utiliza o Puell Multiple
- [[mvrv-z-score]] — indicador complementar de ciclo (valorização relativa)
- [[nupl]] — indicador complementar (sentimento baseado em lucro não realizado)
- [[realized-price]] — base para cálculos de ciclo
