# Receipt — Pace Regra B repair

Data: 2026-05-28T20:27:08.046718+00:00

## Regra aplicada
- Top 4: últimos 4 produtos criados, ativos e publicados na Online Store.
- Corpo: score = 70% venda líquida/capturada Shopify + 30% visitas GA4 em página de produto.
- Expurgo: cancelado/refunded/void/pending/authorized/fraude.
- OOS/não vendável depois do corpo vendável.

## Verificação
- Admin full ok: True
- Admin top12 ok: True
- Público top12 ok: True
- Moves: 1

## Top 12 final público
1. Camiseta Pace Óxido Cotton Code Grey Cinza — top4_recent_active_published — score `0.000697` — vendas `0` un / R$ `0.0` — visitas `3`
2. Camiseta Pace Tsuho Regular Stone Washed Black Preto — top4_recent_active_published — score `0.00209` — vendas `0` un / R$ `0.0` — visitas `9`
3. Suéter Pace Overlock Black Vintage Preto — top4_recent_active_published — score `0.001625` — vendas `0` un / R$ `0.0` — visitas `7`
4. Calça Pace Nomo Tailoring Trousers Preto — top4_recent_active_published — score `0.334437` — vendas `2` un / R$ `2199.98` — visitas `279`
5. Regata Pace Waffle Knit Off White — body_sellable_score_70_sales_30_visits — score `0.622579` — vendas `6` un / R$ `1068.33` — visitas `493`
6. Camisa Pace EOT Cuban Collar Off White — body_sellable_score_70_sales_30_visits — score `0.462634` — vendas `3` un / R$ `1107.49` — visitas `764`
7. Regata Pace Pattent Dark Grey Cinza — body_sellable_score_70_sales_30_visits — score `0.460367` — vendas `5` un / R$ `822.46` — visitas `175`
8. Regata Pace Waffle Knit Preto — body_sellable_score_70_sales_30_visits — score `0.44354` — vendas `4` un / R$ `619.81` — visitas `473`
9. Calça Pace Milli Cargo Azul Marinho — body_sellable_score_70_sales_30_visits — score `0.432427` — vendas `3` un / R$ `1858.47` — visitas `458`
10. Camiseta Pace Patavision Off White — body_sellable_score_70_sales_30_visits — score `0.39419` — vendas `3` un / R$ `608.98` — visitas `586`
11. Camiseta Pace PRB Off White — body_sellable_score_70_sales_30_visits — score `0.387413` — vendas `4` un / R$ `787.49` — visitas `192`
12. Shorts Pace Midmasa Tailored Charcoal — body_sellable_score_70_sales_30_visits — score `0.331372` — vendas `2` un / R$ `1008.0` — visitas `545`

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/pace-ruleB-repair-20260528T202645Z/rollback-snapshot-pre-write.json`
- Receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/pace-ruleB-repair-20260528T202645Z/receipt-final.json`

## Não ações
- Nenhum cron ativado.
- Nenhum produto/preço/estoque/tema/tag/SEO/GMC/campanha/checkout/cliente alterado.
