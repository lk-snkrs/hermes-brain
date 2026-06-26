# LK Sneakers — Remoção da trust bar no Dev — Receipt

Data UTC: 2026-05-31 21:31:16

## Escopo
- Tema Dev: `155065450718`
- Asset: `sections/lk-collection.liquid`
- Production: inalterado
- Sem alterações em produto, preço, estoque, feed/GMC ou campanha.

## Pedido
Lucas pediu remover a trust bar porque as fotos do hero já cumprem o papel visual/variedade/confiança.

## Mudança
- Adicionado CSS condicional no Dev:
  - quando o bloco `.lk-sneakers-hero-photos` existe, a `.lk-cro-trust-strip` fica oculta.
- As 3 fotos novas do hero foram preservadas:
  - `GF_3805_hi.jpg`
  - `GF_3812_hi.jpg`
  - `GF_3840_hi.jpg`

## Verificação readback
- `dev_has_remove_marker`: true
- `dev_still_has_hero_photos`: true
- `production_unchanged`: true
- `dev_readback_matches_target`: true

## Preview
https://www.lksneakers.com.br/collections/sneakers?preview_theme_id=155065450718

## Rollback
Restaurar `dev.before.liquid` do receipt técnico:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-remove-trustbar-dev-20260531T213116Z/`
