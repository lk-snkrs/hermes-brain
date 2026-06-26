# Receipt — LKGOC New Balance 9060 Full DEV preview

Data UTC: 2026-06-05T09:42:31Z

## Escopo aprovado
Lucas aprovou materializar o preview em Shopify DEV/unpublished para New Balance 9060 Full LKGOC, sem tocar produção.

## Theme alvo verificado
- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role verificado por API: `unpublished`
- Produção/main: não alterada.

## Writes executados
Somente em Shopify DEV/unpublished + página Shopify não publicada para shell de guia.

Assets DEV:
- `snippets/lk-goc-new-balance-9060.liquid`
- `sections/lk-collection.liquid` — hook/render do snippet + desc override 9060.
- `sections/lk-goc-new-balance-9060-guide-page.liquid`
- `templates/page.new-balance-9060-guia-lkgoc.json`
- `sections/main-page.liquid` — hook condicional para handle do guia.
- `layout/theme.liquid` — dedupe DEV: removida duplicação de body/content_for_layout que estava fazendo a página renderizar duas vezes no DEV preview.

Shopify page:
- Handle: `new-balance-9060-original-brasil-guia-lk`
- Status: não publicada (`published: false`)
- Observação: por estar não publicada, URL pública do guia retorna 404. Correto para não expor produção antes de approval.

## Preview coleção
- URL DEV preview: `https://lksneakers.com.br/collections/new-balance-9060?preview_theme_id=155065450718`

## QA executado
Playwright desktop/mobile:
- Desktop: 1 main, 1 banner, 1 guia, 0 menções antigas de prazo/estoque.
- Mobile: 1 main, 1 banner, 1 guia, 0 menções antigas de prazo/estoque.

Screenshots:
- `shopify-dev-preview/qa/nb9060-desktop-v2.png`
- `shopify-dev-preview/qa/nb9060-mobile-v2.png`

Fetch/readback textual:
- Hero novo aparece.
- Guia Editorial LK aparece pós-grid.
- FAQ antigo com “Qual o prazo de entrega” e “Produtos em estoque” removido do preview DEV via desc override/theme, sem alterar a descrição global da coleção em produção.

## Backups/rollback
Backups locais:
- `shopify-dev-preview/20260605T093600Z/`
- `shopify-dev-preview/20260605T093733Z/`
- `shopify-dev-preview/20260605T094110Z/`

Rollback DEV:
- Restaurar `layout/theme.liquid` e `sections/lk-collection.liquid` a partir dos `.before` correspondentes.
- Remover/ignorar snippet/section/template novos se necessário.
- Remover página não publicada `new-balance-9060-original-brasil-guia-lk` se Lucas decidir descartar.

## Scorecard DEV
Score atual: 86/100.

Ganhou pontos por:
- padrão LKGOC aplicado em DEV/unpublished;
- role verificado por API;
- readback de assets;
- QA desktop/mobile;
- remoção do FAQ antigo com linguagem operacional inadequada no preview;
- rollback local existente.

Pendências para >90:
- QA visual humano do Lucas no link/screenshot;
- eventual publicação do guia dedicado em produção após approval;
- revisão de impacto pós-produção com GSC/GA4/Shopify.

## Guardrails
- Nenhum write em tema production/main.
- Nenhum SEO field/descrição global visível em produção alterado.
- Nenhum GMC/feed/campanha/Klaviyo/preço/estoque tocado.
