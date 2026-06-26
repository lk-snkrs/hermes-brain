# Receipt — LKGOC componente único em Production

Data: 2026-06-05T19:22:33
Aprovador: Lucas Cimino, Telegram: "aprovo".
Tema Production: `155065417950`, role verificado: `main`.
Tema DEV fonte: `155065450718`, role verificado: `unpublished`.

## Escopo publicado
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`

## Mudança
- Production migrou as coleções LKGOC para o componente genérico único `lk-goc-collection`.
- Corrige a arquitetura: não depender mais de snippets estruturais por coleção para 204L/9060/530/Mexico 66/Samba.
- Corrige a Samba em Production, que podia quebrar por chamadas a snippets ausentes.
- Mantém snippets antigos no tema sem referência ativa; não foram deletados neste deploy para reduzir risco de rollback.

## Coleções validadas ao vivo
- `new-balance-204l`: Liquid error `False`, hero `True`, guide `True`, legacy `.coll-rich-content` `False`, Ler mais desktop visível `False`, deltaTop `0px`.
- `new-balance-9060`: Liquid error `False`, hero `True`, guide `True`, legacy `.coll-rich-content` `False`, Ler mais desktop visível `False`, deltaTop `0px`.
- `new-balance-530`: Liquid error `False`, hero `True`, guide `True`, legacy `.coll-rich-content` `False`, Ler mais desktop visível `False`, deltaTop `0px`.
- `onitsuka-tiger-mexico-66`: Liquid error `False`, hero `True`, guide `True`, legacy `.coll-rich-content` `False`, Ler mais desktop visível `False`, deltaTop `0px`.
- `adidas-samba`: Liquid error `False`, hero `True`, guide `True`, legacy `.coll-rich-content` `False`, Ler mais desktop visível `False`, deltaTop `0px`.

Veredito QA: `True`.
Arquivo QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/lkgoc-generic-component-migration-20260605/qa-prod-generic-live-final.json`.

## Backups / rollback
Backup principal: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/lkgoc-generic-component-prod-deploy-20260605T191753Z`.

Rollback seguro:
1. Repor `sections/lk-collection.liquid` com `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/backups/theme-production/lkgoc-generic-component-prod-deploy-20260605T191753Z/sections__lk-collection_liquid.prod-before`.
2. Remover ou ignorar `snippets/lk-goc-collection.liquid` se necessário.
3. Validar ao vivo as 5 URLs de collection, especialmente `adidas-samba`, sem `preview_theme_id`.

## Não alterado
- Produtos, preços, estoque, checkout, apps, GMC, Meta/Google Ads, Klaviyo, WhatsApp/e-mail e campanhas externas.
- Não publiquei novo tema; apenas assets do tema `main` já aprovado.

## Impact review
Revisar em aproximadamente 7 dias: 2026-06-12.
Métricas: GA4 sessões/conversão/receita por collection, GSC cliques/impressões/CTR/posição, funil collection → PDP → carrinho → checkout.
