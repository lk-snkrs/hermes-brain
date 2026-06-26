# Receipt — LKGOC namespace dual-class migration em DEV

Data UTC: 2026-06-03T00:04:50Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Decisão aplicada
O componente editorial que nasceu como `lk-204l-*` passou a emitir também o namespace canônico `lk-lkgoc-*`, mantendo `lk-204l-*` como alias temporário para CSS/JS e rollback seguro.

## Assets alterados
- `sections/lk-collection.liquid` — 204L inline agora tem classes LKGOC + aliases legacy; JS aceita os dois seletores.
- `snippets/lk-sambae-204l-hero.liquid` — Sambae hero agora tem classes LKGOC + aliases legacy; JS aceita os dois seletores.
- `snippets/lk-sambae-204l-guide.liquid` — guia Sambae emite `lk-lkgoc-guide-panel` junto de `lk-guide-standard-panel`.

## QA static/readback
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "section_bytes_before": 255148,
  "section_bytes_after": 256894,
  "section_under_256kb_after": true,
  "section_lkgoc_preview_count": 12,
  "section_legacy_preview_count": 71,
  "sambae_hero_lkgoc_preview_count": 3,
  "sambae_hero_legacy_preview_count": 3,
  "sambae_guide_lkgoc_guide_panel_count": 1,
  "js_generic_root_check_section": true,
  "section_still_has_sambae_desc_override": true,
  "section_sambae_renders": 2,
  "readback_attempts": 1,
  "readback_matches_all": true,
  "readback_counts": {
    "sections/lk-collection.liquid": {
      "lk_lkgoc_coll_preview": 12,
      "lk_204l_coll_preview": 71,
      "lk_lkgoc_card": 21,
      "lk_lkgoc_guide_panel": 0,
      "open204LReveal": 12,
      "sambae_desc_override": 1
    },
    "snippets/lk-sambae-204l-hero.liquid": {
      "lk_lkgoc_coll_preview": 3,
      "lk_204l_coll_preview": 3,
      "lk_lkgoc_card": 6,
      "lk_lkgoc_guide_panel": 0,
      "open204LReveal": 3,
      "sambae_desc_override": 0
    },
    "snippets/lk-sambae-204l-guide.liquid": {
      "lk_lkgoc_coll_preview": 0,
      "lk_204l_coll_preview": 0,
      "lk_lkgoc_card": 0,
      "lk_lkgoc_guide_panel": 1,
      "open204LReveal": 0,
      "sambae_desc_override": 0
    }
  }
}
```

## QA render
```json
{
  "new-balance-204l": {
    "url": "https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&qa=lkgoc-ns",
    "status": 200,
    "final_url": "https://lksneakers.com.br/collections/new-balance-204l?qa=lkgoc-ns",
    "bytes": 583204,
    "counts": {
      "lk-lkgoc-coll-preview": 3,
      "lk-204l-coll-preview": 98,
      "lk-lkgoc-card": 6,
      "lk-204l-card": 35,
      "lk-lkgoc-read-more": 2,
      "lk-204l-read-more": 5,
      "lk-lkgoc-guide-panel": 0,
      "lk-guide-standard-panel": 52,
      "open204LReveal": 3,
      "lk-guia-adidas-sambae": 0,
      "lk-guia-new-balance-204l": 57,
      "coll-rich-content": 0
    }
  },
  "adidas-sambae": {
    "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718&qa=lkgoc-ns",
    "status": 200,
    "final_url": "https://lksneakers.com.br/collections/adidas-sambae?qa=lkgoc-ns",
    "bytes": 564015,
    "counts": {
      "lk-lkgoc-coll-preview": 3,
      "lk-204l-coll-preview": 98,
      "lk-lkgoc-card": 6,
      "lk-204l-card": 35,
      "lk-lkgoc-read-more": 2,
      "lk-204l-read-more": 5,
      "lk-lkgoc-guide-panel": 1,
      "lk-guide-standard-panel": 57,
      "open204LReveal": 3,
      "lk-guia-adidas-sambae": 27,
      "lk-guia-new-balance-204l": 56,
      "coll-rich-content": 0
    }
  }
}
```

## Rollback
Reaplicar os arquivos `*.before.liquid` deste diretório nos respectivos asset keys do tema DEV.
