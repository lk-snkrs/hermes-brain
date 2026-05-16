# LK GMC — Approval packets A/B preview

Gerado em: `2026-05-15T20:36:04.224372+00:00`
Status: `preview_only_needs_explicit_approval`

## Resultado

- Pacote A price-only: `42` IDs exatos.
- Pacote B DRAFT/404: `20` IDs exatos.
- Writes executados: `0`.
- Shopify/Merchant/feed/campanha/envio externo: `0`.

## Pacote A — price-only micro-pilot

- Escopo: `productAttributes.price` somente via Merchant API ProductInputs v1.
- Exclui salePrice, strikethrough e qualquer item com `compare_at_price`.
- Fonte alvo: preço atual Shopify no snapshot local/variant ID exato.
- Rollback: patch de volta para preço Merchant capturado antes do write.
- Pós-check exigido: Product API/statuses após delay; se não convergir, parar.

### Amostra A
- `online:pt:BR:01424-002-2` — R$ 5999.90 → R$ 8999.99 — Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul
- `online:pt:BR:CU3244100-41` — R$ 14999.99 → R$ 22999.99 — Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido
- `online:pt:BR:CZ2239600-3` — R$ 4699.99 → R$ 6999.90 — Tênis Nike SB Dunk Low What The P-Rod Colorido
- `online:pt:BR:DQ4040400-39` — R$ 2999.90 → R$ 2999.99 — Tênis Nike SB Dunk Low PRM Phillies Azul
- `online:pt:BR:HQ6998-211` — R$ 2499.99 → R$ 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-212` — R$ 2499.99 → R$ 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-213` — R$ 2499.99 → R$ 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HV0823-119` — R$ 3499.99 → R$ 4499.99 — Tênis Nike Air Jordan 4 Retro Valentine's Day Sierra Red Vermelho
- `online:pt:BR:ID0440-1` — R$ 1449.90 → R$ 1749.99 — Tênis adidas Sambae Cloud White Collegiate Green Branco
- `online:pt:BR:ID0440-3` — R$ 1449.90 → R$ 1749.99 — Tênis adidas Sambae Cloud White Collegiate Green Branco

## Pacote B — DRAFT/404 suppress/delete

- Escopo: produtos `source=crawl`/Merchant com Shopify `DRAFT/ARCHIVED` e URL pública 404 + `.js` 404.
- Exclui os 2 casos public 200/monitor.
- Não publica Shopify automaticamente.
- Rollback: snapshot do Merchant product + Shopify admin para recriar/reprocessar se necessário.

### Amostra B
- `online:pt:BR:11810372920072143991` — Shopify DRAFT / public 404 / js 404 — 40
- `online:pt:BR:3876299146406606317` — Shopify DRAFT / public 404 / js 404 — Calça Saint Studio Jeans Baggy Preta
- `online:pt:BR:6562590402534581177` — Shopify DRAFT / public 404 / js 404 — Calça Nude Project Illegal Jeans Ash Cinza - LK
- `online:pt:BR:2258634078163248862` — Shopify DRAFT / public 404 / js 404 — Calça Chino Saint Studio Supima Preto
- `online:pt:BR:15334125053592144145` — Shopify DRAFT / public 404 / js 404 — Camiseta Oversized Fear of God Essentials Heavy Healther Wood Marrom
- `online:pt:BR:13498809788548851139` — Shopify DRAFT / public 404 / js 404 — Moletom Essentials Fear of God Jet black SS24 Preto | LK Sneakers
- `online:pt:BR:10002025469927148791` — Shopify DRAFT / public 404 / js 404 — Calça Nude Project Jeans Soft Velvet Azul Marinho
- `online:pt:BR:14252480804615463970` — Shopify DRAFT / public 404 / js 404 — 41
- `online:pt:BR:4041641007094962608` — Shopify DRAFT / public 404 / js 404 — Camisa Saint Studio Trico Palha | LK Sneakers
- `online:pt:BR:10591784840915585992` — Shopify DRAFT / public 404 / js 404 — Boné Saint Studio Art Department Azul - LK

## Aprovação necessária para executar

Escolher explicitamente uma destas opções:

1. `aprovo GMC A 10 IDs price-only` — mais conservador.
2. `aprovo GMC A 42 IDs price-only` — aplica todos os candidatos price-only.
3. `aprovo GMC B 20 DRAFT/404 suppress/delete` — limpa landing errors DRAFT/404.

Sem uma dessas frases, continuar só em preview/read-only.

## Artefatos
- packet_a_json: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_a_price_only_42_preview.json`
- packet_a_csv: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_a_price_only_42_preview.csv`
- packet_a_rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_a_price_only_42_rollback_snapshot.json`
- packet_b_json: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_b_draft404_20_preview.json`
- packet_b_csv: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_b_draft404_20_preview.csv`
- packet_b_rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/gmc_approval_packets_20260515/packet_b_draft404_20_rollback_snapshot.json`
- briefing_md: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/rotinas/gmc-approval-packets-ab-preview-2026-05-15.md`

## Não executado

- Merchant write
- ProductInputs PATCH
- Content API delete/upsert
- Shopify write
- feed fetch/upload
- campanha/envio/contato externo
