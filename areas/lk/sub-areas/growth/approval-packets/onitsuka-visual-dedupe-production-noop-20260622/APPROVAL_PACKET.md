# Approval Packet — Onitsuka visual legacy no-op in production — 2026-06-22

**Status:** pronto para decisão; nenhum write production executado por este packet.  
**Gerado:** 2026-06-22T19:14:19.487316+00:00  
**values_printed:** false.

## Contexto

O DEV theme `155065450718` não possui `sections/lk-onitsuka-ai-visibility-v7.liquid` — Shopify Theme API retornou 404. Portanto, o DEV já representa o cenário sem esse bloco extra e carregou corretamente.

## Evidência DEV

- `/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718`: HTTP 200, H1 1, FAQPage 1, Guia editorial LK 1, Bloco citável LK 0, legacy marker 0, sem Liquid error.
- `/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718`: HTTP 200, H1 1, FAQPage 1, sem Liquid error.

## Evidência produção atual

- `/collections/onitsuka-tiger-todos-os-modelos`: HTTP 200, H1 1, FAQPage 1, Guia editorial LK 2, Bloco citável LK 2, legacy marker 1.
- O asset map production aponta `sections/lk-onitsuka-ai-visibility-v7.liquid` como origem do bloco visual extra.

## Escopo proposto

Aplicar no production theme `155065417950` somente o no-op da section:

- `sections/lk-onitsuka-ai-visibility-v7.liquid`

Sem mexer em DEV, templates JSON, snippets, collection body, title/meta, produtos, preço, estoque, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout ou theme publish.

## Rollback

1. Backup do asset production antes do PUT.
2. Se QA falhar, restaurar backup no mesmo asset.
3. Readback pós-rollback e QA público.

## QA esperado

- Onitsuka broad: HTTP 200, H1 1, FAQPage 1, um único guia/citável canônico, sem Liquid error.
- Mexico 66: sem regressão.

## Aprovação necessária

> Aprovo aplicar no **Shopify production theme `155065417950`** somente o no-op da section visual legacy `sections/lk-onitsuka-ai-visibility-v7.liquid`, sem mexer em DEV, templates JSON, snippets, collection body, title/meta, produtos, preço, estoque, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout ou theme publish, com backup, readback, QA público e rollback.
