# Receipt — PDP Size Guide DEV Upload

- Timestamp UTC: 2026-06-15T00:31:16Z
- Storefront surface: LK Sneakers PDP
- Asset: `sections/lk-pdp.liquid`
- Scope approved by Lucas: upload do fix do guia de tamanhos para tema DEV e geração de preview

## Themes verified immediately before write

- DEV theme: `lk-new-theme/dev`
  - Theme ID: `155065450718`
  - Role: `unpublished`
- Production theme: `lk-new-theme/production`
  - Theme ID: `155065417950`
  - Role: `main`

## Action performed

Uploaded only `sections/lk-pdp.liquid` to DEV theme `155065450718`.

No Production upload, publish, product/catalog write, price, stock, checkout, Klaviyo, GMC, ads, WhatsApp, or email action was performed.

## Readback / verification

- DEV before SHA256: `5597dc4d04dc2c284441c295a5a47b0a5573cecea57bebb2de841275c44a5116`
- DEV target SHA256: `0573b0bac438818be428e26da0fd2d11c819657dba6cf56b02b5f69049061ee8`
- DEV after SHA256: `0573b0bac438818be428e26da0fd2d11c819657dba6cf56b02b5f69049061ee8`
- Production before SHA256: `5597dc4d04dc2c284441c295a5a47b0a5573cecea57bebb2de841275c44a5116`
- Production after SHA256: `5597dc4d04dc2c284441c295a5a47b0a5573cecea57bebb2de841275c44a5116`
- Production unchanged: yes

DEV readback checks:

- `sgFocusTrap` absent: yes
- `openSizeGuide(triggerEl)` present: yes
- modal `aria-hidden="true"` present: yes
- modal panel `tabindex="-1"` present: yes
- tabs scoped under `sizeGuideModal.querySelectorAll`: yes

Public preview probe after setting preview cookie:

- URL: `https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?preview_theme_id=155065450718`
- HTTP: 200
- contains `function openSizeGuide(triggerEl)`: yes
- contains `sgFocusTrap`: no
- contains `lk-sizeguide-modal`: yes
- contains `pi-size-guide`: yes

## Backup

Backup directory:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/backups/theme-assets/pdp-sizeguide-dev-upload-20260615T003116Z`

Rollback file:

`dev-155065450718-before-sections__lk-pdp.liquid`

## Rollback

To rollback DEV, PUT the backup file `dev-155065450718-before-sections__lk-pdp.liquid` back to theme `155065450718`, asset `sections/lk-pdp.liquid`, then re-read SHA and public preview.

## Status

DEV upload/readback completed. Production remains unchanged. Pending Lucas visual QA / approval before any Production promotion.
