# Nike Mind — GTIN discovery via KicksDev

Data: 2026-06-07T20:55:21.649575+00:00
Escopo: descoberta read-only de GTIN/EAN/UPC para produtos Nike Mind com barcode ausente no Shopify/GMC.

## Status executivo

- Shopify auditado em read-only.
- KicksDev consultado em read-only usando endpoint StockX/GOAT já validado no playbook LK.
- Nenhum write em Shopify.
- Nenhum write em GMC.
- Resultado: **KicksDev ajudou no match de produto, mas não retornou GTIN/EAN/UPC/barcode nos campos disponíveis desses endpoints.**

## Shopify audit

- Collection handle: `nike-mind-001`
- Total de variantes auditadas: `201`
- Variantes sem barcode/GTIN: `123`
- Style SKUs sem barcode: `19` + casos com SKU vazio

## KicksDev

Endpoints consultados:

- `GET /v3/stockx/products?query=<style_sku>&limit=5&display[variants]=true&display[prices]=true&display[traits]=true&display[statistics]=true`
- `GET /v3/goat/products?query=<style_sku>&limit=5&display[variants]=true&display[prices]=true&display[traits]=true&display[statistics]=true`

Autorização operacional permanente registrada por Lucas:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/rules/REGRA-KICKSDEV-READONLY-PREAUTORIZADO.md`

## Resultado GTIN

- Campos exatos procurados: `gtin`, `upc`, `ean`, `barcode`, `bar_code`, `universal_product_code`, plurais equivalentes.
- Resultado: `0` campos GTIN/EAN/UPC/barcode encontrados.
- Observação: o parser inicial detectava falso positivo em `upcoming`; isso foi corrigido. `upcoming` não é UPC.

## Match de produto

- Styles com pelo menos um match direto de SKU em KicksDev: `10`
- Styles sem match direto claro ou com resultados aproximados: `9`

### Exemplos de match direto

- `HQ4307-100`
  - stockx: `HQ4307-100` — Nike Mind 001 Slide Sail
  - goat: `HQ4307 100` — Nike Mind 001 'Sail'
- `HQ4307-101`
  - stockx: `HQ4307-101` — Nike Mind 001 Slide White Speed Red
  - goat: `HQ4307 101` — Nike Mind 001 'White Speed Red'
- `HQ4307-300`
  - stockx: `HQ4307-300` — Nike Mind 001 Mineral Slate Light Pumice Hyper Crimson Metallic Platinum
  - goat: `HQ4307 300` — Nike Mind 001 'Mineral Slate'
- `HQ4307-400`
  - stockx: `HQ4307-400` — Nike Mind 001 Slide Blackened Blue Game Royal
  - goat: `HQ4307 400` — Nike Mind 001 'Blackened Blue'
- `HQ4307-601`
  - stockx: `HQ4307-601` — Nike Mind 001 Slide Team Red University Red
  - goat: `HQ4307 601` — Nike Mind 001 'Team Red'
- `HQ4308-001`
  - stockx: `HQ4308-001` — Nike Mind 002 Black Hyper Crimson
  - goat: `HQ4308 001` — Nike Mind 002 'Black Hyper Crimson'
- `HQ4308-003`
  - stockx: `HQ4308-003` — Nike Mind 002 Light Smoke Grey
  - goat: `HQ4308 003` — Nike Mind 002 'Light Smoke Grey'
- `HQ4309-610`
  - stockx: `HQ4309-610` — Nike Mind 001 Slide Pearl Pink (Women's)
  - goat: `HQ4309 610` — Wmns Nike Mind 001 'Pearl Pink'

## Recomendação

Não aplicar GTIN agora.

Motivo: KicksDev confirmou produtos/market signal, mas não forneceu GTIN/EAN/UPC nos endpoints StockX/GOAT disponíveis. Aplicar GTIN sem código real violaria o guardrail LK e pode piorar qualidade do Merchant.

## Próximas opções seguras

1. Buscar GTIN em fonte primária/verificável:
   - embalagem/etiqueta;
   - invoice/fornecedor;
   - base Nike/GS1 quando disponível;
   - Tiny/ERP se existir barcode confiável.

2. Se o problema no GMC for `missing GTIN` para produtos sem identificador verificável, avaliar política de feed:
   - `brand=Nike`;
   - `mpn=style_sku` quando aplicável;
   - `identifier_exists` apenas conforme política Google e tipo real do item.

3. Corrigir SKUs vazios no Shopify antes de qualquer feed enrichment.

## Arquivos

- Shopify audit: `shopify_nike_mind_variants_barcode_audit.json`
- KicksDev raw: `kicksdev_query_raw.json`
- KicksDev summary: `kicksdev_query_results.json`
- Exact GTIN analysis: `kicksdev_gtin_exact_field_analysis.json`

## Approval necessário para writes futuros

- Atualizar barcode/GTIN em Shopify: exige aprovação explícita atual e lista SKU→GTIN verificável.
- Alterar GMC/feed: exige aprovação explícita atual com rollback/receipt.
