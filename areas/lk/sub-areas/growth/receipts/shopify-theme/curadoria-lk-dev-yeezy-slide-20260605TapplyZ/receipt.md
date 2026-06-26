# Curadoria LK PDP — DEV Yeezy Slide

- timestamp UTC: `2026-06-05T18:13:52.099749+00:00`
- approval: `Lucas approved in Telegram: apply to DEV group top30-yeezy-slide-regular with 7 handles/short labels/validated images; no Production/product/price/stock/app writes.`
- DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- asset: `snippets/lk-variante-top30-visited.liquid`
- production unchanged: `True`
- readback matches target: `True`
- hashes: before `01af5cea362d`, target `493429e95ac5`, readback `493429e95ac5`

## Grupo aplicado
- `tenis-adidas-yeezy-slide-slate-marine-azul-escuro` → Slate Marine — `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-adidas-yeezy-slide-slate-marine-azul-escuro-lk-sneakers-937161.jpg?v=1717500027`
- `yeezy-slide-azure` → Azure — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-azure-azul-262524.jpg?v=1710449811`
- `yeezy-slide-bone-937693978` → Bone — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-bone-branco-185148.webp?v=1710449811`
- `yeezy-slide-glow-green` → Glow Green — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-glow-green-verde-513437.webp?v=1710449810`
- `yeezy-slide-ochre-925686464` → Ochre — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-ochre-marrom-211761.webp?v=1710449812`
- `yeezy-slide-onyx` → Onyx — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-onyx-preto-317608.webp?v=1710449811`
- `yeezy-slide-pure-2022` → Pure — `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-yeezy-slide-pure-2022-bege-380649.jpg?v=1710449811`

## QA
- preflight products OK: `True`
- preflight images OK: `True`
- static arrays equal: `True`
- marker count: `1`
- handles/labels/images: `7` / `7` / `7`
- handles match: `True`
- labels match: `True`
- images valid: `True`
- bad URL occurrences: `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`

## Preview HTML QA
- Caveat: a tentativa pública com `preview_theme_id=155065450718` redirecionou para a URL canônica sem parâmetro de preview, então o HTML retornado era da Production/live e não serve como reprovação do DEV.
- QA confiável desta execução: Asset API DEV readback + QA estático do Liquid.
- Simulação estática: todos os 7 PDPs teriam 5 cards e excluem o produto atual.

## Rollback
- restore DEV asset from `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/curadoria-lk-dev-yeezy-slide-20260605TapplyZ/dev-before.liquid`

## Non-actions
- No Production/main write
- No product write
- No price/stock/app/GMC/Tiny/Klaviyo/Meta/checkout/discount/fulfillment write