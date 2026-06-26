# Approval packet — Chatwoot `avisar-enc` / encomenda

Data: 2026-06-22
Agente: lk-ops
Área: LK / Atendimento / Chatwoot

## Pedido

Aprovar as mensagens prontas para avisar o cliente quando um pedido tiver produto sob encomenda por causa do estoque híbrido da LK.

Contexto: alguns tamanhos/produtos são pronta entrega e outros são sob encomenda. Quando o pedido receber uso operacional/tag `avisar-enc`, o atendimento precisa avisar o cliente antes de seguir.

## Escopo desta aprovação

Aprovar **copy de resposta pronta no Chatwoot**.

Não inclui:

- envio automático ao cliente;
- alteração de Shopify/Tiny/estoque;
- promessa de disponibilidade;
- reserva de produto;
- alteração de automação por tag.

## Versão 1 — pedido com 1 item

Shortcode: `avisar-enc`

```text
Olá, tudo bem? Aqui é a Larissa da LK.

Estou entrando em contato para te avisar que, conforme informado na descrição do produto, o item do seu pedido é sob encomenda. Por isso, o prazo de entrega é de 4 a 6 semanas.

Antes de seguirmos com o pedido, queria confirmar se está tudo certo para você.

Caso prefira, também posso verificar opções à pronta entrega na sua numeração.
```

## Versão 2 — pedido com mais de 1 item

Shortcode: `avisar-enc-multi`

```text
Olá, tudo bem? Aqui é a Larissa da LK.

Estou entrando em contato para te avisar que, conforme informado na descrição do produto, um dos itens do seu pedido é sob encomenda. Por isso, o prazo de entrega desse item é de 4 a 6 semanas.

Antes de seguirmos com o pedido, queria confirmar se está tudo certo para você.

Caso prefira, também posso verificar opções à pronta entrega na sua numeração.
```

## Observações de segurança

- A frase “posso verificar opções à pronta entrega” evita prometer disponibilidade sem validação.
- A mensagem pede confirmação antes de seguir, reduzindo risco de reclamação posterior.
- Para mais de um item, a copy separa o prazo “desse item”, sem sugerir que todo o pedido é encomenda.

## Status atual

Já aplicado no Chatwoot para validação operacional:

- `avisar-enc` criado/atualizado para 1 item.
- `avisar-enc-multi` criado para múltiplos itens.
- `encomenda` alinhado com a versão de 1 item.

Rollback disponível em:

`/root/chatwoot-rollbacks/20260622T1621Z-canned-avisar-enc-split/canned_before.json`

## Decisão solicitada

Aprovar a copy atual ou solicitar ajuste de texto antes de uso pelo time.
