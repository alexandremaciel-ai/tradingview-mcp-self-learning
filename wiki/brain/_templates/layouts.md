# Brain — Registry de Layouts do TradingView

> O agente lê este arquivo no **passo 0c do AUTO-PILOT** (detecção de layout ativo).
> A análise técnica (Fase 6) é **DIRIGIDA pelos indicadores do layout ativo** — não por um checklist fixo.
> Recalibrar quando o usuário mudar indicadores: operação **RECALIBRATE LAYOUTS** (ver CLAUDE.md).
> Última calibração: _(preencher)_

## Como detectar o layout ativo (runtime)
1. `chart_get_state()` → conjunto de `studies` + símbolo/TF.
2. (opcional) nome via `ui_evaluate` lendo o toolbar: `[aria-label^="Entrou como"]` → "Layout ativo: X".
3. Casar o conjunto de studies com o **Fingerprint** de um perfil abaixo (match parcial ≥3 studies basta).
4. Sem match → rótulo `layout-adhoc`: analisar com os indicadores presentes e registrar o perfil ao final.

## Trocar de layout (modo híbrido — só se o pedido/classe exigir)
- Navegação confiável: `ui_evaluate("location.href = location.origin + '/chart/{SLUG}/'")` (navegação real recarrega o layout salvo).
- Verificar: `ui_evaluate` lendo "Layout ativo: X" + `tv_health_check` (símbolo/TF batem com o esperado).
- ⚠️ `layout_switch` (internal_api) **não** recarrega a janela do Desktop sozinho; precisa de navegação por URL ou `location.reload()`.

---

## Layout: {NOME}
- **Slug/URL:** /chart/{SLUG}/ | **ID:** {id}
- **Símbolo/TF padrão:** {symbol} | {tf}
- **Fingerprint (studies):** {lista de indicadores}
- **Panes:** {estrutura}
- **Indicadores e leitura:** {indicador → [[conceito]] → como ler}
- **Recipe Fase 6:** {quais sub-itens aplicar ✓ / quais são N/A}
- **Serve para:** {classe/estilo}
- **Peso de confluência:** {o que pesa mais/menos neste layout}
- **Snapshot {data}:** {valores capturados na calibração}

---

> Atualizar via RECALIBRATE LAYOUTS. Layouts não usados há muito tempo → candidatos a remoção.
