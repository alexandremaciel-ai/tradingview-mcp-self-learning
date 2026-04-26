# 📊 Trading Dashboard

## ⏳ Previsões Abertas (Brain)
```dataview
TABLE ativo, confidence as "Confiança", status
FROM "wiki/brain/predictions-log"
WHERE contains(status, "aberta")
```

## 📈 Últimas Sessões
```dataview
TABLE bias, Preço, assets as "Ativos"
FROM "wiki/sessions"
SORT file.mtime DESC
LIMIT 10
```

## 🎯 Top Setups
```dataview
TABLE win-rate as "Win Rate", R-médio as "R:R", ocorrências as "Vezes"
FROM "wiki/setups"
WHERE win-rate > 0
SORT win-rate DESC
LIMIT 5
```

## 🧠 Últimos Insights
```dataview
TABLE Ativo, Baseado-em as "Evidência"
FROM "wiki/brain/insights"
SORT file.mtime DESC
LIMIT 5
```

## Backlinks
- [[index]]
- [[overview]]
