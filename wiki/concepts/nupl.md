# NUPL (Net Unrealized Profit/Loss)

> Métrica on-chain de sentimento e ciclo Bitcoin.
> Criadores: Tuur Demeester, Tamás Blummer, Michiel Lescrauwaet | Compilado: 2026-04-23

## Definição

**NUPL** mede a diferença entre lucros e perdas não realizados de todos os detentores de Bitcoin, normalizada pelo Market Cap. Indica o estado emocional médio do mercado.

## Fórmula

```
NUPL = (Market Cap - Realized Cap) / Market Cap
```

- **Positivo** → o mercado está, em média, em lucro não realizado (segurando BTC acima do custo)
- **Negativo** → o mercado está, em média, em prejuízo não realizado (segurando abaixo do custo)

## Zonas de Sentimento

| Zona | NUPL | Emoção | Implicação |
|------|------|--------|-----------|
| **Capitulação** | < 0 | Desespero | Fundos históricos — melhor zona de compra macro |
| **Esperança** | 0 – 0,25 | Esperança/Medo | Acumulação pós-fundo |
| **Otimismo** | 0,25 – 0,5 | Otimismo/Ansiedade | Tendência confirmada |
| **Crença** | 0,5 – 0,75 | Crença/Negação | Bull market maduro |
| **Euforia** | > 0,75 | Euforia/Ganância | **Zona de topo — risco máximo** |

## Uso Operacional

**Identificação de fundos:**
- NUPL < 0 = capitulação em andamento → historicamente melhor entrada macro para BTC
- NUPL voltando acima de 0 = fim da capitulação, confirmação de reversão

**Identificação de topos:**
- NUPL > 0,75 = euforia → início de distribuição progressiva
- NUPL descendo de 0,75+ = confirmação de topo de ciclo

**Limitações:**
- Indicador de médias — não reflete comportamento de grupos específicos (LTH vs STH)
- Melhor combinado com SOPR (comportamento real de gastos) e MVRV-Z (valorização relativa)

## Backlinks
- [[mvrv-z-score]] — indicador complementar (valorização relativa ao "valor justo")
- [[sopr]] — mede lucro realizado em transações (comportamento atual vs. NUPL = posição latente)
- [[realized-price]] — Realized Cap é o denominador do NUPL
- [[research/2026-04-23-onchain-metrics-batch7]]
