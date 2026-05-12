# LK Mission Control Snapshot, 2026-05-12

Generated at: `2026-05-12T00:47:47.142082+00:00`

## Veredito

Status: `mission_control_ready_readonly`

Mission Control v1 consolida crons ativos, relatórios obrigatórios, aprovações abertas, bloqueios de dados, Klaviyo Draft, sourcing readiness e GMC queue. É uma visão executiva read-only; não cria UI, não dispara campanha, não compra, não altera catálogo/feed e não cria n8n.

## Painel curto

- Crons ativos LK: 4
- Reports obrigatórios: 3
- Ledger: 24 registros, 8 executados verificados, 5 aguardando aprovação, 3 bloqueados por dados, 8 futuros
- Klaviyo P1: Draft / sem envio
- Sourcing: 4 famílias prontas só após aprovação manual
- GMC: 963 itens P1/P2, 963 P1
- Writes/envios/contatos/compras/marketplace/n8n: 0/0/0/0/0

## Crons operacionais

- `7c688553e293` — Daily Sales Brief: diário 08:00 BRT, mandatory_report, active
- `953b9055458e` — Weekly CEO Review: segunda 09:00 BRT, mandatory_report, active
- `15777e3416dc` — SEO/CRO Weekly: segunda 10:00 BRT, read_only_preview, active
- `d4c26da4cd48` — GMC Review: quinta 09:00 BRT, mandatory_report, active

## Top decisões / bloqueios

### P1 · approval_needed · Nike Moon Shoe SP Jacquemus
- Dono: Lucas/Júlio
- Próximo passo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado: supplier_contact, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · approval_needed · New Balance 9060
- Dono: Lucas/Júlio
- Próximo passo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado: supplier_contact, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · approval_needed · Nike Mind 002
- Dono: Lucas/Júlio
- Próximo passo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado: supplier_contact, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · approval_needed · Comme des Garçons PLAY Polo
- Dono: Lucas/Júlio
- Próximo passo seguro: prepare_supplier_send_preview_with_named_destination
- Bloqueado: supplier_contact, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · approval_needed · New Balance 530
- Dono: Lucas/Júlio
- Próximo passo seguro: bundle_in_existing_p0_quote_preview_only
- Bloqueado: supplier_contact, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · data_blocker · Onitsuka Tiger Mexico 66
- Dono: Hermes/LK ops data cleanup
- Próximo passo seguro: resolve_data_gap_readonly_before_approval
- Bloqueado: supplier_contact_and_purchase, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · data_blocker · Camiseta Saint Studio Boxy
- Dono: Hermes/LK ops data cleanup
- Próximo passo seguro: resolve_data_gap_readonly_before_approval
- Bloqueado: supplier_contact_and_purchase, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

### P1 · data_blocker · Bearbrick Series 48
- Dono: Hermes/LK ops data cleanup
- Próximo passo seguro: resolve_data_gap_readonly_before_approval
- Bloqueado: supplier_contact_and_purchase, purchase, purchase_order, reservation
- Fonte: `reports/lk-os-approval-decision-log-router-2026-05-04_2026-05-10.json`

## Gates especiais

- CRM/Klaviyo: `ready_for_lucas_review_no_send`, campaign `01KRC1DPTY615GF5FNBPXMPKY6`, próximo seguro: Lucas review by verified list/template/campaign IDs; prepare send packet only if explicitly requested.
- GMC/feed: 963 itens na fila, 963 P1, próximo seguro: review top feed issue groups; prepare Merchant/feed fix preview only after prioritization.

## Próximas ações seguras

- Acompanhar primeira entrega Daily Sales Brief em 2026-05-12 08:00 BRT.
- Manter Klaviyo P1 em Draft; só preparar pacote de envio se Lucas pedir explicitamente.
- Preparar uma fila de decisão curta para sourcing: 4 famílias aprováveis + 3 bloqueios de dados, sem pesquisa externa.
- Transformar GMC P1 em pacotes de correção de feed/PDP, preview-only.

## Checks

- OK: `phase8_guardrails_green` — Fase 8 must be green before Mission Control v1.
- OK: `mandatory_crons_count` — Expected 4 active LK crons and 3 mandatory deliveries after GMC reconciliation.
- OK: `ledger_has_open_decisions` — Mission Control must expose 5 approvals and 3 data blockers.
- OK: `no_writes_or_external_actions` — Mission Control snapshot must remain read-only/no-external-action.
- OK: `klaviyo_draft_safe` — Klaviyo must remain Draft/no-send.
- OK: `sourcing_safe` — Sourcing must remain decision-only/no marketplace calls.
- OK: `merchant_safe` — GMC must be read-only with product statuses available.

## Não executado

- shopify_write
- tiny_write
- klaviyo_send_or_schedule
- merchant_feed_write
- gsc_admin_or_indexing_submit
- supplier_contact
- marketplace_lookup
- purchase_order
- customer_contact
- n8n_flow_creation
