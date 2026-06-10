# Receipt — LKGOC Shopify template standard preview DEV

## Status
PASS parcial para preview técnico DEV. Production bloqueada.

## Aprovação Lucas
Lucas aprovou seguir com: subir branch LKGOC template standard para GitHub e preparar preview em DEV/unpublished.

## GitHub
- Repo: `lk-snkrs/lk-new-theme`
- Branch publicada: `hermes/lkgoc-template-standard-20260609`
- Commit: `dcc9c00 Add LKGOC standard collection template`
- PR URL sugerida: `https://github.com/lk-snkrs/lk-new-theme/pull/new/hermes/lkgoc-template-standard-20260609`

## Shopify DEV
- Theme: `155065450718`
- Name: `lk-new-theme/dev`
- Role verificado por API antes do write: `unpublished`

## Assets aplicados em DEV/unpublished
- `templates/collection.lkgoc.json`
- `sections/lk-collection.liquid`

## Readback
- `templates/collection.lkgoc.json` remoto contém `lkgoc_template_mode: true` após reenvio posterior ao schema.
- `sections/lk-collection.liquid` remoto contém setting `lkgoc_template_mode`.

## Preview técnico
- URL: https://www.lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&view=lkgoc
- HTML salvo: `preview-curl.html`
- Desktop screenshot: `preview-204l-lkgoc-desktop.png`
- Mobile screenshot: `preview-204l-lkgoc-mobile.png`

## Checks
```json
{
  "preview_url": "https://www.lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&view=lkgoc",
  "bytes": 648601,
  "theme_name_dev": true,
  "theme_id_155065450718": true,
  "theme_role_unpublished": true,
  "liquid_error": false,
  "lk_goc_count": 225,
  "guide_idx": 396239,
  "grid_idx": 253770,
  "grid_before_guide": true,
  "desktop_screenshot": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/theme-dev/lkgoc-shopify-template-standard-preview-20260609T1135Z/preview-204l-lkgoc-desktop.png",
  "desktop_screenshot_bytes": 639022,
  "mobile_screenshot": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/theme-dev/lkgoc-shopify-template-standard-preview-20260609T1135Z/preview-204l-lkgoc-mobile.png",
  "mobile_screenshot_bytes": 109567
}
```

## Observações
- Não alterei collection object/template_suffix; usei `view=lkgoc` para preview sem mudar produção.
- Não houve write em theme `main`.
- Não houve promoção/merge para production.
- `shopify theme check` tinha dado timeout local na etapa anterior; nesta etapa a validação foi via API readback + render público preview + screenshots.

## Rollback DEV
- Restaurar `sections/lk-collection.liquid` a partir de `sections__lk-collection.liquid.before`.
- Remover ou zerar `templates/collection.lkgoc.json` no theme DEV se necessário.
