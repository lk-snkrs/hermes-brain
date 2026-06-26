# Receipt — teste interno Crisp com shape legado `as:text`

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / Meta

## Motivo

Lucas autorizou seguir após a auditoria mostrar que a WABA canônica da LK já aparece inscrita no app Crisp, enquanto o teste que não chegou usou um shape novo/documentado de `crisp_options`.

Objetivo: isolar se a não-entrega foi causada pela mudança de payload (`type=text/new_session=true`) versus o shape historicamente funcional da LK (`as=text`).

## Ação executada

Envio de 1 teste interno para o número pré-aprovado de Lucas, sem ativar workflow n8n e sem enviar para clientes.

- Canal: Crisp Template API
- Template: `lk_checkout_abandonado_30min_v2`
- Tipo: sem imagem (`no HEADER IMAGE`) para reduzir variáveis de falha
- `crisp_options`: `{ "as": "text" }`
- Destino: número interno de Lucas
- Origem: WhatsApp LK
- HTTP status: `200`
- Provider reason: `request_accepted`
- Request ID: `abe22708-1145-4cfe-b526-3ddcd7b9dfa0`
- Código visível esperado no texto: `HERMES113812`

## Interpretação

`request_accepted` segue sendo confirmação de aceite/enfileiramento, não entrega final. A validação depende de confirmação visual de Lucas no WhatsApp/Crisp.

Se Lucas receber este teste, a principal diferença provável foi o shape `crisp_options`, não o webhook Meta.

Se Lucas não receber este teste, o problema passa a ser rota/provider/receipt/template geral e não apenas o shape novo.

## Não executado

- Workflow n8n não foi ativado.
- Nenhum cliente/terceiro recebeu mensagem.
- Nenhum webhook Meta foi alterado.
- Nenhuma configuração de produção foi alterada.
