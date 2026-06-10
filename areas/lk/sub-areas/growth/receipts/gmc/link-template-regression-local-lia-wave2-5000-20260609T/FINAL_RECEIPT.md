# FINAL RECEIPT — GMC link_template regressão Local/LIA — Wave 2 5000 — 2026-06-09

- Timestamp UTC: 2026-06-09T12:24:16.237907+00:00
- Aprovação: Lucas `Aprovo` no Telegram após gate da wave 2.
- Write externo: sim, Google Merchant Center / Merchant API `productInputs.patch`.
- Escopo: 5.000 offerIds do packet `gmc-link-template-regression-local-lia-11410-20260609` remanescentes após wave1.
- Campos alterados: `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`.
- Shopify alterado: não.
- Preço/estoque/título/GTIN/imagem/campanhas alterados: não.

## Resultado do patch

- Targets: `5000`
- Patch OK: `5000`
- Falhas: `0`
- Patch results lines: `5000`

Observação: o executor principal foi interrompido após concluir os 5.000 patches, para evitar readback sequencial longo. A validação foi feita em paralelo.

## Readback

Readback paralelo inicial:

- Lidos: `5000`
- `linkTemplate` confirmado: `4999`
- Ainda com issue: `1`
- Erros de leitura: `0`

Um item ficou com lag/mismatch no primeiro readback e foi repatchado dentro do mesmo escopo aprovado:

- OfferId: `LIA_CZ0790-102-7`
- Confirmado após repatch: `True`
- Issue após repatch: `False`

Validação final do alvo:

- Confirmados: `5000` / `5000`
- Issue remanescente no alvo: `0`

## Post-scan global

- Antes wave1: `11410`
- Pós wave1: `10408`
- Pós wave2: `5409`
- Redução total aproximada desde início: `6001`

## Evidências

- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-regression-local-lia-11410-20260609/APPROVAL_PACKET.md`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/patch_results.jsonl`
- Readback paralelo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/readback_wave2_parallel.json`
- Repatch single mismatch: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/repatch_single_mismatch.json`
- Post-scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/post_scan/scan_missing_link_template.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/summary.json`

## Rollback

- Snapshot pré-write salvo em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-wave2-5000-20260609T/snapshot_before_patch.json`.
- Rollback possível por offerId, reaplicando valores pré-snapshot nos três campos, mediante nova aprovação.

## Próximo gate recomendado

Restam `5409` ocorrências globais. Recomendo onda final controlada para o saldo remanescente, com snapshot/readback/post-scan.
