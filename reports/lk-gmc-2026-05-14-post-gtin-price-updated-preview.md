# LK GMC post-GTIN price_updated preview — 2026-05-14

Gerado em: `2026-05-15T20:10:16.593919+00:00`

## Summary
- Productstatuses lidos: `23277`
- Produtos online com price/strikethrough issue: `310`
- Decision states: `{'candidate_price_only_patch_to_shopify_current_price': 42, 'review_promotional_price_or_compare_at_price': 268}`
- Piloto recomendado: `42` price-only rows

## Recomendação
- Primeiro aplicar **somente preço atual** em 100 produtos sem `strikethrough_price_updated`/salePrice/compareAt; rota Merchant API ProductInputs v1 `productAttributes.price`.
- Deixar `strikethrough_price_updated` para preview separado, porque envolve sale/compare-at e pode afetar preço riscado.

## Amostras do piloto
- `online:pt:BR:01424-002-2` — Merchant 5999.90 → Shopify 8999.99 — Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul
- `online:pt:BR:CU3244100-41` — Merchant 14999.99 → Shopify 22999.99 — Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido
- `online:pt:BR:CZ2239600-3` — Merchant 4699.99 → Shopify 6999.90 — Tênis Nike SB Dunk Low What The P-Rod Colorido
- `online:pt:BR:DQ4040400-39` — Merchant 2999.90 → Shopify 2999.99 — Tênis Nike SB Dunk Low PRM Phillies Azul
- `online:pt:BR:HQ6998-211` — Merchant 2499.99 → Shopify 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-212` — Merchant 2499.99 → Shopify 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-213` — Merchant 2499.99 → Shopify 3499.99 — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HV0823-119` — Merchant 3499.99 → Shopify 4499.99 — Tênis Nike Air Jordan 4 Retro Valentine's Day Sierra Red Vermelho
- `online:pt:BR:ID0440-1` — Merchant 1449.90 → Shopify 1749.99 — Tênis adidas Sambae Cloud White Collegiate Green Branco
- `online:pt:BR:ID0440-3` — Merchant 1449.90 → Shopify 1749.99 — Tênis adidas Sambae Cloud White Collegiate Green Branco
- `online:pt:BR:IG5932` — Merchant 1599.99 → Shopify 1799.99 — Tênis Adidas Samba Wonder Clay Branco
- `online:pt:BR:IG5932-4` — Merchant 1599.99 → Shopify 1799.99 — Tênis Adidas Samba Wonder Clay Branco

## Não executado
- Merchant write
- ProductInputs patch
- Content API upsert/delete
- Shopify write
- Tiny write
- feed fetch/upload
- salePrice/strikethrough update
- local/LIA change
- campaign/message/send
