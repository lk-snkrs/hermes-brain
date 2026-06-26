# Handoff — GMC link_template regressão Local/LIA onda final executada — 2026-06-09

- Timestamp UTC: 2026-06-09T14:06:16.173546+00:00
- Write externo: sim, GMC Merchant API.
- Aprovação: Lucas `seguir`.
- Escopo: onda final 5409 offerIds + cleanup residual dentro do packet original; campos `linkTemplate`, `mobileLinkTemplate`, `adsRedirect`.
- Patch principal: 5409/5409 OK; falhas 0.
- Readback principal: 5272/5409 confirmados; remaining issue 137.
- Cleanup executado: repatch 137, reread 80, repatch 37, repatch 12.
- Post-scan final: 17 issues remanescentes; 17 dentro do packet original.
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-regression-local-lia-final-5409-20260609T/FINAL_RECEIPT.md`
- Próximo: recheck read-only em algumas horas/D+1; se residual persistir, investigar data source overwrite.
