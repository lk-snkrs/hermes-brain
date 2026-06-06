# Receipt Production — LKGOC P0 Nike x Jacquemus Moon Shoe SP

Data UTC: 2026-06-05T23:14:25.000921+00:00
Tema Production: `155065417950` (`main` verificado)
Tema DEV fonte: `155065450718` (`unpublished` verificado)
Collection: `nike-x-jacquemus-moon-shoe-sp`

## Aprovação

Lucas aprovou: “Aprovado PR e merge pra Production”.

## Assets promovidos DEV → Production

- `snippets/lk-goc-collection.liquid`
- `sections/lk-collection.liquid`
- `templates/collection.jacquemus-nike.json`
- `snippets/lk-goc-guide-contract.liquid`
- `snippets/lk-goc-title-headline-contract-v2.liquid`

Hotfix complementar durante QA Production:

- `snippets/lk-samba-204l-hero-v2.liquid`
- `snippets/lk-samba-204l-guide-v2.liquid`
- `snippets/lk-sambae-204l-hero.liquid`

Motivo: após merge da section, Production referenciava snippets Samba legados que existiam no DEV e não existiam no Production; QA detectou Liquid error em Adidas Samba. Snippets copiados do DEV para Production e erro resolvido.

## Backups / rollback

Backup principal pré-deploy:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/lkgoc-moon-shoe-p0-prod-deploy-20260605T225200Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/lkgoc-moon-shoe-p0-prod-deploy-continue-20260605T225227Z`

Backup hotfix snippets Samba:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/lkgoc-prod-missing-samba-snippets-20260605T231309Z`

Rollback: restaurar os `.prod.before` dos backups acima no tema Production `155065417950`.

## QA Production — Moon Shoe

Desktop live:

- Hero LKGOC: true
- Guide LKGOC: true
- Guide standard: true
- FAQ dentro do guia: visível
- Details visíveis fora do guia: 0
- FAQ legada visível fora do guia: 0
- Imagens hero: 3
- `object-position`: `50% 100%`, `50% 100%`, `50% 100%`
- Packshot/product-only no hero: false
- “Ler mais” desktop: oculto
- Delta imagens/breadcrumb: `0px`
- `.coll-rich-content`: false
- Liquid error: false
- Something went wrong: false

Mobile live:

- Hero LKGOC: true
- Guide LKGOC: true
- FAQ dentro do guia: visível
- Details visíveis fora do guia: 0
- Imagens hero: 3
- `object-position`: `50% 100%`, `50% 100%`, `50% 100%`
- Packshot/product-only no hero: false
- “Ler mais” mobile: visível
- Liquid error: false
- Something went wrong: false

## QA regressão coleções existentes

- `new-balance-204l`: hero true, guide true, Liquid error false, readmore desktop false
- `new-balance-9060`: hero true, guide true, Liquid error false, readmore desktop false
- `new-balance-530`: hero true, guide true, Liquid error false, readmore desktop false
- `onitsuka-tiger-mexico-66`: componente editorial legado `lk-next-coll-preview` presente; guide true; Liquid error false; readmore desktop false
- `adidas-samba`: após hotfix snippets, hero true, guide true, Liquid error false, readmore desktop false

## Escopo não alterado

Não foram alterados:

- produtos;
- preço;
- estoque;
- checkout;
- apps;
- GMC/feed;
- campanhas Google/Meta;
- Klaviyo;
- WhatsApp/e-mail.

## Revisão de impacto

Revisar impacto aproximado em: `2026-06-12`.

Métricas sugeridas:

- sessões da coleção;
- CTR orgânico/GSC se houver dados;
- PDP click-through da collection;
- add-to-cart rate;
- revenue e pedidos da família Moon Shoe;
- scroll/engajamento no guia quando disponível.
