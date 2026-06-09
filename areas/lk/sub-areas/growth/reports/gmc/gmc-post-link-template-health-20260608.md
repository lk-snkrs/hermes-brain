# GMC Post-Link-Template Health — 2026-06-08

Generated: `2026-06-08T15:02:33.930314+00:00`  
Modo: read-only / sem write GMC  
Fonte: Merchant API `products_v1.products.list`

## Resultado executivo

O recheck confirmou que a correção em massa de `linkTemplate` funcionou, mas houve **regressão parcial** após o scan final: agora existem `162` itens Local/LIA novamente com `mhlsf_full_missing_valid_link_template`.

Interpretação: provável overwrite/novo lote do feed/dataSource após o patch anterior. Não corrigi ainda porque este novo bloco é write GMC e precisa approval escopado.

## Totais do scan

- Páginas varridas: 23
- Produtos/statuses: 22681
- Legacy local products: 11066

## Top issues atuais

- `missing_item_attribute_for_product_type`: 11760
- `local_stores_lack_inventory`: 1306
- `strikethrough_price_updated`: 762
- `price_updated`: 726
- `restricted_gtin`: 165
- `mhlsf_full_missing_valid_link_template`: 162
- `item_missing_required_attribute`: 130
- `landing_page_error`: 67
- `availability_updated`: 54
- `image_link_internal_error`: 53
- `attribute_pending_review`: 37
- `attribute_violated_discovery_ads_policy`: 37


## Alvos do PRD

- `landing_page_error`: 67
- `missing_item_attribute_for_product_type`: 11760
- `mhlsf_full_missing_valid_link_template`: 162
- `price_updated`: 726
- `strikethrough_price_updated`: 762
- `restricted_gtin`: 165

## Landing page error triage

Foram amostrados 13 links com `landing_page_error` e todos retornaram 404 no check público.

Status HTTP:
- `404`: 13

Causa provável: produtos/URLs removidos ou handles antigos ainda presentes no feed, não problema genérico de crawler.

## Recomendações

### P0 approval packet — repatch dos 162 `link_template`

Reexecutar patch somente nos 162 itens atuais, com snapshot/readback. É a correção mais direta e de baixo risco, mas é write GMC.

### P1 — landing page error

Não fazer patch de URL cego. Primeiro classificar se cada 404 é:

- produto despublicado/indisponível;
- handle alterado;
- variant antiga;
- item órfão no dataSource.

Ação futura pode ser remover/expirar item no feed ou corrigir URL, mas depende de fonte Shopify/feed.

### P1 — missing attribute/product type

Gerado micro-piloto preview com 50 candidatos high-confidence de `color`.

Packet: `approval-packets/gmc-missing-color-micro-pilot-20260608/APPROVAL_PACKET.md`

## Artefatos

- JSON scan: `reports/gmc/gmc-post-link-template-health-20260608.json`
- Landing URL check: `reports/gmc/landing-page-error-url-check-20260608.json`
