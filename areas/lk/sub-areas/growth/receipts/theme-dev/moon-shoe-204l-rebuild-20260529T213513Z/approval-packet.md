# Approval packet — Moon Shoe collection rebuild in LK 204L pattern

Date: 2026-05-29T21:35:13Z

## Scope

Rebuilt the Nike x Jacquemus Moon Shoe SP collection page in the dev Shopify theme using the canonical LK 204L pattern.

- Collection: `/collections/nike-x-jacquemus-moon-shoe-sp`
- Dev theme: `155065450718`
- Production source/gold reference: `155065417950`
- Main asset changed: `sections/lk-collection.liquid`
- Support asset synced to remove dev Liquid error: `snippets/et-tracker.liquid`

## What changed

- Reconstructed the top editorial collection block using the 204L logic:
  - H1 remains collection title.
  - Kicker simplified to `Curadoria LK`.
  - Editorial H2: `Perfil baixo, leitura fashion.`
  - Premium copy focused on Jacquemus, Nike archive, slim proportion, colorways, originality and human guidance.
- Added post-grid editorial guide in the canonical 204L structure:
  - Guide panel after product grid.
  - Two-column desktop layout.
  - `Como escolher` section.
  - FAQ accordion inside the guide.
  - CTA to the standalone Moon Shoe guide page.
- Suppressed the legacy below-grid collection FAQ for this handle to avoid duplicate UX.
- Added Moon-specific CSS parity for the 204L after-grid guide pattern.
- Synced `snippets/et-tracker.liquid` from production into dev because the dev preview footer showed a Liquid error for a missing snippet.

## Validation

Preview URL:

https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065450718

Verified:

- HTTP 200 on dev preview.
- `lk-moon-coll-preview`: present.
- `lk-guia-nike-x-jacquemus-moon-shoe-sp`: present.
- Legacy `.coll-faq`: not rendered.
- FAQPage JSON-LD count: 1.
- Liquid error: not present after snippet sync.
- Forbidden operational terms not present in rendered HTML/text:
  - `Pronta entrega`
  - `Estoque limitado`
  - `Entrega SP`
  - `Sujeito a encomenda`
  - `produtos em estoque`
  - `rodar`
- Standalone guide link returns HTTP 200:
  - `/pages/nike-moon-shoe-jacquemus-guia-lk`

## Risk

Low/medium.

- Dev only so far.
- Production publish would touch `sections/lk-collection.liquid` and, only if missing, `snippets/et-tracker.liquid` is already present in production.
- Main risk is visual/content preference, not functional breakage.

## Rollback

Dev rollback:

- Restore backup: `backups/theme-dev/moon-shoe-204l-rebuild-20260529T213513Z/dev-lk-collection.before.liquid`
- Remove or restore `snippets/et-tracker.liquid` only if needed; in dev it was missing and caused a visible Liquid error.

Production rollback if approved/published later:

- Snapshot production `sections/lk-collection.liquid` before publish.
- Restore that snapshot if visual/SEO issues are found.

## Approval needed

Explicit Lucas approval is required before publishing this rebuild to production/main theme `155065417950`.
