# Receipt — correção Crisp Inbox re-anchoring WhatsApp CRM

Data: 2026-05-21
Área: LK CRM / WhatsApp / Crisp / n8n

## Pedido
Lucas confirmou que o canary `IMG9740065351` chegou no WhatsApp do número final `4616`, mas não apareceu na Inbox do Crisp, e pediu correção para os próximos envios entrarem na Inbox.

## Diagnóstico

- O canary foi entregue no handset, então o problema não era mais entrega WhatsApp/media/header.
- A falha ficou isolada em **ancoragem/visibilidade de sessão no Crisp Inbox**.
- Payload do canary entregue:
  - `crisp_options.as`: `text`
  - `crisp_options.type`: `text`
  - `crisp_options.new_session`: `true`
  - `BODY.text`: presente
  - `message_template.components[].BODY.text`: presente
  - `HEADER IMAGE`: presente
- Resultado observado: WhatsApp recebeu, Inbox não mostrou. Portanto, para LK, `new_session:true` não pode ser tratado como garantia de Inbox.
- Auditoria dos workflows ativos encontrou também `from_number` mascarado literal (`+551****5000`) nos Code nodes de produção; isso foi corrigido usando o número real validado no canary entregue, sem registrar o número completo no Brain.

## Correção aplicada

Foram patchados os dois workflows ativos que montam payload Crisp:

1. `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`
   - Nó: `Preparar payload Crisp`

2. `XLODECE4MvNRNCQ9` — `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`
   - Nó: `Preparar payload Crisp Cart`

Mudanças:

- `crisp_options.new_session`: `true` → `false`
- `from_number`: removido valor mascarado literal e restaurado para o número real LK validado no canary entregue.
- Mantido:
  - `crisp_options.as: text`
  - `crisp_options.type: text`
  - `BODY.text`
  - `message_template.components[].BODY.text`
  - `HEADER IMAGE` nos templates de checkout.

## Verificação pós-write

Readback n8n:

- Checkout workflow:
  - `active`: `true`
  - `triggerCount`: `1`
  - `versionId == activeVersionId`: `true`
  - valor mascarado literal ausente
  - número real presente no workflow, não registrado neste receipt
  - `new_session:true`: ausente
  - `new_session:false`: presente

- Cart intent workflow:
  - `active`: `true`
  - `triggerCount`: `1`
  - `versionId == activeVersionId`: `true`
  - valor mascarado literal ausente
  - número real presente no workflow, não registrado neste receipt
  - `new_session:true`: ausente
  - `new_session:false`: presente

## Segurança / rollback

- Snapshots pré-correção salvos fora do Brain, em `.secrets/n8n-snapshots/`, com permissão restrita.
- Nenhum reenvio WhatsApp foi feito nesta correção.
- Nenhuma template Meta/Crisp foi alterada.
- Rollback: restaurar snapshots pré-correção dos workflows `kWQbmEMuvdipcGjd` e `XLODECE4MvNRNCQ9`, ou reverter apenas os Code nodes para `new_session:true`/estado anterior.

## Observação

A conversa do canary `IMG9740065351` que já chegou no WhatsApp pode não aparecer retroativamente na Inbox. A correção vale para os próximos envios. Para validar visualmente, é necessário aguardar o próximo envio elegível ou Lucas aprovar um novo canary controlado com imagem.
