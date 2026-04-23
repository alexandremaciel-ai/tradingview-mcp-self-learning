# Realized Price (Preço Realizado)

> Métrica on-chain fundamental — "preço médio de compra de toda a rede Bitcoin".
> Fonte: bitbo.io | Compilado: 2026-04-23

## Definição

**Realized Price** é o preço médio pelo qual cada Bitcoin foi movimentado pela última vez na blockchain. Diferente do preço de mercado (cotação atual), a Realized Price reflete o custo médio real de aquisição de todos os coins circulantes.

**Em outras palavras:** é o preço que cada BTC "pagou" para chegar à mão do seu atual detentor.

## Cálculo

```
Realized Cap = Σ (preço no momento do último movimento × quantidade)
Realized Price = Realized Cap / Oferta Circulante
```

- Coins perdidas ou em cold storage há muito tempo ficam presas no preço de quando foram movimentadas pela última vez
- Coins que se movem frequentemente atualizam o Realized Price para o preço atual

## Componentes do Gráfico (bitbo.io)

| Elemento | Descrição |
|---------|-----------|
| **Linha colorida (arco-íris)** | Preço atual do BTC, colorido por dias até o halving |
| **Linha amarela** | Realized Price |
| **Oscilador cinza (bottom)** | Razão Preço / Realized Price |
| **Barra vermelha (oscilador)** | Nível 1,0 = preço = Realized Price |

## Uso Operacional

**Como suporte macro:**
- Historically, a Realized Price tem servido como **suporte de longo prazo**
- Quando o preço cai até ou abaixo da Realized Price = capitulação → oportunidade de compra macro
- Preço muito acima da Realized Price = mercado com grande lucro latente → risco de distribuição

**Oscilador Realized Price:**
- Oscilador alto = preço sobe mais rápido que os coins se movem (acumulação passiva)
- Oscilador baixo/< 1 = preço abaixo do custo médio da rede = capitulação

**Long-Term Holder (LTH) implication:**
- LTHs que compraram abaixo da Realized Price atual e não moveram seus coins "puxam" o Realized Price para baixo
- Quando esses LTHs vendem (movimentam), o Realized Price sobe e cria "floor" maior

## Relação com Outras Métricas

| Métrica | Como usa o Realized Price |
|---------|--------------------------|
| **MVRV** | Market Cap / Realized Cap |
| **MVRV-Z** | Desvios padrão do MVRV acima da média histórica |
| **NUPL** | (Market Cap - Realized Cap) / Market Cap |
| **SOPR** | Preço no gasto / Preço na aquisição (mesma lógica aplicada a outputs) |

## Backlinks
- [[mvrv-z-score]] — usa Realized Cap para calcular "valor justo"
- [[nupl]] — usa Realized Cap como base do lucro não realizado
- [[sopr]] — versão por output individual do mesmo conceito
- [[research/2026-04-23-onchain-metrics-batch7]]
