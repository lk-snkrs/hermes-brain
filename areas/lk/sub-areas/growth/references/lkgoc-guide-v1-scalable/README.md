# LKGOC Guide v1 — padrão escalável

Registrado em: 2026-06-03T18:45:54.686647+00:00

## Fonte aprovada
- DEV theme: `lk-new-theme/dev` (`155065450718`, role `unpublished`)
- Section: `sections/lk-goc-guide-v1.liquid`
- Template exemplo: `templates/page.nb204l-guide.json`
- Preview validado: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk?preview_theme_id=155065450718&lkgoc_qa=804160

## O que mudou
O guia 204L deixou de ser uma página hardcoded `lk-source-page--nb204l` e virou um componente reutilizável com namespace `lk-goc-guide-*`.

## Estrutura escalável
- Settings para hero, CTAs, blocos de texto, sizing, produtos, FAQ e CTA final.
- Blocks JSON para:
  - `table_row`
  - `style_card`
  - `media_card`
  - `product_card`
  - `faq`
- FAQ visual e FAQ JSON-LD são gerados da mesma fonte de blocks `faq`.
- Mobile 2 colunas para style cards, sinais editoriais, produtos e FAQ.

## Guardrails
- Copiar/adaptar; não reinventar layout.
- Trabalhar em DEV/unpublished.
- Production só após approval explícito de Lucas.
- Para novas páginas, usar este componente e trocar apenas conteúdo, imagens, links, produtos e FAQ.

## Estado
- Production não tocada nesta transformação.
- DEV renderiza o novo componente.
- JSON template readback é semanticamente igual ao candidato; Shopify normalizou formatação.


## Production promotion — 2026-06-03T18:55:00.643201+00:00

Lucas aprovou explicitamente o padrão: “aprovado !! FICOU OTIMO!! AGORA ESTA 100% O PADRAO DO GUIA!!”.

Publicado em Production:
- Theme: `lk-new-theme/production` (`155065417950`, role `main`)
- Section: `sections/lk-goc-guide-v1.liquid`
- Template: `templates/page.nb204l-guide.json`
- URL pública: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk

QA Production:
- 6/6 chamadas públicas 200
- `data-lkgoc-guide="v1"` presente
- namespace `lk-goc-guide-*` presente
- mobile 2 colunas presente
- produto com `aspect-ratio:auto!important`
- FAQ schema presente com 6 perguntas
- sem `Liquid error`
- sem `imagem pendente`

Receipt:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production-approved/lkgoc-guide-v1-merge-dev-to-production-20260603T185425Z/RECEIPT.json`

Arquivos gold source finais:
- `lk-goc-guide-v1.production-gold.liquid`
- `page.nb204l-guide.production-gold.json`
