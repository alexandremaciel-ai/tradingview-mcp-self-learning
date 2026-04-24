# Bollinger Bands — Squeeze, Riding e Reversões

> Parâmetros padrão: 20 períodos, 2 desvios padrão
> Fonte: Crypto Trading KB v1.0 | Integrado: 2026-04-23

---

## 1. Padrões Principais

### Reversão nas Bandas
- Preço tocando **banda superior** + RSI sobrecomprado + volume declinante = reversão bearish iminente
- Preço tocando **banda inferior** + RSI sobrevendido + divergência bullish = reversão bullish
- **Atenção:** tocar a banda NÃO é sinal automático — exige confirmação de RSI + volume

### Squeeze (Compressão)
- Bandas comprimidas = volatilidade historicamente baixa → expansão explosiva iminente
- Aguardar rompimento da banda superior ou inferior com volume
- Operar **na direção** do rompimento, não contra ele
- Squeeze + StochRSI cruzando = confirmação adicional

### Riding the Band (Andar na Banda)
- Em tendência forte, o preço "anda" na banda sem reverter
- Preço tocando banda superior repetidamente em uptrend = **continuação**, não reversão
- Preço tocando banda inferior repetidamente em downtrend = **continuação**, não reversão
- Distinguir: riding = tendência forte; toque isolado = potencial reversão

---

## 2. Tabela de Leitura Rápida

| Cenário | Volume | RSI | Sinal |
|---------|--------|-----|-------|
| Toque banda superior | Declinante | > 70 | Reversão bearish |
| Toque banda inferior | Declinante | < 30 | Reversão bullish |
| Squeeze → rompimento superior | Crescente | -- | Long (riding the band) |
| Squeeze → rompimento inferior | Crescente | -- | Short (riding the band) |
| Riding the band superior | Normal | 50-70 | Continuação bullish |

---

## 3. Parâmetros

- **Padrão:** BB(20, 2) — média de 20 períodos, ±2 desvios padrão
- **Timeframes:** 1H (gatilho), 4H (confirmação), Diário (macro)
- **StochRSI 3/3/14/14** como confirmador de reversões nas bandas

---

## 4. Integração

- Squeeze + FVG na mesma região = entrada de alta convicção pós-expansão
- Riding the band + MACD crescente = tendência sustentada (não contra-operar)
- Toque banda + divergência RSI 1H = setup de reversão sniper

---

## Backlinks
- [[rsi-divergences]]
- [[macd]]
- [[trade-playbooks]]
- [[vvir-framework]] — volume declinante em toque de banda = critério V.V.I.R.
