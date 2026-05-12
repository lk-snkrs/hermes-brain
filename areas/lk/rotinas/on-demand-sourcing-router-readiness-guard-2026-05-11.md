# LK On-demand Sourcing Router Readiness Guard, 2026-05-11

Generated at: `2026-05-12T00:14:49.618296+00:00`

## Veredito

Status: `ready_for_per_item_lucas_julio_decision_no_external_action`

LK-AUTO-006 avançou para guard manual/read-only por item. Ele valida que a fila de sourcing está pronta para decisão Lucas/Júlio, mas não consulta marketplaces, não fala com fornecedor, não compra e não escreve em Shopify/Tiny.

## Snapshot

- Checks: 15
- Fails: 0
- Warnings: 0
- Router rows: 8
- Ready only after manual approval: 4
- Optional bundle: 1
- Blocked needs data: 3
- Fila A rows considered: 40
- Quote preview records: 15
- Quote qty total, not purchase qty: 39
- External marketplace calls: 0
- Supplier contacts: 0
- Purchases/POs: 0/0
- Shopify/Tiny writes: 0/0

## Famílias prontas apenas após aprovação manual

### LK-SOURCING-20260504-20260510-01 | Nike Moon Shoe SP Jacquemus
- Gate: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras se aprovado: GOAT, Droper, StockX, KicksDev
- Sinal receita Shopify: R$ 48.999,92

### LK-SOURCING-20260504-20260510-02 | New Balance 9060
- Gate: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras se aprovado: GOAT, Droper, StockX, KicksDev
- Sinal receita Shopify: R$ 18.799,93

### LK-SOURCING-20260504-20260510-03 | Nike Mind 002
- Gate: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras se aprovado: GOAT, Droper, StockX, KicksDev
- Sinal receita Shopify: R$ 6.399,98

### LK-SOURCING-20260504-20260510-04 | Comme des Garçons PLAY Polo
- Gate: Lucas/Júlio approval required before external lookup/contact
- Fontes futuras se aprovado: GOAT, Droper, StockX, KicksDev
- Sinal receita Shopify: R$ 3.599,98

## Top quote preview, não compra

- #1 Tênis Nike Moon Shoe SP Jacquemus Medium Brown | SKU `HV8547-200-38` | variação `38` | P0 — ruptura com venda repetida | quote qty `3` | receita R$ 26.999,95
- #2 Tênis Nike Air Jordan 4 Retro Metallic Gold Branco | SKU `AQ9129-170-7` | variação `40` | P0 — ruptura com venda repetida | quote qty `3` | receita R$ 13.399,96
- #3 Tênis Onitsuka Tiger Mexico 66 White Black Branco | SKU `1183A201-126-3` | variação `36` | P0 — ruptura com venda repetida | quote qty `3` | receita R$ 7.199,97
- #4 Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto | SKU `HV8547-001-8` | variação `41` | P0 — ruptura com venda repetida | quote qty `2` | receita R$ 11.999,98
- #5 Tênis Nike Moon Shoe SP Jacquemus Off White | SKU `HV8547-002-39` | variação `39` | P0 — ruptura com venda repetida | quote qty `2` | receita R$ 9.999,98

## Checks

- OK: `router_read_only_flag` — Router payload must be explicitly read-only.
- OK: `router_rows_present` — Router must contain decision-scoped rows.
- OK: `external_sources_on_demand_only` — External sources must be defined only as on-demand tools.
- OK: `no_rows_eligible_for_external_lookup_now` — No row may authorize immediate external marketplace lookup.
- OK: `all_rows_block_forbidden_actions` — Every row must explicitly block contact/purchase/write/full-sync actions.
- OK: `source_labels_include_truth_sources` — Rows must label Shopify/Tiny source boundaries.
- OK: `size_normalization_required_for_external` — Rows with StockX/GOAT future sources must require US Men vs US Women size normalization.
- OK: `decision_scoped_no_full_sync` — External price results, if approved later, must persist only decision-scoped summaries, not full-sync tables.
- OK: `fila_a_pending_excluded` — Fila A should explicitly exclude stand-by residuals from sourcing.
- OK: `quote_preview_has_records` — Quote preview records must match summary top_items_validated.
- OK: `quote_qty_not_purchase_qty` — Quote records must not imply purchase approval; optional rows may say cotar/monitorar only.
- OK: `supplier_fields_required_not_filled_as_truth` — Supplier data must remain required/pending rather than invented.
- OK: `lead_time_gate_present` — Each quote preview record must carry a lead-time or pronta-entrega/remessa gate.
- OK: `cost_caps_not_real_margin` — Margins must be represented as cost ceilings, not actual margin claims.
- OK: `quote_guardrails_no_external_actions` — Source guardrails must explicitly prohibit supplier contact, purchases, and Shopify/Tiny writes.

## Guardrails

- No Droper/StockX/GOAT/KicksDev call executed by this guard.
- No supplier contact executed.
- No purchase, PO, reservation, or payment executed.
- No Shopify/Tiny write executed.
- No price, stock, product, campaign, or customer change executed.
- No full-sync external price table created.
- Quote quantity remains reference quantity, not purchase quantity.
- Actual per-item external search requires explicit Lucas/Júlio approval naming the family/SKU/scope.

## Próximo gate

Choose one family/SKU for a separate on-demand external price search, or keep as internal decision queue. Any supplier contact/purchase remains separate approval.
