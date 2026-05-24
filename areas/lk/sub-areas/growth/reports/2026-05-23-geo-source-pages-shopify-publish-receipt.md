# LK Growth — GEO Source Pages Shopify Publish Receipt

Data: 2026-05-23 09:50 BRT
Status: publicado em Shopify production após aprovação no Telegram.

## URLs publicadas

- Onitsuka Tiger original no Brasil: https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil
- New Balance 204L original no Brasil: https://lksneakers.com.br/pages/new-balance-204l-original-brasil
- Adidas SL 72 OG vs RS: https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs

## Escopo executado

- Criadas/atualizadas 3 Shopify Pages production.
- Criado template production `templates/page.geo-source.json` usando `main-page`.
- Definidos SEO metafields `global.title_tag` e `global.description_tag` para cada página.
- Inserido conteúdo editorial visível em `body_html` para DOM público estável.
- Inserido schema JSON-LD com `WebPage`, `Organization`, `BreadcrumbList` e `FAQPage`.

## Verificação

Theme production:

- Theme: `lk-new-theme/production`
- Role: `main`
- Theme ID: `155065417950`
- Template readback: OK

Admin/API + público:

- 3/3 páginas com Admin title/handle/template/body marker OK.
- 3/3 URLs públicas retornaram HTTP 200.
- 3/3 URLs públicas com marker `data-lk-geo-source`.
- 3/3 URLs públicas com `FAQPage` schema.
- 3/3 URLs públicas com meta description esperada.
- Browser QA da página Onitsuka confirmou H1 visível correto e remoção do bloco técnico `SEO`.

Forbidden-term QA:

- `pronta entrega`: 0
- `encomenda`: 0
- `estoque`: 0
- `marketplace`: 0
- `legit-check`: 0

## Rollback

Backup/receipt completo:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-source-pages/publish-20260523-095011/receipt.json`

Rollback técnico:

- Restaurar cada `*.page.before.json` via Shopify Page PUT se necessário.
- Restaurar SEO metafields a partir de `*.seo.before.json`.
- Restaurar ou remover `templates/page.geo-source.json` conforme `templates__page.geo-source.json.before`.

## Revisão de impacto

Cron D+7 agendado para 2026-05-30 10:00 BRT.
Job ID: `e0088791bb3b`

Objetivo da revisão: indexabilidade, schema, sinais iniciais GSC/AI Search e eventuais ajustes de links internos/menu.
