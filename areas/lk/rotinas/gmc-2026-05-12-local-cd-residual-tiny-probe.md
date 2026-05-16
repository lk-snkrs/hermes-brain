# LK GMC Local C/D Residual Tiny Probe, 2026-05-12

Status: `gmc_local_cd_residual_tiny_probe_readonly`

## Resumo executivo
- Residuais C/D de entrada: 63
- Estados Tiny: {'tiny_no_exact_code_match_residual_cleanup_candidate_needs_pos_source_validation': 63}
- Preservar/revisar antes de cleanup: 0
- Candidatos finais ainda dependentes de POS/source validation: 63
- Tiny/Merchant/Shopify/POS/DB writes: 0

## Veredito
- Este probe reduz a fila local para um pacote residual estrito; continua proibido deletar/alterar local em massa.
- Qualquer candidato final ainda precisa validação POS/source e rollback privado antes de aprovação de execução.

## Arquivos
- JSON público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-residual-tiny-probe.json`
- CSV público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-residual-tiny-probe.csv`
- CSV privado/auditoria chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-local-cd-residual-tiny-probe.csv`

## Não executado
- merchant_product_delete
- merchant_product_update
- tiny_write
- shopify_write
- feed_update
- database_write
- local_inventory_disable
- pos_inventory_write
- campaign_or_external_send
