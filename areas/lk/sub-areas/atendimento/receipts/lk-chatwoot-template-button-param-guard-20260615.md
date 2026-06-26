# Receipt — LK Chatwoot — guard de template com botão URL obrigatório

- Data/hora: 2026-06-15 14:15 UTC
- Agente/profile: lk-ops
- Área: LK / Atendimento / Chatwoot / Shopify order lifecycle
- Pedido humano: corrigir fluxo aprovado para não enviar template quando botão URL obrigatório estiver sem parâmetro.
- Aprovação: explícita pelo Lucas (“CORRIGIR POR FAVOR, APROVADO”).
- Classificação: produção aprovada; alteração em Chatwoot Rails/Sidekiq.

## Problema tratado

Template WhatsApp com botão URL dinâmico podia seguir para a Meta com parâmetro vazio. A Meta rejeita esse payload como parâmetro inválido. O caso citado foi o template `lk_online_pagamento_aprovado_v1`, que exige parâmetro para o botão URL.

## Alterações aplicadas

Arquivos alterados no source live `/opt/data/lk-chatwoot-v2`:

- `app/services/recovery/conversation_dispatcher.rb`
  - adiciona bloqueio antes do envio quando template aprovado tem botão URL com variável e o parâmetro resolvido fica vazio;
  - cria nota privada sanitizada na conversa com o motivo: “template não enviado: botão URL sem parâmetro obrigatório”;
  - inclui `template_name`, `order_name` sanitizado e `button_parameter_empty: true` na nota;
  - passa a usar `order_status_url` como fonte de link para lifecycle/order quando não há `cart_recovery_url`.

- `app/services/shopify/order_notification_service.rb`
  - adiciona `order_status_url` / `status_url` aos `custom_attributes` usados pelo dispatcher.

- `app/services/whatsapp/providers/base_service.rb`
  - melhora observabilidade de falhas Meta com detalhe sanitizado em log e `content_attributes.external_error_detail`;
  - registra `code`, `type`, mensagem sanitizada, detalhes sanitizados, `template_name`, `order_name` sanitizado e `button_parameter_empty`;
  - URLs são redigidas como `[URL_REDACTED]`; valores de token/PII não são impressos.

## Deploy

- Backup/rollback criado em `/root/chatwoot-rollbacks/template-button-param-block-20260615T140206Z/`.
- Imagem anterior: `lk-chatwoot:v2-recovery23-131049-cooldown-fix-20260615`.
- Imagem nova: `lk-chatwoot:v2-recovery24-template-button-guard-20260615`.
- Compose atualizado em `/opt/chatwoot/docker-compose.yaml` apenas para trocar a imagem.
- Serviços recriados: `chatwoot-rails-1` e `chatwoot-sidekiq-1`.

## Verificação executada

Resultado live:

- `chatwoot-rails-1|lk-chatwoot:v2-recovery24-template-button-guard-20260615|Up`
- `chatwoot-sidekiq-1|lk-chatwoot:v2-recovery24-template-button-guard-20260615|Up`
- HTTP local Chatwoot: `200`
- Ruby syntax check:
  - `conversation_dispatcher.rb`: `Syntax OK`
  - `order_notification_service.rb`: `Syntax OK`
  - `base_service.rb`: `Syntax OK`

Smoke no-send via Rails runner:

```json
{"blank_blocks_send":true,"valid_url_allows_send":true,"valid_button_param_present":true,"blocked_note_has_reason":true,"values_printed":false}
```

## Side effects e segurança

- Não houve envio real de WhatsApp/customer-facing durante o smoke.
- Não foram impressos secrets, tokens, telefones, e-mails ou URLs reais de checkout/pedido.
- A alteração é fail-closed: se o botão URL obrigatório não tiver parâmetro, o envio público é bloqueado e fica somente nota privada com motivo sanitizado.

## Rollback

Rollback seguro, se necessário:

1. Restaurar os arquivos do backup `/root/chatwoot-rollbacks/template-button-param-block-20260615T140206Z/` ou voltar a imagem no compose para `lk-chatwoot:v2-recovery23-131049-cooldown-fix-20260615`.
2. Rodar `docker compose up -d rails sidekiq` em `/opt/chatwoot`.
3. Verificar `docker ps`, HTTP local `200` e readback da imagem.
