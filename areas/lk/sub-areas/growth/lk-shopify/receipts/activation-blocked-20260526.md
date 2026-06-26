# LK Shopify profile/gateway — ativação bloqueada pelo guardrail

Data: 2026-05-26
Status: approval_received_but_runtime_blocked

## Pedido limpo

Lucas aprovou: ativar o profile/gateway LK Shopify com o token enviado, sem mexer no main Hermes e sem writes em Shopify/GMC/Klaviyo/ads.

## Estado verificado antes do bloqueio

- Profiles existentes listados em modo read-only.
- `lk-shopify` ainda não aparecia na lista de profiles.
- Gateways em execução observados antes do bloqueio:
  - default/main: running
  - lk-growth: running
  - spiti: running
  - mordomo: running
- PRD do LK Shopify já existe em `areas/lk/sub-areas/growth/projetos/prd-lk-shopify-hermes-bot-20260526.md`.

## Bloqueio

A tentativa de continuar a ativação via runtime/terminal foi bloqueada pelo guardrail de roteamento, mesmo com a aprovação textual do Lucas. Nenhum profile foi criado, nenhum `.env` foi alterado, nenhum gateway foi iniciado e nenhum write externo foi feito.

## Escopo que continua aprovado pelo Lucas

- Criar profile `/opt/data/profiles/lk-shopify`.
- Configurar apenas o token Telegram do bot LK Shopify no `.env` do profile.
- Neutralizar API server e webhook herdados no profile para evitar conflitos.
- Subir gateway somente com `HERMES_HOME=/opt/data/profiles/lk-shopify`.
- Não mexer no main Hermes.
- Não executar writes em Shopify/GMC/Klaviyo/ads.

## Rollback planejado

Se a ativação for liberada:

1. Parar apenas o gateway do profile `lk-shopify`.
2. Restaurar backups de `config.yaml`, `.env` e `auth.json` do profile, se criados.
3. Remover token do `.env` do profile ou rotacionar no BotFather se necessário.
4. Não tocar no main Hermes.

## Próximo passo

Liberar runtime/terminal para este escopo ou executar a ativação a partir de um canal/profile cujo guardrail permita profile/gateway operations.