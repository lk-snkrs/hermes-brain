# LK OS — Data Quality Layer / Modelo operacional por variante

Status: `data_quality_layer_audit_ready`
Data: 2026-05-15
Modo: read-only/local SQL. Nenhuma API externa, write produtivo, cron, UI, worker, compra, contato ou envio executado.

## Veredito

A base local já cobre o esqueleto operacional Shopify/Supabase — clientes, pedidos, itens, produtos, variantes e RFM — mas ainda não atende completamente o PRD inicial porque falta transformar os dados em uma camada canônica por variante/tamanho com qualidade, estado comercial, estoque Tiny completo, histórico de preço e ledger único de ações/aprendizado.

## Evidência atual sem PII

- SQLite privado auditado: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite` (`0o600`).
- `lk_products`: 2241 linhas.
- `lk_product_variants`: 14466 linhas.
- `lk_orders`: 6059 linhas.
- `lk_order_items`: 8166 linhas.
- `lk_customers`: 26413 linhas.
- `lk_customer_rfm`: 3679 linhas.
- `tiny_anchor_stock`: 49 linhas.
- Variantes com SKU: 13078/14466 (90.41%).
- Variantes com preço Shopify atual: 14458/14466 (99.94%).
- Variantes sem join de produto: 0.
- Grupos de SKU duplicado: 239.
- Itens de pedido com SKU: 7054/8166 (86.38%).
- Itens de pedido com variant id/source_variant_id: 8045/8166 (98.52%).
- Tiny anchor stock parcial: 49 linhas; ainda não é snapshot completo por variante/tamanho/deposito.

## Gap contra PRD inicial

### canonical_product

- Status: `partial`
- Tabelas atuais: `lk_products`, `lk_product_variants`.
- Falta:
  - canonical style/model id.
  - normalized brand/model/colorway.
  - curation status.

### variant_size

- Status: `partial`
- Tabelas atuais: `lk_product_variants`.
- Falta:
  - normalized BR size.
  - US M/W/EU conversion fields.
  - size confidence.
  - variant commercial state.

### shopify_tiny_sku_map

- Status: `partial`
- Tabelas atuais: `lk_product_variants`, `tiny_anchor_stock`.
- Falta:
  - dedicated alias table.
  - Tiny product id/variation id confidence.
  - manual review state.

### tiny_stock_truth

- Status: `partial`
- Tabelas atuais: `tiny_anchor_stock`.
- Falta:
  - full variant-level Tiny snapshot.
  - free vs reserved stock.
  - deposit id/name.
  - snapshot history.

### commercial_state

- Status: `missing`
- Tabelas atuais: nenhuma tabela canônica dedicada.
- Falta:
  - disponivel.
  - reservado.
  - sob_encomenda_br.
  - sob_encomenda_us.
  - em_transito.
  - recebido_ja_vendido.
  - recebido_livre.
  - divergente.

### price_current_and_history

- Status: `partial`
- Tabelas atuais: `lk_product_variants`, `lk_order_items`, `sourcing_price_comparisons`.
- Falta:
  - price snapshot table.
  - compare_at snapshot.
  - approved price decision ledger.
  - external price evidence TTL.

### sales_history

- Status: `partial`
- Tabelas atuais: `lk_orders`, `lk_order_items`.
- Falta:
  - variant/model/day rollup table.
  - 120d demand materialization.
  - channel/source reconciliation confidence.

### approvals_events

- Status: `partial`
- Tabelas atuais: `final_approval_groups`, `lk_os_entity_dictionary`.
- Falta:
  - canonical approval/event ledger table.
  - superseded/no-op states.
  - result/learning links.

### data_quality_flags

- Status: `missing`
- Tabelas atuais: nenhuma tabela canônica dedicada.
- Falta:
  - per-variant dq status.
  - blocking reason.
  - source freshness.
  - last verified at.

## Modelo canônico recomendado

### `lk_variant_quality_status`

- Função: One row per Shopify variant/SKU/size with source-labeled readiness and blocking reasons.
- Campos-chave: `variant_id`, `source_variant_id`, `sku`, `normalized_size`, `dq_status`, `blocking_reason`, `last_verified_at`.
- Modo: local/materialized from read-only sources.

### `lk_sku_alias_map`

- Função: Canonical Shopify SKU to Tiny code/product/variation aliases with confidence and manual-review state.
- Campos-chave: `shopify_variant_id`, `shopify_sku`, `tiny_product_id`, `tiny_codigo`, `match_confidence`, `review_status`.
- Modo: local/materialized + approval-gated correction queue.

### `lk_tiny_stock_snapshots`

- Função: Full Tiny stock truth by SKU/size/deposit, preserving free/reserved/physical counts over time.
- Campos-chave: `snapshot_at`, `deposit_name`, `tiny_codigo`, `sku`, `size`, `stock_free`, `stock_reserved`, `stock_physical`.
- Modo: read-only sync; no Tiny writes.

### `lk_variant_commercial_state`

- Função: Business state per variant: available/reserved/encomenda/transit/sold/divergent with evidence.
- Campos-chave: `variant_id`, `sku`, `commercial_state`, `state_source`, `confidence`, `evidence_ref`, `updated_at`.
- Modo: derived preview first; human approval for uncertain states.

### `lk_price_snapshots`

- Função: Current and historical price/compare-at/cost/landed-price evidence separated by source.
- Campos-chave: `captured_at`, `variant_id`, `sku`, `source_label`, `price_brl`, `compare_at_brl`, `cost_brl`, `evidence_ref`.
- Modo: read-only capture; price writes remain approval-gated.

### `lk_variant_sales_rollups`

- Função: Daily/weekly/120d demand by variant/model/size to feed Stock, CRO, Brand Mix and sourcing.
- Campos-chave: `window`, `variant_id`, `sku`, `units`, `revenue`, `orders`, `last_sale_at`, `source_label`.
- Modo: derived from Shopify/Supabase order_items.

### `lk_action_event_ledger`

- Função: Unified Approval Manager / Learning Loop event table for recommendations, approvals, executions and lessons.
- Campos-chave: `event_id`, `area`, `artifact`, `status`, `approval_text`, `executed_at`, `result`, `learning_ref`.
- Modo: local ledger; external writes need approval.

## Sequência segura de implementação

1. Criar somente tabelas/views locais derivadas em SQLite, sem tocar Shopify/Tiny/Notion/Merchant.
2. Materializar `lk_variant_quality_status` a partir das tabelas existentes.
3. Criar `lk_sku_alias_map` e marcar ambiguidades, sem corrigir SKUs automaticamente.
4. Planejar sync read-only completo Tiny para `lk_tiny_stock_snapshots` antes de qualquer decisão de estoque livre/reservado.
5. Só depois alimentar Pulso Comercial, CRO, Brand Mix, Content Engine e Pricing com essa camada.

## Não executado

- No external API call.
- No Shopify/Tiny/Merchant/Klaviyo/Notion/WhatsApp write.
- No cron/UI/worker created.
- No PII exported in reports.

## Próximo bloco recomendado

Implementar a primeira materialização local: `lk_variant_quality_status` + `lk_sku_alias_map` em modo SQLite/local, usando apenas dados já existentes, e gerar um relatório de quantos variants ficam `ready`, `needs_tiny_stock`, `needs_sku_alias`, `needs_price_history` ou `blocked_ambiguous`. Isso não autoriza writes externos.
