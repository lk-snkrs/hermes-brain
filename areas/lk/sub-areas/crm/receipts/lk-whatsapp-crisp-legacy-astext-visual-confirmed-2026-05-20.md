# Receipt — confirmação visual de entrega do teste Crisp `as:text`

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp

## Confirmação visual

Lucas enviou screenshot do WhatsApp mostrando que o teste interno chegou no chat `LK Sneakers & Apparels`.

## Teste confirmado

- Canal: Crisp Template API
- Template: `lk_checkout_abandonado_30min_v2`
- `crisp_options`: `{ "as": "text" }`
- Request ID: `abe22708-1145-4cfe-b526-3ddcd7b9dfa0`
- Código visível no WhatsApp: `HERMES113812`
- Horário visual no screenshot: `08:38`
- CTA exibido: `Voltar ao checkout`

## Conclusão operacional

A rota Crisp entrega quando usamos o shape legado/historicamente funcional da LK: `{ "as": "text" }`.

A falha anterior de não recebimento ficou fortemente associada à troca para o shape documentado novo `crisp_options: { "type": "text", "new_session": true }`, não a uma necessidade imediata de alterar webhook Meta.

## Decisão recomendada

- Não alterar webhook Meta agora.
- Patchar o workflow n8n inativo para usar o shape entregue `{ "as": "text" }`.
- Manter workflow `active=false` até validação final.
- Fazer próximo teste interno pelo próprio workflow/nó corrigido antes de qualquer ativação.
