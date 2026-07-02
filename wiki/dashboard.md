# 📊 Trading Dashboard

> Consultas ao vivo (Dataview) sobre o frontmatter das notas atômicas. Substitui pedir ao
> LLM "como estão minhas previsões / quais setups pagam" — o Obsidian responde a custo zero.

## ⏳ Previsões Abertas
```dataview
TABLE symbol AS "Ativo", tf AS "TF", side AS "Lado", confluence AS "Conf", confidence AS "Confiança", date AS "Data"
FROM "wiki/brain/predictions"
WHERE type = "prediction" AND status = "open"
SORT date DESC
```

## ✅ Últimas Previsões Fechadas
```dataview
TABLE symbol AS "Ativo", tf AS "TF", side AS "Lado", status AS "Resultado", rr_real AS "R:R real", setup AS "Setup"
FROM "wiki/brain/predictions"
WHERE type = "prediction" AND status != "open"
SORT date DESC
LIMIT 15
```

## 📈 Últimas Sessões
```dataview
TABLE symbol AS "Ativo", tf AS "TF", bias AS "Bias", price AS "Preço", confluence AS "Conf", result AS "Resultado"
FROM "wiki/sessions"
WHERE type = "session"
SORT date DESC
LIMIT 12
```

## 🎯 Win Rate por Setup (previsões fechadas)
```dataview
TABLE length(rows) AS "N", sum(choice(status = "win", 1, 0)) AS "Wins", round(100 * sum(choice(status = "win", 1, 0)) / length(rows)) + "%" AS "Win Rate"
FROM "wiki/brain/predictions"
WHERE type = "prediction" AND status != "open" AND setup
GROUP BY setup
SORT length(rows) DESC
```

## 📊 Win Rate por Regime
```dataview
TABLE length(rows) AS "N", round(100 * sum(choice(status = "win", 1, 0)) / length(rows)) + "%" AS "Win Rate"
FROM "wiki/brain/predictions"
WHERE type = "prediction" AND (status = "win" OR status = "loss")
GROUP BY regime
```

## Backlinks
- [[index]] · [[metrics]]
