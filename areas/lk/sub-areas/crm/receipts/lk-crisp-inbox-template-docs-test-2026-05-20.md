# Receipt — Crisp Inbox visibility test for LK WhatsApp template

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n

## Pedido

Lucas pediu: "seguir… vamos tentar fazer aparecer na inbox do crisp… procure na documentação".

## Documentação consultada

Fonte: Crisp docs — Messaging APIs → WhatsApp Business API → Quickstart.

Achados relevantes:

1. Ao enviar WhatsApp template via Crisp, o template pode aparecer no Inbox como `note` ou como `text`.
2. O padrão documentado é `crisp_options: { "type": "note", "new_session": false }`.
3. Para aparecer como mensagem normal/visível imediatamente no Inbox, a documentação orienta usar `crisp_options: { "type": "text", "new_session": false }`.
4. Quando `type=text`, a documentação exige `text` em pelo menos um componente; recomenda preencher `text` em todos os componentes aplicáveis para melhor resultado.
5. A própria doc diz que mensagens como `note` podem não aparecer no inbox até o usuário responder, mas podem ser recuperadas via `session_id` retornado no Callback URL.

## Achado técnico local

A rota `/templates` do plugin Crisp funcionou com o auth do workflow e listou templates aprovados visíveis para o Crisp:

- `lk_checkout_abandonado_img_fix_1` — APPROVED — HEADER IMAGE
- `lk_checkout_abandonado_30min_v3` — APPROVED — HEADER IMAGE
- `lk_checkout_abandonado_24h_v2` — APPROVED — sem imagem
- `lk_checkout_abandonado_30min_v2` — APPROVED — sem imagem

Observação: `lk_checkout_abandonado_img_fix_2` não apareceu na lista do Crisp, pois foi criado no caminho/WABA de compatibilidade operacional anterior, não no catálogo que o Crisp lista.

## Teste executado

Foi enviado um único teste interno para Lucas via Crisp Template API, usando a forma documentada para aparecer no Inbox:

- Endpoint: Crisp WhatsApp Plugin `/template/send`
- Template: `lk_checkout_abandonado_30min_v3`
- `crisp_options`: `{ "type": "text", "new_session": true }`
- BODY inclui campo `text` literal além dos parâmetros `Lucas` e `teste interno Crisp Inbox`
- HEADER IMAGE usa URL pública LK
- Destinatário: número interno de Lucas

Resultado API:

- HTTP: 200
- `reason`: `request_accepted`
- `request_id`: `6ea55176-5cd6-48a5-9c41-84be37f27a8a`

## Verificações adicionais

- Tentativa de ler Inbox via Crisp REST API com o mesmo Basic Auth do plugin retornou `401 invalid_session`; o token do plugin WhatsApp não serve como REST Inbox API credential.
- n8n API pública retornou `403` para os tokens disponíveis nesta sessão; não foi aplicado patch no workflow nesta etapa.

## Conclusão

A hipótese mais forte é que o teste anterior não apareceu no Inbox porque usava shape legado `crisp_options.as=text` ou uma forma não documentada; o teste atual seguiu a documentação (`type=text`, `new_session=true`, componente BODY com `text`).

Próximo passo: Lucas confirmar visualmente se apareceu no Crisp Inbox. Se sim, patchar o workflow n8n inativo para usar a forma documentada. Se não, precisamos do Callback URL/status do plugin Crisp ou de credencial REST Crisp real para inspecionar `session_id`/conversa.
