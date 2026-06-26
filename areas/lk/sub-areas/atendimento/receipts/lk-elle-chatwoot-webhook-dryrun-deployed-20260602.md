# Receipt — Elle Chatwoot webhook dry-run deployed

- Data: 2026-06-02
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: LK Sneakers / ID `1`
- Serviço: Elle MVP 1C webhook receiver
- URL pública: `https://elle.lkskrs.online`
- VPS: `lc.vps` / `72.60.150.124`
- Diretório remoto: `/opt/elle-chatwoot`

## Ações executadas

1. Receiver Elle implantado em Docker separado em `/opt/elle-chatwoot`.
2. Traefik roteando `https://elle.lkskrs.online` para o container `elle-chatwoot`.
3. Health check público validado:
   - `GET https://elle.lkskrs.online/healthz` → 200
   - estado: `dry_run=true`, `write_enabled=false`, `kill_switch=true`
4. Webhook criado no Chatwoot:
   - nome: `Elle MVP 1C dry-run`
   - subscriptions: `message_created`
   - host da URL: `elle.lkskrs.online`
   - id observado: `1`
5. Smoke test sintético enviado ao receiver:
   - status HTTP: 200
   - resultado: `processed`
   - labels retornadas: `pedido`, `whatsapp-api`
   - action status: `dry_run_or_kill_switch`

## Segredos/configuração

Fonte de verdade: Doppler `lc-keys/prd`.

Secret names usados, sem valores no Brain:

- `ELLE_CHATWOOT_WEBHOOK_SECRET`
- `ELLE_CHATWOOT_WEBHOOK_URL`
- `CHATWOOT_LK_API_TOKEN`
- `CHATWOOT_BASE_URL`
- `CHATWOOT_ACCOUNT_ID`
- `CHATWOOT_TEAM_ID`
- `ELLE_DRY_RUN`
- `CHATWOOT_WRITE_ENABLED`
- `ELLE_KILL_SWITCH`

## Guardrails efetivos no deploy atual

- `ELLE_DRY_RUN=true`
- `CHATWOOT_WRITE_ENABLED=false`
- `ELLE_KILL_SWITCH=true`
- Nenhuma mensagem pública implementada no receiver.
- O webhook processa apenas `message_created` incoming e ignora private notes/outbound/eventos não previstos.
- Idempotência local por hash/evento em `/opt/elle-chatwoot/data`.
- Logs redigem e-mail/telefone/token-like patterns.

## O que NÃO foi feito

- Nenhuma mensagem pública enviada.
- Nenhum write real em conversa feito, porque dry-run + kill-switch estão ativos.
- Nenhuma alteração em Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema.
- Não habilitado auto-reply, Captain/IA, chatbot ou automação customer-visible.

## Próxima etapa possível

Depois de observar eventos reais em dry-run, Lucas pode aprovar separadamente a liberação de writes internos somente:

1. `ELLE_KILL_SWITCH=false`
2. `CHATWOOT_WRITE_ENABLED=true`
3. `ELLE_DRY_RUN=false`

Mesmo nessa etapa, escopo permitido continua restrito a nota privada, labels e assignment para `atendimento whatsapp`; nenhuma resposta pública.
