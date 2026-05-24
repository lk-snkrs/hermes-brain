# Receipt — teste fallback sem imagem WhatsApp LK via Crisp

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Motivo

Lucas confirmou que não recebeu no WhatsApp o teste anterior com template `lk_checkout_abandonado_30min_v3` com `HEADER IMAGE`, apesar de HTTP 200 / `request_accepted`.

## Ação diagnóstica

Enviado 1 teste interno adicional para Lucas com template sem imagem, para isolar possível falha do provider no caminho de mídia.

- Template: `lk_checkout_abandonado_30min_v2`
- Diagnóstico: fallback sem `HEADER IMAGE`
- Canal: Crisp Template API
- Workflow de referência: `kWQbmEMuvdipcGjd`
- Workflow status no momento do envio: `active=false`
- Número destino: `5511991203361`
- Número origem: `5511949565000`
- HTTP status: `200`
- Provider reason: `request_accepted`
- Request ID: `90ed5476-1f53-44f7-8574-0368d18e2f8a`

## Observação

`request_accepted` segue não sendo confirmação de entrega. Confirmar recebimento humano e/ou provider receipt.
