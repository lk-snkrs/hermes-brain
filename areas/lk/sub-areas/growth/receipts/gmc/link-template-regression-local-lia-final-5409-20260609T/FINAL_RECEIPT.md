# FINAL RECEIPT — GMC link_template regressão Local/LIA — Onda final + cleanup — 2026-06-09

- Timestamp UTC: 2026-06-09T14:06:16.173546+00:00
- Aprovação: Lucas `seguir` no Telegram para onda final do saldo remanescente.
- Write externo: sim, Google Merchant Center / Merchant API `productInputs.patch`.
- Escopo principal: 5.409 offerIds remanescentes do packet `gmc-link-template-regression-local-lia-11410-20260609`.
- Campos alterados: `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`.
- Shopify alterado: não.
- Preço/estoque/título/GTIN/imagem/campanhas alterados: não.

## Resultado da onda final

- Targets principais: `5409`
- Patch OK: `5409`
- Patch fail: `0`
- Skipped: `0`

Readback paralelo inicial:

- Lidos: `5409`
- Confirmados: `5272`
- Ainda com issue: `137`
- Erros leitura: `0`

## Cleanup dentro do mesmo issue/packet

- Repatch dos 137 mismatches: `137` patch OK; `57` confirmados imediatos; `80` ainda com issue.
- Reread dos 80 restantes: `1` confirmados; `79` ainda com issue.
- Repatch pós-scan de 37 itens em escopo final: `37` OK; `36` confirmados imediatos; `1` ainda com issue.
- Repatch global de 12 itens do packet original: `12` OK; `1` confirmados imediatos; `11` ainda com issue.

## Post-scan global final

- Antes da correção ampla: `11410`
- Pós wave1: `10408`
- Pós wave2: `5409`
- Pós onda final + cleanup: `17`
- Itens finais dentro do packet original: `17`

Interpretação: a correção em massa foi aplicada e praticamente zerou o problema. O residual final pequeno indica lag/sobrescrita pontual do data source local/LIA; não é falha de patch em massa.

## Evidências

- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/snapshot_before_patch.json`
- Patch results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/patch_results.jsonl`
- Readback final paralelo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/readback_final_parallel.json`
- Repatch mismatches: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/repatch_mismatches.json`
- Reread remaining: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/reread_remaining.json`
- Repatch postscan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/repatch_postscan_48.json`
- Repatch global remaining: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/repatch_global_remaining_12.json`
- Post-scan final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/post_scan/scan_missing_link_template_retry.json`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/summary.json`

## Rollback

- Snapshot pré-write salvo.
- Rollback possível por offerId, reaplicando valores pré-snapshot nos três campos, mediante nova aprovação.

## Próximo follow-up

- Recheck read-only em algumas horas / D+1 para confirmar se o residual final estabiliza em zero ou volta a crescer.
- Se residual persistir, tratar como fonte/data source governance, não como mais um bulk patch cego.
