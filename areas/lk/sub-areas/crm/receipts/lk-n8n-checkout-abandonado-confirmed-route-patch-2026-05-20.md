# Receipt — patch n8n workflow to confirmed Crisp delivery route

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Contexto

Lucas confirmou visualmente no WhatsApp que o teste interno com código `HERMES113812` chegou usando:

- Template: `lk_checkout_abandonado_30min_v2`
- `crisp_options`: `{ "as": "text" }`
- Sem `HEADER IMAGE`
- Request ID: `abe22708-1145-4cfe-b526-3ddcd7b9dfa0`

## Ação executada

Foi aplicado patch no workflow n8n inativo:

- Workflow ID: `kWQbmEMuvdipcGjd`
- Nome: `LK - Checkout Abandonado 30min MVP - Crisp (INATIVO)`
- Status antes: `active=false`
- Status depois: `active=false`

Alteração no nó Crisp:

- Node antes: `Crisp Send lk_checkout_abandonado_img_fix_2`
- Node depois: `Crisp Send lk_checkout_abandonado_30min_v2`
- Template antes: `lk_checkout_abandonado_img_fix_2`
- Template depois: `lk_checkout_abandonado_30min_v2`
- `HEADER IMAGE`: removido
- `crisp_options`: mantido/garantido como `{ "as": "text" }`

## Backup / rollback

Backup live pré-patch salvo em área restrita:

`/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-v2-no-image-confirmed-route-20260520T114302Z.json`

Rollback: reimportar/PUT o backup acima no workflow `kWQbmEMuvdipcGjd` mantendo `active=false`.

## Verificação pós-patch

Readback do n8n confirmou:

- Workflow `active=false`
- Nó Crisp atualizado para `Crisp Send lk_checkout_abandonado_30min_v2`
- Template no JSON: `lk_checkout_abandonado_30min_v2`
- Sem `HEADER`
- `crisp_options` contém `as:text`

## Não executado

- Workflow não foi ativado.
- Nenhuma mensagem para cliente/terceiro foi enviada.
- Nenhum webhook Meta foi alterado.
- Nenhum template Meta/Crisp foi criado/editado.

## Próximo passo recomendado

Executar um teste interno do próprio workflow/nó corrigido ou simular o payload final via n8n, ainda com workflow inativo. Só ativar produção após confirmação visual do teste end-to-end.
