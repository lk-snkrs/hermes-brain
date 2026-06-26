# Elle / Chatwoot — observação de eventos reais pós-ativação

Data: 2026-06-09T13:53:40Z
Área: LK / Atendimento / Elle / Chatwoot
Modo: read-only, sem tocar cliente real

## Escopo

Lucas pediu “seguir” após o canário pós-ativação. Foi feita observação read-only de mensagens/eventos recentes no Chatwoot e logs da Elle/Sidekiq para confirmar se o webhook real já estava batendo na Elle.

## Janela observada

Desde: `2026-06-09T13:38:00Z`.

## Chatwoot — metadados de mensagens

Consulta Rails read-only em `Message` encontrou:

- total recente: `2`
- tipos: `outgoing=2`
- private: `true=2`
- conversa: real, inbox `1`, labels Shopify/pedido.

Interpretação: eram notas privadas/automação operacional já existente, não mensagem inbound de cliente.

## Sidekiq / WebhookJob

Logs filtrados do `chatwoot-sidekiq-1` desde `13:38Z` encontraram:

- `6` entradas relacionadas a WebhookJob para `elle.lkskrs.online`.
- 2 jobs foram enfileirados para a Elle.
- 2 jobs foram executados.
- 2 jobs foram marcados como performed.

Sem payload sensível salvo no receipt.

## Elle — log interno

`docker logs` stdout do container não mostra eventos, mas o arquivo interno existe:

- `/var/log/elle/events.jsonl`

Resumo desde `13:38Z`:

- total: `3`
- `ignored=2`
- `processed=1`
- motivos: `event_filter=2`
- tipos observados: `outgoing=2`

Entradas relevantes:

- `2026-06-09T13:39:52Z`: `ignored`, `event=message_created`, `message_type=outgoing`.
- `2026-06-09T13:39:52Z`: `ignored`, `event=message_created`, `message_type=outgoing`.
- `2026-06-09T13:41:09Z`: smoke sintético, `processed`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, conversa fake `990001`, `HTTPError` esperado.

## Código/filtro confirmado

`/opt/elle-chatwoot/app.py` filtra eventos assim:

- processa somente `event == message_created`;
- processa somente `message_type == incoming`;
- ignora `private=true`;
- ignora `content_type == private_note`.

Isso explica o comportamento correto: os dois eventos reais eram `outgoing/private`, então a Elle recebeu e ignorou.

## Status

- Webhook real Chatwoot → Elle está entregando eventos.
- Elle está ativa e com writes internos habilitados.
- Ainda não houve mensagem real `incoming` de cliente desde a ativação.
- Nenhuma conversa real foi alterada por esta observação.

## Próximo passo seguro

Aguardar a primeira mensagem real inbound no Chatwoot para verificar criação de nota privada/labels/assignment pela Elle; ou aprovar explicitamente um teste controlado com conversa de teste real.

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhum WhatsApp enviado.
- Nenhuma nota/label/assignment criada manualmente.
- Nenhuma alteração em webhook/inbox/container/Chatwoot/Shopify/Tiny.

`values_printed=false`.
