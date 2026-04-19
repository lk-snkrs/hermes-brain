# Pending Tasks — 2026-04-19 14:00

## Status Sistema (100% auditado)

### Data Sources — Status Real
| Source | Status | Nota |
|--------|--------|------|
| Shopify orders | ✅ OK | Synced 2026-04-19 01:25 |
| Shopify customers | ✅ OK | 26.560 customers |
| Frenet shipping | ✅ OK | 131 registros |
| JudgeMe reviews | ✅ OK | 429 reviews |
| GA4 traffic | ✅ OK | 444.977 registros |
| Klaviyo | ✅ OK | |
| transactions_full | ✅ FIXADO | Script criado + adicionado ao full_sync |
| Meta Ads | ❌ TOKEN INVÁLIDO | Desde 12/03 — re-autenticar no Doppler |
| inventory | ✅ OK | Usa variants.inventory_quantity |

### Cron Jobs — 26 total
- **10 ativos** — todos com last_status=ok
- **9 pausados** — Inventory, Market Intel, Wisdom, COO, Proactive, Daily Report, Memory, Learning Loop, Morning
- **3 nunca executaram** — Consolidation (20/04), Monthly Review (28/04), Decisions (01/05)

### Bugs Corrigidos Hoje (19/04)
1. **Shopify pagination** — page_info fallback pra timestamp ✅
2. **Timezone anomaly_deepdive** — 8x CURRENT_DATE → BRT ✅
3. **Timezone anomaly_check** — 8x CURRENT_DATE → BRT ✅
4. **lk_morning_briefing** — NameError (datetime/timezone import) ✅
5. **transactions_full** — script recriado + adicionado ao full_sync ✅
6. **Full Sync** — agora com 6 fontes (add Tx Full) ✅

## O que PRECISA DE VOCÊ
- **Meta Ads** — re-autenticar: `doppler secrets set META_ACCESS_TOKEN=seu_token -p lc-keys -c prd`
