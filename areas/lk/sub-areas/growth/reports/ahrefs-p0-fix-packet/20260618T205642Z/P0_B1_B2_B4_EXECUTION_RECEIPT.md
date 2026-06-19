# P0 Execution Receipt — B1/B2/B4

Data UTC: `2026-06-18T22:26:27Z`
Execution dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-p0-fix-packet/20260618T205642Z/execution-B1-B2-B4-20260618T222244Z`
values_printed=false

## B1 — Links internos 404

Executado:

- Editados 7 recursos Shopify:
  - 5 artigos de blog.
  - 2 páginas.
- Backups salvos antes dos PUTs:
  - `article-*-before.json`
  - `page-*-before.json`
- Readback Admin dos recursos editados: `remaining_broken=0` em `body_html`.
- Também verificado `summary_html`: sem ocorrências dos paths antigos.

Recursos editados:

- Nude Project — 3 links trocados para `/collections/nude-project`.
- Fear of God Essentials — 3 links trocados para `/collections/fear-of-god-essentials`.
- Saint Studio — 2 links trocados para `/pages/saint-studio-guia`.
- Streetwear SP — `/collections/streetwear` trocado para `/collections/sneakers`.
- Autenticidade — 4 links de guias inexistentes trocados para collections públicas.
- Jordan SP — `/collections/cuidados` trocado para `/pages/autenticidade`.
- Lançamentos 2026 — `/newsletter` trocado para `/`.

Observação pública:

- Alguns requests públicos ainda mostram HTML antigo/cache para 2 blogs, mas o Admin readback está limpo.
- Isso deve ser tratado como cache/propagação Shopify até novo crawl; não há ocorrência restante no `body_html`/`summary_html` via Admin.

## B2 — Redirects seletivos

Executado:

- Criados 10 redirects seletivos para paths não-produto.
- Product paths foram pulados por segurança para evitar conflito com produtos draft/futuros.
- Readback Admin: OK para todos os 10 redirects.

Redirects criados:

- `/collections/streetwear` → `/collections/sneakers`
- `/pages/nike-x-jacquemus-moon-shoe-guia-lk` → `/collections/nike-x-jacquemus-moon-shoe-sp`
- `/pages/new-balance-9060-original-brasil-guia-lk` → `/collections/new-balance-9060`
- `/pages/new-balance-204l-original` → `/collections/new-balance-204l`
- `/pages/onitsuka-tiger-mexico-66-original` → `/collections/onitsuka-tiger-mexico-66`
- `/pages/air-jordan-travis-scott-original` → `/collections/air-jordan`
- `/collections/cuidados` → `/pages/autenticidade`
- `/newsletter` → `/`
- `/pages/new-balance-530-original-brasil-guia-lk` → `/collections/new-balance-530`
- `/pages/yeezy-original` → `/collections/yeezy`

## B4 — Judge.me production

Executado:

- Production theme `lk-new-theme/production` atualizado no asset `snippets/judgeme_widgets.liquid`.
- Patch aplicado: usa `lk_picture_src` com fallback `original`, `huge`, `compact`, `small` antes de renderizar `<img src>`.
- Backup salvo: `judgeme-prod-before.liquid`.
- Readback Admin production:
  - contém `lk_picture_src`: OK.
  - não contém padrão bruto `picture_url | escape`: OK.

Validação pública:

- `camiseta-jacquemus-the-typo-azul`: cachebuster limpo, `bad_markers=0`.
- `air-jordan-4-craft-medium-olive`: alterna entre HTML antigo e novo conforme cache variant; em cache novo, `bad_markers=0`; em cache antigo, ainda aparece `=&gt;`.
- Interpretação: patch aplicado corretamente no theme; há cache/propagação pública intermitente.

## Rollback

- B1: restaurar `body_html` dos backups `article-*-before.json` e `page-*-before.json`.
- B2: remover redirects pelos IDs em `receipt.json` / `final-readback.json`.
- B4: restaurar `judgeme-prod-before.liquid` no production theme.

## Próxima verificação recomendada

- Rechecar público/Ahrefs em 12–24h para confirmar expiração de cache e queda dos 404/broken image.
- Merchant Center Local segue em aberto aguardando validação do LK Stock/Simprosys.
