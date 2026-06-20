# Receipt — Pacote B CTR Produtos — 2026-06-19

- Escopo aplicado: 4 PDPs do Pacote B.
- Onitsuka collection: não alterada neste passo; permanece em QA de propagação.
- Segredos: não impressos (`values_printed=false`).
- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/shopify-backups`
- Rollback payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/growth-commercial-ctr-package-b-20260619/rollback-package-b-20260619T194435Z.json`

## Readback Admin
- `slide-nike-mind-001-light-smoke-grey-cinza`: SEO title OK `True`, meta OK `True`, FAQ/body marker OK `True`
- `slide-nike-mind-001-pearl-pink-rosa`: SEO title OK `True`, meta OK `True`, FAQ/body marker OK `True`
- `tenis-nike-vomero-premium-white-bright-crimson-branco`: SEO title OK `True`, meta OK `True`, FAQ/body marker OK `True`
- `tenis-nike-dunk-low-cacao-wow-marrom`: SEO title OK `True`, meta OK `True`, FAQ/body marker OK `True`

## Readback público inicial
- `slide-nike-mind-001-light-smoke-grey-cinza`: HTTP `200`, title OK `True`, meta OK `True`, FAQ público `True`, cache `DYNAMIC`
- `slide-nike-mind-001-pearl-pink-rosa`: HTTP `200`, title OK `True`, meta OK `True`, FAQ público `False`, cache `DYNAMIC`
- `tenis-nike-vomero-premium-white-bright-crimson-branco`: HTTP `200`, title OK `False`, meta OK `False`, FAQ público `False`, cache `DYNAMIC`
- `tenis-nike-dunk-low-cacao-wow-marrom`: HTTP `200`, title OK `True`, meta OK `True`, FAQ público `False`, cache `DYNAMIC`

## QA de propagação público

- Status: Admin API confirma 4/4; storefront público oscilou entre versão antiga e nova em múltiplas amostras, indicando propagação/cache por réplica.
- `slide-nike-mind-001-light-smoke-grey-cinza`: title novo visto em `5/5` amostras; FAQ novo visto em `1/5` amostras; último title OK `True`; último FAQ visto `False`.
- `slide-nike-mind-001-pearl-pink-rosa`: title novo visto em `5/5` amostras; FAQ novo visto em `1/5` amostras; último title OK `True`; último FAQ visto `True`.
- `tenis-nike-vomero-premium-white-bright-crimson-branco`: title novo visto em `2/5` amostras; FAQ novo visto em `2/5` amostras; último title OK `False`; último FAQ visto `False`.
- `tenis-nike-dunk-low-cacao-wow-marrom`: title novo visto em `4/5` amostras; FAQ novo visto em `2/5` amostras; último title OK `True`; último FAQ visto `False`.

## Revisão de impacto

- Due: 2026-06-26.
- Comparar GSC CTR/query-page, GA4 organic PDP sessions e Shopify/CRO signals.
