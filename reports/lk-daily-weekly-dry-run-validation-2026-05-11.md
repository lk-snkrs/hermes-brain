# LK Daily + Weekly Dry-run Validation, 2026-05-11

Generated at: `2026-05-11T22:16:18.914510+00:00`

## Veredito

Daily Sales Brief e Weekly CEO Review passaram no dry-run manual read-only. Eles ficam elegíveis para uma decisão de cadência/destino, mas não foram ativados como cron/n8n e não foram enviados.

## Snapshot

- Automações validadas: 2
- Dry-runs passed: 2
- Review needed: 0
- Crons criados: 0
- n8n flows criados: 0
- Telegram sends: 0
- Envios externos: 0
- Writes produtivos: 0

## Validações

### LK-AUTO-001 · Daily Sales Brief read-only

- Status: `passed`
- Artefato: `reports/lk-os-daily-sales-brief-2026-05-10.json`
- Preview Telegram: `reports/lk-os-daily-sales-brief-telegram-preview-2026-05-10.json`
- Would notify: `True`
- Recomendação: `eligible_for_lucas_cadence_approval_not_active`
- Ações bloqueadas confirmadas: campaign, cron, external_send, production_db_write, shopify_write, supplier_contact, telegram_send, tiny_write
- Snapshot: `{"business_date": "2026-05-10", "shopify_orders": 9, "shopify_revenue": 34809.92, "ga4_sessions": 4301.0, "tiny_risk_counts": {"ruptura": 5, "ok_amostra": 1, "baixo_estoque_vs_venda_do_dia": 3, "unknown": 1}}`

### LK-AUTO-002 · Weekly CEO Review read-only

- Status: `passed`
- Artefato: `reports/lk-os-weekly-ceo-review-2026-05-04_2026-05-10.json`
- Preview Telegram: `reports/lk-os-weekly-ceo-review-telegram-preview-2026-05-04_2026-05-10.json`
- Would notify: `True`
- Recomendação: `eligible_for_lucas_cadence_approval_not_active`
- Ações bloqueadas confirmadas: campaign, cron, external_send, production_db_write, shopify_write, supplier_contact, telegram_send, tiny_write
- Snapshot: `{"start_date": "2026-05-04", "end_date": "2026-05-10", "shopify_orders": 97, "shopify_revenue": 312261.74, "ga4_sessions": 29605.0, "meta_spend": 9374.43, "metricool_google_ads_rows": 21, "tiny_risk_counts": {"ruptura": 3, "baixo_estoque_vs_venda_da_semana": 1, "unknown": 11}}`

## Próximo gate

Lucas can approve cadence/delivery for LK-AUTO-001 and/or LK-AUTO-002 if he wants recurring activation; otherwise keep manual/on-demand.

## Não realizado

- Nenhum cron criado.
- Nenhum n8n flow criado.
- Nenhum Telegram enviado.
- Nenhum e-mail, WhatsApp, Klaviyo ou campanha enviado/agendado.
- Nenhum write Shopify/Tiny/Merchant/GSC/produção.
