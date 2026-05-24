# LK GMC — Preview residual deduplicado sem write

Gerado em: `2026-05-15T20:13:30Z`
Status: `preview_only_no_write`

## Veredito

Preview residual GMC refeito em modo read-only. O residual separa preço/strikethrough de landing/crawl e mantém preço bloqueado para aprovação específica, porque altera sinal comercial no Merchant.

## Fonte

- Base residual: `reports/lk-gmc-2026-05-14-residual-triage-current.json`
- Preview preço: `reports/lk-gmc-2026-05-14-post-gtin-price-updated-preview.md`
- Drilldown landing/crawl: `reports/lk-gmc-2026-05-14-landing-page-current-drilldown.md`

## Preço / strikethrough

- Productstatuses lidos: `23.277`
- Produtos online com `price_updated` ou `strikethrough_price_updated`: `310`
- Candidatos price-only contra preço atual Shopify: `42`
- Em revisão promocional/compare-at/strikethrough: `268`

Decisão recomendada:

1. Não aplicar `strikethrough_price_updated` agora.
2. Se Lucas aprovar, fazer apenas piloto price-only dos 42 produtos candidatos, com snapshot/rollback e verificação posterior.
3. Antes do write, confirmar governança Google & YouTube/Shopify/Merchant porque preço pode estar stale por upstream/source ownership.

## Landing / crawl

- Produtos com `landing_page_error`: `22`
- Shopify DRAFT + public 404/.js 404: `20`
- Public 200 + `.js` 200 + Shopify ACTIVE: `2`

Decisão recomendada:

1. Os 2 com public 200 devem ficar em monitor/reprocessamento, sem delete/suppress.
2. Os 20 DRAFT/404 podem virar pacote exato de supressão/delete no Merchant, mas só com aprovação específica por IDs e rollback.
3. Não publicar Shopify automaticamente para resolver Merchant.

## O que não foi feito

- Merchant write
- ProductInputs patch
- Content API upsert/delete
- Shopify write
- Tiny write
- feed fetch/upload
- salePrice/strikethrough update
- local/LIA change
- campaign/message/send
- supplier/customer contact

## Próximo gate

`gmc-governance-next-decision` continua bloqueando preço: antes de qualquer patch de preço, precisa checklist UI/manual Google & YouTube/Shopify/Merchant e pacote exato aprovado.
