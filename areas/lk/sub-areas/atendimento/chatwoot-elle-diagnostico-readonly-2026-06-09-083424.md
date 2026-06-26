# Diagnóstico Chatwoot/Elle LK — 2026-06-09-083424 -03

## Escopo

Diagnóstico read-only solicitado por Lucas em Telegram: “Seguir diagnóstico”.

Sem alterações de produção, sem criação de webhook/inbox, sem envio de mensagem, sem impressão de secrets.

## Fonte/credenciais

- Doppler helper disponível: sim.
- Projeto/config padrão: `lc-keys/prd` via helper central.
- Secrets Chatwoot/Elle encontrados por nome:
  - `CHATWOOT_BASE_URL`: presente.
  - `CHATWOOT_ACCOUNT_ID`: presente.
  - `CHATWOOT_LK_API_TOKEN`: presente.
  - `CHATWOOT_TEAM_ID`: presente.
  - `CHATWOOT_WRITE_ENABLED`: presente.
  - `ELLE_CHATWOOT_WEBHOOK_SECRET`: presente.
  - `ELLE_CHATWOOT_WEBHOOK_URL`: presente.
  - `ELLE_DRY_RUN`: presente.
  - `ELLE_KILL_SWITCH`: presente.
  - `ELLE_WEBHOOK_BASE_URL`: presente.
- `values_printed=false`.

Observação: injeção `hermes_doppler.py run --profile lk-ops` não expôs `CHATWOOT_LK_API_TOKEN`; a checagem API precisou usar `hermes_doppler.py run --` completo. Isso indica possível lacuna no inventário de secrets esperados para o profile `lk-ops`.

## Saúde pública

Endpoint: `https://chat.lkskrs.online/api`

Resultado:

```json
{
  "version": "4.14.1",
  "queue_services": "ok",
  "data_services": "failing"
}
```

Interpretação: Chatwoot está online, mas não está 100% saudável porque `data_services` está `failing`.

Endpoint: `https://elle.lkskrs.online/healthz`

Resultado:

```json
{
  "ok": true,
  "dry_run": true,
  "write_enabled": false,
  "kill_switch": true
}
```

Interpretação: Elle receiver está online em modo seguro, mas não escreve no Chatwoot. Kill switch ativo.

## API Chatwoot — conta 1

Base URL: `https://chat.lkskrs.online`  
Account ID: `1`

- Conta: HTTP 200, nome `LK Sneakers`, locale `pt_BR`.
- Labels: HTTP 200, 16 labels:
  - `carrinho-abandonado`
  - `cliente-shopify`
  - `devolucao`
  - `estoque`
  - `financeiro`
  - `humano`
  - `pedido`
  - `prazo`
  - `reclamacao`
  - `recuperacao`
  - `shopify`
  - `shopify-duplicate-review`
  - `shopify-phone-valid`
  - `troca`
  - `vip`
  - `whatsapp-api`
- Teams: HTTP 200, 2 teams:
  - ID 1: `suporte`, auto-assign true.
  - ID 2: `atendimento whatsapp`, auto-assign false.
- Inboxes: HTTP 200, 1 inbox:
  - ID 1: `Shopify Carrinho Abandonado`, `Channel::Api`.
- Webhooks: HTTP 200, 1 webhook:
  - ID 1, host `elle.lkskrs.online`, subscriptions: `message_created`.
- Integrations apps: HTTP 200, 7 apps:
  - `webhook`: enabled true.
  - `shopify`: enabled true.
  - `openai`, `dialogflow`, `google_translate`, `dashboard_apps`, `dyte`: false.

## Veredito operacional

Não está 100% conectado para atendimento WhatsApp end-to-end.

Camadas OK:

- Chatwoot responde publicamente.
- API token operacional funciona quando injetado via Doppler completo.
- Conta LK Sneakers existe e responde.
- Labels operacionais existem.
- Team `atendimento whatsapp` existe.
- Webhook `message_created` para Elle existe.
- Elle receiver está online.

Camadas pendentes/bloqueadas:

- Chatwoot health acusa `data_services=failing`.
- Não há inbox WhatsApp Cloud; inbox atual é `Channel::Api` para Shopify carrinho abandonado.
- Elle está em `dry_run=true`, `write_enabled=false`, `kill_switch=true`; portanto não escreve no Chatwoot.
- Sem evidência neste diagnóstico de eventos reais de WhatsApp chegando, até porque não há inbox WhatsApp Cloud listada.
- `lk-ops` profile não injeta `CHATWOOT_LK_API_TOKEN` pelo inventário restrito; usar env completo funcionou.

## Próximos passos sugeridos

1. Diagnosticar `data_services=failing` no Chatwoot core por SSH/Docker read-only, se Lucas aprovar escopo de infraestrutura.
2. Conectar WhatsApp Cloud API inbox em Chatwoot somente com aprovação explícita e dados Meta/WABA.
3. Antes de qualquer resposta pública, manter Elle como copiloto interno: private notes/labels, sem customer-visible sends.
4. Se Lucas aprovar modo copiloto interno, destravar gradualmente: `kill_switch=false` e depois `write_enabled=true` apenas para notas privadas, com verificação e rollback.
5. Corrigir inventário de secrets do profile `lk-ops` para incluir `CHATWOOT_LK_API_TOKEN` caso seja o padrão esperado.

## Guardrails

- Sem promessa de estoque/pronta entrega; qualquer disponibilidade deve ir para `lk-stock`/Tiny.
- Sem mensagens externas, automações públicas, webhook writes, inbox WhatsApp ou produção sem aprovação explícita.
