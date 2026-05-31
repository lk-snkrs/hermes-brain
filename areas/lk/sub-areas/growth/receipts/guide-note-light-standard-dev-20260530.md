# Receipt — LK guide note light background standard

Date: 2026-05-30
Theme: Shopify dev `155065450718`
File: `sections/lk-collection.liquid`

## Lucas correction
The helper note block with the copy “Para aprofundar versões, materiais e proporção, abra o guia completo da coleção.” must have a light/clear background as the standard.

## Change
Changed the base `.lk-guide-standard-media` rule from dark to light:

- background: `#fff`
- text color: `#171717` / paragraph `#333`
- border: `1px solid #e2dbd0`
- link color: `#171717`

This makes the light helper note the default for LK after-grid guide panels, not only a handle-specific override.

## Verification
Shopify Admin readback after upload:

- `light_standard_present`: true
- `dark_media_base_present`: false

Storefront dev preview computed style for Onitsuka helper note:

- background: `rgb(255, 255, 255)`
- text color: `rgb(23, 23, 23)`
- border: `rgb(226, 219, 208) 1px`
- guide present: true
- legacy `.coll-faq`: false
- `FAQPage` JSON-LD count: 1

Visual validation confirmed the block is light/white, text is dark, and the CTA remains black.

## Backup
Local pre-change backup:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-dev/guide-note-light-standard-20260530T174851/sections__lk-collection.liquid`

## Production status
Production untouched. Requires Lucas approval before publishing to main theme `155065417950`.
