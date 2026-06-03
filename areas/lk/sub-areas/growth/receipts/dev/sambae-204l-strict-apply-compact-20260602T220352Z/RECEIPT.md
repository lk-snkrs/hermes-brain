# Receipt — Sambae strict 204L clone compact DEV

Data UTC: 2026-06-02T22:03:57Z
Tema DEV: 155065450718
Produção: não alterada.

Aplicado no mesmo padrão estrutural 204L:
- hero/editorial reutiliza classes `lk-204l-coll-preview`;
- guia entra em `lk_phase1_*` / `lk-guide-standard-panel`;
- sem snippets soltos antigos;
- section abaixo de 256 KB.

QA:
```json
{
  "theme_id": "155065450718",
  "section_bytes": 258271,
  "under_256kb": true,
  "sambae_hero_class_count": 1,
  "sambae_uses_204l_class_count": 1,
  "sambae_phase_anchor_count": 1,
  "sambae_guide_h2_count": 1,
  "sambae_card_count": 0,
  "old_bad_snippet_render_hero": 0,
  "old_bad_snippet_render_guide": 0,
  "pattern_markers": {
    "hero_204l_class_reuse": true,
    "phase1_system": true,
    "guide_standard_card_wide": true,
    "same_read_more_class": true
  }
}
```
