# LK GMC — Missing color high-confidence — aggregate 2026-05-31

Status: `gmc_missing_color_high_confidence_batch_partially_applied_verified`

## Escopo aprovado
- 795 linhas high-confidence de cor do preview 2026-05-28.
- Campo alterado: `productAttributes.color` somente.
- Superfície: Merchant API ProductInputs v1.
- Sem write em preço, imagem, título, availability, GTIN, Shopify, Tiny ou campanhas.

## Resultado agregado
- Produtos tentados: 795/795
- Aplicados com sucesso: 776
- Falhas: 19
- Motivos de falha: {'http_404_not_found': 13, 'http_400_uploaded_other_path': 6}

## Recheck imediato GMC
- Missing color products após lote: 246
- Required attr counts após lote: {'color': 246, 'size': 241, 'age group': 211, 'gender': 211, 'price': 23}
- Observação: itemLevelIssues do GMC podem levar horas/dias para estabilizar totalmente.

## Falhas para triagem manual
- `U204L4HH-42` — Cinza — 404 Product not found
- `3128383465433270909` — Branco — 400 uploaded through another path/data source
- `U204L4HH-39` — Cinza — 404 Product not found
- `U204L4HH-37` — Cinza — 404 Product not found
- `18247085260254546037` — Azul — 404 Product not found
- `U204L4HH-35` — Cinza — 404 Product not found
- `8959342836169786069` — Verde — 400 uploaded through another path/data source
- `U204L4HH-34` — Cinza — 404 Product not found
- `U204L4HH-44` — Cinza — 404 Product not found
- `5462073588214018584` — Laranja — 400 uploaded through another path/data source
- `U204L4HH-40` — Cinza — 404 Product not found
- `U204L4HH-36` — Cinza — 404 Product not found
- `10312083433143971915` — Azul — 400 uploaded through another path/data source
- `U204L4HH-38` — Cinza — 404 Product not found
- `336032976649007126` — Off White — 400 uploaded through another path/data source
- `1228945336873866536` — Branco — 400 uploaded through another path/data source
- `U204L4HH-41` — Cinza — 404 Product not found
- `U204L4HH-43` — Cinza — 404 Product not found
- `11362592317382846242` — Branco — 404 Product not found

## Rollback privado
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-31-missing-color-high-confidence-fast-apply-rollback-20260531T165845Z.json`
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-31-missing-color-high-confidence-fast-apply-rollback-20260531T170812Z.json`

## Progress files
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-31-missing-color-high-confidence-fast-apply-progress-20260531T165845Z.jsonl`
- `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-31-missing-color-high-confidence-fast-apply-progress-20260531T170812Z.jsonl`
