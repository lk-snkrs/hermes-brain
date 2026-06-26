# LK GMC — A42 post-fallback read-only recheck

Gerado em: `2026-05-15T22:21:20.650713+00:00`
Status: `readonly_post_fallback_recheck_complete`

## Resumo
- A42 total: `42`
- (a) Merchant/Content agora igual ao público e ao target original: `1`
- (b) Merchant/Content igual ao público, mas diferente do target original: `24`
- (c) Merchant/Content diferente do público: `17`
- Content API product price == público: `25/42`
- Merchant API v1 product price == público: `25/42`
- Público == target original snapshot: `18/42`
- Linhas com issues de preço em productstatuses: `41`; códigos: `{'price_updated': 123}`
- B20 DRAFT/404 ausentes products.list: `20/20`; productstatuses.list: `20/20`; public .js 404: `20/20`

## Recomendação
- Não fazer rollback em lote. Tratar somente as linhas (c): ainda há divergência entre Merchant/Content e vitrine pública live.

## Classificação A42
- (c) `online:pt:BR:01424-002-2` — Content `5999.90` / Merchant v1 `5999.90` / Público `8999.99` / Target orig `8999.99` issues=3 — Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul
- (c) `online:pt:BR:CU3244100-41` — Content `14999.99` / Merchant v1 `14999.99` / Público `22999.99` / Target orig `22999.99` issues=3 — Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido
- (c) `online:pt:BR:CZ2239600-3` — Content `4699.99` / Merchant v1 `4699.99` / Público `6999.90` / Target orig `6999.90` issues=3 — Tênis Nike SB Dunk Low What The P-Rod Colorido
- (c) `online:pt:BR:DQ4040400-39` — Content `2999.90` / Merchant v1 `2999.90` / Público `2999.99` / Target orig `2999.99` issues=3 — Tênis Nike SB Dunk Low PRM Phillies Azul
- (c) `online:pt:BR:HQ6998-211` — Content `2499.99` / Merchant v1 `2499.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- (c) `online:pt:BR:HQ6998-212` — Content `2499.99` / Merchant v1 `2499.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- (c) `online:pt:BR:HQ6998-213` — Content `2499.99` / Merchant v1 `2499.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- (c) `online:pt:BR:HV0823-119` — Content `3499.99` / Merchant v1 `3499.99` / Público `4499.99` / Target orig `4499.99` issues=3 — Tênis Nike Air Jordan 4 Retro Valentine's Day Sierra Red Vermelho
- (c) `online:pt:BR:ID0440-1` — Content `1449.90` / Merchant v1 `1449.90` / Público `1749.99` / Target orig `1749.99` issues=3 — Tênis adidas Sambae Cloud White Collegiate Green Branco
- (c) `online:pt:BR:ID0440-3` — Content `1449.90` / Merchant v1 `1449.90` / Público `1749.99` / Target orig `1749.99` issues=3 — Tênis adidas Sambae Cloud White Collegiate Green Branco
- (c) `online:pt:BR:IG5932` — Content `1599.99` / Merchant v1 `1599.99` / Público `1799.99` / Target orig `1799.99` issues=3 — Tênis Adidas Samba Wonder Clay Branco
- (a) `online:pt:BR:IG5932-4` — Content `1799.99` / Merchant v1 `1799.99` / Público `1799.99` / Target orig `1799.99` — Tênis Adidas Samba Wonder Clay Branco
- (c) `online:pt:BR:IG5932-5` — Content `1599.99` / Merchant v1 `1599.99` / Público `1799.99` / Target orig `1799.99` issues=3 — Tênis Adidas Samba Wonder Clay Branco
- (c) `online:pt:BR:IG5932-6` — Content `1599.99` / Merchant v1 `1599.99` / Público `1799.99` / Target orig `1799.99` issues=3 — Tênis Adidas Samba Wonder Clay Branco
- (b) `online:pt:BR:IQ0028-200` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-201` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-202` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-203` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-204` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-205` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-206` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-207` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-208` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-209` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-210` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `3999.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-211` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `4499.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (b) `online:pt:BR:IQ0028-212` — Content `5999.99` / Merchant v1 `5999.99` / Público `5999.99` / Target orig `4499.99` issues=3 — Tênis Nike Vomero Premium Flat Stout Marrom
- (c) `online:pt:BR:U9060504` — Content `2399.99` / Merchant v1 `2399.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis New Balance 9060 Cortado Marrom
- (c) `online:pt:BR:U9060505` — Content `2399.99` / Merchant v1 `2399.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis New Balance 9060 Cortado Marrom
- (c) `online:pt:BR:U9060506` — Content `2399.99` / Merchant v1 `2399.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis New Balance 9060 Cortado Marrom
- (c) `online:pt:BR:U9060507` — Content `2399.99` / Merchant v1 `2399.99` / Público `3499.99` / Target orig `3499.99` issues=3 — Tênis New Balance 9060 Cortado Marrom
- (b) `online:pt:BR:U9060CCC-1` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-10` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-11` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-2` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-3` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-4` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-5` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-6` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-7` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-8` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom
- (b) `online:pt:BR:U9060CCC-9` — Content `2799.99` / Merchant v1 `2799.99` / Público `2799.99` / Target orig `2399.99` issues=3 — Tênis New Balance 9060 Rich Oak Marrom

## B20 DRAFT/404 recheck
- Todos os 20 seguem ausentes de products.list/productstatuses.list e continuam 404/ausentes no `.js` público.

## Artefatos
- JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-15-a42-post-fallback-readonly-recheck.json`
- Markdown: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/rotinas/gmc-2026-05-15-a42-post-fallback-readonly-recheck.md`

## Não executado
- Merchant write
- Content API write/upsert
- Merchant ProductInputs PATCH
- Shopify write
- Tiny write
- feed fetch/upload/fetchNow
- salePrice/strikethrough update
- campaign/message/contact
