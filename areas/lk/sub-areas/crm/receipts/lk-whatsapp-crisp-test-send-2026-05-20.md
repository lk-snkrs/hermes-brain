# Receipt — Teste interno WhatsApp LK via Crisp

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Aprovação

Lucas corrigiu a regra operacional no Telegram: testes internos de WhatsApp para o próprio número dele estão aprovados de forma recorrente e não precisam de nova autorização a cada teste. Essa autorização não se aplica a clientes/terceiros.

## Ação executada

Envio de 1 teste interno via Crisp Template API, sem ativar workflow n8n.

- Workflow de referência: `kWQbmEMuvdipcGjd`
- Workflow status no momento do envio: `active=false`
- Canal: Crisp Template API
- Template: `lk_checkout_abandonado_30min_v3`
- Número origem: `5511949565000`
- Número destino: `5511991203361`
- HTTP status: `200`
- Provider reason: `request_accepted`
- Request ID: `143ddd3a-a91e-4067-b18a-ba7d5aecfdec`

## Observação

`request_accepted` confirma que o provider aceitou a requisição. Não substitui confirmação humana de recebimento/renderização no WhatsApp.

## Não executado

- Workflow não foi ativado.
- Não houve envio para clientes.
- Nenhum cupom/desconto foi criado.
- Nenhuma alteração adicional em Shopify/Meta/Crisp/n8n além do teste interno.
