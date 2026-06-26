# Elle / Chatwoot — dry-run controlado pós-credenciais WhatsApp

Data: 2026-06-09
Área: LK / Atendimento / Elle / Chatwoot
Modo: validação segura, sem mensagem pública

## Contexto

Lucas aprovou: atualizar Doppler + validar conexão sem mensagem pública.

Foi detectada e corrigida uma separação de papéis de secrets:

- `ELLE_CHATWOOT_WEBHOOK_URL` / `ELLE_CHATWOOT_WEBHOOK_SECRET`: webhook da Elle recebendo eventos `message_created` do Chatwoot.
- `CHATWOOT_WHATSAPP_WEBHOOK_URL` / `CHATWOOT_WHATSAPP_WEBHOOK_SECRET`: endpoint WhatsApp do Chatwoot informado por Lucas.

Nenhum valor secreto foi salvo neste receipt.
`values_printed=false`.

## Doppler

Projeto/config: `lc-keys/prd`.

Secrets presentes/confirmados:

- `ELLE_CHATWOOT_WEBHOOK_URL`: presente, host `elle.lkskrs.online` confirmado via Chatwoot API.
- `ELLE_CHATWOOT_WEBHOOK_SECRET`: presente.
- `CHATWOOT_WHATSAPP_WEBHOOK_URL`: presente, sem caracteres mascarados, host `chat.lkskrs.online` confirmado.
- `CHATWOOT_WHATSAPP_WEBHOOK_SECRET`: presente, comprimento esperado confirmado.

## Verificação Chatwoot/Elle

- Chatwoot API pública: HTTP `200`.
- Chatwoot versão: `4.14.1`.
- `queue_services=ok`.
- `data_services=ok`.
- Elle health: HTTP `200`.
- Elle status:
  - `ok=True`
  - `dry_run=True`
  - `write_enabled=False`
  - `kill_switch=True`

## Webhook Elle no Chatwoot

Consulta read-only via API Chatwoot:

- Webhooks encontrados: `1`.
- Webhook Elle encontrado: `1`.
- ID: `1`.
- Nome: `Elle MVP 1C dry-run`.
- Host: `elle.lkskrs.online`.
- Subscriptions: `message_created`.

## Dry-run local executado

Com Doppler injetado e sem writes:

- `test_chatwoot_target_config.py`: OK.
- `test_chatwoot_internal_actions.py`: OK.
- `test_elle_classifier.py`: OK.
- `test_elle_idempotency.py`: OK.
- `scripts/elle_mvp1c_dryrun.py`: OK.

Métricas do dry-run:

- Fixtures: `12`.
- Intent OK: `12/12`.
- Labels OK: `12/12`.
- Risk OK: `12/12`.
- Handoff OK: `12/12`.
- Forbidden public actions: `0`.

Relatório gerado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/evaluation/reports/elle_mvp1c_dryrun_20260609.md`

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhum payload WhatsApp enviado ao endpoint do Chatwoot.
- Nenhum write real em conversa.
- Nenhuma nota privada real criada.
- Nenhum label/assignment real aplicado.
- Nenhuma alteração em webhook via Chatwoot UI/API.
- Nenhuma alteração em VPS/Docker/Traefik.
- Nenhuma alteração em Shopify, Tiny, estoque, preço, pedido ou campanha.

## Próximo passo seguro

Para conectar operacionalmente como copiloto interno, próximo gate exige aprovação separada:

1. Smoke test Chatwoot-origin sintético para Elle, ainda `dry_run=true`.
2. Depois, se aprovado, liberar somente writes internos:
   - private note;
   - labels;
   - assignment para time atendimento whatsapp;
   - sem resposta pública.

Não habilitar resposta pública automática sem novo approval packet.
