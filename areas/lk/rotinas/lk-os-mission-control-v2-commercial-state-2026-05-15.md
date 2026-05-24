# LK OS Mission Control v2 — Estado comercial por variante/tamanho

Gerado em: `2026-05-15T19:33:49.038092+00:00`
Status: `partial_tiny_rate_limited_incremental_batch`

## Veredito

Rodei o lote controlado aprovado para o Tiny stock com `--stock-limit 250` e `--delay 3s`. A execução conseguiu consolidar mais `30` produtos antes do Tiny retornar bloqueio/rate limit novamente. Parei automaticamente sem insistir, atualizei a camada `lk_variant_commercial_state` com o incremento e **não promovi para Mission Control final** porque a cobertura ainda está baixa.

## Lote controlado executado

- run_id: `tiny_stock_20260515T092206Z`
- stock_limit solicitado: `250`
- delay: `3s`
- leituras antes do lote: `842`
- leituras depois do lote: `872`
- leituras novas neste lote: `30`
- resultado: `Tiny rate limit/bloqueio após 30 leituras bem-sucedidas`

## Progresso Tiny

- tiny_products_listed: `17605`
- tiny_products_with_codigo: `15372`
- stock_products_checked: `872`
- remaining_stock_checks: `14500`
- checked_ratio_pct: `5.67`
- official_deposit_rows: `872`
- official_positive_rows: `37`

## Estado comercial derivado

- blocked_tiny_not_mapped: `10059`
- monitor_non_active_shopify_product: `1431`
- blocked_missing_shopify_sku: `1388`
- blocked_data_quality: `1032`
- ready_zero_stock_sourcing_candidate: `520`
- ready_available_tiny: `34`
- blocked_tiny_duplicate_code: `2`

## Leitura executiva

- O lote incremental funcionou tecnicamente, mas o Tiny ainda está limitando muito cedo para uma onda de 250–500 SKUs.
- `ready_available_tiny` subiu com o incremento, mas ainda deve ser tratado como baseline parcial, não como verdade final do catálogo inteiro.
- `ready_zero_stock_sourcing_candidate` também é parcial: serve para fila inicial de investigação/sourcing, não para automação de campanha ou baixa de disponibilidade.
- O grande gargalo continua sendo cobertura: ainda faltam milhares de leituras de estoque por produto Tiny.

## Próximo passo seguro

1. Aguardar novo cooldown maior antes de nova tentativa.
2. Na próxima janela, reduzir o lote operacional para `25–50` leituras com `delay 5–8s`, apesar da meta original 250–500, porque o Tiny bloqueou novamente em 30 leituras mesmo com `3s`.
3. Usar acumulação incremental até cobertura suficiente; só depois declarar Mission Control final.
4. Não criar cron/worker automático sem definir cadência aprovada e guardrail de pausa em rate limit.

## O que não foi feito

- Tiny write
- Shopify write
- Merchant write
- price/stock change
- campaign/send
- supplier/customer contact
- purchase
- new cron/worker

Relatório JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-os-mission-control-v2-commercial-state-2026-05-15.json`

## Approval Manager v1 — 2026-05-15

Status: `active_local_router_layer`

- Regras ativas: `6`
- Ledger de decisões: `3`
- Router regression tests: `8/8` PASS
- Fila `draft_only`: `2` casos de teste cobertos
- Fila `needs_approval/preview`: `6` casos de teste cobertos
- Fila `autonomous_readonly/local`: `2` casos de teste cobertos
- Artefato: `areas/lk/rotinas/lk-os-approval-manager-v1-2026-05-15.md`
- Contrato: antes de execução LK OS futura, consultar regra/ledger/router; envio externo, campanha, compra, fornecedor, Merchant/feed, Shopify/Tiny/theme/deploy continuam approval-gated.
