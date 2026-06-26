# Final Receipt — Nike Mind SEO/GEO/schema production merge — 2026-06-09

Criado em: 2026-06-09 14:34 UTC

## Aprovação

Lucas: “pode fazer o merge..”

Interpretação: aprovação explícita atual para merge do preview DEV Nike Mind para production, mantendo o mesmo escopo aprovado e sem alterar produto/preço/estoque/GMC/campanhas.

## Escopo aplicado

Production theme:

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role verificado por API: `main`

Fonte DEV:

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado por API: `unpublished`

Arquivos production alterados:

- `snippets/lk-growth-nike-mind-seo-geo-preview.liquid`
- `layout/theme.liquid` — render condicional do snippet

Condição final:

- Render apenas quando `canonical_url contains '/collections/nike-mind-001'`.

## Conteúdo publicado

- Bloco citável Nike Mind 001.
- FAQ visível com 5 perguntas.
- JSON-LD `FAQPage` com paridade do FAQ.

## Readback / QA

Asset readback:

- Snippet contém bloco Nike Mind: OK.
- Snippet contém `FAQPage`: OK.
- Layout contém render marker: OK após marker fix.

Storefront público:

- URL: `https://lksneakers.com.br/collections/nike-mind-001`
- Bloco `Nike Mind 001: slide escultural`: OK.
- FAQ “O que o Nike Mind 001 faz?”: OK.
- Classe `lk-growth-nike-mind-geo`: OK.
- `FAQPage`: OK.
- `Liquid error`: false.
- Production theme detectado: OK.
- Dev theme detectado: false.

Evidência:

- `production-storefront-post-line-fix.json`
- `production-storefront-post-line-fix.html`
- `production_snippet.after-line-fix.liquid`
- `production_layout.after-marker-fix.liquid`

## Observação técnica

Durante o merge, o primeiro readback indicou que o snippet havia subido, mas o marker do layout não renderizava no storefront. Foi corrigido antes do fechamento:

1. `fix_layout_marker.py` confirmou marker no layout production.
2. `fix_snippet_line.py` corrigiu a condição Liquid para `canonical_url contains '/collections/nike-mind-001'` e removeu o if antigo que não renderizava no production layout.
3. Storefront público validado com cache buster e sem `Liquid error`.

## Fora do escopo / não alterado

- Shopify product data: 0.
- Collection Admin SEO title/meta/metafields: 0.
- Preço: 0.
- Estoque/disponibilidade: 0.
- GMC/feed: 0.
- Ads/Klaviyo/customer-facing outbound: 0.
- `llms.txt`/`agents.md` público: 0.

## Rollback

Arquivo:

- `ROLLBACK.md`

Backups:

- `production_layout.before.liquid`
- `production_snippet.before.liquid`
- `production_layout.before-marker-fix.liquid`
- `production_snippet.before-line-fix.liquid`

## Impact review

Revisar em D+7/D+14:

- GSC impressions/clicks/CTR para collection `/collections/nike-mind-001`.
- Queries: `nike mind 001`, `nike mind`, `nike mind 001 original`, `nike mind 001 vs 002`.
- GA4 orgânico da collection.
- HTML/schema público.
