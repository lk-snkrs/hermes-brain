# Shopify upstream fields para GMC/Simprosys — 2026-06-17

**Modo:** read-only.  
**Writes:** 0.  
**Objetivo:** identificar onde configurar atributos duráveis na Shopify para que o Simprosys/GMC receba os dados após sync, evitando patches temporários direto no Merchant.

## Resposta curta

O campo correto para `color` não é no Merchant como solução definitiva. Na Shopify da LK existe namespace/metafield próprio de Google Shopping:

- Owner: `PRODUCT`
- Namespace: `mm-google-shopping`
- Key: `color`
- Nome Admin: `Cor`
- Tipo: `single_line_text_field`

Exemplo de valor observado em produtos 204L:

- `mm-google-shopping.color = Bege`
- `mm-google-shopping.color = Cinza`
- `mm-google-shopping.color = Marrom`

## Outros campos GMC encontrados na Shopify

### Product-level
- `mm-google-shopping.color` — Cor
- `mm-google-shopping.gender` — Gender
- `mm-google-shopping.age_group` — Adulto / age group
- `mm-google-shopping.identifier_exists`
- `mm-google-shopping.google_product_category`
- `mm-google-shopping.custom_product`
- `mm-google-shopping.size` — existe em PRODUCT, mas no catálogo 204L o tamanho real parece vir de variantes/SKU/feed, não necessariamente daqui.

### Variant-level
- `mm-google-shopping.mpn`
- `mm-google-shopping.gender`
- `mm-google-shopping.age_group`
- `mm-google-shopping.condition`
- `mm-google-shopping.size_type`
- `mm-google-shopping.size_system`
- `mm-google-shopping.custom_label_0..4`

## Interpretação

A correção durável deve ser feita em Shopify Product metafields, principalmente:

```text
namespace: mm-google-shopping
key: color
owner: Product
value: Cor em PT/label canônico, ex: Bege, Cinza, Marrom, Preto, Prateado
```

Isso deve alimentar o app/feed ligado ao namespace `mm-google-shopping` e sobreviver às sincronizações, diferentemente de patch direto no Merchant.

## Observação importante

Alguns produtos 204L já mostram `mm-google-shopping.color` preenchido na Shopify, mesmo quando o Merchant tinha `color` ausente antes do micro-piloto. Portanto, antes de aplicar batch, precisamos validar uma destas hipóteses:

1. O Simprosys ainda não sincronizou esses metafields para o GMC.
2. O campo existe na Shopify, mas o mapeamento do app/feed não está ativo para todos os produtos/data sources.
3. O Merchant estava lendo uma versão anterior/processada e atualizou depois.
4. Há diferença entre data source online/API e local/LIA/autofeed.

## Próximo packet recomendado

Preparar micro-piloto Shopify upstream, não Merchant:

- Ler produtos 204L com `mm-google-shopping.color` ausente.
- Inferir cor apenas por evidência forte do título/handle.
- Escrever `mm-google-shopping.color` no Product, não Variant, em lote pequeno.
- Backup dos metafields antes.
- Readback Shopify imediato.
- Aguardar sync Simprosys/GMC.
- Confirmar no Merchant se `productAttributes.color` aparece sem patch direto.

## Escopo proibido sem nova aprovação

- Publicar produto DRAFT.
- Alterar preço, estoque, disponibilidade, grade ou variantes.
- Alterar theme, campanhas, feed global ou Simprosys config.
- Alterar GTIN/MPN sem fonte confiável.

## Artefatos

- `metafield-definitions-product-variant.json`
- `sample-204l-shopify-metafields.json`

Gerado em: 2026-06-17T18:27:24.556829+00:00
