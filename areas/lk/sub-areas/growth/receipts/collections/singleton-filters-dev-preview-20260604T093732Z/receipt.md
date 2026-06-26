# Singleton filters Dev preview

- PRD: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/prds/prd-collection-singleton-filters-20260604.md`
- Asset: `sections/lk-collection.liquid`
- Dev: `lk-new-theme/dev` `155065450718` role `unpublished`
- Production: `lk-new-theme/production` `155065417950` role `main`
- Rule: hide inactive list filters when `filter.values.size <= 1`; preserve active filters.
- Active href fix: use `value.url_to_remove` when active.
- Preview: https://lksneakers.com.br/collections/new-balance-9060?preview_theme_id=155065450718
- Rollback Dev: re-upload `dev_before.sections.lk-collection.liquid`.
- Non-actions: no Production, no products, no taxonomy/metafields, no price/stock/checkout/apps/campaigns.
