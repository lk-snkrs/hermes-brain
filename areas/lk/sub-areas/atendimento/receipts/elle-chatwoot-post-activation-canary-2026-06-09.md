# Elle / Chatwoot — canário pós-ativação

Data: 2026-06-09T13:49:36Z
Área: LK / Atendimento / Elle / Chatwoot
Modo: read-only pós-ativação, sem tocar cliente real

## Escopo

Lucas pediu “seguir” após ativação da Elle como copiloto interno. Foi executado canário seguro/read-only para validar saúde, runtime, webhook e logs recentes.

## Health checks

Elle `https://elle.lkskrs.online/healthz`:

- HTTP `200`
- `ok=true`
- `dry_run=false`
- `write_enabled=true`
- `kill_switch=false`

Chatwoot `https://chat.lkskrs.online/api`:

- HTTP `200`
- `version=4.14.1`
- `queue_services=ok`
- `data_services=ok`

## VPS / containers

Probe SSH read-only no VPS `lc`:

- `elle-chatwoot`: `Up`
- `chatwoot-sidekiq-1`: `Up`
- `chatwoot-rails-1`: `Up`
- `chatwoot-redis-1`: `Up`
- `chatwoot-postgres-1`: `Up`
- `traefik-traefik-1`: `Up`

## Logs Elle

`docker logs` do container `elle-chatwoot`:

- janela `--since 20m --tail 120`: sem saída.
- `--tail 300`: sem saída.

Interpretação: não há evidência de evento real recebido/logado desde a recriação do container, ou a aplicação não está escrevendo stdout para esse caminho.

## Webhook Chatwoot → Elle

API `GET /api/v1/accounts/1/webhooks` retornou `0` para o token usado, então foi feita confirmação read-only direta no Rails/DB para evitar falso negativo.

Rails/DB confirmou:

- `webhook_count=1`
- account `1`
- host `elle.lkskrs.online`
- subscription `message_created`
- URL cadastrada bate com `ELLE_CHATWOOT_WEBHOOK_URL` do Doppler por comparação hash/equivalência, sem imprimir o valor.

## Conversas abertas — amostra metadata-only

Consulta read-only de conversas abertas retornou HTTP `200` e amostra de 25 conversas. Apenas metadados foram inspecionados; nenhum conteúdo de mensagem foi salvo.

Amostra recente mostrava conversas com labels Shopify como:

- `pedido-aprovado`, `shopify`
- `pedido-criado`, `shopify`
- `pos-venda`, `shopify`
- `pedido-entregue`, `shopify`
- `carrinho-abandonado`, `shopify`

Sem write aplicado.

## Status

Elle segue ativa como copiloto interno. O webhook Chatwoot → Elle existe e aponta para o receiver esperado. Não houve evidência em logs de evento real pós-restart até o momento do canário.

## Próximo passo seguro recomendado

Aguardar a primeira mensagem real `message_created` inbound e checar logs/nota privada/labels depois, ou aprovar explicitamente um canário controlado em conversa de teste real no Chatwoot.

## O que não foi feito

- Nenhuma mensagem pública enviada.
- Nenhum WhatsApp enviado.
- Nenhuma conversa real alterada.
- Nenhuma nota/label/assignment aplicada em cliente real.
- Nenhuma alteração de webhook/inbox/containers/Traefik/Chatwoot/Tiny/Shopify.

`values_printed=false`.
