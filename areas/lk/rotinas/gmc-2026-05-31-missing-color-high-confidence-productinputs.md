# LK GMC — Missing color high-confidence apply — 2026-05-31

Status: `gmc_missing_color_high_confidence_dry_run_ready`
Modo: `dry-run`

## Escopo
- Campo alterado: `productAttributes.color` somente.
- Linhas: 795 high-confidence do preview de 2026-05-28.
- Superfície: Merchant API v1 ProductInputs.
- Não alterado: preço, availability, title, image, GTIN, Shopify, Tiny, campanhas.

## Resultado
- Linhas fonte: 1
- Execução: {}
- Verificação: {}
- Match de cor esperado: 0/0

## Rollback privado
- Não criado no dry-run.

## Não executado
- price_update
- availability_update
- title_update
- image_update
- gtin_update
- feed_fetch_or_reprocess
- shopify_write
- tiny_write
- campaign_or_message_send
