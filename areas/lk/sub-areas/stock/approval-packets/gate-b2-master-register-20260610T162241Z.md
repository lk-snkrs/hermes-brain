# Gate B2 — Master register P0+P1+P2 por lane — 20260610T162241Z

## Veredito

Master register consolidado em modo **local/read-only**. Ele une P0, P1 e P2 por `priority + lane + handle`, aponta o packet de decisão e preserva as linhas detalhadas de proposta para consulta operacional.

Este artefato **não** autoriza Tiny/Shopify write, não ativa runtime e não libera promessa de pronta entrega.

## Totais

- Linhas master por handle/lane: `558`
- Linhas detalhadas de proposta: `8333`
- Handles únicos: `558`
- Linhas com estoque interno positivo lido: `349`
- Matches exatos resolvidos com saldo zero: `4123`

## Prioridades

- `P0_saneamento`: 9
- `P1_saneamento`: 141
- `P2_saneamento`: 408

## Lanes

- `LOCAL_RESOLVED_REFERENCE_PACKET`: 9
- `SHOPIFY_DUPLICATE_PACKET`: 225
- `TINY_CODE_INVESTIGATION_PACKET`: 165
- `TINY_DEPOSIT_PACKET`: 105
- `TINY_DUPLICATE_PACKET`: 54

## Mapping status detalhado

- `matched_exact_sku_stock_missing_deposit`: 272
- `matched_exact_sku_stock_resolved`: 4466
- `shopify_duplicate_sku_blocked`: 411
- `shopify_variant_tiny_missing`: 3092
- `tiny_duplicate_exact_code_blocked`: 92

## Como usar

1. Abrir o CSV master e filtrar por `priority` e `lane`.
2. Abrir `packet_md` para decisão humana por handle.
3. Usar o CSV de propostas ou SQLite para ver linha SKU/tamanho/Tiny/Shopify.
4. Se a decisão virar write externo futuro, criar diff/rollback/readback e pedir aprovação escopada antes de executar.

## Guardrails

- Tiny write: `0`
- Shopify write: `0`
- Writes externos: `0`
- Runtime novo: `0`
- Disponibilidade pública/pronta entrega: `0`
- Fonte final para disponibilidade: Tiny/fonte viva consultada no momento.

## Artefatos

- JSON master: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.json`
- CSV master por handle/lane: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/gate-b2-master-register-20260610T162241Z.csv`
- CSV propostas detalhe: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/reports/gate-b2-master-register-proposals-20260610T162241Z.csv`
- SQLite consulta local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/data/gate_b2_master_register_20260610T162241Z.db`
