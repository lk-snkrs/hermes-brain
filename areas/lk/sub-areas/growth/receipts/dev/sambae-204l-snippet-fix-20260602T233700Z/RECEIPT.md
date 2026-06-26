# Receipt — Sambae DEV corrigido para padrão 204L

Data UTC: 2026-06-02T23:46:58Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Mudanças aplicadas
- `snippets/lk-sambae-204l-hero.liquid` atualizado para usar o mesmo contrato do hero 204L:
  - classes `.lk-204l-*`;
  - `open204LReveal`;
  - estado `is-open`;
  - modal de imagem `lk-204l-photo-modal`;
  - botão “Ler mais” abrindo o reveal/collage, como no 204L.
- `snippets/lk-sambae-204l-guide.liquid` atualizado para usar o contrato visual do guia 204L:
  - `lk-guide-standard-panel`;
  - `lk-guide-standard-card--wide`;
  - CSS ID-specific para `#lk-guia-adidas-sambae`;
  - grid desktop `minmax(380px,.88fr) minmax(520px,1.12fr)`;
  - FAQPage JSON-LD.
- `sections/lk-collection.liquid` não foi alterado nesta correção; continua renderizando os 2 snippets e permanece abaixo do limite Shopify.

## QA final
```json
{
  "theme_id": "155065450718",
  "theme_role": "unpublished/dev",
  "production_changed": false,
  "section_bytes": 254715,
  "section_under_256kb": true,
  "section_hero_render_count": 1,
  "section_guide_render_count": 1,
  "hero_readback": {
    "LK Adidas Sambae": 1,
    "open204LReveal": 3,
    "is-open": 4,
    "lk-collection-v2--adidas-sambae": 1,
    "lk-sambae-204l-hero": 0
  },
  "guide_readback": {
    "LK Adidas Sambae": 1,
    "lk-guide-standard-panel": 9,
    "lk-guide-standard-card--wide": 6,
    "grid-template-columns:minmax(380px,.88fr)": 1,
    "lk-guia-adidas-sambae": 27,
    "FAQPage": 1
  },
  "render_public_preview_counts": {
    "lk-collection-v2--adidas-sambae": 1,
    "open204LReveal": 3,
    "lk-guia-adidas-sambae": 27,
    "lk-guide-standard-card--wide": 37,
    "Adidas Sambae: plataforma gum": 1,
    "Plataforma gum, leitura fashion": 1
  },
  "screenshots": {
    "preview-desktop.png": {
      "exists": true,
      "bytes": 866797
    },
    "preview-mobile.png": {
      "exists": true,
      "bytes": 168332
    }
  }
}
```

## Evidências visuais
- Desktop: `preview-desktop.png`
- Mobile: `preview-mobile.png`

## Rollback
Reaplicar:
- `hero.before.liquid` → `snippets/lk-sambae-204l-hero.liquid`
- `guide.before.liquid` → `snippets/lk-sambae-204l-guide.liquid`

Diretório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/dev/sambae-204l-snippet-fix-20260602T233700Z`
