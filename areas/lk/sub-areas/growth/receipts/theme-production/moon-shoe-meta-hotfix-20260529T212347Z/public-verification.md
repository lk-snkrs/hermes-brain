# Moon Shoe meta hotfix — public verification

Timestamp UTC: 2026-05-29T21:24-21:25Z

## Approved scope
Lucas approved: "Aprovo hotfix theme.liquid Moon Shoe meta em produção".

## Shopify Admin readback
- Theme: `155065417950` (`lk-new-theme/production`, role `main`)
- Asset: `layout/theme.liquid`
- Patched anchors: meta description, OG description, Twitter description
- New description:
  `Nike x Jacquemus Moon Shoe SP na curadoria LK: modelos originais, leitura fashion, colorways desejadas e atendimento humano para confirmar tamanho e prazo.`
- Admin readback contains the new conditional blocks for `nike-x-jacquemus-moon-shoe-sp`.

## Public verification
- Production preview URL with explicit theme ID validated clean:
  `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp?preview_theme_id=155065417950`
- Preview HTML contains the new meta description.
- Preview HTML terms:
  - `Estoque limitado`: 0
  - `Entrega SP`: 0

## Cache note
At verification time, the clean public URL without `preview_theme_id` was still serving stale Shopify/CDN HTML with the old meta description. The production theme preview proves the main theme asset is correct; recheck the clean URL after cache propagation.

## Rollback
Restore backup asset:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/moon-shoe-meta-hotfix-20260529T212347Z/layout__theme.liquid.before`
