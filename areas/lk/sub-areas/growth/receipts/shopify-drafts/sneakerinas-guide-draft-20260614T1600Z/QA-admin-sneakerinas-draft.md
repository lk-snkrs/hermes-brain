# QA admin — Sneakerinas draft Shopify

- Data UTC: 2026-06-14T16:44:29.797151Z
- Status: QA read-only concluído via Shopify Admin GraphQL + fetch público.
- Shopify dev/admin: https://admin.shopify.com/store/lk-sneakerss/content/pages/128410616030
- Legacy admin: https://lk-sneakerss.myshopify.com/admin/pages/128410616030
- URL pública: https://lksneakers.com.br/pages/guia-sneakerinas-ballet-sneakers — 404 esperado porque `isPublished=false`.

## Readback
- Page ID: gid://shopify/Page/128410616030
- Handle: guia-sneakerinas-ballet-sneakers
- Title: Sneakerinas e Ballet Sneakers | Guia LK
- Published: False
- Published at: None
- Updated at: 2026-06-14T16:13:27Z

## Checks
- Body chars: 8683
- H2 count: 11
- Link para Ballet Core: True
- Termos proibidos no body do draft: False
- FAQ section: True
- SEO metafields: description_tag, title_tag
- Modelos mencionados: {"Taekwondo Mei Ballet": true, "Ballerina": true, "Tokyo Mary Jane": true, "Speedcat Ballet": true, "Samba Crochet": true}

## Observação
- O body do draft não inclui H1 porque o título da Page deve ser renderizado pelo tema como título da página. Validar visualmente no admin/preview antes de publicar.
- A coleção pública `/collections/ballet-core` está acessível, mas contém texto live sobre prazo/encomenda em FAQ. Não foi alterado nesta execução; recomendo revisar em pacote separado por guardrail de linguagem.

## Resultado
- Aprovado para revisão visual por Lucas no Shopify Admin.
- Publicação exige aprovação explícita separada.
