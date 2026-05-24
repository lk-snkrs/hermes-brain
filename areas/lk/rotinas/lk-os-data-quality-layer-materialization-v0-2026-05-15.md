# LK OS — Data Quality Layer v0 materializado

Status: `local_materialization_complete`
Data: 2026-05-15
Modo: SQLite local/reversível. Nenhuma API externa ou write produtivo executado.

## Veredito

A primeira camada local do Data Quality Layer foi materializada com duas tabelas derivadas: `lk_variant_quality_status` e `lk_sku_alias_map`. Isso cria a base para o PRD voltar a operar por produto/variante/tamanho, sem ainda afirmar estoque livre ou estado comercial final.

## Backup / rollback

- Backup privado antes do write local: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups/lk_os_phase5_before_data_quality_layer_v0_20260515.sqlite`.
- Permissão do backup: `0o600`.
- Rollback: restaurar esse SQLite sobre o DB de trabalho se necessário.

## Tabelas criadas

- `lk_variant_quality_status`: 14466 linhas.
- `lk_sku_alias_map`: 14466 linhas.

## Status de qualidade por variante

- `needs_tiny_stock_truth`: 11934 variants.
- `blocked_missing_sku`: 1388 variants.
- `needs_sku_alias_review`: 1113 variants.
- `ready_basic_variant_layer`: 31 variants.

## Status do mapa SKU/Alias

- `needs_full_tiny_lookup`: 11934 variants.
- `needs_shopify_sku_or_manual_mapping`: 1388 variants.
- `needs_duplicate_sku_review`: 1113 variants.
- `anchor_mapped_partial_stock_only`: 31 variants.

## Leitura executiva

- A maior lacuna prática continua sendo Tiny: a tabela atual `tiny_anchor_stock` é parcial, então a maior parte das variants fica em `needs_tiny_stock_truth` ou `needs_full_tiny_lookup`.
- Variants sem SKU ou com SKU duplicado já ficam bloqueadas/revisão antes de entrarem em sourcing, pricing, CRO ou conteúdo.
- A camada já permite que os próximos módulos não tratem Shopify inventory como verdade de estoque.

## Próximo bloco seguro

Criar o `lk_tiny_stock_snapshots` read-only completo por SKU/tamanho/depósito e depois recalcular `lk_variant_quality_status` para separar `ready_for_stock_decision`, `reserved_or_unclear`, `stockout_exact_ready`, `needs_manual_mapping` e `monitor`. Isso exige apenas consulta Tiny/Supabase/Shopify read-only; qualquer correção de SKU/estoque/preço continua approval-gated.

## Não executado

- No external API call.
- No Shopify/Tiny/Merchant/Klaviyo/Notion/WhatsApp write.
- No cron/UI/worker created.
- No PII exported.
- No purchase/contact/message/campaign.
