# Approval Packet — Merchant micro-piloto New Balance 204L — 2026-06-17

## Pedido de aprovação

Aprovar micro-piloto controlado no Merchant/feed para o cluster `/collections/new-balance-204l`.

## Escopo permitido

- Corrigir/decidir até 3 ofertas 204L com `landing_page_error`.
- Aplicar até 20 correções de atributo `color` em offers 204L quando a cor estiver evidente no title/link.
- Readback imediato + tardio.
- Backup antes e rollback payload por item.

## Escopo proibido

- Não alterar produtos Shopify.
- Não alterar preço, estoque, disponibilidade, desconto ou grade.
- Não alterar campanhas Google/Meta.
- Não alterar theme, checkout, Klaviyo/WhatsApp.
- Não mexer em GTIN/MPN sem fonte oficial.
- Não fazer alteração massiva em LIA/link_template nesta etapa.

## Evidência

- 228 itens New Balance 204L encontrados no Merchant.
- 260 instâncias de `missing_item_attribute_for_product_type` no cluster, com 67 ausências agregadas de `color`.
- 3 `landing_page_error` confirmados publicamente com HTTP 404.
- 66 instâncias `mhlsf_full_missing_valid_link_template` em local/LIA, mantidas fora do micro-piloto.

## Risco

- Baixo/médio se limitado a atributo e URL mapping com backup.
- Risco principal: Simprosys sobrescrever ProductInput ou conflito entre data sources.

## Rollback

- Salvar estado anterior por offer.
- Reaplicar ProductInput anterior ou remover patch supplemental, conforme superfície usada.
- Readback e registrar receipt.

## Frase de aprovação sugerida

"Aprovo o micro-piloto Merchant New Balance 204L: até 3 landing-page errors e até 20 correções de color por evidência, sem mexer em produtos Shopify, preço, estoque, campanhas, theme ou checkout, com backup, QA e rollback."
