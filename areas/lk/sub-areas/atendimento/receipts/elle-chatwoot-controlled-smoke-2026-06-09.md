# Elle / Chatwoot — smoke test controlado em dry-run

Data: 2026-06-09
Área: LK / Atendimento / Elle / Chatwoot
Modo: smoke test sintético, `dry_run=true`, sem write público

## Aprovação/escopo

Lucas pediu “Seguir” após o gate anterior. Pela regra operacional, isso permitiu continuar o fluxo seguro, sem autorizar produção/write externo customer-visible.

Escopo executado:

- POST sintético controlado para o receiver da Elle usando `ELLE_CHATWOOT_WEBHOOK_URL` do Doppler.
- Payload falso com `event=message_created`, `message_type=incoming`, IDs sintéticos e contato `.invalid`.
- Nenhuma chamada de write ao Chatwoot API.
- Nenhuma mensagem pública ao cliente.

## Secrets

Fonte: Doppler `lc-keys/prd`.

Usado em processo:

- `ELLE_CHATWOOT_WEBHOOK_URL`: presente.

Não impresso/salvo:

- URL completa do receiver.
- Secret/path/token.
- Valores de token.

`values_printed=false`.

## Resultado do smoke test

Resposta do receiver Elle:

- HTTP: `200`.
- `ok=true`.
- `status=processed`.
- `dry_run=true`.
- `write_enabled=false`.
- `kill_switch=true`.
- Labels retornadas: `pedido`, `whatsapp-api`.
- Handoff retornado: `false`.

## Verificação pós-smoke

Health público:

- Chatwoot `/api`: HTTP `200`.
- `queue_services=ok`.
- `data_services=ok`.
- Elle `/healthz`: HTTP `200`.
- Elle:
  - `ok=True`.
  - `dry_run=True`.
  - `write_enabled=False`.
  - `kill_switch=True`.

Probe read-only no Chatwoot:

- Conversa sintética ID `990000`: HTTP `404`.
- Interpretação: o smoke não criou conversa real nem write detectável no Chatwoot.

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhuma nota privada real criada.
- Nenhum label real aplicado.
- Nenhum assignment real aplicado.
- Nenhuma conversa real criada.
- Nenhum webhook/inbox alterado.
- Nenhuma alteração em VPS/Docker/Traefik.
- Nenhuma alteração em Shopify, Tiny, estoque, preço, pedido, campanha ou WhatsApp send.

## Próximo gate

Se Lucas aprovar explicitamente, o próximo passo operacional é habilitar **copiloto interno real**, ainda sem resposta pública:

1. Manter ausência de método de resposta pública.
2. Destravar somente writes internos:
   - nota privada;
   - labels;
   - assignment para `atendimento whatsapp`.
3. Exigir rollback claro:
   - `ELLE_KILL_SWITCH=true`;
   - `CHATWOOT_WRITE_ENABLED=false`;
   - `ELLE_DRY_RUN=true`.

Sem nova aprovação explícita, manter Elle em `dry_run=true`, `write_enabled=false`, `kill_switch=true`.
