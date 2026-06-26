# Receipt — Elle official public send via Chatwoot Messages API

Data: 2026-06-15
Origem: Lucas Telegram
Área: LK / Atendimento / Elle / Chatwoot

## Pedido
Lucas corrigiu o fluxo: sempre que houver próximo passo seguro, executar; para mensagem oficial ao cliente, usar envio oficial pelo Chatwoot.

## Documentação consultada
Fonte pública oficial Chatwoot:

- `https://developers.chatwoot.com/api-reference/messages/create-new-message`

Contrato relevante:

- Endpoint: `POST /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages`
- Header: `api_access_token`
- Texto público: JSON com `content`, `message_type=outgoing`, `private=false`
- Anexos: `multipart/form-data` com `attachments[]`
- WhatsApp templates: `template_params` com templates pré-aprovados no WhatsApp Business Manager

## Alteração aplicada
Arquivo extraído do container vivo `elle-chatwoot:/app/app.py`, patchado e aplicado de volta ao container.

Mudança:

- criado helper `send_official_chatwoot_public_reply(conversation_id, reply)`;
- todas as respostas públicas da Elle agora passam por esse helper;
- payload oficial usa:
  - `message_type: outgoing`
  - `private: false`
  - `content_attributes.elle_generated: true`
  - `content_attributes.official_channel: chatwoot_messages_api`

## Segurança / limites

- Nenhuma mensagem manual enviada para cliente durante esta manutenção.
- Nenhuma consulta/alteração em Tiny, Shopify ou estoque.
- Estoque/pronta entrega continua dono `lk-stock`.
- Labels continuam somente na conversa; não há tag automática no contato/cliente.

## Backup / rollback

Backup local:

- `/opt/data/backups/elle-chatwoot-official-send-20260615/app.py.before`
- `/opt/data/backups/elle-chatwoot-official-send-20260615/app.py.after`

Hashes:

- before: `cccab802976724b430c3387698a680a8e802882ec90da2fc5a7902fe2242e7e0`
- after: `4f78a9e111f92762d275e914c41b8f02e5097dfea0b5fc620f98da59b505d1b5`

Rollback rápido:

```bash
docker cp /opt/data/backups/elle-chatwoot-official-send-20260615/app.py.before elle-chatwoot:/app/app.py
docker exec elle-chatwoot python -m py_compile /app/app.py
docker restart elle-chatwoot
```

## Verificação executada

Local/no-send smoke:

- import do app patchado;
- monkeypatch de `chatwoot()`;
- chamada de `send_official_chatwoot_public_reply(999, 'Olá, teste')`;
- confirmado endpoint `/api/v1/accounts/1/conversations/999/messages`;
- confirmado payload `message_type=outgoing`, `private=false`, `elle_generated=true`, `official_channel=chatwoot_messages_api`.

Deploy:

```bash
docker cp /opt/data/tmp/elle_chatwoot_live_extract/app.py elle-chatwoot:/app/app.py
docker exec elle-chatwoot python -m py_compile /app/app.py
docker restart elle-chatwoot
```

Health/readback:

- `https://elle.lkskrs.online/healthz`: HTTP 200
- flags: `dry_run=false`, `kill_switch=false`, `public_reply_enabled=true`, `catalog_cache_present=true`, `catalog_stock_included=false`
- container: `running=true`
- readback interno: helper presente, marker `official_channel` presente, endpoint Messages API presente
- logs pós-restart: sem erro impresso nos últimos 2 minutos

## Observação técnica

O compose/source `/opt/elle-chatwoot` apontado no label Docker não está presente no filesystem desta sessão. A aplicação foi feita como hotpatch controlado no container vivo, com backup local e rollback explícito. Em próxima janela, vale reconciliar o source persistente/compose para evitar perda em recriação de container.
