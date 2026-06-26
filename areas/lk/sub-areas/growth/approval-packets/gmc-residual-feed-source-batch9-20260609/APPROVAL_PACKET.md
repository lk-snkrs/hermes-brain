# Approval Packet — GMC Residual Feed Source Batch 9 — 2026-06-09

Status: templates/review only / sem write

## Summary
- manual_review_items_template: `148`
- feed_source_items_template: `115`

## Arquivos gerados

- Manual enrichment CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-residual-manual-enrichment-batch8-20260608/manual_review_template.csv`
- Feed/source fix CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-residual-feed-source-batch9-20260609/feed_source_fix_template.csv`

## Uso recomendado

1. Preencher apenas linhas com `approved_for_*_write = yes`.
2. Validar `proposed_*` / `suggested_*` manualmente.
3. Gerar batch write separado com snapshot/readback/rollback.

## O que NÃO foi feito

- Nenhum write em GMC.
- Nenhuma alteração Shopify.
- Nenhuma alteração de preço/estoque/GTIN/título/link em produção.

## Próxima aprovação necessária

Para executar qualquer write, preciso do arquivo revisado/preenchido e aprovação explícita do escopo.