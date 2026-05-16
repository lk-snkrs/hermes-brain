# LK GMC P1-B Availability Tiny Packet, 2026-05-12

Status: `gmc_p1_availability_tiny_packet_ready_no_write`

## Resumo executivo
- Produtos online com diagnóstico `availability` ausente: 5
- Ready para apply se Lucas aprovar: 0
- Proposta `in stock`: 0
- Proposta `out of stock`: 0
- Bloqueados/revisão: 5
- Estados: {'blocked_review_no_official_deposit': 5}
- Merchant/Tiny/Shopify/feed/DB/POS writes: 0

## Fonte e regra
- `fact_tiny_stock`: Tiny `codigo` exato + depósito oficial `LK | CONTROLE ESTOQUE`.
- Shopify local é apenas evidência auxiliar, não verdade de estoque.
- `availability` só entra como proposta quando Tiny tem `codigo` exato e saldo do depósito oficial.

## Arquivos
- JSON público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.json`
- CSV público: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-2026-05-12-p1-availability-tiny-packet.csv`
- CSV privado/auditoria chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-p1-availability-tiny-packet-full-private.csv`
- Cache Tiny privado chmod 600: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_reconciliation/lk-gmc-2026-05-12-p1-availability-tiny-packet-tiny-stock-cache.jsonl`

## Approval wording
`Aprovo aplicar availability no Merchant para os 0 itens ready do packet P1-B usando Tiny oficial: 0 in stock e 0 out of stock; sem alterar Tiny/Shopify/feed/DB/POS/campanhas, com rollback snapshot privado antes do write.`

## Não executado
- merchant_product_update
- merchant_product_insert_upsert
- tiny_write
- shopify_write
- feed_update_or_fetch
- database_write
- pos_write
- campaign_or_external_send
