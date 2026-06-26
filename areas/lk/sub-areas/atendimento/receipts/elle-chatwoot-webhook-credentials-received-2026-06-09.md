# Elle / Chatwoot webhook — credenciais recebidas

Data: 2026-06-09
Área: LK / Atendimento / Elle / Chatwoot

## Entrada recebida

- Webhook URL recebida de Lucas para Chatwoot WhatsApp: `https://chat.lkskrs.online/webhooks/whatsapp/+5511949565000`
- Secret/token recebido na conversa: **sim**
- Secret/token registrado neste arquivo: **não**
- values_printed: `false`

## Verificação Doppler sanitizada

Secret names candidatos verificados em `lc-keys/prd`:

- `ELLE_CHATWOOT_WEBHOOK_URL`: existe
- `ELLE_CHATWOOT_WEBHOOK_SECRET`: existe
- `CHATWOOT_WEBHOOK_URL`: ausente
- `CHATWOOT_WEBHOOK_SECRET`: ausente
- `CHATWOOT_CLOUD_WEBHOOK_URL`: ausente
- `CHATWOOT_CLOUD_WEBHOOK_SECRET`: ausente

## Status atualizado após aprovação de Lucas

Aprovado por Lucas nesta conversa: atualizar Doppler + validar conexão sem mensagem pública.

Ações executadas:

- Doppler `lc-keys/prd` atualizado/confirmado com os nomes canônicos:
  - `ELLE_CHATWOOT_WEBHOOK_URL`
  - `ELLE_CHATWOOT_WEBHOOK_SECRET`
- Verificação de presença: ambos `OK`.
- `values_printed=false`.

Validação passiva/conexão:

- `GET https://chat.lkskrs.online/api`: HTTP `200`.
- Health público retornou Chatwoot `4.14.1`, `queue_services=ok`, `data_services=ok`.
- `HEAD` no endpoint webhook WhatsApp: HTTP `401` sem payload, coerente com endpoint protegido/não aberto.

O que não foi feito:

- Nenhuma mensagem pública enviada.
- Nenhum payload de WhatsApp simulado/enviado.
- Nenhuma resposta automática ativada.
- Nenhum webhook externo criado/alterado via UI/API.
- Nenhuma alteração em Shopify, Tiny, estoque, preço ou pedido.

## Próximo passo seguro

Testar o receiver/Elle em dry-run usando os secrets do Doppler, com evento controlado/local e somente nota privada se houver aprovação separada para Chatwoot write interno.
