# APPROVALS — LK Shopify Hermes

## Estado

A documentação e o approval packet foram preparados. A ativação de profile/gateway/watchdog requer liberação de runtime nesta sessão, pois o guardrail bloqueou terminal.

## Aprovação necessária para ativar o bot

Escopo proposto:

1. Criar/usar profile `/opt/data/profiles/lk-shopify`.
2. Configurar token Telegram apenas no `.env` desse profile.
3. Limpar API/webhook herdados para evitar conflitos.
4. Subir gateway isolado do LK Shopify.
5. Criar watchdog silent-OK se autorizado.
6. Verificar `getMe`, logs e ausência de segredos em docs.

## Bloqueios permanentes sem aprovação específica

- Shopify writes.
- Theme/dev-theme upload.
- GMC/feed writes.
- Ads/Klaviyo/campanhas.
- Produção/publish.
- Cliente/WhatsApp/email externo.

## Frase de aprovação sugerida

“Pode ativar o profile/gateway LK Shopify com o token enviado, sem mexer no main Hermes e sem writes em Shopify/GMC/Klaviyo/ads.”

## Rollback de ativação

- Parar gateway `lk-shopify`.
- Remover token do `.env` do profile ou rotacionar no BotFather.
- Restaurar backups de `.env`/`config.yaml`.
- Desabilitar watchdog/cron do profile.
- Confirmar main Hermes e LK Growth intactos.