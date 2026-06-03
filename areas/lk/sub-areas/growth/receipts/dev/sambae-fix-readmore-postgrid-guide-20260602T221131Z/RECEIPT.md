# Receipt — fix Sambae read-more and post-grid guide DEV

Data UTC: 2026-06-02T22:11:35Z
Tema DEV: 155065450718
Produção: não alterada.

## Correções
1. Incluído `adidas-sambae` no outer condition do bloco `lk-guide-standard-panel` pós-grid.
2. Corrigido botão `Ler mais` do hero Sambae para alternar expansão de texto e texto `Ler menos`.
3. Mantido padrão 204L: hero com `lk-204l-coll-preview`, guia via `lk_phase1_*` / `lk-guide-standard-panel`.

## QA
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "section_bytes": 260169,
  "under_256kb": true,
  "outer_condition_has_sambae": true,
  "sambae_phase_anchor_count": 1,
  "sambae_guide_h2_count": 1,
  "sambae_card_count": 1,
  "sambae_hero_count": 4,
  "readmore_fix_css": 1,
  "readmore_js_has_copy_toggle": true,
  "readmore_js_has_ler_menos": true,
  "old_wrong_snippet_refs": 0,
  "outer_condition_after": "{%- if collection.handle == 'adidas-sambae' or collection.handle == 'adidas-samba-jane' -%}"
}
```
