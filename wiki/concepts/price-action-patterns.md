# Padrões de Price Action — Gráficos e Velas

> Criado: 2026-04-26
> Categoria: Price Action / Padrões Gráficos

## Visão Geral

Price Action é análise baseada exclusivamente no movimento do preço. Os padrões se dividem em dois grupos:
- **Padrões gráficos** — formações que independem do tipo de candle (visíveis até em gráfico de linha)
- **Padrões de vela (candle)** — formações de 1-3 barras com significado de reversão/continuidade

---

## Parte 1 — Padrões Gráficos

### Categoria: Reversão

#### 1. Topos e Fundos Duplos (Double Top / Double Bottom)
- Dois topos próximos = resistência dupla → gatilho: rompimento do eixo (fundo entre os topos) para baixo
- Dois fundos próximos = suporte duplo → gatilho: rompimento do eixo (topo entre os fundos) para cima
- Segundo topo/fundo pode ser ligeiramente menor que o primeiro (não precisam ser simétricos)
- Alvo: 100% da amplitude (distância do topo/fundo ao eixo), com parcial em 50%
- Stop: acima do maior topo (para short) ou abaixo do maior fundo (para long)

#### 2. Ombro-Cabeça-Ombro (OCO) / OCO Invertido
- 3 topos: ombro esquerdo < cabeça > ombro direito
- Ombros devem ter 38–62% do tamanho da cabeça (variações permitidas)
- Neckline: linha ligando os fundos entre cabeça e ombros
- Gatilho de venda: fechamento abaixo da neckline
- Stop: no segundo ombro (não na cabeça)
- Alvo: 100% da amplitude (cabeça → neckline), com parcial em 50%
- OCO invertido = figura de fundo com regras espelhadas

#### 3. Topos e Fundos Arredondados (Rounded Top / Bottom)
- Progressão gradual de topos decrescentes (arredondado) → entrada no rompimento do gatilho traçado pelos fundos
- Objetivo: 100% de amplitude do topo mais alto ao ponto de entrada (parcial) e 200% (final)
- Stop: topo mais alto da formação
- Menos frequente mas com bons resultados quando bem definido

---

### Categoria: Continuidade

#### 4. Bandeiras (Flag)
- Estrutura: **mastro** (movimento forte e abrupto) + **bandeira** (lateralização, até levemente inclinada)
- Regras críticas:
  - Mastro deve ser abrupto — alta suave descaracteriza o padrão
  - Bandeira precisa de ≥ 2 topos + 2 fundos
  - Duração da bandeira: mais longa que o mastro mas < 3× o mastro (senão vira congestão)
  - Bandeira declinada: retração máxima de 38% do mastro
- Gatilho: máxima do candle que rompeu a linha superior da bandeira
- Alvo: amplitude do mastro, projetada a partir do fundo mais baixo da bandeira
- Stop: linha inferior ou fundo mais baixo da bandeira

#### 5. Pivots de Alta e Baixa
- Estrutura: perna direcional → correção de 38–62% → retomada rumo ao topo/fundo anterior
- Gatilho de compra: máxima do candle que rompe o topo anterior
- Alvo: 38%, 50%, 62% ou 100% da primeira perna
- Stop: fundo da correção

#### 6. Triângulos Ascendentes e Descendentes
- Triângulo ascendente: linha de tendência de alta + resistência horizontal → rompimento para cima esperado
- Triângulo descendente: linha de tendência de baixa + suporte horizontal → rompimento para baixo esperado
- Gatilho: máxima/mínima do candle que rompeu a linha horizontal
- Stop: último fundo (para compra) ou último topo (para venda)
- Alvo: 100% e 200% da distância do stop ao ponto de entrada

---

### Categoria: Indefinição

#### 7. Congestões (Consolidações)
- Critério: ≥ 10 períodos (15 em TFs curtos) comprimidos entre suporte e resistência próximas
- Quanto mais longa a congestão, maior o potencial do movimento resultante
- Entrada: máxima do candle que rompe o teto (long) ou mínima do que rompe o piso (short)
- Objetivo: mínimo 100% da amplitude da congestão (aberto para surfar tendência)
- Stop: piso (para long) ou teto (para short)

#### 8. Triângulos Simétricos
- Linha de tendência de alta + linha de tendência de baixa convergindo com inclinações parecidas
- Direção do rompimento indefinida — entrada após rompimento de uma das linhas
- Alvo: 1×–2× a distância do stop ao ponto de entrada
- Stop: último fundo (long) ou último topo (short)

#### 9. Alargamentos Simétricos
- Linhas de retorno que caminham em sentidos opostos (ampliando)
- Amplitude grande mas movimento resultante frequentemente menor que esperado
- Entrada: rompimento da linha de retorno superior (long) ou inferior (short)
- Stop: mínima do candle de rompimento (long)

---

## Parte 2 — Padrões de Vela (Candle Patterns)

### Doji — Indecisão e Reversão
Doji ocorre quando preço de abertura ≈ preço de fechamento. Indica equilíbrio entre compradores e vendedores = potencial reversão de tendência.

#### Tipos de Doji

| Tipo | Característica | Sinal |
|------|---------------|-------|
| **Doji Star** | Sombras simétricas, corpo no centro | Indecisão pura |
| **Doji Estrela da Manhã** | Aparece após queda (bearish candle + doji + bullish candle) | Reversão de baixa para alta |
| **Doji Estrela da Tarde** | Aparece após alta (bullish candle + doji + bearish candle) | Reversão de alta para baixa |
| **Dragonfly (Libélula)** | Sombra inferior longa, sem sombra superior | Rejeição de baixos → bullish |
| **Gravestone (Lápide)** | Sombra superior longa, sem sombra inferior | Rejeição de altos → bearish |
| **Long-legged (Pernalta)** | Sombra inferior dominante mas com pequena sombra superior | Bullish moderado |

#### Regra de Uso do Doji
- Sempre analisar 3 candles: anterior + doji + posterior
- O candle após o doji **confirma** a reversão
- Doji isolado = sinal fraco; doji em zona de S/R + confirmação = sinal forte
- Em cripto (alta volatilidade): exige confirmação adicional (volume, RSI, estrutura)

---

## Integração com SMC e Volume

### Bandeiras como FVGs
Bandeiras de alta frequentemente criam FVGs na perna do mastro — o retest da bandeira pode coincidir com o fill do FVG = confluência máxima de entrada.

### Volume Confirma
- Rompimento com volume acima da média = setup válido
- Rompimento em volume fraco = possível bull/bear trap → ver [[bull-bear-traps]]
- Mastro de bandeira deve ter volume alto; a própria bandeira deve ter volume declinando

### Doji em Níveis Chave
- Doji Gravestone em resistência + divergência RSI = bull trap de alta probabilidade
- Doji Dragonfly em suporte + RSI oversold = spring Wyckoff potencial

---

## Backlinks
- [[SMC]] — BOS/CHoCH ocorrem como rompimentos dos padrões aqui descritos
- [[Wyckoff]] — Spring = bear trap estrutural; UTAD = bull trap estrutural
- [[bull-bear-traps]] — regra do fechamento H4/D1 aplica-se a todos estes padrões
- [[fibonacci-structural]] — alvos de OCO/pivots frequentemente em Fib 100%, 162%, 200%
- [[volume-profile]] — confirmação de volume em rompimentos
- [[vvir-framework]] — V.V.I.R. valida rompimentos de triângulos e bandeiras
