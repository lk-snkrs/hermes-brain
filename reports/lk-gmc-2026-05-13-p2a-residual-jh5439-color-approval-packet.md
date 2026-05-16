# LK GMC P2A residual — JH5439 color approval packet, 2026-05-13

Status: `approval_packet_no_write`

## Veredito

A escala P2A de Calçados foi aplicada e verificada. O residual real acionável não é categoria/product_type: é **color ausente** em 11 variantes do produto `Tênis Adidas Handball Spezial Bordô` (`JH5439`).

A categoria/product_type aparecem localizadas pelo Merchant como:

- `googleProductCategory`: `Vestuário e acessórios > Sapatos`
- `productTypes`: `["Tênis"]`

Isso é semanticamente equivalente ao alvo Calçados/Shoes e não exige reapply cego. O problema que ainda aparece em `productstatuses` é `missing_item_attribute_for_product_type` para `color`.

## Escopo proposto

Patch Merchant API v1 ProductInputs no dataSource `10636492695` somente para:

- campo: `productAttributes.color`
- valor: `Bordô`
- produtos: 11 variantes `online:pt:BR:JH5439-*`

## Produtos

1. `online:pt:BR:JH5439-1` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
2. `online:pt:BR:JH5439-2` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
3. `online:pt:BR:JH5439-3` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
4. `online:pt:BR:JH5439-4` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
5. `online:pt:BR:JH5439-5` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
6. `online:pt:BR:JH5439-6` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
7. `online:pt:BR:JH5439-7` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
8. `online:pt:BR:JH5439-8` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
9. `online:pt:BR:JH5439-9` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
10. `online:pt:BR:JH5439-10` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`
11. `online:pt:BR:JH5439-11` — Tênis Adidas Handball Spezial Bordô — color atual: vazio → `Bordô`

## Evidência

- `fact_merchant`: `productstatuses` pós-P2A mostram 11 rows ainda exigindo `color`.
- `fact_merchant`: Merchant read de cada ProductInput confirma `current_color = null`.
- `fact_merchant`: o título de todas as 11 variantes é `Tênis Adidas Handball Spezial Bordô`.
- `derived_reconciliation`: token de cor explícito no título: `Bordô`.

## Rollback/verificação exigidos se aprovado

Antes de qualquer PATCH:

1. gerar snapshot privado chmod 600 com atributos atuais de cada ProductInput;
2. executar PATCH Merchant API v1 `updateMask=productAttributes.color`;
3. verificar via Merchant product get cada uma das 11 variantes;
4. reprocessar `productstatuses` após delay para confirmar queda de `required_attr_rows_after`.

## Não executar neste pacote

- título;
- preço;
- availability;
- categoria/productTypes;
- imagem/link;
- Shopify;
- Tiny;
- Supabase/banco;
- feed fetch/upload;
- Klaviyo/WhatsApp/campanha;
- compra/sourcing/fornecedor.

## Texto de aprovação necessário

Para aplicar, Lucas precisa aprovar explicitamente:

```text
Aprovo corrigir color Bordô nas 11 variantes JH5439 no GMC via Merchant API v1, com rollback e verificação.
```
