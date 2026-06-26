# Approval packet — Coleção Nike Mind 001/002 dev

Data: 2026-05-31
Tema dev: `155065450718`
Tema produção/main: `155065417950` — não alterado neste pacote.
URL dev/preview: https://www.lksneakers.com.br/collections/nike-mind-001?preview_theme_id=155065450718&lkqa=dev-final-collection-mind

## Escopo aplicado no dev theme

- H1 visual da coleção ajustado para `Nike Mind 001/002`.
- Breadcrumb visual ajustado para `Nike Mind 001/002`.
- Bloco editorial superior no padrão `lk-collection-v2` / `lk-204l-coll-preview` já presente e validado.
- Guia pós-grid `Guia editorial LK` presente no padrão `lk-guide-standard-panel--nike-mind-redo`.
- FAQ consolidado dentro do guia; legacy `.coll-faq` ausente no preview dev.
- CTA do guia pós-grid agora aponta para a página publicada: `/pages/guia-nike-mind-001-002`.
- FAQPage JSON-LD único validado no DOM renderizado.

## Verificação DOM — dev preview

- `h1`: `Nike Mind 001/002`
- `collectionV2`: true
- `afterGridGuide`: true
- `legacyFaq`: false
- `faqPageCount`: 1
- `linksToStandaloneGuide`: `https://lksneakers.com.br/pages/guia-nike-mind-001-002`
- Produtos: `18 itens`

## Evidência visual

- Topo/hero desktop: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_58d83f13ea17431f8b914cdd6937b681.png`
- Guia pós-grid desktop: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_d9cbc379a2cd436f88d73067aa1f2620.png`

## Receipts / rollback

- Snippet dev final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-collection-dev-snippet-final-20260531T131117Z/receipt.json`
- Tentativa de section dev com backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-theme/nike-mind-collection-dev-h1-guide-link-20260531T131012Z/receipt.json`

Rollback dev: restaurar o backup do snippet/section via Shopify Admin Asset API no tema dev.

## Ponto técnico

O ajuste de H1 no dev foi validado no DOM renderizado. O snippet do guia contém o ajuste runtime para H1/breadcrumb porque a escrita direta de `sections/lk-collection.liquid` sofreu readback inconsistente imediato na API. Para produção, o ideal é aplicar como patch limpo no asset/collection source e validar readback + storefront antes de considerar publicado.

## Aprovação necessária para produção

Para publicar em produção/main, aplicar apenas o delta escopado em `theme_id=155065417950`:

1. link/CTA do guia pós-grid para `/pages/guia-nike-mind-001-002`;
2. consolidação do guia/FAQ sem `.coll-faq` legado;
3. H1 visual `Nike Mind 001/002` ou update controlado do título/SEO da coleção, se aprovado.

Risco: baixo/médio — altera superfície pública de coleção e schema FAQ. Rollback direto por backup de asset.
