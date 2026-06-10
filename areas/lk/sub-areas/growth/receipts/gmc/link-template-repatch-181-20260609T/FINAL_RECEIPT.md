# FINAL RECEIPT — GMC LIA link_template repatch 181 — 2026-06-09

- Timestamp UTC: 2026-06-09T10:48:55.236513+00:00
- Aprovação: Lucas `Aprovo` no Telegram após packet `gmc-link-template-repatch-181-20260609`.
- Write externo: sim, Google Merchant Center / Merchant API `productInputs.patch`.
- Escopo aprovado: 181 offerIds do CSV; campos `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`.
- Shopify alterado: não.
- Preço/estoque/título/GTIN/imagem/campanhas alterados: não.

## Resultado do patch

- Targets: `181`
- Patch OK: `181`
- Falhas: `0`
- Skipped: `0`
- Processados: `181`

## Readback alvo

Readback inicial do executor:

- Confirmados com `linkTemplate`: `143`
- Ainda com issue no readback inicial: `38`

Readback posterior alvo:

- Confirmados com `linkTemplate`: `161` / `181`
- Ainda com `mhlsf_full_missing_valid_link_template`: `20`
- Erros de leitura: `0`

## Post-scan global

- Scan pós-write encontrou `11410` itens com `mhlsf_full_missing_valid_link_template`.
- Destes, `22` pertencem ao alvo aprovado de 181.
- Itens novos/não aprovados neste write: `11388`.

Interpretação: o write aprovado funcionou para o alvo imediato, mas houve/foi revelada uma regressão ampla no data source local/LIA (`10636384718`). Não foi feito patch fora dos 181 aprovados.

## Evidências

- Approval packet: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-repatch-181-20260609/APPROVAL_PACKET.md`
- Target CSV: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-repatch-181-20260609/link_template_targets_181.csv`
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/patch_results.jsonl`
- Readback executor: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/readback_after_patch.json`
- Readback posterior: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/targeted_readback_now.json`
- Post-scan global: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/post_scan/scan_missing_link_template.json`

## Rollback

- Snapshot pré-write salvo em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/snapshot_before_patch.json`.
- Rollback possível por offerId, reaplicando os valores pré-snapshot nos três campos, com nova aprovação se necessário.

## Próximo gate recomendado

Gerar/validar packet separado para a regressão ampla `mhlsf_full_missing_valid_link_template` no data source local/LIA. Qualquer patch além dos 181 exige nova aprovação escopada.
