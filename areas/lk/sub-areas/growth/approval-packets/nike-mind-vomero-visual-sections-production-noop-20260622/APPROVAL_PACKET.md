# Approval Packet — Production visual sections no-op — Nike Mind/Vomero — 2026-06-22

**Status:** preparado; produção não alterada.  
**Gerado:** 2026-06-22T17:28:51.289366+00:00  
**values_printed:** false.

## Contexto

Lucas aprovou DEV preview para desativar duas sections visuais legacy no theme DEV `155065450718`:

- `sections/lk-nike-mind-ai-visibility-v7.liquid`
- `sections/lk-vomero-premium-ai-visibility-v7.liquid`

Ao executar o backup/readback no DEV, a Shopify Theme API retornou `404 Not Found`: essas duas sections **não existem no DEV theme**. Verificação de assets confirmou que também não existem no DEV os templates JSON relacionados:

- `templates/collection.nike-mind-ai-v7.json`
- `templates/page.nike-mind-ai-v7.json`
- `templates/collection.vomero-premium-ai-v7.json`
- `templates/page.vomero-premium-ai-v7.json`

## QA do DEV atual

Mesmo sem write, o DEV já representa o estado desejado para esses blocos visuais:

| URL preview | HTTP | H1 | FAQPage | Visual legacy v7 | Liquid error |
|---|---:|---:|---:|---|---|
| `/collections/nike-mind-001?preview_theme_id=155065450718` | 200 | 1 | 1 | ausente | não |
| `/pages/guia-nike-mind-001-002?preview_theme_id=155065450718` | 200 | 1 | 1 | ausente | não |
| `/collections/nike-vomero-premium?preview_theme_id=155065450718` | 200 | 1 | 1 | ausente | não |

## Diagnóstico

A diferença produção vs DEV é estrutural:

- Production theme `155065417950` contém as duas sections visuais v7 e templates que as renderizam.
- DEV theme `155065450718` não contém esses assets; por isso a tentativa de “desativar no DEV” não tinha onde aplicar o patch.
- O preview DEV já confirma que, sem essas sections, as páginas permanecem com HTTP 200, H1 único, FAQPage único e sem Liquid error.

## Proposta production-safe

Aplicar no production theme `155065417950` somente no-op/comment nas duas sections visuais legacy:

1. `sections/lk-nike-mind-ai-visibility-v7.liquid`
2. `sections/lk-vomero-premium-ai-visibility-v7.liquid`

Não alterar templates JSON neste passo.

## Escopo fora

Não mexer em:

- DEV theme;
- templates JSON;
- snippets já aplicados;
- produtos;
- preço;
- estoque/disponibilidade;
- ordenação;
- desconto;
- PDPs;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp;
- checkout;
- theme publish.

## QA esperado pós-production

- `/collections/nike-mind-001`: HTTP 200, H1 1, FAQPage 1, sem `lk-nike-mind-ai-visibility-v7-citable`, sem Liquid error.
- `/pages/guia-nike-mind-001-002`: HTTP 200, H1 1, FAQPage 1, sem `lk-nike-mind-ai-visibility-v7-citable`, sem Liquid error.
- `/collections/nike-vomero-premium`: HTTP 200, H1 1, FAQPage 1, sem `lk-vomero-premium-ai-visibility-v7-citable`, sem Liquid error.

## Aprovação necessária

> Aprovo aplicar no **Shopify production theme `155065417950`** somente o no-op das duas sections visuais legacy `sections/lk-nike-mind-ai-visibility-v7.liquid` e `sections/lk-vomero-premium-ai-visibility-v7.liquid`, sem mexer em DEV, templates JSON, snippets já aplicados, produtos, preço, estoque, ordenação, descontos, PDPs, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout ou theme publish, com backup, readback, QA público e rollback.

## Evidência

- Asset existence check: `growth/work/nike-mind-vomero-remaining-visual-blocks-20260622/dev-asset-existence-check.json`
- DEV QA: `growth/work/nike-mind-vomero-remaining-visual-blocks-20260622/dev-current-qa-after-visual-request.json`
