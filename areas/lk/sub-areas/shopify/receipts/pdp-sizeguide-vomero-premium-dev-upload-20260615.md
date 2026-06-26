# Receipt — PDP Size Guide Nike Vomero Premium DEV upload

Date: 2026-06-15
Agent/profile: lk-shopify
Scope: Shopify theme DEV/unpublished, asset `sections/lk-pdp.liquid`

## User request
Lucas asked to make Nike Vomero Premium with normal sizing and a New Balance 9060-style table using Vomero Premium/Nike sizing research.

## Research evidence
- Nike Vomero Premium is listed by Nike as Men’s/Women’s Road Running Shoes.
- Nike size chart provides US Men, US Women, EU and CM/JP conversion. LK table used the Nike BR-grade/foot-length conversion already used for Nike Mind 002.
- Running Warehouse: `Sizing: True to Size`; length true to size and fit fairly generous/adaptive.
- Gearist: `Sizing: True to size in a typical Nike Running shape`.

## Local implementation
File: `sections/lk-pdp.liquid`

Added:
- `lk_is_vomero_premium` detection via handle/title containing `vomero-premium` / `vomero premium`.
- Modal brand label: `Nike Vomero Premium`.
- TTS copy: `O Nike Vomero Premium costuma vestir normal. Recomendamos comprar seu tamanho habitual. Grade Nike com conversão US masculino, US feminino, EU e CM.`
- Full table shape: `BR | US M | US W | EU | CM`.
- Tip: `Se estiver entre dois tamanhos, escolha o maior.`

## Table rows
- `34 / 3.5 / 5 / 35.5 / 21.6`
- `34.5 / 4 / 5.5 / 36 / 22.0`
- `35 / 4.5 / 6 / 36.5 / 22.4`
- `35.5 / 5 / 6.5 / 37.5 / 22.9`
- `36 / 5.5 / 7 / 38 / 23.3`
- `37 / 6 / 7.5 / 38.5 / 23.7`
- `37.5 / 6.5 / 8 / 39 / 24.1`
- `38 / 7 / 8.5 / 40 / 24.5`
- `39 / 7.5 / 9 / 40.5 / 25.0`
- `39.5 / 8 / 9.5 / 41 / 25.4`
- `40 / 8.5 / 10 / 42 / 25.8`
- `40.5 / 9 / 10.5 / 42.5 / 26.2`
- `41 / 9.5 / 11 / 43 / 26.7`
- `42 / 10 / 11.5 / 44 / 27.1`
- `42.5 / 10.5 / 12 / 44.5 / 27.5`
- `43 / 11 / 12.5 / 45 / 27.9`
- `43.5 / 11.5 / 13 / 45.5 / 28.3`
- `44 / 12 / 13.5 / 46 / 28.8`
- `45 / 12.5 / 14 / 47 / 29.2`

## DEV upload
Approval: Lucas approved via Telegram clarify button: `Aprovado — subir para DEV/unpublished`.

Theme:
- DEV theme ID: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`

Asset API:
- HTTP PUT status: 200
- Target/readback SHA12: `8444d3aede2f`
- Production unchanged during DEV upload.
- Backup directory: `/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/backups/shopify-dev-sizeguide-vomero-premium-20260615`

## QA DEV mobile
Cookie-preserving preview session with `preview_theme_id=155065450718`.

Handles tested:
- `tenis-nike-vomero-premium-black-volt-preto`
- `tenis-nike-vomero-premium-sail-coconut-milk-branco`
- `tenis-nike-vomero-premium-hyper-pink-rosa`
- Control: `air-jordan-1-mid-wolf-grey`

Checks passed:
- DEV theme seen in server timing.
- HTTP 200.
- Size guide modal present.
- Vomero label present.
- TTS copy present.
- Full columns present: BR, US M, US W, EU, CM.
- Rows `38 / 7 / 8.5 / 40 / 24.5` and `45 / 12.5 / 14 / 47 / 29.2` present.
- Jordan 1 Mid control preserved.

Known unrelated DEV issue observed:
- `Liquid error (layout/theme line 513): Could not find asset snippets/lk-growth-geo-faq-schema.liquid`
- This was previously observed on DEV and is not caused by this size-guide change.

## Non-actions
- No Production merge/publish.
- No product, price, stock, collection, GMC, Klaviyo, ads, WhatsApp or email changes.

## Rollback
Restore DEV asset from backup:
`/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/backups/shopify-dev-sizeguide-vomero-premium-20260615/dev_before_sections_lk-pdp.liquid`
