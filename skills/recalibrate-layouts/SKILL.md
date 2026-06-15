---
name: recalibrate-layouts
description: Recalibrar os perfis de layout do TradingView em wiki/brain/layouts.md. Use quando o usuário pede "recalibrar layouts" ou muda os indicadores no TradingView. Operação do agente via MCP (os scripts de scripts/tools são offline). Percorre cada layout, captura os studies via CDP e reescreve os fingerprints.
---

# RECALIBRATE LAYOUTS

⚠️ Operação do agente via MCP (não há script offline para isto).

1. `layout_list` → por layout: navegar `ui_evaluate("location.href=location.origin+'/chart/{slug}/'")`
   → verificar toolbar "Layout ativo: X" + `tv_health_check`.
2. `chart_get_state` + `pane_list` + `data_get_study_values` (+ pine lines/labels/tables/boxes p/ SMC)
   + `capture_screenshot`.
3. Atualizar `wiki/brain/layouts.md` + `brain/indicators.md`; restaurar o layout original; append `wiki/log.md`.

> Mecânica de troca: navegação por `/chart/{slug}/` recarrega o layout salvo (`layout_switch` puro
> NÃO recarrega o Desktop). ⚠️ Navegar reseta o símbolo para o salvo do layout → re-setar
> `chart_set_symbol` após cada navegação ao varrer multi-ativo.
