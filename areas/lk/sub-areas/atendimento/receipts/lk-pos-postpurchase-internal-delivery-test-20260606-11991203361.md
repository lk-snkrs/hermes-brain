# LK POS post-purchase — teste interno de entrega Evolution

Data: 2026-06-06
Área: LK / Atendimento / POS pós-venda

## Escopo
Lucas pediu teste controlado para número interno final `3361` via Evolution API / instância `LK Flagship`.

## Ação executada
Envio de mensagem de teste curta e explícita para número interno autorizado.

Mensagem:
> Teste LK/Hermes pós-venda POS — teste controlado de entrega WhatsApp (12:24:48 BRT). Me avisa se chegou, por favor.

## Resultado sanitizado
- Instância: `LK Flagship`
- Endpoint: `message/sendText/{instance}`
- HTTP: `201`
- Status inicial Evolution: `PENDING`
- `fromMe`: `true`
- `messageType`: `conversation`
- ID presente: sim

## Probe pós-envio
Consulta read-only em `chat/findMessages` para o JID interno final `3361` encontrou a mensagem outgoing.

MessageUpdate observado:
- `SERVER_ACK`
- `DELIVERY_ACK`

Conclusão: para o número interno controlado, o fluxo completou confirmação de entrega (`DELIVERY_ACK`). Isso reforça que o caso da cliente #147693 não falhou em Shopify/fila/payload geral; a diferença está na entrega/roteamento para aquele destinatário específico ou na ausência de reconciliação automática para clientes.

## Segurança
- Nenhum token/API key registrado.
- Número e IDs completos omitidos.
- Sem novo envio para cliente real.
