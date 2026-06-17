# Receipt — Collection SEO/GEO New Balance 9060

Executado em: 2026-06-16T19:48:51.833318+00:00

## Status
- Aprovação recebida: sim, no turno atual.
- Collection production alterada: `new-balance-9060`.
- Campos alterados: `descriptionHtml`, `seo.title`, `seo.description`.
- Theme/feed/produtos/preço/estoque/campanhas/Klaviyo: não alterados.
- Secrets: não impressos (`values_printed=false`).

## QA Admin
- SEO title/meta: OK.
- Description nova: OK; Shopify normalizou HTML, por isso match literal não é usado como bloqueio.
- Termos operacionais proibidos na descrição/SEO da coleção: 0.

## QA público
- URL normal já mostra texto novo e FAQ novo.
- Cache-buster ainda serviu versão antiga em uma tentativa; tratar como propagação/cache.
- Ainda aparecem `frete grátis`/`10x sem juros` em blocos globais da página, fora do texto da coleção.

## Evidência
- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/backup-before.json`
- Apply result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/apply-result.json`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/readback-after.json`
- Readback QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/readback-qa.json`
- Public QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/public-cache-recheck.json`
- Rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/collection-seo-geo-new-balance-9060-20260616/apply-20260616T194640Z/rollback_collection_9060_from_backup.py`

## Rollback
Rollback preparado a partir do backup anterior. Executar somente com aprovação explícita ou falha crítica.

## Próximo controle
Recheck D0/D1 da coleção para confirmar cache 100% propagado e monitorar GSC/GA4 em ~7 dias.