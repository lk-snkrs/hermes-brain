# FINAL RECEIPT — GMC link_template regressão Local/LIA — Wave 1 1000 — 2026-06-09

- Timestamp UTC: 2026-06-09T11:43:03.149671+00:00
- Aprovação: Lucas `Seguir` no Telegram após recomendação/packet de onda 1.
- Write externo: sim, Google Merchant Center / Merchant API `productInputs.patch`.
- Escopo: até 1.000 offerIds do packet `gmc-link-template-regression-local-lia-11410-20260609`.
- Campos alterados: `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`.
- Shopify alterado: não.
- Preço/estoque/título/GTIN/imagem/campanhas alterados: não.

## Resultado do patch

- Targets: `1000`
- Patch OK: `1000`
- Falhas: `0`
- Patch results lines: `1000`

Observação: o executor principal estourou timeout durante etapa de readback sequencial depois de concluir os patches. A validação foi retomada em script paralelo read-only.

## Readback paralelo

- Lidos: `1000`
- `linkTemplate` confirmado: `1000`
- Ainda com `mhlsf_full_missing_valid_link_template`: `0`
- Erros de leitura: `0`

## Post-scan global

- Issue global pós-wave1: `10408`
- Antes da wave1: `11410`
- Redução esperada/aproximada: `1002` ocorrências

## Evidências

- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-regression-local-lia-11410-20260609/APPROVAL_PACKET.md`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/patch_results.jsonl`
- Readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/readback_wave1_parallel.json`
- Post-scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/post_scan/scan_missing_link_template.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/summary.json`

## Rollback

- Snapshot pré-write salvo em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave1-1000-20260609T/snapshot_before_patch.json`.
- Rollback possível por offerId, reaplicando valores pré-snapshot nos três campos, mediante nova aprovação.

## Próximo gate recomendado

Como a wave1 teve `1000/1000` confirmados e `0` issue remanescente no alvo, tecnicamente dá para escalar. Recomendo próxima onda de 5.000, ainda com snapshot/readback/post-scan, antes de finalizar o saldo.
