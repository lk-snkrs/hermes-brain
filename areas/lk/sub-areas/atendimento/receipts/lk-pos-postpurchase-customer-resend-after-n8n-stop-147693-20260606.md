# LK POS post-purchase — reenvio após n8n pausado para cliente #147693

Data: 2026-06-06
Área: LK / Atendimento / POS pós-venda

## Escopo
Lucas informou: "Parei o n8n, pode enviar ok?". Isso foi tratado como aprovação explícita para novo envio customer-visible para a cliente do pedido `#147693`.

## Pedido
- Pedido: `#147693`
- Cliente: primeiro nome `Thais`
- Telefone: final `7101` (completo omitido)
- Mensagem: pós-venda POS assinada por Danilo, conforme fila local.

## Ação executada
Novo envio via Evolution API / instância `LK Flagship`, payload oficial:
- `number`
- `text`
- `delay=1000`
- `linkPreview=false`

## Resultado sanitizado
- HTTP: `201`
- Status inicial: `PENDING`
- `fromMe`: `true`
- ID presente: sim
- `messageType`: `conversation`

## Probe pós-envio
Consulta read-only em `chat/findMessages` encontrou a mensagem outgoing para o contato.

Após polling, `MessageUpdate` observado:
- `SERVER_ACK`

Ainda não observado:
- `DELIVERY_ACK`

## Conclusão operacional
Mesmo após Lucas informar que pausou o n8n, o envio via Evolution saiu e chegou ao servidor WhatsApp (`SERVER_ACK`), mas até o fechamento desta verificação ainda não havia confirmação de entrega ao destinatário (`DELIVERY_ACK`).

## Segurança
- Nenhum token/API key registrado.
- Número completo, JID e message ID omitidos/hashados apenas no ledger local.
- Reenvio executado somente após aprovação explícita.
