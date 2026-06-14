# Approval packet — ativação régua WhatsApp online LK

- Data: 2026-06-13
- Agente: lk-ops
- Área: LK / atendimento / WhatsApp Business API
- Pedido: verificar se webhooks/gatilhos estão configurados e preparar ativação da régua online aprovada na Meta.
- Classificação: activation packet / sem execução produtiva
- Secrets: Doppler `lc-keys/prd`, `values_printed=false`

## Veredito curto

Os templates estão aprovados na Meta, mas a régua **não está pronta para ativar automaticamente**.

Existe captura Shopify/Hermes para parte do ciclo, principalmente `orders/create`, `orders/updated` e `orders/cancelled` no `lk-shopify-orders-ingest`, porém ela está em modo **record_only**. Não há, no inventário local atual, um sender/worker aprovado para disparar os templates WABA `lk_online_*_v1` aos clientes.

## Evidência read-only consultada

### Meta / WABA

6/6 templates aprovados:

- `lk_online_pedido_enviado_v1`: APPROVED
- `lk_online_pedido_entregue_v1`: APPROVED
- `lk_online_avaliacao_compra_v1`: APPROVED
- `lk_online_pagamento_pendente_v1`: APPROVED
- `lk_online_pagamento_nao_aprovado_v1`: APPROVED
- `lk_online_troca_devolucao_solicitada_v1`: APPROVED

### Shopify Admin webhooks

Foram encontrados 20 webhooks na Shopify. Tópicos relevantes observados:

- `orders/create`: presente, incluindo rota Hermes `lk-shopify-orders-ingest`.
- `orders/updated`: presente, incluindo rota Hermes `lk-shopify-orders-ingest`.
- `orders/cancelled`: presente, incluindo rota Hermes `lk-shopify-orders-ingest`.
- `orders/paid`: presente, mas não apontando para `lk-shopify-orders-ingest`; aparece em rotas de POS/stock/legadas.
- `orders/fulfilled`: presente apenas em rotas legadas, não no sender WABA online.
- `refunds/create`: presente apenas em rota legada.
- `fulfillments/create` / `fulfillments/update`: não encontrados no inventário Shopify.

### Hermes gateway/local

Rotas relevantes observadas no registry local:

- `lk-shopify-orders-ingest`: enabled=true, `orders/create|orders/updated|orders/cancelled`, record-only, sem envio a cliente.
- `lk-shopify-pos-restock`: rota POS, não é régua online WABA.
- `lk-shopify-tiny-stock-sync`: rota stock/Tiny local, não é atendimento WABA.
- Não foi encontrado sender/worker local com `lk_online_*`, WABA template sending ou Chatwoot template automation para esta régua.

### Ledger de eventos

Ledger `lk_shopify_orders_ingest` existe e está recebendo eventos recentes. Exemplo de estado agregado:

- 168 pedidos registrados no ledger.
- Eventos recentes em 2026-06-13 incluem `orders/updated`, web/POS, com `automation_action=record_only` para web.

## Cobertura por template

### 1. Pedido enviado — `lk_online_pedido_enviado_v1`

- Template: aprovado.
- Evento necessário: fulfillment criado/atualizado ou order fulfilled com rastreio.
- Cobertura atual: parcial.
- Observado: `orders/fulfilled` existe em rotas legadas; `orders/updated` chega no ingest; `fulfillments/create/update` não encontrado.
- Bloqueio: falta sender WABA e regra de elegibilidade com rastreio/link.

### 2. Pedido entregue — `lk_online_pedido_entregue_v1`

- Template: aprovado.
- Evento necessário: entrega confirmada por tracking/logística, não apenas fulfillment.
- Cobertura atual: insuficiente.
- Observado: não há webhook de transportadora/entrega confirmado neste inventário.
- Bloqueio: precisa fonte de entrega confiável e dedupe/cooldown.

### 3. Avaliação compra — `lk_online_avaliacao_compra_v1`

- Template: aprovado.
- Evento necessário: pós-entrega + link único Judge.me por pedido/cliente.
- Cobertura atual: insuficiente para produção.
- Bloqueio: falta resolver tecnicamente de onde vem `judgeme_review_url` e quando disparar.

### 4. Pagamento pendente — `lk_online_pagamento_pendente_v1`

