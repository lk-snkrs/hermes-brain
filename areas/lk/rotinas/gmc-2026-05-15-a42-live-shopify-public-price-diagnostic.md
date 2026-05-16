# LK GMC — A42 live Shopify public price diagnostic

Gerado em: `2026-05-15T21:29:13.736052+00:00`
Status: `read_only_live_public_price_diagnostic_complete`

## Resumo
- rows: `42`
- public_matches_merchant_after: `25`
- public_matches_target_snapshot: `18`
- public_errors: `0`
- public_price_relation_counts: `{'public_eq_target': 17, 'public_eq_merchant': 25}`

## Amostra
- `online:pt:BR:01424-002-2` — public `8999.99` / Merchant pós `5999.90` / target snapshot `8999.99` — Tênis Born Raised x Nike SB Dunk Low One Block At A Time Azul
- `online:pt:BR:CU3244100-41` — public `22999.99` / Merchant pós `14999.99` / target snapshot `22999.99` — Tênis Ben & Jerry's x Dunk Low SB Chunky Dunky Colorido
- `online:pt:BR:CZ2239600-3` — public `6999.90` / Merchant pós `4699.99` / target snapshot `6999.90` — Tênis Nike SB Dunk Low What The P-Rod Colorido
- `online:pt:BR:DQ4040400-39` — public `2999.99` / Merchant pós `2999.90` / target snapshot `2999.99` — Tênis Nike SB Dunk Low PRM Phillies Azul
- `online:pt:BR:HQ6998-211` — public `3499.99` / Merchant pós `2499.99` / target snapshot `3499.99` — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-212` — public `3499.99` / Merchant pós `2499.99` / target snapshot `3499.99` — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HQ6998-213` — public `3499.99` / Merchant pós `2499.99` / target snapshot `3499.99` — Tênis Nike Air Jordan 1 Low OG Olive Verde
- `online:pt:BR:HV0823-119` — public `4499.99` / Merchant pós `3499.99` / target snapshot `4499.99` — Tênis Nike Air Jordan 4 Retro Valentine's Day Sierra Red Vermelho
- `online:pt:BR:ID0440-1` — public `1749.99` / Merchant pós `1449.90` / target snapshot `1749.99` — Tênis adidas Sambae Cloud White Collegiate Green Branco
- `online:pt:BR:ID0440-3` — public `1749.99` / Merchant pós `1449.90` / target snapshot `1749.99` — Tênis adidas Sambae Cloud White Collegiate Green Branco
- `online:pt:BR:IG5932` — public `1799.99` / Merchant pós `1599.99` / target snapshot `1799.99` — Tênis Adidas Samba Wonder Clay Branco
- `online:pt:BR:IG5932-4` — public `1799.99` / Merchant pós `1799.99` / target snapshot `1799.99` — Tênis Adidas Samba Wonder Clay Branco

## Interpretação
- Se `public_matches_merchant_after` for alto, o Merchant está refletindo a vitrine pública e o snapshot local/Shopify usado como target estava stale ou divergente.
- Nesse caso, não insistir em preço via Merchant; corrigir fonte Shopify/canal/loja primeiro.

## Não executado
- Merchant write
- Shopify write
- Tiny write
- feed fetch/upload
- campaign/message/contact
