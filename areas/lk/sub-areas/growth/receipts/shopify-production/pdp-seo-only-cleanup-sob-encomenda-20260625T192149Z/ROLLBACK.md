# Rollback — PDP SEO-only cleanup — 20260625T192149Z

Fonte de backup:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/production-apply/backup-before.json`

Procedimento:
1. Para cada handle, restaurar via Shopify Admin API somente:
   - `product.body_html` do backup;
   - metafields `global.title_tag` e `global.description_tag` do backup.
2. Não tocar preço, estoque, variants, images, tags, collections, GMC, Klaviyo, campanhas, checkout ou tema.
3. Readback Admin + público após rollback.
