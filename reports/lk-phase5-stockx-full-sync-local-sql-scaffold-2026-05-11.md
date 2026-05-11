# LK OS — StockX full sync scaffold no SQL local — 2026-05-11

## Veredito

O SQL local **não estava perfeito** para o PRD LK OS porque ainda não tinha as tabelas de full sync StockX/KicksDev/GOAT/Droper. Corrigi a estrutura local, mas **não executei full sync externo vivo** porque o conector/endpoints oficiais ainda precisam ser validados e scraping direto de StockX/GOAT é bloqueado pelo PRD.

## Banco local

- SQLite: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_phase5.sqlite`
- Permissão: `0o600`
- Sem PII e sem secrets.

## Tabelas adicionadas

- `external_market_sources`: 3
- `market_product_identity`: 87
- `market_full_sync_runs`: 1
- `stockx_product_snapshots`: 0
- `stockx_size_offers`: 0
- `sourcing_price_comparisons`: 0
- `size_conversion_rules`: 2
- `market_sync_gaps`: 4

## Status das credenciais

- Secret names encontrados no Doppler: KICKSDB_API_KEY, KICKS_API_KEY, KICKS_DEV_API_KEY
- Valores não foram impressos nem salvos.

## Lacunas abertas antes do FULL SYNC real

- Validar contrato oficial do endpoint KicksDev/StockX e limites de rate limit.
- Criar matriz explícita US Men / US Women → LK/BR/EU por marca/categoria.
- Popular snapshots por produto/tamanho somente via fonte permitida, sem scraping proibido.
- Comparar Droper, StockX e GOAT com custo final LK antes de qualquer sourcing.

## Guardrails

- Nenhuma compra, contato, campanha, PO, Notion ou WhatsApp executado.
- Nenhum write em Shopify/Tiny/Supabase.
- Nenhum scraping direto de StockX/GOAT.
