# LK GMC Local C/D Shopify Live Preview, 2026-05-12

Status: `gmc_local_cd_shopify_live_preview_readonly`

## Resumo executivo
- Produtos Merchant lidos: 23147
- Linhas local C/D avaliadas: 1302
- SKUs normalizados consultados no Shopify live: 1302
- Pacotes: {'C_local_identifier_fix': 847, 'D_local_stale_triage': 455}
- Estados: {'valid_local_listing_after_shopify_live_sku_match_noop': 1239, 'no_shopify_live_exact_sku_no_tiny_local_match_cleanup_candidate_after_pos_validation': 63}
- Merchant/Shopify/feed/POS/DB writes: 0

## Veredito operacional
- Validar por Shopify live reduziu o risco local: 1239 linhas têm SKU exato ativo no Shopify e devem ser preservadas como `noop/valid`.
- Restam 63 candidatos sem SKU exato no Shopify live e sem match Tiny local; ainda são apenas candidatos e exigem validação POS/Tiny antes de qualquer cleanup.
- 0 linhas têm SKU no Shopify mas produto não ativo; revisão manual/POS antes de mexer no local.
- 0 linhas têm sinal Tiny local sem Shopify live; revisar mapeamento antes de mexer no Merchant.

## Próximo bloco seguro
- Não executar C/D como delete/update em massa.
- Incorporar esta validação Shopify-live no classificador para que Data Spine drift não gere falsos positivos.
- Só depois montar pacote residual com rollback para os candidatos que também falharem em POS/Tiny.

## Arquivos
- JSON público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-shopify-live-preview.json`
- CSV público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-local-cd-shopify-live-preview.csv`
- CSV privado/auditoria chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-local-cd-shopify-live-preview.csv`

## Não executado
- merchant_product_delete
- merchant_product_update
- content_api_custombatch
- feed_update
- shopify_write
- database_write
- local_inventory_disable
- pos_inventory_write
- campaign_or_external_send
