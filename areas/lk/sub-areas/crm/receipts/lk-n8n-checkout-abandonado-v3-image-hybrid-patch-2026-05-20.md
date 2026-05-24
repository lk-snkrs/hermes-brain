# Receipt — n8n checkout abandonado com imagem dinâmica + Crisp Inbox

Data UTC: 2026-05-20T12:01:31Z
Área: LK CRM / WhatsApp / Crisp / n8n

## Pedido

Lucas aprovou seguir para incluir a imagem do produto do carrinho/checkout abandonado.

## Ações executadas

1. Auditado o workflow n8n `kWQbmEMuvdipcGjd`.
2. Confirmado que o workflow estava `active=false` antes do patch.
3. Confirmado via Crisp `/templates` que `lk_checkout_abandonado_30min_v3` está `APPROVED`, `MARKETING`, `pt_BR`, com `HEADER IMAGE`.
4. Enviado teste interno para Lucas via Crisp Template API com imagem e payload híbrido:
   - Template: `lk_checkout_abandonado_30min_v3`
   - Marcador: `IMG120032`
   - Request ID: `d9dea110-6389-4aa3-91b8-72b695227c7a`
   - Status: HTTP 200 / `request_accepted`
5. Patched workflow inativo para usar o template com imagem:
   - Node: `Crisp Send lk_checkout_abandonado_30min_v3`
   - `HEADER IMAGE`: `={{$json.productImage}}`
   - BODY com `parameters` + `text`
   - `crisp_options`: `{ "as": "text", "type": "text", "new_session": false }`
6. Corrigida a conexão do node `Preparar dados` para apontar para `Crisp Send lk_checkout_abandonado_30min_v3`.

## Extração de imagem

O node `Preparar dados` agora tenta usar, nesta ordem:

1. `line_items[0].image_url`
2. `line_items[0].image`
3. `line_items[0].image.src`
4. `line_items[0].variant_image`
5. `line_items[0].product_image`
6. fallback LK logo público

## Verificação pós-patch

Readback n8n confirmou:

- `active=false`
- Template no payload: `lk_checkout_abandonado_30min_v3`
- `HEADER IMAGE` presente
- `productImage` presente no header
- payload híbrido confirmado presente
- conexão para o node Crisp v3 correta

## Backup / rollback

Backup pré-patch salvo em área restrita:

`/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-v3-image-hybrid-patch-20260520T120131Z.json`

Rollback: restaurar esse JSON no workflow `kWQbmEMuvdipcGjd` via n8n API/UI e confirmar `active=false`.

## Não executado

- Workflow não foi ativado.
- Nenhuma mensagem para cliente/terceiro foi enviada.
- Nenhum webhook Meta/Crisp foi alterado.
- Nenhum template foi criado/editado.

## Pendente

Confirmação visual de Lucas para o teste `IMG120032`:

- chegou no WhatsApp?
- apareceu no Inbox Crisp?
- a imagem renderizou corretamente?
