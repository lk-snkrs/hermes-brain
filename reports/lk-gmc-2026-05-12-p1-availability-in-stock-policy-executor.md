# LK GMC P1-B Availability In-Stock Policy Executor, 2026-05-12

Status: `gmc_p1_availability_in_stock_policy_pilot_apply_verified`

## Aprovação usada
- Lucas respondeu: `Aprovo`.
- Interpretação aplicada: opção recomendada anterior, piloto 25, não todos os 1.616.

## Escopo executado
- Campo alterado: `availability` apenas.
- Valor aplicado: `in stock`.
- Regra: GMC deve mostrar disponível mesmo com Tiny zerado.
- Tiny/Shopify/feed/DB/POS/campanha/sourcing não foram tocados.

## Resultado final verificado
- Ready total no fresh preflight: 1616
- Selecionados para apply: 25
- Updates iniciais com sucesso: 25
- Retries adicionais dentro do mesmo piloto: 3
- Falhas finais: 0
- Verificados via `products.get` como `in stock`: 25/25
- Ainda faltando `availability` no `productstatuses` dos 25: 0

## IDs aplicados/verificados
- `online:pt:BR:1023851-1A17746_2NM8J-1` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-10` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-2` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-3` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-4` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-5` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-6` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-7` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-8` — availability=in stock verify=verified_product_get
- `online:pt:BR:1023851-1A17746_2NM8J-9` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660001` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660002` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660003` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660004` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660005` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A660006` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-1` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-10` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-11` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-12` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-2` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-3` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-4` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-5` — availability=in stock verify=verified_product_get
- `online:pt:BR:1182A677.001-6` — availability=in stock verify=verified_product_get

## Rollbacks privados
- Inicial: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-p1-availability-in-stock-policy-executor-rollback-20260512T231951Z.json`
- Retry: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-12-p1-availability-in-stock-policy-executor-retry3-rollback-20260512T232331Z.json`

## Não executado
- merchant_delete
- merchant_price_title_link_image_update
- tiny_call
- tiny_write
- shopify_write
- feed_update_or_fetch
- database_write
- pos_write
- campaign_or_external_send
- sourcing_or_supplier_contact
