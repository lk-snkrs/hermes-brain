# APPROVALS — LK Trend Hermes

## Permanente

Read-only, documentação local, pesquisa, síntese, score e previews internos são permitidos.

## Exige aprovação atual de Lucas

- Ativar gateway Telegram do profile.
- Criar cron recorrente.
- Publicar conteúdo.
- Criar/editar Shopify.
- Alterar preço, estoque, SKU, tag, collection, theme ou feed.
- Escrever em Tiny/Merchant/Klaviyo/Meta/Google Ads.
- Contatar fornecedor ou cliente.
- Comprar, reservar, negociar ou prometer disponibilidade.

## Aprovação mínima para ativação Telegram

Lucas deve aprovar explicitamente:

> Ativar o profile `lk-trends` no Telegram com bot dedicado, sem API/webhook, sem cron e sem writes externos.

## Rollback

- Parar gateway do profile `lk-trends`.
- Remover/zerar token do `.env` do profile.
- Manter Brain docs e receipts para auditoria.