- Template: aprovado.
- Evento necessário: pedido criado/checkout com pagamento pendente e checkout/recovery URL válido.
- Cobertura atual: parcial.
- Observado: `orders/create` e `orders/updated` chegam no ingest; há Recovery OS separado para checkouts.
- Bloqueio: falta regra de delay, elegibilidade, checkout URL e sender WABA.

### 5. Pagamento não aprovado — `lk_online_pagamento_nao_aprovado_v1`

- Template: aprovado.
- Evento necessário: falha/cancelamento/expiração de pagamento identificável.
- Cobertura atual: parcial/ambígua.
- Observado: `orders/updated` e `orders/cancelled` chegam no ingest.
- Bloqueio: distinguir não aprovado vs cancelado vs reembolsado vs pendente, sem mensagem indevida.

### 6. Troca/devolução solicitada — `lk_online_troca_devolucao_solicitada_v1`

- Template: aprovado.
- Evento necessário: solicitação real de troca/devolução em fonte oficial.
- Cobertura atual: insuficiente.
- Observado: `refunds/create` existe em rota legada; não há rota Hermes WABA dedicada; returns webhook não identificado.
- Bloqueio: fonte oficial do fluxo de troca/devolução e regra de atendimento humano.

## Recomendação de ativação segura

Fase 0 — agora, sem envio:

1. Manter templates aprovados inativos para produção.
2. Criar/validar motor local em dry-run para mapear evento → template → variáveis → decisão `would_send` / `skip_reason`.
3. Não enviar WhatsApp ainda.

Fase 1 — gaps de webhook/evento:

1. Adicionar ou confirmar captura dedicada para:
   - `orders/paid` para pagamento aprovado, se for usado na régua online.
   - `fulfillments/create` e/ou `fulfillments/update` para pedido enviado.
   - fonte de entrega real para pedido entregue.
   - fonte de troca/devolução real, se existir app/returns/refunds adequado.
2. Separar captura de eventos de envio a cliente.
3. Persistir ledger idempotente por `order_id + template_name + event_source`.

Fase 2 — sender WABA controlado:

1. Implementar sender com kill-switch default ON.
2. Enviar apenas se:
   - template APPROVED;
   - telefone normalizado e elegível;
   - variáveis completas;
   - evento confirmado;
   - não enviado antes;
   - janela/cooldown respeitada;
   - nenhum bloqueio humano/manual no pedido.
3. Primeiro modo: dry-run + relatório.
4. Segundo modo: teste controlado com pedido/telefone aprovado por Lucas.
5. Terceiro modo: produção gradual por template.

## Variáveis necessárias

### Pedido enviado

- nome_cliente
- numero_pedido
- codigo_rastreio
- url_rastreio
- primeiro_produto_imagem_url

### Pedido entregue

- nome_cliente
- numero_pedido
- primeiro_produto_imagem_url

### Avaliação compra

- nome_cliente
- numero_pedido
- judgeme_review_url
- primeiro_produto_imagem_url

### Pagamento pendente

- nome_cliente
- numero_pedido
- checkout_url
- primeiro_produto_imagem_url

### Pagamento não aprovado

- nome_cliente
- numero_pedido
- primeiro_produto_imagem_url

### Troca/devolução solicitada

- nome_cliente
- numero_pedido
- primeiro_produto_imagem_url

## Riscos principais

- Duplicidade de mensagem por múltiplos `orders/updated`.
- Enviar pagamento pendente depois de pagamento aprovado.
- Enviar pedido entregue sem confirmação real de entrega.
- Disparar avaliação sem link único correto do Judge.me.
- Usar rotas legadas como se fossem sender aprovado.
- Confundir POS/Evolution com online/WABA.

## O que não foi feito

- Nenhum webhook foi criado/alterado.
- Nenhuma automação foi ativada.
- Nenhuma mensagem foi enviada a cliente.
- Nenhum write em Shopify, Chatwoot, Meta, Klaviyo, Judge.me ou Tiny.

## Aprovação necessária para próxima etapa

Para executar a próxima etapa técnica sem envio a cliente, aprovação sugerida:

> Aprovado criar o motor dry-run da régua online WABA, usando eventos Shopify/Judge.me/Chatwoot apenas em leitura e ledger local, sem enviar WhatsApp e sem ativar produção.

Para configurar webhooks faltantes ou sender produtivo depois, será necessária aprovação separada com lista exata de tópicos, URLs, rollback e teste.
