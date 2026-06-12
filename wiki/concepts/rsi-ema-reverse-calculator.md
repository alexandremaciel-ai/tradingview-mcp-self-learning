# RSI & EMA with Reverse Calculator Panel [pig]

> Criado: 2026-06-12
> Categoria: Indicador / RSI / Calculadora reversa

## Definição
RSI com uma **EMA do próprio RSI** mais um **painel de cálculo reverso**: informa-se um valor de RSI desejado e o indicador devolve o preço necessário para atingi-lo. Componente do layout **RSI's e MACD**.

## O que plota
| Campo | Leitura |
|-------|---------|
| `Plot` | valor atual do RSI |
| `EMA` | média móvel do RSI (suaviza; cruzamento RSI×EMA = momentum) |
| `Entered RSI Value` | o RSI-alvo configurado (ex: 30) → painel calcula o preço correspondente |

## Leituras práticas
- **RSI cruzando sua EMA para cima** = momentum ganhando força; para baixo = perdendo (gatilho mais fino que o RSI puro).
- **Calculadora reversa**: planejar "a que preço o RSI chega em 30/70" → define alvos objetivos de entrada/saída e stops por momentum.
- Complementa a [[tabela-rsi-dinamica-maciel]] (que já dá P.RSI 30/50/70 por TF) — aqui o foco é o TF do gráfico + a EMA do RSI.

## Limitações
- O preço-alvo assume condições constantes; recalcula a cada barra.
- A EMA do RSI adiciona atraso — usar como confirmação.

## Backlinks
- [[rsi-divergences]]
- [[tabela-rsi-dinamica-maciel]]
- [[layouts]]
- [[indicators]]
