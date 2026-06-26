# LKGOC P1 DEV corrections receipt

- Timestamp UTC: 2026-06-03T14:25:50.437110+00:00
- Theme DEV: 155065450718
- Scope: Shopify DEV theme only; production untouched.
- Assets updated:
  - `snippets/lk-sambae-204l-hero.liquid` readback_match=True bytes=5212
  - `snippets/lk-sambae-204l-guide.liquid` readback_match=True bytes=7281
  - `sections/lk-collection.liquid` readback_match=True bytes=257083
  - `sections/main-page.liquid` readback_match=True bytes=1062

## Checks
- sambae_hero_chars: 570
- sambae_refs: True
- samba_jane_schema_branch: True
- main_page_namespace: True
- removed_prod_comment: True

## Rollback
Reenviar os arquivos `before__*` deste receipt para os mesmos asset keys no theme DEV.