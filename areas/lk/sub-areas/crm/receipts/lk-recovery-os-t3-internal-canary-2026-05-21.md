# Receipt — LK Recovery OS T3 internal canary

Data: 2026-05-21
Área: LK CRM / WhatsApp / Crisp / Shopify

## Aprovação

Lucas aprovou no turno atual: `11991203361 manda o t3`.

## Escopo executado

Envio único e controlado para número interno/autorizado de Lucas.

- Template: `lk_checkout_abandonado_72h_cupom10_v1`
- Canal: Crisp WhatsApp Plugin Template API
- Origem: LK WhatsApp final `5000`
- Destino: final `3361`
- Header image: sim
- Cupom Shopify criado: sim, 10%, uso único, válido por 24h
- `crisp_options`: `{ as: "text", type: "text", new_session: false }`
- `BODY.text`: fallback renderizado incluído para visibilidade/ancoragem

## Resultado

- Marker: `T3CANARY160914`
- Cupom: `LK10-T3CANARY160914-3361`
- Expiração UTC: `2026-05-22T16:09:14Z`
- Shopify DiscountCodeNode: `gid://shopify/DiscountCodeNode/1672843428062`
- Crisp HTTP status: `200`
- Crisp reason: `request_accepted`
- Crisp request ID: `ddeabc98-9594-4f37-be5c-11db874b4d90`

## Interpretação

`request_accepted` confirma aceite/enfileiramento pelo provider, não confirmação final de entrega no aparelho nem visibilidade no Crisp Inbox.

## Próxima verificação

Lucas deve confirmar no WhatsApp se recebeu a mensagem T3 com o cupom `LK10-T3CANARY160914-3361`. Se não aparecer em alguns minutos, investigar callback/Crisp Inbox antes de reenviar.
