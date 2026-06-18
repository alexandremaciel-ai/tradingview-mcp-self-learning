# Disciplina Operacional — Psicologia e Proteção de Capital

> O edge técnico só sobrevive se a disciplina o protege depois de uma perda.
> Esta página é PROTOCOLO, não teoria: o LLM consulta [[metrics]] antes de emitir bias operável e aplica as regras de bloqueio abaixo.
> Complementa os Circuit Breakers de [[position-sizing]].
> **Escopo:** aqui é a psicologia de **autodisciplina** (proteger-se de si mesmo). A psicologia de
> **estrutura de mercado** (Sardelas vs Institucionais, "Sair da Matrix", varejo = liquidez) vive em
> [[institutional-flow-poi]] — as duas se complementam.

## 1. Estados de Bloqueio (enforcement)

Antes de emitir QUALQUER recomendação operável, checar `metrics.md`:

| Gatilho | Estado | Ação obrigatória |
|---------|--------|------------------|
| **3 losses consecutivos** (streak atual ≥ 3) | 🔴 Circuit breaker | Rebaixar para "somente observação / paper". Nenhuma entrada real por 24h ou até reset com 1 win em paper. |
| **Drawdown 5% no dia** | 🔴 Stop diário | Parar. Retomar só no dia seguinte. |
| **2 losses no mesmo ativo no dia** | 🟡 Cooldown | Trocar de ativo ou pausar 4h. O ativo "te pegou" — sair do duelo. |
| **Confiança descalibrada** (alta < média no `metrics.md`) | 🟡 Revisão | Reduzir tamanho em 50% até recalibrar os critérios de confiança. |

> Quando um estado 🔴/🟡 estiver ativo, declarar EXPLICITAMENTE na sessão: `⛔ Disciplina: [estado] → recomendação rebaixada para observação`.

## 2. Anti-Revenge Trade
O revenge trade (reentrar no impulso logo após um stop, para "recuperar") é o maior destruidor de conta.
- Após um stop: **aguardar 1 candle do TF de gatilho fechar** antes de avaliar nova entrada.
- A nova entrada precisa de [[confluence-score]] ≥ 6 **próprio** — não vale "é a mesma tese de antes".
- Se a vontade de entrar é "recuperar o que perdi" e não um setup novo válido → **não é trade, é emoção**. Registrar em [[mistakes]] categoria `psicologico`.

## 3. Anti-FOMO
- Não perseguir candle já estendido. Se o preço já saiu da zona de entrada planejada, o trade acabou — esperar o próximo.
- Movimento "sem você" não é prejuízo; entrada ruim é.
- FOMO clássico: comprar topo de pump / vender fundo de dump. Cruzar sempre com RSI/StochRSI extremo antes de perseguir.

## 4. Anti-Overtrading
- Máximo de entradas por dia coerente com o capital e o circuit breaker (qualidade > quantidade).
- Sem setup com score ≥ 6 → **não operar é uma posição válida**. "Nenhum setup identificado" é resposta legítima.
- Cada entrada precisa de registro em `wiki/sessions/` — se você não consegue justificar por escrito, não entre.

## 5. Rotina de Recuperação (após série de perdas)
1. Parar de operar (respeitar o circuit breaker).
2. Reler os últimos 3 trades + as entradas recentes de [[mistakes]].
3. Identificar o padrão do erro: foi técnico (bias/timing) ou emocional (revenge/fomo/overtrading)?
4. Voltar em **paper / tamanho mínimo** até 2 wins consecutivos no método antes de retomar tamanho normal.
5. Registrar a lição em [[mistakes]] e, se for padrão, em [[patterns]].

## 6. Checklist Mental Pré-Entrada (10s)
- [ ] Tenho um [[confluence-score]] ≥ 6 escrito?
- [ ] O macro/regime confirma ou estou contra-macro (size menor)?
- [ ] Nenhum circuit breaker ativo no `metrics.md`?
- [ ] Estou entrando por SETUP ou por EMOÇÃO (recuperar/medo de ficar de fora)?
- [ ] Meu SL está definido ANTES da entrada e é sagrado?

## Backlinks
- [[institutional-flow-poi]] — psicologia de estrutura de mercado (Sardelas vs Institucionais)
- [[position-sizing]] — circuit breakers e regras de ouro
- [[mistakes]] — categoria `psicologico`
- [[confluence-score]] — gate objetivo de entrada
- [[metrics]] — estado de circuit breaker e calibração
- [[trade-playbooks]]
