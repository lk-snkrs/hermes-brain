# Schema Gate B — Base local read-only LK Stock

Status: PRD / preview técnico
Writes externos executados: 0
Fonte final de disponibilidade: Tiny / `LK | CONTROLE ESTOQUE`

## Objetivo

Definir a base local que acelera decisão de estoque sem virar fonte final de disponibilidade.

A base local serve para:

- formar candidatos de ruptura/reposição;
- guardar snapshots e freshness;
- cruzar vendas, demanda e SKU/Tiny;
- recalcular score P0/P1/P2/P3;
- manter ledger auditável de eventos webhook, cron, backfill e falhas.

## Tabelas mínimas

### schema_migrations

- version: string
- applied_at: datetime
- description: string

### products

- product_id: string
- shopify_product_id: string nullable
- handle: string nullable
- title: string
- brand: string nullable
- family: string nullable
- status_comercial: string nullable
- first_seen_at: datetime
- updated_at: datetime

### variants

- variant_id: string
- product_id: string
- shopify_variant_id: string nullable
- sku: string nullable
- size_label: string nullable
- tiny_codigo: string nullable
- tiny_product_id: string nullable
- mapping_confidence: string enum: high / medium / low / blocked
- mapping_reason: string nullable
- updated_at: datetime

### stock_snapshots

- snapshot_id: string
- variant_id: string
- source: string enum: tiny / shopify / manual / other
- location: string nullable
- warehouse: string nullable
- quantity_available: integer nullable
- quantity_reserved: integer nullable
- freshness: string enum: live / cron_diario / stale / fonte_viva_consultada_agora
- source_observed_at: datetime
- ingested_at: datetime
- source_ref: string nullable

### sales_velocity

- velocity_id: string
- variant_id: string
- source: string enum: shopify / manual / other
- window_days: integer enum: 7 / 30 / 90
- net_units_sold: integer
- gross_units_sold: integer nullable
- net_revenue: decimal nullable
- last_order_at: datetime nullable
- computed_at: datetime

### demand_signals

- signal_id: string
- variant_id: string nullable
- product_id: string nullable
- source: string enum: growth / trends / campaign / loja / atendimento / manual
- signal_type: string
- weight: integer
- evidence: text
- valid_from: datetime
- valid_until: datetime nullable
- created_by: string nullable
- created_at: datetime

### scores

- score_id: string
- variant_id: string
- score_total: integer
- priority: string enum: P0 / P1 / P2 / P3 / needs_sku_resolution
- sales_points: integer
- margin_points: integer nullable
- demand_points: integer
- rupture_points: integer
- history_points: integer
- confidence_points: integer
- explanation: text
- computed_at: datetime

### event_ledger

- event_id: string
- provider: string
- event_type: string
- idempotency_key: string unique
- payload_hash: string
- status: string enum: received / processed / ignored / failed / reconciled
- failure_reason: text nullable
- source_observed_at: datetime nullable
- received_at: datetime
- processed_at: datetime nullable
- receipt_path: string nullable

### receipts

- receipt_id: string
- receipt_type: string enum: fila / packet / handoff / approval / error / reconciliation
- title: string
- path: string
- related_variant_id: string nullable
- related_event_id: string nullable
- writes_externos: integer default 0
- created_at: datetime

## Índices obrigatórios

- variants.sku
- variants.tiny_codigo
- variants.mapping_confidence
- stock_snapshots.variant_id + source_observed_at
- sales_velocity.variant_id + window_days + computed_at
- scores.priority + computed_at
- event_ledger.idempotency_key unique
- event_ledger.provider + event_type + received_at

## Regras de freshness

- `live`: evento webhook validado e processado.
- `cron_diario`: reconciliação diária validada.
- `stale`: fonte atrasada, cron falhou, webhook falhou ou freshness vencida.
- `fonte_viva_consultada_agora`: consulta direta feita no momento da resposta.

Nenhuma resposta pode afirmar disponibilidade usando apenas `stale`.

## Fluxos

### Backfill inicial

1. Ler fontes autorizadas em modo read-only.
2. Popular products, variants, sales_velocity e stock_snapshots.
3. Criar evento ledger `backfill_initial`.
4. Marcar freshness conforme fonte.
5. Gerar receipt.

### Webhook live

1. Receber evento pelo ingresso autorizado.
2. Validar assinatura do provedor.
3. Normalizar payload.
4. Calcular idempotency_key.
5. Gravar event_ledger.
6. Atualizar entidades afetadas.
7. Recalcular score afetado.
8. Não enviar Telegram se não houver P0/falha/aprovação.

### Cron diário

1. Rodar em janela aprovada.
2. Reconciliar catálogo/vendas/estoque.
3. Detectar eventos perdidos ou divergências.
4. Recalcular scores.
5. Marcar base `stale` se a reconciliação falhar.
6. Gerar receipt local; Telegram só se houver exceção acionável.

## Guardrails

- Base local não substitui Tiny como fonte final.
- Sem Tiny/fonte viva, não afirmar disponibilidade.
- Sem writes Tiny/Shopify.
- Sem compra, fornecedor, cliente, WhatsApp, campanha ou promessa automática.
- Webhook/cron produtivos exigem aprovação escopada.
- Secrets não entram no Brain; registrar apenas nomes/contratos.
