# Approval Packet — Onitsuka visual dedupe DEV preview — 2026-06-22

**Status:** pronto para aprovação; nenhum write executado.  
**Gerado:** 2026-06-22T19:06:35.795263+00:00  
**values_printed:** false.

## Motivo

Onitsuka broad está saudável em schema e tráfego, mas o HTML público tem 2 blocos visuais editoriais/citáveis. O schema está único; o problema é redundância visual/GEO, não indexação crítica.

## Evidência

- Broad `/collections/onitsuka-tiger-todos-os-modelos`: HTTP 200, H1 único, FAQPage 1, 2x `Guia editorial LK`, 2x `Bloco citável LK`.
- GSC 28d broad: 585 cliques / 50.405 impressões / CTR 1,16% / posição 6,75.
- GA4 28d broad: 910 sessões orgânicas / 1.820 pageviews / engagement 75,6%.
- Theme map production: `sections/lk-onitsuka-ai-visibility-v7.liquid` é o candidato de bloco extra; guia canônico vem de `lk-collection`/`lk-goc-collection`.

## Escopo proposto

Criar DEV preview no theme `155065450718` para desativar somente:

- `sections/lk-onitsuka-ai-visibility-v7.liquid`

Sem mexer em production, templates JSON, snippets, collection body, title/meta, produtos, preço, estoque, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout.

## QA esperado

- `/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718`: HTTP 200, H1 1, FAQPage 1, apenas 1 bloco guia/citável canônico, sem Liquid error.
- `/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718`: sem regressão.

## Rollback

Restaurar o asset DEV a partir do backup salvo antes do PUT.

## Aprovação necessária

> Aprovo aplicar no **Shopify DEV theme `155065450718`** somente o preview que desativa a section visual legacy `sections/lk-onitsuka-ai-visibility-v7.liquid`, sem mexer em production, templates JSON, snippets, collection body, title/meta, produtos, preço, estoque, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout, com backup, readback, QA público e rollback.
