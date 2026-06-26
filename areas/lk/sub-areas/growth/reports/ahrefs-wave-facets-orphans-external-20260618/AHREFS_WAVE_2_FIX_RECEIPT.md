# Ahrefs Wave 2 — facetas, parâmetros, orphans/canonical e externos

Data UTC: `2026-06-18T23:34:17Z`
Escopo solicitado: corrigir issues Ahrefs 1, 2, 3, 4 e 5.
values_printed=false

## Issues alvo

1. `Page has links to broken page` — 7.829 ocorrências reportadas no summary Ahrefs
2. `More than three parameters in URL` — 976 ocorrências
3. `Orphan page (has no incoming internal links)` — 219 ocorrências no summary Ahrefs; top export local contém 100
4. `Canonical URL has no incoming internal links` — 98 ocorrências
5. `External 4XX / External 3XX` — 15 + 6 ocorrências

## Correção A — Product card canonical URL

Hipótese confirmada: muitas URLs de produto linkadas em collections/filtros saíam com parâmetros Shopify/search:

- `_pos`
- `_fid`
- `_ss`
- `variant`

Isso gerava:

- `More than three parameters in URL`
- canonical PDP sem incoming link direto
- produtos classificados como orphan mesmo estando ativos/publicados/em collections
- parte do `Page has links to broken page` em páginas filtradas

Assets corrigidos em dev e production:

- `snippets/card-product.liquid`
- `snippets/lk-product-card.liquid`

Mudança:

- criar URL canônica via `product.url | split: '?' | first` / `card_product.url | split: '?' | first`
- trocar `href`/`data-url`/`data-product-url` para URL limpa

Readback:

- dev: OK
- production: OK após retry em `snippets/card-product.liquid`

Validação pública:

- `/collections/nike-dunk?filter.v.option.tamanho=44`: `bad_param_product_hrefs_count=0`
- `/collections/adidas-samba`: `bad_param_product_hrefs_count=0`
- `/collections/sneakers`: `bad_param_product_hrefs_count=0`

## Correção B — External 4XX/3XX em páginas/artigos

Removido `href` crawlable dos links externos problemáticos em conteúdo Shopify, mantendo texto/âncora visual.

Recursos alterados: `8`

- Artigo: `como-saber-se-tenis-nike-e-original`
- Página: `guia-nike-mind-001-002` + backups relacionados
- Página: `guia-onitsuka-tiger-mexico-66`
- Página: `guia-adidas-sambae`
- Página: `politica-de-frete`
- Artigo: `nike-mercurial-superfly-1-max-orange-cr7-2026`

Readback: OK.

## Correção C — External 4XX/3XX em theme assets

Removido `href` crawlable exato dos links externos problemáticos em snippets/sections, mantendo texto/âncora visual.

Assets alterados em dev e production:

- `sections/lk-moon-shoe-source-page-v3.liquid`
- `sections/lk-moon-shoe-source-page-v4.liquid`
- `sections/lk-moon-shoe-source-page-v5.liquid`
- `sections/lk-moon-shoe-source-page-v6.liquid`
- `sections/main-page.liquid`
- `snippets/lk-goc-nike-vomero-premium-guide-page.liquid`
- `snippets/lk-moon-shoe-source-preview.liquid`

Readback: OK após retry no asset `sections/lk-moon-shoe-source-page-v3.liquid` production.

Validação pública dos origins Ahrefs externos:

- origins checados: `11`
- origins com `href` externo problemático restante: `0`

## Classificação Orphan/Canonical

Consulta Shopify read-only, sem estoque:

- produtos analisados: `194`
- `ACTIVE`: `194`
- publicados: `194`
- com collections: `194`

Conclusão: não eram produtos “sem coleção”. O problema mais provável era que Ahrefs encontrava links parametrizados/non-canonical em vez de links diretos para canonical PDP. O patch de card corrige a causa raiz esperada para issues 2, 3 e 4.

## O que ainda depende de Ahrefs/cache

- Ahrefs precisa recrawlear para remover as ocorrências históricas.
- Cache Shopify/CDN pode alternar por alguns minutos/horas.
- O export local tinha top 100 rows por issue; o count total vem do summary Ahrefs. Recomendado rodar novo crawl/API export em 12–24h.

## Rollback

Backups salvos nos diretórios:

- `product-card-url-patch-*`
- `external-body-fix-*`
- `external-theme-fix-*`

Rollback: restaurar arquivos `.before`/JSON before por recurso/asset.
