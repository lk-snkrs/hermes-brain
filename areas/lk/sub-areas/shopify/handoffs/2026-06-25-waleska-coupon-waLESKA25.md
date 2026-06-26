# Handoff — cupom individual Waleska Masutti / pedido #147193

Reminder OS loop needed: yes
Reminder OS owner: `[LK] Shopify` / `lk-shopify`
Reminder OS next action: criar/validar no Shopify um cupom individual para cliente Waleska Masutti, código `WALESKA25`, desconto de 20%, e devolver confirmação/readback sanitizado para o Mordomo/Lucas antes do e-mail final se necessário.
Reminder OS review trigger: quando o cupom estiver criado/readback OK, ou se houver bloqueio de Shopify/escopo/validação.
Reminder OS evidence: feedback 1 estrela informado por Lucas via Telegram em 2026-06-25; pedido `#147193`; cliente Waleska Masutti; e-mail `Waleskamasutti@hotmail.com`; reclamação de compra em 28/04/2026, entrega apenas em 18/06/2026 após troca de cor por indisponibilidade não comunicada.
Status: handoff aberto para criação de cupom; nenhum write Shopify executado por Mordomo.
Approval/context: Lucas pediu explicitamente para oferecer cupom de 20% e pedir ao LK Shopify criar especialmente para Waleska com código `WALESKA25`.
External writes declared: Shopify discount/coupon write pendente sob owner `lk-shopify`; Mordomo fez apenas documento local de handoff.
values_printed=false

## Escopo solicitado

- Cliente: Waleska Masutti
- Pedido: #147193
- Cupom: `WALESKA25`
- Desconto: 20%
- Uso esperado: individual/especial para a cliente, como gesto de reparação pelo atraso, falta de aviso de indisponibilidade e necessidade de troca de cor.

## Requisitos de segurança

- Não alterar pedido, estoque, preço de produto, campanha, Klaviyo ou customer tags sem aprovação separada.
- Não imprimir tokens/secrets.
- Retornar apenas status/readback sanitizado do cupom: código, desconto, restrições principais e `values_printed=false`.

## Contexto do e-mail que Mordomo está preparando

Lucas quer responder em primeira pessoa como fundador da LK, com educação, empatia, reconhecimento do erro, agradecimento por avisar, e oferta do cupom de 20%.
