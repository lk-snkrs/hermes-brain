# Impact review plan — AI Visibility / LKGOC Ondas A+B

Criado em UTC: 2026-06-18T22:44:02Z
Revisar em: D+7 (~20260625)
Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260618T224252Z-ai-visibility-waves-a-b-published`

## Coleções publicadas
- `/collections/new-balance-9060`
- `/collections/new-balance-530`
- `/collections/alo-yoga-1`
- `/collections/air-jordan-1-low`
- `/collections/adidas-tokyo`
- `/collections/nike-air-rift`

## Métricas a revisar
- GSC: impressões, cliques, CTR e posição por URL/queries principais.
- GA4/Shopify: sessões por coleção, add-to-cart, checkout e receita assistida.
- AI visibility/readback: presença de bloco citável e ausência de promessa pública de estoque/prazo/preço.
- QA: snippets públicos, FAQ sem duplicidade, sem truncamento.

## Rollback
Usar `backup-before.json` do receipt para restaurar `body_html`; SEO pode ser restaurado via GraphQL `collectionUpdate` se necessário.
