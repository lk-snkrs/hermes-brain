# LK OS — SQL local operational spine — 2026-05-11

## Veredito

O SQL local agora foi ampliado para o coração operacional correto: pessoas/clientes + pedidos + itens + produtos + variantes + RFM. GOAT/Droper/StockX continuam como consulta on-demand, não como full sync permanente de preço externo.

## Banco

- SQLite: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite`
- Permissão: `0o600`
- Fonte: Supabase LK REST em modo read-only.

## Contagens materializadas

- `lk_customers`: 26413
- `lk_orders`: 6059
- `lk_order_items`: 8166
- `lk_products`: 2241
- `lk_product_variants`: 14466
- `lk_customer_rfm`: 3679
- `lk_os_entity_dictionary`: 8

## QA sem PII

- `customers_with_email`: 25801
- `customers_with_phone`: 3759
- `variants_with_sku`: 13078
- `orders_paid_like`: 4644

## Guardrails

- Nenhum write externo.
- Nenhum envio/campanha.
- Nenhum segredo impresso.
- PII fica apenas no SQLite privado chmod 600; relatórios do Brain usam contagens/agregados.
