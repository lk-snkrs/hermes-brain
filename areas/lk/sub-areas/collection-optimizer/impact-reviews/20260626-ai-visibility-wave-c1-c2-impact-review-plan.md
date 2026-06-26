# Impact review plan — AI Visibility / LKGOC Onda C1+C2

Criado em UTC: 2026-06-19T13:42:22.791654+00:00
Revisar em: D+7 (~20260626)
Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260619T134029Z-ai-visibility-wave-c1-c2-published`

## Coleções publicadas
- `/collections/adidas-handball-spezial`
- `/collections/new-balance-204l`
- `/collections/onitsuka-tiger-mexico-66`
- `/collections/new-balance-1906l`
- `/collections/alo-yoga-1`
- `/collections/air-jordan-1-low`

## Métricas a revisar
- GSC: impressões, cliques, CTR e posição por URL/queries principais.
- GA4: sessões, add-to-cart e eventos por collection page.
- Shopify: pedidos, unidades e receita por produtos pertencentes às coleções.
- AI visibility/readback: presença em `/llms.txt` e `/agents.md`; ausência de promessa pública de estoque/preço/prazo.
- Snippet/SEO: title/meta indexado quando disponível.

## Rollback
Usar `backup-before.json` do receipt para restaurar `descriptionHtml` e SEO; templates públicos podem ser restaurados pelos arquivos `*.before.txt` e `templates__llms.txt.liquid.before-fix-c1c2.txt`.
