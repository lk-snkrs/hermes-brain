# Receipt — Home OG title/description theme patch

Data: 2026-05-31T12:18Z
Status: Asset API aplicado em dev e produção; readback dos assets aprovado; storefront público ainda renderiza HTML antigo no teste imediato.

## Aprovação

Lucas aprovou aplicar em dev e depois em produção o OG title da home e aprovou também OG description.

## Escopo executado

Asset: `layout/theme.liquid`

Temas:

- Dev: `lk-new-theme/dev`, role `unpublished`, ID `155065450718`
- Production: `lk-new-theme/production`, role `main`, ID `155065417950`

Campos no branch da home/index:

```liquid
<meta property="og:title" content="LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium">
<meta property="og:description" content="Sneaker boutique premium no Jardins, São Paulo. Nike, Adidas Samba, New Balance e Onitsuka Tiger originais. Até 10x sem juros, frete grátis acima de R$499 e loja física na Rua Melo Alves.">
```

## Evidência de aplicação

Receipt final:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-home-og/home-og-static-desc-20260531T121807Z/receipt.json`

Backups finais:

- Dev rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-home-og/home-og-static-desc-20260531T121807Z/dev/before.layout.theme.liquid`
- Production rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-home-og/home-og-static-desc-20260531T121807Z/production/before.layout.theme.liquid`

Readback production confirma:

- `og:title` novo presente na linha 75.
- `og:description` nova presente na linha 76.
- SHA readback = SHA after.

## QA público imediato

URL testada com cachebuster:

`https://lksneakers.com.br/?_lkverify=1780229902`

Resultado imediato do storefront público ainda antigo:

- `og:title`: `LK`
- `og:description`: texto antigo `Na LK Sneakers & Apparels...`

Interpretação: o Asset API aceitou e leu de volta o asset correto, mas o storefront público ainda está servindo render/cache antigo no teste imediato. Não fiz publish/re-publish/purge/cache write adicional porque isso não estava no escopo explícito e pode afetar produção.

## Rollback

Reenviar o backup `before.layout.theme.liquid` do tema correspondente para `layout/theme.liquid` via Shopify Asset API.

## Não alterado

- Produtos
- Coleções
- Preço
- Estoque
- Checkout
- Apps
- GMC/feed
- Klaviyo/ads/WhatsApp/email
- Theme publish / republish

## Próximo passo recomendado

Revalidar o HTML público após propagação curta. Se continuar renderizando antigo, preparar um micro-pacote de diagnóstico/aprovação para cache/render do tema, sem mexer em produto/coleção/preço/estoque.
