# Receipt — LK PDP FAQ/schema parity patch — 2026-06-19

- Escopo: `sections/lk-pdp.liquid` no tema production.
- Regra nova: se `custom.faq` existir, FAQ visual e JSON-LD usam somente FAQ do produto; FAQ institucional vira fallback.
- Sem alteração em preço, estoque, produto, campanha ou checkout.
- Backup before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-faq-schema-fix-20260619/theme-backup/lk-pdp.before.20260619T202707Z.liquid`
- Rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/nike-mind-001-faq-schema-fix-20260619/rollback-theme-lk-pdp-faq-schema-20260619T202707Z.json`

## Asset readback
- visual_else_added: `False`
- schema_sd07: `False`
- schema_forloop_last: `True`
- generic_fallback_only: `False`