# Emergency rollback — Sambae wrong preview DEV

Data UTC: 2026-06-02T22:20:23Z
Tema DEV: 155065450718
Produção: não alterada.

Motivo: implementação Sambae em DEV continuou errada visualmente. Rollback para backup limpo pré-Sambae.

Fonte rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/dev/sambae-204l-strict-apply-compact-20260602T220352Z/section.before.liquid`

QA:
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "rollback_source": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/dev/sambae-204l-strict-apply-compact-20260602T220352Z/section.before.liquid",
  "section_bytes": 253948,
  "under_256kb": true,
  "sambae_strict_hero_markers": 0,
  "sambae_guide_markers": 0,
  "sambae_wrong_snippet_refs": 0,
  "restored_equals_backup": true
}
```
