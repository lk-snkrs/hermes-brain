# Incidente LKGOC — DEV publicado temporariamente

Data UTC: 2026-06-03T17:43:21.895709+00:00

## Estado verificado
- Production ativo/main: `lk-new-theme/production` `155065417950`
- Dev rascunho/unpublished: `lk-new-theme/dev` `155065450718`

## Observação
Durante a correção visual da coleção New Balance 204L, o tema DEV estava publicado como main. Lucas corrigiu manualmente no Shopify, retornando Production para ativo e DEV para rascunho.

## Guardrail reforçado
Antes de qualquer write LKGOC: verificar via API que o alvo de edição tem `role: unpublished`. Se o tema `lk-new-theme/dev` estiver `role: main`, abortar write e avisar Lucas. Production só recebe merge/promoção após approval explícito.

## Comparativo 204L
```json
{
  "production": {
    "theme_id": "155065417950",
    "asset_sha256": "9737251b38f92e68dc37ed6b49761ca44fcf99dff2629f707d6454766e18ce4a",
    "asset_bytes": 253801,
    "block_found": true,
    "block_sha256": "31d3120ee9d2458bf8812dadcc81dc94cb397b0f4cb195a39316524604b8e4d6",
    "block_bytes": 5295,
    "goc_count": 0,
    "lkgoc_count": 0,
    "legacy_204l_count": 20,
    "critical_css": 0,
    "typography_fix": 0,
    "paragraph_good_color": 0,
    "paragraph_bad_color": 0
  },
  "dev": {
    "theme_id": "155065450718",
    "asset_sha256": "59544bd7263170301745defd87613ae97c94788ad23f131969e6bee61421a4bc",
    "asset_bytes": 259537,
    "block_found": true,
    "block_sha256": "c060cbeb3134568a8c2be5fee88253e4d3acf5e4af255803d1268d72fa2f6475",
    "block_bytes": 7913,
    "goc_count": 50,
    "lkgoc_count": 0,
    "legacy_204l_count": 14,
    "critical_css": 1,
    "typography_fix": 1,
    "paragraph_good_color": 1,
    "paragraph_bad_color": 1
  }
}
```
