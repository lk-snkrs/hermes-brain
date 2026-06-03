# Receipt — 204L DEV guide spacing fix

Data UTC: 2026-06-03T00:12:19Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Correção
Adicionada regra CSS escopada para `collection.handle == 'new-balance-204l'` criando respiro entre o final do grid e o Guia LK.

Regra aplicada:
```css
#lk-guia-new-balance-204l.lk-guide-standard-panel { margin-top: clamp(56px,6vw,88px)!important; }
@media(max-width:989px) { #lk-guia-new-balance-204l.lk-guide-standard-panel { margin-top:42px!important; } }
```

## QA
```json
{
  "readback": {
    "readback_bytes": 257213,
    "readback_spacing_marker_count": 1,
    "readback_spacing_rule_count": 3,
    "under_262144": true
  },
  "render": {
    "url": "https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&qa=204l-spacing-final",
    "status": 200,
    "final_url": "https://lksneakers.com.br/collections/new-balance-204l?qa=204l-spacing-final",
    "bytes": 583472,
    "counts": {
      "LK DEV fix — 204L post-grid spacing before LK guide": 1,
      "#lk-guia-new-balance-204l.lk-guide-standard-panel": 4,
      "lk-guia-new-balance-204l": 59,
      "lk-lkgoc-coll-preview": 3,
      "New Balance 204L: perfil baixo": 1
    }
  },
  "screenshot": {
    "exists": true,
    "bytes": 759925
  }
}
```

## Rollback
Reaplicar `section.before.liquid` no asset `sections/lk-collection.liquid` do tema DEV.
