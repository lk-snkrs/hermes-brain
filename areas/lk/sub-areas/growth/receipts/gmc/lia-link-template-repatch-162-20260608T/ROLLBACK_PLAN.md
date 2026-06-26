# Rollback Plan — GMC LIA linkTemplate repatch 162 — 2026-06-08

Escopo aprovado: repatch dos 162 itens LIA com `mhlsf_full_missing_valid_link_template`.

Snapshot pré-write: `snapshot_before_patch.json`.
Resultados: `patch_results.jsonl`.
Readback: `readback_after_patch.json`.

Rollback lógico:
1. Usar `snapshot_before_patch.json` para identificar `offerId`, `dataSource`, `linkTemplate`, `mobileLinkTemplate`, `adsRedirect` anteriores.
2. Se algum campo anterior tinha valor, reexecutar `productInputs.patch` com os valores anteriores e readback.
3. Se o valor anterior era ausente/nulo, rollback operacional recomendado é remover/corrigir a origem do overwrite no feed/dataSource ou reprocessar item pela fonte original; não executar delete de produto sem aprovação específica.
4. Registrar readback pós-rollback.

Observação: o patch aprovado só adiciona `linkTemplate`, `mobileLinkTemplate` e `adsRedirect`; não altera preço, estoque, título, GTIN, Shopify ou campanhas.
