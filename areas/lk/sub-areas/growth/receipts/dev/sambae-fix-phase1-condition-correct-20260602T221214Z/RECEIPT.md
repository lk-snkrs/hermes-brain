# Receipt — correct Sambae phase1 condition DEV

Data UTC: 2026-06-02T22:12:18Z
Tema DEV: 155065450718
Produção: não alterada.

Correção: `adidas-sambae` removido do branch interno Samba Jane e incluído no if externo do bloco phase1 pós-grid.

QA:
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "section_bytes": 260169,
  "under_256kb": true,
  "outer_condition_has_sambae": true,
  "inner_first_condition_exact_samba_jane": true,
  "sambae_has_own_elsif_assignment": true,
  "sambae_assignment_after_samba_jane": true,
  "sambae_phase_anchor_count": 1,
  "sambae_guide_h2_count": 1,
  "sambae_card_count": 1,
  "readmore_js_has_copy_toggle": true,
  "old_wrong_snippet_refs": 0,
  "outer_condition_after": "{%- if collection.handle == 'adidas-sambae' or collection.handle == 'nike-mind-001' -%}"
}
```
