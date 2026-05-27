# LK Shopify profile/gateway — ativação concluída

Data: 2026-05-26
Status: active

## Pedido

Lucas aprovou concluir a ativação do `@LKShopify_HermesBot` usando o token enviado, sem mexer no main Hermes e sem writes em Shopify/GMC/Klaviyo/ads.

## Executado

- Token gravado somente no `.env` do profile `/opt/data/profiles/lk-shopify`.
- `.env` mantido com permissão `0600`.
- Token salvo em Doppler como `TELEGRAM_LK_SHOPIFY_BOT_TOKEN` no projeto/config `lc-keys/prd`.
- `getMe` validado com sucesso para username `LKShopify_HermesBot`, sem imprimir token.
- Gateway iniciado com `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- API server e webhook explicitamente desativados no ambiente do profile.
- Logs confirmaram:
  - Active profile: `lk-shopify`.
  - Telegram conectado em polling mode.
  - Gateway rodando com 1 plataforma.

## Verificação de isolamento

Gateways observados após ativação:

- default/main: running, `HERMES_HOME=/opt/data`.
- lk-growth: running, `HERMES_HOME=/opt/data/profiles/lk-growth`.
- lk-shopify: running, `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- spiti: running.
- mordomo: running.

Main Hermes não foi reiniciado nem re-tokenado.

## Não executado

- Nenhum write em Shopify.
- Nenhum write em GMC/feed.
- Nenhum write em Klaviyo/ads.
- Nenhum envio externo/campanha.
- Nenhum Docker/VPS/Traefik/container alterado.
- Nenhum watchdog/cron criado nesta etapa.

## Próximo passo operacional

Lucas deve abrir `t.me/LKShopify_HermesBot` e enviar `/start`. Se quiser que esse bot tenha canal home próprio, usar `/sethome` dentro do chat dele.

## Rollback

Para rollback:

1. Parar apenas o processo gateway com `HERMES_HOME=/opt/data/profiles/lk-shopify`.
2. Remover/limpar `TELEGRAM_BOT_TOKEN` do `.env` do profile ou restaurar backup local.
3. Opcional: rotacionar o token no BotFather e atualizar Doppler.
4. Main Hermes permanece independente.
