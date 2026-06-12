# Crypto Smart Volume PRO

> Criado: 2026-06-12
> Categoria: Indicador / Volume / Fluxo institucional

## Definição
Indicador de volume "inteligente" que tenta isolar o fluxo institucional do ruído de varejo. Presente nos layouts do usuário em duas versões: **v1** (Liquidity e SMC) e **v2** (Trade Diario).

## O que plota
| Campo | Versão | Leitura |
|-------|--------|---------|
| `Volume Inteligente` | v1+v2 | volume "limpo" estimado da barra |
| `Média de Volume` | v1+v2 | baseline de comparação |
| `Smart Score` | v2 | score de convicção do fluxo (negativo = distribuição/fraqueza) |
| `Z-Score` | v2 | desvio do volume vs média (quão anômalo) |
| `PVO` | v2 | Percentage Volume Oscillator (momentum de volume) |

## Leituras práticas
- **Volume Inteligente < Média + Smart Score negativo** → movimento sem convicção (rally/queda fraca) → não confiar no rompimento.
- **Z-Score alto** → barra de volume anômala = clímax ou início de expansão.
- Confirma (não origina) o sinal: cruzar com price action, RSI/MACD e estrutura.

## Limitações
- Caixa-preta (lógica proprietária) — usar como confirmação, nunca gatilho isolado.
- Em cripto 24/7, "média de volume" distorce em fins de semana de baixa liquidez.

## Backlinks
- [[layouts]] — presente em Trade Diario (v2) e Liquidity e SMC (v1)
- [[volume-profile]] — complementa o perfil de volume por preço
- [[indicators]]
