# Handoff — LK Stock — validar estoque do pedido #147912

- Data/hora: 2026-06-24T09:43:00Z
- Origem: Mesa COO decisão 2/3 aprovada por Lucas (`Fazer`)
- Dono destinatário: `[LK] Estoque Loja Física` / `lk-stock`
- Contexto: pedido Shopify #147912 pago/confirmado/unfulfilled; gift bag marcado.
- Fonte Shopify read-only: `areas/lk/sub-areas/shopify/reports/order-147912-readonly-check-20260624.md`
- Writes externos executados: 0
- Envios externos executados: 0
- values_printed: false

## Pedido

Validar disponibilidade/estoque dos itens abaixo usando o caminho canônico do `lk-stock`:

1. Stock OS DB local como caminho quente primário;
2. fallback/reconciliação Tiny/Olist somente se DB local estiver stale/ambígua/sem SKU/freshness insuficiente;
3. retornar status por SKU/tamanho com fonte/freshness;
4. não prometer disponibilidade pública e não executar Tiny/Shopify write.

## Itens para validação

1. **Tênis Adidas SL 72 OG Sand Strata Preloved Brown Cream White Bege**
   - SKU Shopify: `43774078386880`
   - Tamanho: 35
   - Handle: `tenis-adidas-sl-72-og-sand-strata-preloved-brown-cream-white-bege`
   - Quantidade vendida: 1

2. **Tênis Adidas Samba Jane Cream Black Gum Bege**
   - SKU Shopify: `43774078387770`
   - Tamanho: 35
   - Handle: `tenis-adidas-samba-jane-cream-black-gum-bege`
   - Quantidade vendida: 1

3. **Calça Alo Yoga Suit Up Trouser (Regular) Azul Marinho**
   - SKU Shopify: `w51432r_00-2`
   - Tamanho: XS/PP
   - Handle: `calca-alo-yoga-suit-up-trouser-regular-azul-marinho`
   - Quantidade vendida: 1

## Output esperado do lk-stock

- `confirmado` / `não confirmado` por item.
- Fonte e freshness por item.
- Se SKU Shopify for ID/alias sem código Tiny resolvido, apontar lane de saneamento (`needs_sku_resolution` ou equivalente) em vez de concluir sem estoque.
- Recomendação: liberar separação, segurar para reconciliação, ou escalonar para operação.

## Bloqueios

- Tiny write: 0
- Shopify write: 0
- fulfillment: 0
- cliente/WhatsApp/e-mail: 0
- compra/transferência/reserva: 0

Reminder OS loop needed: yes
Reminder OS owner: lk-stock
Próxima ação: lk-stock validar Stock OS/Tiny e devolver evidência por item antes de qualquer fulfillment/promessa operacional.
