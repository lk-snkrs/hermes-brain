# LK GMC P1-B Availability In-Stock Policy Packet, 2026-05-12

Status: `gmc_p1_availability_in_stock_policy_packet_ready_no_write`

## Correção de política
- Lucas corrigiu: mesmo sem estoque no Tiny, o produto deve aparecer disponível no GMC.
- Portanto, a proposta corrigida é `availability = in stock` para os produtos online exatos com availability ausente.
- Tiny continua valendo para operação/sourcing/stockout, mas não para enviar `out of stock` ao GMC.

## Resumo executivo
- Produtos online com diagnóstico `availability` ausente: 1616
- Proposta `in stock`: 1616
- Proposta `out of stock`: 0
- Tiny calls nesta correção: 0
- Merchant/Tiny/Shopify/feed/DB/POS writes: 0

## Amostra inline — primeiros 25 IDs
- `online:pt:BR:1023851-1A17746_2NM8J-1` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-10` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-2` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-3` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-4` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-5` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-6` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-7` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-8` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1023851-1A17746_2NM8J-9` → `availability: in stock` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom
- `online:pt:BR:1182A660001` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A660002` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A660003` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A660004` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A660005` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A660006` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Triple Black Preto
- `online:pt:BR:1182A677.001-1` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-10` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-11` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-12` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-2` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-3` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-4` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-5` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto
- `online:pt:BR:1182A677.001-6` → `availability: in stock` — Tênis Onitsuka Tiger Mexico 66 TGRS Black/Gunmetal Glitter Pack Preto

## Approval wording
`Aprovo aplicar availability=in stock no Merchant para os 1616 produtos online exatos do packet P1-B corrigido; Tiny zero/no stock não deve derrubar GMC availability; sem alterar Tiny/Shopify/feed/DB/POS/campanhas/sourcing, com rollback privado antes do write e piloto fail-fast primeiro.`

## Não executado
- merchant_product_update
- merchant_product_insert_upsert
- tiny_call
- tiny_write
- shopify_write
- feed_update_or_fetch
- database_write
- pos_write
- campaign_or_external_send
- sourcing_or_supplier_contact
