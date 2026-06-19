# Diagnóstico — Opção C SWYM híbrido — Home cache Production — 20260618T1704Z

- values_printed: false
- escopo: read-only; nenhum write Shopify/Git/tema executado nesta etapa.

## Contexto

Após merge/aplicação da Opção C em Production, o Shopify Admin/readback mostra o código novo no tema publicado, mas a Home pública ainda apresenta HTML antigo em parte das amostras.

## Monitor encerrado

Arquivo:
`/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-home-monitor-20260618T165343Z.json`

Resultado:

- stable_last3: false
- rounds: 10
- round 1: asset_ref true, swym_ext_count 0
- rounds 2–10: asset_ref false, swym_ext_count 4

Interpretação: Home não convergiu de forma estável para o HTML novo.

## Diagnóstico público adicional

Amostras com query cache-bust e headers `Cache-Control: no-cache` / `Pragma: no-cache`:

- 6/6 status 200
- 6/6 `asset_ref=false`
- 6/6 `hybrid_marker=false`
- 6/6 `swym_ext_count=4`
- 6/6 `wishlist_link=true`
- cache_status: `DYNAMIC`
- etag repetido: `W/"page_cache:62189699294:IndexController:cff0c9e6837a01efe4c1aedebbf8a634"`

Interpretação: a Home pública está sendo servida por page_cache antigo do `IndexController` em pelo menos o caminho testado. O botão topbar de wishlist continua presente.

## Readback Admin Production

Arquivo:
`/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/option_c_production/production-readback-20260618T170426Z.json`

Resultado:

- ok: true
- production_theme_id: 155065417950
- layout_marker_count: 1
- asset_ref_count: 1
- asset_present: true
- asset_hash: `2ba6b9c7d919974bbf772ee389e66208333bd3c0a619c57d9e416e0599ee3f6a`
- swym_enabled_count: 0
- 2 blocos SWYM/Wishlist Plus com disabled=true

Interpretação: Shopify Admin está com o código novo; divergência atual é storefront/page cache da Home, não ausência do patch no tema.

## Risco

- Estado atual não indica quebra funcional: HTML antigo ainda carrega SWYM automático, e testes em PDP/Coleção/Wishlist passaram quando serviram o novo fluxo.
- Estado atual impede declarar ganho de performance na Home como efetivo/convergido.

## Próxima decisão segura

Sem novo write: aguardar e revalidar.
Com aprovação explícita: executar uma ação mínima de invalidação/touch no tema Production, com backup/readback/rollback, para tentar forçar purge da Home.
