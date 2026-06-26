# Receipt — PDP DEV missing GEO FAQ schema snippet fix

Date UTC: 20260616T104541Z
Profile: lk-collection-optimizer / LKGOC

## Trigger

Lucas reported PDP Liquid error:

`Liquid error (layout/theme line 513): Could not find asset snippets/lk-growth-geo-faq-schema.liquid`

## Diagnosis

Read-only Shopify Admin check:

- Production theme: `lk-new-theme/production` — theme_id `155065417950`, role `main`
  - `layout/theme.liquid` has `{% render 'lk-growth-geo-faq-schema' %}` at line 513.
  - `snippets/lk-growth-geo-faq-schema.liquid` exists.
- DEV theme: `lk-new-theme/dev` — theme_id `155065450718`, role `unpublished`
  - `layout/theme.liquid` has `{% render 'lk-growth-geo-faq-schema' %}` at line 513.
  - `snippets/lk-growth-geo-faq-schema.liquid` was missing.
- DEV v2 theme: `lk-new-theme/dev-v2` — theme_id `155306164446`, role `unpublished`
  - does not render the snippet; snippet absent; no action needed for this error.

Conclusion: error was isolated to `lk-new-theme/dev` because the layout render existed without the corresponding snippet asset.

## Action taken

DEV-only write after verifying `role=unpublished`:

- Uploaded `snippets/lk-growth-geo-faq-schema.liquid` to theme_id `155065450718` (`lk-new-theme/dev`).
- Source file reused from approved Growth receipt candidate:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/llms-fix-all-20260609/assets-candidate/snippets__lk-growth-geo-faq-schema.liquid`
- Source SHA-12: `5a57110a7602`
- Readback SHA-12: `5a57110a7602`
- Readback matches source: `true`

No Production write was made.

## QA

Preview PDP checked:

- `https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto?preview_theme_id=155065450718`
- HTTP fetch returned product HTML.
- Raw HTML QA:
  - `Liquid error`: absent
  - `lk-growth-geo-faq-schema`: absent in rendered HTML, expected because the snippet is conditional for selected GEO pages and emits nothing for this PDP.

## Rollback

If needed in DEV only:

- Delete asset `snippets/lk-growth-geo-faq-schema.liquid` from theme_id `155065450718`, or restore DEV theme from prior backup/state.
- Note: deleting while layout line 513 remains will reintroduce the Liquid error on PDPs.

## Risk

Low. Snippet is non-visual and conditional. For PDPs outside the target URLs, it outputs no markup. Production already had the matching asset and was not changed.
