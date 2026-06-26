# Approval Packet — Curadoria LK PDP — Adidas Tokyo Mary Jane Expansion — DEV — 2026-06-06

## Status

Prepared read-only. No Shopify write executed in this step.

## Timestamp

2026-06-06T14:36:41+00:00

## Context

After the AF1 Special expansion + title light correction was merged to Production and verified, Lucas asked to continue. Following the Curadoria LK PDP workflow, this continuation is read-only and stops at a DEV approval packet.

## Production baseline

- Theme Production: `155065417950`
- Active asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Source SHA: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`
- Scan product count: `2331`
- Covered handles detected: `929`
- Groups detected in snippet: `60`

## Proposed next safe batch

Expand the existing static Adidas Tokyo regular group:

- Marker: `top30-adidas-tokyo-regular`
- Current count: `6`
- Proposed count: `10`
- New items: `4`

Why this batch:

- It expands an already-active semantic group instead of creating a small new group.
- All new items are Adidas Tokyo Mary Jane/MJ variants, visually and semantically close to the existing Adidas Tokyo group.
- The group remains above the >5 sibling rendering threshold.
- All 4 candidates passed public PDP HTML, public `.js`, and CDN image checks.

## New items

1. `tenis-adidas-tokyo-mary-jane-cream-white-red-gold-metallic-creme`
   - Label: `Mary Jane Cream`
   - Title: `Tênis Adidas Tokyo Mary Jane Cream White Red Gold Metallic Creme`
   - HTML: 200
   - JS: 200
   - Image: 200

2. `tenis-adidas-tokyo-mary-jane-crystal-sky-cream-white-azul`
   - Label: `Mary Jane Sky`
   - Title: `Tênis Adidas Tokyo Mary Jane Crystal Sky Cream White Azul`
   - HTML: 200
   - JS: 200
   - Image: 200

3. `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa`
   - Label: `Mary Jane Pink`
   - Title: `Tênis Adidas Tokyo Mary Jane Sandy Pink Earth Strata Rosa`
   - HTML: 200
   - JS: 200
   - Image: 200

4. `tenis-adidas-tokyo-mj-core-black-cream-white-gold-metallic-preto`
   - Label: `MJ Core Black`
   - Title: `Tênis Adidas Tokyo MJ Core Black Cream White Gold Metallic Preto`
   - HTML: 200
   - JS: 200
   - Image: 200

## Candidate local

- Candidate file: `/opt/data/tmp/lk_curadoria_adidas_tokyo_expansion_candidate.liquid`
- Candidate summary: `/opt/data/tmp/lk_curadoria_adidas_tokyo_expansion_candidate_summary.json`
- Candidate SHA: `91df02fa44a717c61047b77f511ca5a351a8f4b3c4600b53da47ce0813d1c0e3`
- Diff stat vs current Production readback: `1 file changed, 4 insertions(+), 4 deletions(-)`

## Static QA

- Marker count for `top30-adidas-tokyo-regular`: `1`
- Before count: `6`
- After counts:
  - handles: `10`
  - labels: `10`
  - images: `10`
  - titles: `10`
- Duplicate handles: `0`
- Malformed `https`: false
- Placeholder image (`TenisMoldeLK`): false

## Risk

Low/medium:

- This is a static legacy-style group, not the generic `lk_top30_*` array group. The patch must target the static Adidas Tokyo block, preserving all other static and array groups.
- Public edge/cache may show mixed results shortly after DEV/Production writes.
- The new items are Mary Jane/MJ variations; semantically close enough to Adidas Tokyo, but visually they are a sub-style. If desired, this can later become a separate Mary Jane-specific group once there are enough items and a business rule favors separation.

## Rollback plan

For DEV:

1. Backup DEV asset before write.
2. Apply candidate only to DEV theme `155065450718` if approved.
3. Read back DEV until the exact candidate or expected static group counts appear.
4. If QA fails, restore the DEV backup asset.

For Production later:

- Separate approval required for merge para Production.
- Production must go through GitHub PR/review → merge branch `production` → Shopify readback → live QA → receipt.

## Requested approval

To apply this to DEV only, Lucas should approve explicitly:

`Aprovo DEV Adidas Tokyo Mary Jane Expansion`
