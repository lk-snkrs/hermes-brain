# LK OS — Tiny stock micro-lote incremental

Gerado em: `2026-05-15T20:23:00Z`
Status: `partial_incremental_micro_batch_success_not_final`

## Veredito

Rodei o micro-lote Tiny pós-governança com `25` leituras e `delay 6s`. Desta vez o lote completou as 25 leituras sem novo bloqueio no processo, mas o run continua parcial porque ainda faltam milhares de produtos para cobertura confiável. Não promover para Mission Control final.

## Lote executado

- run_id: `tiny_stock_20260515T092206Z`
- modo: `resume`
- stock_limit: `25`
- delay: `6s`
- leituras antes: `872`
- leituras depois: `897`
- leituras novas: `25`
- resultado do processo: `micro_batch_completed`

## Progresso Tiny

- tiny_products_listed: `17.605`
- tiny_products_with_codigo: `15.372`
- stock_products_checked: `897`
- remaining_stock_checks aproximado: `14.475`
- cobertura aproximada: `5,84%`
- official_deposit_rows: `897`
- official_positive_rows: `40`

## Estado comercial derivado

- blocked_tiny_not_mapped: `10.054`
- monitor_non_active_shopify_product: `1.431`
- blocked_missing_shopify_sku: `1.388`
- blocked_data_quality: `1.032`
- ready_zero_stock_sourcing_candidate: `520`
- ready_available_tiny: `37`
- blocked_tiny_duplicate_code: `4`

## Decisão

- Continuar acumulando por micro-lotes, não por lote 250–500, até o Tiny parar de bloquear.
- Próximo lote seguro: `25–50` leituras, `delay 6–8s`, com pausa imediata se `status=Erro`/rate limit.
- Não criar cron/worker automático ainda.
- Não usar esse estado parcial para campanha, baixa de disponibilidade ou compra automática.

## O que não foi feito

- Tiny write
- Shopify write
- inventory_change
- price_change
- supplier/customer contact
- purchase
- campaign/send
- cron creation
