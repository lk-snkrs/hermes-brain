# DEV sync receipt — PR72 New Balance 2002R LKGOC

Data UTC: 20260613T122548Z

## Approval
Lucas aprovou: "Fazer aprovado" para sync do PR/branch no tema DEV.

## Scope
Branch: `lkgoc/new-balance-2002r-fix-20260613`
PR: https://github.com/lk-snkrs/lk-new-theme/pull/72
Commit head at deploy: `2314a87 Align 2002R hero with 204L golden contract`
Destination theme: `lk-new-theme/dev`
Theme ID: `155065450718`
Role: `unpublished`

## Command path
Used Shopify CLI theme push via Hermes wrapper, not direct Shopify Admin API asset write.
Flags:
- `--theme 155065450718`
- `--nodelete`
- `--only` changed LKGOC files
- `--json`

## Files synced
- `sections/lk-collection.liquid`
- `snippets/lk-goc-new-balance-2002r-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-2002r-guide-panel.liquid`
- `templates/collection.new-balance-2002r.json`

## CLI result
Theme upload complete.
Preview URL: https://lksneakers.com.br/collections/new-balance-2002r?preview_theme_id=155065450718

## Public preview QA readback
After cache warm-up, preview HTML contained:
- `lk-goc-coll-preview--2002r`: OK
- `Retrô running, presença urbana.`: OK
- `lk-guia-new-balance-2002r`: OK
- `collection.new-balance-2002r`: OK

## Production
No Production sync/merge was performed in this step.
