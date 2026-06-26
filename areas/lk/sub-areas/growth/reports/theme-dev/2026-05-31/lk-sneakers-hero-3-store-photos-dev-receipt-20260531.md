# LK Sneakers — Hero 3 fotos da loja no Dev — Receipt

Data UTC: 2026-05-31 21:20:05

## Escopo
- Tema Dev: `155065450718`
- Asset: `sections/lk-collection.liquid`
- Production: inalterado
- Sem alterações em produto, preço, estoque, feed/GMC ou campanha.

## Aprovação
Lucas aprovou no turno atual: `Aprovo Dev: 3 fotos no hero Sneakers`.

## Mudanças
- Adicionado bloco visual no hero da coleção Sneakers com 3 fotos novas da loja.
- Fotos usadas:
  - `GF_3805_hi.jpg?v=1728506174`
  - `GF_3812_hi.jpg?v=1728506174`
  - `GF_3840_hi.jpg?v=1728506174`
- Foto antiga `Loja-LK.jpg?v=1705163797` removida do asset Dev e substituída no bloco de confiança pós-grid.
- Layout mobile: 3 cards compactos no hero, preservando o grid como prioridade.

## Verificação readback
{
  "dev_has_hero_3_photo_css_marker": true,
  "dev_has_photo_GF_3805": true,
  "dev_has_photo_GF_3812": true,
  "dev_has_photo_GF_3840": true,
  "old_Loja_LK_removed_from_dev_asset": true,
  "production_unchanged_vs_known_hash": true
}

## Observação técnica
O primeiro readback imediato do Shopify Asset API veio defasado; após alguns segundos, o readback do Dev confirmou os marcadores e as 3 imagens novas.

## Preview
https://www.lksneakers.com.br/collections/sneakers?preview_theme_id=155065450718

## Rollback
Restaurar `dev.before.liquid` do receipt técnico mais recente em:
`hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-hero-3-store-photos-dev-20260531T211920Z/`
