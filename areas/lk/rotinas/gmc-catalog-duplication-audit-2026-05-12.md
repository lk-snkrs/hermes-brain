# LK GMC Catalog Duplication Audit, 2026-05-12

Status: `gmc_catalog_duplication_audit_ready_readonly`

## Resumo executivo
- Merchant productstatuses: 25578
- Merchant products: 25578
- Merchant unique offer IDs: 23926
- Shopify local products total/active: 2241 / 1819
- Shopify local variants total: 14466
- Shopify local variants with SKU / distinct SKUs: 13078 / 12204

## Veredito
- Os 25,6 mil itens do Merchant não parecem representar o catálogo real único da LK.
- A contagem do Merchant é por item/oferta e pode incluir variantes, histórico/stale items, fontes duplicadas ou combinações por país/idioma/canal.
- Antes de excluir qualquer coisa, é necessário mapear fontes/feeds e provar qual origem está inflando a base.

## Dimensões Merchant products
- online:pt:BR: 13940
- local:pt:BR: 11638

## Exemplos de offer_id duplicado
- LIA_1023851-1A17746_2NM8J-1: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-1', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-1']
- LIA_1023851-1A17746_2NM8J-10: 2 ids; amostra=['online:pt:BR:LIA_1023851-1A17746_2NM8J-10', 'local:pt:BR:LIA_1023851-1A17746_2NM8J-10']
- LIA_1023851-1A17746_2NM8J-2: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-2', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-2']
- LIA_1023851-1A17746_2NM8J-3: 2 ids; amostra=['online:pt:BR:LIA_1023851-1A17746_2NM8J-3', 'local:pt:BR:LIA_1023851-1A17746_2NM8J-3']
- LIA_1023851-1A17746_2NM8J-4: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-4', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-4']
- LIA_1023851-1A17746_2NM8J-5: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-5', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-5']
- LIA_1023851-1A17746_2NM8J-6: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-6', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-6']
- LIA_1023851-1A17746_2NM8J-7: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-7', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-7']
- LIA_1023851-1A17746_2NM8J-8: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-8', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-8']
- LIA_1023851-1A17746_2NM8J-9: 2 ids; amostra=['local:pt:BR:LIA_1023851-1A17746_2NM8J-9', 'online:pt:BR:LIA_1023851-1A17746_2NM8J-9']

## Não executado
- merchant_product_delete
- feed_delete_or_exclusion
- shopify_write
- database_write
- campaign_or_external_send
- checkout_or_theme_change
