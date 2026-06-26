# LK Chatwoot — WhatsApp Template Builder deploy

Data: 2026-06-03 16:21 UTC
Status: `deployed_custom_image_with_rollback_containers_retained`

## Escopo aprovado

Lucas aprovou mudar a versão atual do Chatwoot com rollback, com o entendimento operacional de que o Chatwoot ainda não está em uso crítico.

## Produção antes do deploy

- Domínio: `chat.lkskrs.online`
- Chatwoot versão pública: `4.14.1`
- Containers originais:
  - `chatwoot-rails-1` usando `chatwoot/chatwoot:latest`
  - `chatwoot-sidekiq-1` usando `chatwoot/chatwoot:latest`
- Health antes do deploy registrado em backup: `/api` respondeu `version=4.14.1`, `queue_services=ok`, `data_services=failing`.

## Imagem customizada

- Base: Chatwoot tag `v4.14.1`
- Branch build local: `/opt/data/chatwoot-v4.14.1-build`, branch `lk/whatsapp-template-builder-prod`
- Commit aplicado: `be6ec66 feat: add whatsapp template builder`
- Imagem criada: `lk-chatwoot:whatsapp-template-builder-be6ec66`
- Image ID: `sha256:902accbef71bc92a03ac96977329004973b1e81d9e183869169338513b470191`

## Deploy executado

- `chatwoot-rails-1` e `chatwoot-sidekiq-1` antigos foram parados e renomeados para rollback:
  - `chatwoot-rails-1.pre-20260603-161825Z`
  - `chatwoot-sidekiq-1.pre-20260603-161825Z`
- Novos containers ativos:
  - `chatwoot-rails-1` com `lk-chatwoot:whatsapp-template-builder-be6ec66`
  - `chatwoot-sidekiq-1` com `lk-chatwoot:whatsapp-template-builder-be6ec66`
- Redis/Postgres/volumes foram preservados.
- Traefik labels e porta `127.0.0.1:3000->3000` foram mantidos no novo Rails.

## Verificações pós-deploy

- `docker ps`: Rails e Sidekiq ativos com a imagem customizada.
- `https://chat.lkskrs.online/api`: respondeu HTTP 200 com `version=4.14.1`, `queue_services=ok`, `data_services=failing`.
- Rotas confirmadas dentro do container Rails:
  - `GET /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates`
  - `POST /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates`
  - `POST /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates/sync`
- `/app/.git_sha`: `be6ec66e8f7c646a4f38ece31e764af8678c0465`
- Arquivo do service presente: `app/services/whatsapp/template_payload_builder.rb`
- Assets de produção incluem a UI do template builder.
- Logs recentes Rails: Puma subiu, Postgres aceitou conexão, `/api` completou `200 OK`. Warnings observados não bloqueantes: RubyLLM legacy API e redis-namespace deprecation.

## Rollback

Backup/rollback reference:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/chatwoot-deploy-backup-20260603-161825Z/ROLLBACK.md`

Rollback rápido:

```bash
docker stop chatwoot-rails-1 chatwoot-sidekiq-1 || true
docker rm chatwoot-rails-1 chatwoot-sidekiq-1 || true
docker rename chatwoot-rails-1.pre-20260603-161825Z chatwoot-rails-1 || true
docker rename chatwoot-sidekiq-1.pre-20260603-161825Z chatwoot-sidekiq-1 || true
docker start chatwoot-redis-1 chatwoot-postgres-1 chatwoot-sidekiq-1 chatwoot-rails-1
curl -fsS https://chat.lkskrs.online/api
```

## Segurança / não feito

- Nenhum template foi criado na Meta.
- Nenhuma mensagem WhatsApp foi enviada.
- Nenhuma campanha foi ativada.
- Nenhuma feature flag de campanha WhatsApp foi alterada.
- Arquivos raw com env/secrets gerados temporariamente foram removidos do Brain após o deploy. Mantidos apenas summaries redigidos e rollback sem secrets.

## Observação operacional

O `data_services=failing` já apareceu no predeploy e permaneceu pós-deploy. O Rails responde `/api` com 200 e as rotas novas existem, mas esse status deve ser tratado como alerta operacional separado se o Chatwoot passar a ser usado criticamente.
