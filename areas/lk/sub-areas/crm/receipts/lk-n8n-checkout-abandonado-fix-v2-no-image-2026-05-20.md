# Receipt — correção n8n checkout abandonado LK para template sem imagem

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Motivo

Lucas reportou que não recebeu os novos testes apesar de `request_accepted` no Crisp. Screenshot e `wacli` mostraram que o teste que chegou de fato foi a mensagem sem imagem/renderizada como card textual, às 21:38, com texto:

> Oi Lucas, aqui é da LK. Vi que você estava olhando Air Jordan 1 e seu checkout ficou salvo por aqui...

Os testes posteriores com `lk_checkout_abandonado_30min_v3` com imagem e fallback `v2` sem imagem retornaram apenas aceite assíncrono, sem nova mensagem visível no WhatsApp/wacli.

## Correção aplicada

Workflow n8n atualizado mantendo-o inativo:

- Workflow ID: `kWQbmEMuvdipcGjd`
- Nome: `LK - Checkout Abandonado 30min MVP - Crisp (INATIVO)`
- Status após correção: `active=false`
- Node de envio: `Crisp Send lk_checkout_abandonado_30min_v2`
- Template configurado: `lk_checkout_abandonado_30min_v2`
- Mudança: removido `HEADER IMAGE` do payload
- Mudança: `crisp_options` ajustado para `{ "as": "text" }`, padrão do workflow/backups que gerou renderização textual recebida
- Mantido: BODY com 2 variáveis (`firstName`, `productName`)
- Mantido: BUTTON URL com 1 variável (`checkoutToken`)

## Verificação pós-write

- Workflow ativo? não (`active=false`)
- `lk_checkout_abandonado_30min_v2` presente? sim
- `lk_checkout_abandonado_30min_v3` ausente? sim
- `HEADER` ausente no payload? sim
- `crisp_options.as = text` presente? sim

## Backup / rollback

Backup bruto salvo em diretório restrito porque contém headers de integração n8n/Crisp:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-fix-v2-no-image-20260520T100151.json`

Rollback:

1. Reimportar o JSON acima via n8n API/UI.
2. Confirmar `active=false`.
3. Validar node de envio e ausência de disparos.

## Interpretação

A correção remove o caminho de mídia do MVP e alinha o workflow ao formato que Lucas efetivamente viu no WhatsApp. A ausência de novos recebimentos no mesmo número depois do primeiro envio pode envolver recibo assíncrono/frequency cap/roteamento do provider; portanto `request_accepted` não será usado como critério de sucesso.

## Não executado

- Workflow não foi ativado.
- Nenhum cliente recebeu mensagem.
- Nenhum desconto/cupom criado.
- Nenhuma mudança em Shopify/Meta/Crisp production fora do workflow n8n inativo.
