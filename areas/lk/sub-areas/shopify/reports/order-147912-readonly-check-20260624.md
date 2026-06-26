# LK Shopify — pedido #147912 — checagem read-only

- Data/hora: 2026-06-24T09:42:00Z
- Escopo aprovado: Mesa COO decisão 2/3 — checagem/handoff read-only.
- Fonte: Shopify Admin API GET/query-only via Doppler `lc-keys/prd`; `values_printed=false`.
- Writes externos: 0
- Envios externos: 0
- PII: não reproduzida; este relatório registra apenas estado operacional, itens, SKUs/handles e flags.

## Veredito operacional

Pedido #147912 está **pago**, **confirmado**, **não cancelado**, **não fechado** e **unfulfilled** no Shopify. Gift bag está marcado como `yes`. Shopify risk retornou recomendação `accept` com score `0.0`.

## Dados read-only verificados

- Criado em: 2026-06-24T02:09:27Z
- Financeiro: `PAID`
- Fulfillment: `UNFULFILLED`
- Confirmed: `true`
- Cancelled: `false`
- Closed: `false`
- Total atual: BRL 4.274,98
- Desconto total: BRL 474,99
- Gift bag: `lk_gift_bag=yes`
- Fulfillments existentes: 0
- Transação observada: `SALE` / `SUCCESS` / gateway Appmax cartão de crédito
- Shopify risk: `recommendation=accept`, `score=0.0`

## Itens do pedido — para validação pelo dono de estoque

1. Tênis Adidas SL 72 OG Sand Strata Preloved Brown Cream White Bege
   - Quantidade: 1
   - Variante/tamanho: 35
   - SKU Shopify: `43774078386880`
   - Handle: `tenis-adidas-sl-72-og-sand-strata-preloved-brown-cream-white-bege`
   - Product status: `ACTIVE`
   - Fulfillment item: `unfulfilled`

2. Tênis Adidas Samba Jane Cream Black Gum Bege
   - Quantidade: 1
   - Variante/tamanho: 35
   - SKU Shopify: `43774078387770`
   - Handle: `tenis-adidas-samba-jane-cream-black-gum-bege`
   - Product status: `ACTIVE`
   - Fulfillment item: `unfulfilled`

3. Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho
   - Quantidade: 1
   - Variante/tamanho: XS/PP
   - SKU Shopify: `w51432r_00-2`
   - Handle: `calca-alo-yoga-suit-up-trouser-regular-azul-marinho`
   - Product status: `ACTIVE`
   - Fulfillment item: `unfulfilled`

## Handoff necessário

- `[LK] Estoque Loja Física / lk-stock`: validar disponibilidade/estoque dos 3 itens no Stock OS/Tiny e retornar status por SKU/tamanho/freshness. Hermes Geral/Shopify **não** está afirmando estoque.
- LK Shopify/Ops: pedido está pronto para triagem operacional read-only de separação, gift bag e fulfillment, mas qualquer fulfillment/tag/order write exige aprovação/ação do dono operacional.

## Bloqueios preservados

- Sem WhatsApp/e-mail/cliente.
- Sem Shopify/Tiny write.
- Sem fulfillment/cancelamento/refund/tag/note.
- Sem promessa de disponibilidade.
- Sem exposição de PII.
