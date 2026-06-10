# LK Stock OS — guia de demanda/score local

Pointer atual: `areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json`.

A DB apontada contém agora:

- `current_local_stock`: superfície canônica de estoque/identidade.
- `demand_signals_stock_os`: sinais locais agregados por SKU normalizado, lidos de reports locais LK Sales/Data Spine.
- `current_stock_scored`: visão operacional com demanda, risco e prioridade local.
- `demand_score_summary`: resumo auditável.

Consulta exemplo:

```bash
sqlite3 $(python3 - <<'PY'
import json
p=json.load(open('areas/lk/sub-areas/stock/data/lk_stock_os_current_pointer.json'))
print(p['artifacts']['sqlite_db'])
PY
) "select action_priority, sku, title, size, units_signal, stock_quantity_max_observed, rupture_risk, operational_score from current_stock_scored where units_signal > 0 order by operational_score desc limit 20;"
```

Regra: confirmar pela DB Stock OS primeiro. Tiny/fonte viva só entra quando a DB estiver stale, bloqueada ou insuficiente para a decisão.

Guardrail: `public_availability_safe=0` e `availability_claim_allowed=0` nesta etapa.
