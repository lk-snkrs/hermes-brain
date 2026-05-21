# Receipt — correção Crisp Inbox checkout abandonado

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Pedido

Lucas informou que a mensagem foi enviada com sucesso para Weslley, mas não entrou na Inbox do Crisp como no teste anterior, e pediu correção.

## Diagnóstico

- Workflow ativo afetado: `LK - Checkout Abandonado 30min Polling GraphQL - Crisp (ATIVO)`
- Workflow ID: `kWQbmEMuvdipcGjd`
- Nó afetado: `Crisp Send lk_checkout_abandonado_30min_v4`
- Estado encontrado: `crisp_options: { type: 'note' }`
- Interpretação: o envio podia chegar no WhatsApp, mas o shape estava orientado a nota/registro, não ao padrão híbrido que anteriormente apareceu na Inbox Crisp.

## Correção aplicada

O nó Crisp foi patchado para usar o shape híbrido validado anteriormente para LK:

- `crisp_options.as`: `text`
- `crisp_options.type`: `text`
- `crisp_options.new_session`: `false`
- `BODY.text`: fallback textual curto com marcador humano/comercial da LK

A template/meta do WhatsApp não foi alterada. O fluxo continua usando o template `lk_checkout_abandonado_30min_v4` com HEADER image e parâmetros do BODY/BUTTON.

## Verificação pós-write

Readback n8n:

- `active`: `true`
- `triggerCount`: `1`
- `activeVersionId` = `versionId`: `ec429c84-00e5-4cfc-af21-158db2dfcf97`
- `as:text`: presente
- `type:text`: presente
- `new_session:false`: presente
- `BODY.text`: presente
- `crisp_options: { type: 'note' }`: ausente

## Segurança / rollback

- Snapshot pré-correção salvo localmente fora do Brain e com permissão restrita em `.secrets/`.
- Nenhum segredo foi registrado neste receipt.
- Nenhum envio manual/reenvio para Weslley foi executado nesta correção.
- Rollback: restaurar o snapshot pré-correção do workflow `kWQbmEMuvdipcGjd` ou reverter apenas o `jsonBody` do nó Crisp para o estado anterior.

## Observação operacional

A conversa já enviada para Weslley pode não retroaparecer na Inbox se o provider não cria sessão retroativamente. A correção vale para os próximos envios. Reenviar ao Weslley seria novo contato customer-facing e exige aprovação explícita separada.
