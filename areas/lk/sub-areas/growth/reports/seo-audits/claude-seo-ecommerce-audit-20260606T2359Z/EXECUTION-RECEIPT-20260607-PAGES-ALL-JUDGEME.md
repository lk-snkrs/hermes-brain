# Execution Receipt — Pages SEO all + Judge.me

Data: 2026-06-07 UTC  
Aprovação: Lucas perguntou “O item 4, não deveríamos fazer em todos? Vamos corrigir o judgeme?” — execução iniciada em produção com rollback.

## 1. Shopify Pages SEO — expandido para todas as páginas problemáticas

- Sitemap auditado: 59 URLs `/pages/`.
- Páginas com title/meta ausente, longo ou inconsistente: 33.
- Metafields aplicados via GraphQL: 33/33 OK.
- Campos usados:
  - `global.title_tag`
  - `global.description_tag`

## Readback

- Admin/GraphQL: 33/33 metafields OK.
- Readback público imediato:
  - title OK: 23/33
  - description OK: 22/33
- Observação: 11 páginas ainda serviram HTML/cache antigo no readback público imediato, mas o Admin/GraphQL confirma os metafields corretos. Revalidar após cache Shopify/Cloudflare expirar.

Artefatos:

- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/judgeme-pages-all-20260607T011306Z/page_metas_all.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/judgeme-pages-all-20260607T011306Z/page_metafields_all_set_results.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/judgeme-pages-all-20260607T011306Z/page_metas_all_public_readback.json`
- `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/judgeme-pages-all-20260607T011306Z/bad_page_metafields_graphql_readback.json`

## 2. Judge.me — correção aplicada

Diagnóstico:

- Warning vinha junto de `https://cdn.judge.me/widget_preloader.js`.
- O tema tinha um preloader legado no `layout/theme.liquid` antes do app block moderno do Judge.me.
- O Judge.me Core app block / extension loader já está ativo e deve ser a fonte principal.

Write:

- Asset: `layout/theme.liquid`
- Removido:
  - `<script src="https://cdn.judge.me/widget_preloader.js" data-shop-domain="{ shop.permanent_domain }" defer></script>`
- Mantido:
  - Judge.me Core app block
  - extension loader `judgeme-556/assets/loader.js`
  - widgets de badge/reviews no PDP

Readback Admin:

- Asset search após patch: nenhum `widget_preloader.js` restante em assets do tema.
- ScriptTags Shopify: nenhum script estático Judge.me ou ET removido indevidamente; só permanecem quickadd e recovery beacon.

Readback público imediato:

- PDP ainda serviu `widget_preloader.js` em uma verificação, apesar do asset já não conter o script. Indica cache/HTML antigo.
- Widget ainda aparece com `9 avaliações`.

Rollback:

- Restaurar `/opt/data/profiles/lk-growth/tmp/seo-audit-20260606/judgeme-pages-all-20260607T011306Z/before__layout__theme_judgeme_preloader.liquid`.

## Pendência

Revalidar em 30–60 min:

- páginas que ainda mostraram cache antigo;
- PDP Judge.me sem `widget_preloader.js` e sem warning `missing jdgm key`.
