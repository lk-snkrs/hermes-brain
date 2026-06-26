# Receipt — unpublish Online Store collection backup

- Timestamp UTC: 20260617T105125Z
- Collection: `/collections/samba-duplicata-backup-20260616`
- Collection ID: `gid://shopify/Collection/424590213342`
- Action: removed publication only from `Online Store`.
- Scope respected: no product, price, stock, feed, campaign or theme changes.
- Backup JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-collections/20260617T105125Z-samba-duplicata-backup-20260616-unpublish-online-store.json`

## QA
- Admin GraphQL: `publishedOnPublication(Online Store)=false`.
- Resource publications no longer include `Online Store`; other channels remain as previously listed.
- Product count unchanged: 95.
- Public cache-busted URL returned HTTP 404; title not present.

## Rollback
- Re-publish same collection ID to original Online Store publication ID using `publishablePublish`.
- Collection ID: `gid://shopify/Collection/424590213342`
- Online Store publication ID: `gid://shopify/Publication/79413379294`
- Original publishDate: `2024-01-18T16:28:16Z`
