# LK OS — Stockout Sourcing Router Template, 2026-05-12

Generated at: `2026-05-12T21:30:03.250897+00:00`

## Veredito

Template operacional pronto para substituir cotação genérica por sourcing somente quando houver venda/pedido + stockout confirmado.

## Gatilho obrigatório

- Existe venda/pedido/necessidade concreta.
- Produto, SKU e tamanho estão definidos.
- Stockout/estoque zero foi confirmado pela fonte correta antes de sourcing.

## Ordem correta

1. Droper primeiro: disponibilidade + custo + link.
2. Se Droper não tiver: comparar StockX vs GOAT, normalizando tamanho.
3. Recomendar menor fonte viável somente como orientação.
4. Preparar tarefa para Júlio/Notion com contexto, link, custo e ressalvas.

## Texto inline para Telegram / aprovação

```text
Router de reposição por stockout — [produto]

Pedido/necessidade: [pedido ou contexto]
Produto/SKU/tamanho: [produto] · [SKU] · [tamanho]
Status de estoque: [stockout confirmado por fonte]

Droper: [tem/não tem] · [preço/link se consultado]
StockX: [preço/link se Droper não tiver]
GOAT: [preço/link se Droper não tiver]

Recomendação para Júlio: [fonte mais barata viável]
Tarefa sugerida: Júlio comprar/avaliar pelo link [link], custo [valor], observações [lead time/tamanho/risco].

Não autorizado: Hermes comprar, reservar, escolher endereço/importador, acionar fornecedor/grupo ou alterar Shopify/Tiny/Merchant.
```

## Frase de aprovação inline

`Aprovo criar tarefa para Júlio/Notion com este produto/SKU/tamanho e a fonte recomendada, apenas como orientação de compra humana; não autorizo Hermes a comprar, reservar, escolher endereço/importador, contatar fornecedor/grupo, nem alterar Shopify/Tiny/Merchant.`

## Nunca autorizado para Hermes

- purchase
- reservation
- purchase_order
- supplier_or_whatsapp_compras_contact_without_explicit_approval
- delivery_address_choice
- importer_or_bring_to_brazil_supplier_choice
- shopify_write
- tiny_write
- merchant_write
- notion_or_n8n_flow_activation_without_explicit_approval

## Não executado

- droper_lookup
- stockx_lookup
- goat_lookup
- notion_or_n8n_creation
- supplier_contact
- purchase
- reservation
- shopify_write
- tiny_write
- merchant_write
- database_write
