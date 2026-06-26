# LK Growth — Pacote B CTR Produtos — Execution summary — 2026-06-19

- Approval: `Aprovado Pacote B CTR produtos`
- Execution UTC: `2026-06-19T19:24:31.628492+00:00`
- Scope: Shopify production product SEO title/meta + FAQ/body block on 4 PDPs.
- Stock/price/variants/campaigns: not queried, not changed.
- Production write: completed.
- Admin readback: passed for all 4 products.
- Public storefront QA: passed for all 4 products after propagation interval.
- H1 QA: 1 H1 on all 4 PDPs.

## Products updated

1. `slide-nike-mind-001-light-smoke-grey-cinza`
   - Public title OK: `Nike Mind 001 Light Smoke Grey Original | LK Sneakers`
   - Meta OK
   - FAQ/body block OK

2. `slide-nike-mind-001-pearl-pink-rosa`
   - Public title OK: `Nike Mind 001 Pearl Pink Original | LK Sneakers`
   - Meta OK
   - FAQ/body block OK

3. `tenis-nike-vomero-premium-white-bright-crimson-branco`
   - Public title OK: `Nike Vomero Premium White Bright Crimson Original | LK`
   - Meta OK
   - FAQ/body block OK

4. `tenis-nike-dunk-low-cacao-wow-marrom`
   - Public title OK: `Nike Dunk Low Cacao Wow Original | LK Sneakers`
   - Meta OK
   - FAQ/body block OK

## Evidence files

- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/PACKAGE_B_APPROVAL_PACKET.md`
- Shopify write receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/package-b-shopify-write-receipt.json`
- Admin readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/package-b-admin-readback-after-write.json`
- Public QA final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/package-b-public-final-qa.json`
- Backup before write: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/package-b-shopify-backup-before.json`
- Rollback script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/rollback_package_b.py`

## Rollback

Run with Doppler-injected Shopify env if rollback is needed:

```bash
/opt/data/scripts/hermes_doppler.py --project lc-keys --config prd run -- python3 /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/rollback_package_b.py
```

## Impact review

Target review window: around `2026-06-26`.

Metrics to compare vs baseline:
- GSC: clicks, impressions, CTR, average position for each URL/query pair.
- GA4/Shopify: PDP sessions, add-to-cart, checkout starts, revenue attributed/assisted where available.
- SEMrush: title/meta crawl reflection and any new warnings.
