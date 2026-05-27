# LK Shopify profile — preparação executada; token ausente

Data: 2026-05-26
Status: profile_prepared_token_pending

## Pedido

Lucas pediu executar a ativação do profile/gateway LK Shopify, sem mexer no main Hermes e sem writes em Shopify/GMC/Klaviyo/ads.

## Executado

- Criado profile isolado `/opt/data/profiles/lk-shopify` por clone seguro do `lk-growth`.
- Main Hermes não foi alterado nem reiniciado.
- `lk-growth`, `spiti` e `mordomo` não foram alterados.
- Criado/atualizado `SOUL.md` do profile com escopo LK Shopify e guardrails.
- `.env` do profile foi ajustado para evitar conflitos:
  - API server desativado.
  - API server key/host/port vazios.
  - Webhook desativado.
  - Webhook secret/host/port vazios.
- Token Telegram clonado foi removido para impedir que o novo profile suba acidentalmente usando o bot do LK Growth.

## Não executado

- Gateway LK Shopify não foi iniciado porque o token do `@LKShopify_HermesBot` não estava disponível em Doppler nem foi encontrado de forma segura nos registros locais.
- Nenhum write em Shopify/GMC/Klaviyo/ads.
- Nenhum contato/envio externo.

## Estado verificado

- `lk-shopify`: profile existe; gateway stopped.
- `default/main`: running.
- `lk-growth`: running.
- `spiti`: running.
- `mordomo`: running.

## Próximo passo seguro

Lucas precisa reenviar o token do `@LKShopify_HermesBot` ou armazená-lo em Doppler como `TELEGRAM_LK_SHOPIFY_BOT_TOKEN`. Depois disso:

1. Gravar token apenas em `/opt/data/profiles/lk-shopify/.env`.
2. Validar `getMe` sem imprimir token.
3. Subir gateway com `HERMES_HOME=/opt/data/profiles/lk-shopify`.
4. Verificar logs/processo.
5. Registrar receipt final.

## Rollback

Se necessário, remover `/opt/data/profiles/lk-shopify` ou restaurar o backup local do `.env` criado durante a preparação. Não há rollback no main Hermes porque ele não foi alterado.
