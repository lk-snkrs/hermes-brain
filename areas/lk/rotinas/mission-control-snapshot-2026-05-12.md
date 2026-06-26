# LK Mission Control Snapshot, 2026-05-12

Generated at: `2026-05-12T10:53:23.304202+00:00`

## Veredito

Status: `mission_control_active_approved_gmc_write`

Mission Control v1 consolida crons ativos, relatórios obrigatórios, aprovações abertas, bloqueios de dados, Klaviyo Draft, sourcing readiness e GMC queue. É uma visão executiva read-only; não cria UI, não dispara campanha, não compra, não altera catálogo/feed e não cria n8n.

## Painel curto

- Crons ativos LK: 4
- Reports obrigatórios: 3
- Ledger: 24 registros, 8 executados verificados, 5 aguardando aprovação, 0 bloqueados por dados após autofix, 8 futuros
- Needs_data resolvidos: 2 para monitor/estoque OK, 1 para higiene interna de código
- Klaviyo P1: Draft / sem envio
- Sourcing: 4 famílias prontas só após aprovação manual
- GMC: 972 itens P1/P2, 972 P1, 6 pacotes preview-only; P0: 32 linhas / 32 PDPs HTTP 200; atributos: 80 revisados / 80 aplicados / 80 verificados
- Writes/envios/contatos/compras/marketplace/n8n: 2/0/0/0/0

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

### P1 · internal_code_hygiene · Bearbrick Series 48
- Dono: Hermes/LK data spine
- Próximo passo seguro: Exact product was found with zero stock but Tiny codigo is blank; prepare internal code hygiene before external sourcing.
- Bloqueado: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Fonte: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

### P1 · data_resolved_monitor · Onitsuka Tiger Mexico 66
- Dono: Hermes/LK data spine
- Próximo passo seguro: Shopify/Tiny SKU mapping is resolved and stock exists; no quote/sourcing needed now.
- Bloqueado: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Fonte: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

### P1 · data_resolved_monitor · Camiseta Saint Studio Boxy
- Dono: Hermes/LK data spine
- Próximo passo seguro: Exact product/size was found in Tiny and stock exists; Tiny codigo remains a hygiene issue but not a sourcing blocker.
- Bloqueado: external sourcing/contact/purchase still blocked; local/read-only hygiene allowed
- Fonte: `reports/lk-needs-data-autofix-readonly-2026-05-12.json`

## Gates especiais

- CRM/Klaviyo: `ready_for_lucas_review_no_send`, campaign `01KRC1DPTY615GF5FNBPXMPKY6`, próximo seguro: Lucas review by verified list/template/campaign IDs; prepare send packet only if explicitly requested.
- GMC/feed: 972 itens na fila, 972 P1, 6 pacotes preview-only, P0 aberto 32 linhas / 32 PDPs HTTP 200, atributos 80 revisados / 80 aplicados / 80 verificados, próximo seguro: 80 required-attribute rows applied and verified in Content API product resources; monitor Merchant item diagnostics until status issues clear after reprocessing.

## Próximas ações seguras

- Acompanhar primeira entrega Daily Sales Brief em 2026-05-12 08:00 BRT.
- Manter Klaviyo P1 em Draft; só preparar pacote de envio se Lucas pedir explicitamente.
- Preparar uma fila de decisão curta para sourcing: 4 famílias aprováveis; os 3 antigos needs_data foram reconciliados em modo read-only/local.
- GMC required attributes: 80 offer_ids aplicados no supplemental feed e verificados no Content API; monitorar reprocessamento de diagnostics do Merchant até limpar item issues.

## Checks

- OK: `phase8_guardrails_green` — Fase 8 must be green before Mission Control v1.
- OK: `mandatory_crons_count` — Expected 4 active LK crons and 3 mandatory deliveries after GMC reconciliation.
- OK: `ledger_has_open_decisions` — Mission Control must expose 5 approvals and zero remaining data blockers after autonomous needs_data autofix.
- OK: `no_unapproved_external_actions` — Mission Control may include the explicitly approved GMC supplemental feed write, but no unapproved sends/contacts/purchases/marketplace/n8n.
- OK: `klaviyo_draft_safe` — Klaviyo must remain Draft/no-send.
- OK: `sourcing_safe` — Sourcing must remain decision-only/no marketplace calls.
- OK: `merchant_safe` — GMC must be read-only with product statuses available.
- OK: `gmc_correction_preview_safe` — GMC correction preview must package issues without permitting writes.
- OK: `gmc_p0_url_review_safe` — GMC P0 URL/checkout review must provide SKU/URL evidence without writes.
- OK: `gmc_required_attrs_preview_safe` — GMC required-attributes preview must propose local corrections without writes.
- OK: `gmc_required_attrs_applied` — Approved required-attributes correction must be applied through supplemental feed, not Shopify mutation.
- OK: `gmc_required_attrs_verified` — Content API products must show the 80 applied ageGroup/gender/size attributes.

## Não executado

- shopify_write
- tiny_write
- klaviyo_send_or_schedule
- additional_merchant_feed_write_without_new_preview
- gsc_admin_or_indexing_submit
- supplier_contact
- marketplace_lookup
- purchase_order
- customer_contact
- n8n_flow_creation
