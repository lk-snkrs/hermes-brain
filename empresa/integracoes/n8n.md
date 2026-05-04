# Integração — n8n

## Escopo

n8n é plataforma de automação em Docker na VPS. Inventário read-only recente indicou container rodando, mas `workflow_count` 0; não presumir automações ativas sem nova verificação.

## Secrets Doppler

- `N8N_URL`
- `N8N_INTERNAL_URL`
- `N8N_API_KEY` ou `N8N_API_TOKEN`

## Read-only

- Listar workflows, execuções e metadados via API.
- Conferir SQLite apenas para metadados, sem ler valores de credenciais.
- Verificar container/logs somente em modo read-only.

## Write

- Criar ou editar workflows apenas após especificação clara e ambiente definido.

## External-send

- Workflows que enviam WhatsApp/email/Telegram/webhook externo precisam preview Lucas antes de ativar.

## Admin/destructive

- Restart de container, alteração compose, volumes, redes, credentials, ativações em produção, deletes e upgrades exigem aprovação explícita + backup/rollback.

## Referências

- `../rotinas/_index.md` para rotinas documentadas.
- `../../areas/operacoes/rotinas/n8n-inventory.md` para inventário atual.
- `../../areas/tecnologia/contexto/hermes-docker-footprint.md` para regra Docker/VPS.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
