# Receipt — teste híbrido para entrega WhatsApp + visibilidade Inbox Crisp

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp

## Pedido

Lucas informou que o teste anterior não apareceu no Inbox Crisp e pediu novo teste para fazer aparecer.

## Auditoria antes do teste

- Não há secrets `CRISP_*` no Doppler `lc-keys/prd`.
- O Basic Auth do WhatsApp Plugin usado no endpoint `plugins.crisp.chat/.../template/send` não autentica na REST API principal da Crisp (`api.crisp.chat/v1`) mesmo com `X-Crisp-Tier` testado como `plugin`, `website` e `user`; resposta: `401 invalid_session`.
- Portanto, não foi possível criar/ler conversa diretamente no Crisp Inbox por REST API nesta etapa.

## Teste enviado

Objetivo: combinar o shape que entregou no WhatsApp (`as:text`) com os campos documentados de visibilidade (`type:text`, `new_session:false`, `BODY.text`).

- Canal: Crisp WhatsApp Plugin Template API
- Template: `lk_checkout_abandonado_30min_v2`
- Sem imagem
- `crisp_options`: `{ "as": "text", "type": "text", "new_session": false }`
- BODY incluiu campo `text` além dos `parameters`
- Destino: número interno de Lucas
- Origem: WhatsApp LK
- HTTP status: `200`
- Provider reason: `request_accepted`
- Request ID: `cf9d38a4-7099-4706-bada-88f7590216f9`
- Código esperado: `INBOX114811`

## Interpretação

Este teste ainda depende de confirmação visual:

- Se chegar no WhatsApp e aparecer no Inbox Crisp: usar este shape híbrido no workflow.
- Se chegar no WhatsApp mas não aparecer no Inbox: entrega e Inbox são rotas separadas; precisaremos de credencial REST Crisp real ou configurar/ler Callback URL do plugin.
- Se não chegar no WhatsApp: o shape híbrido não deve ser usado; voltar ao `{ "as": "text" }` simples para entrega.

## Não executado

- Nenhum cliente/terceiro recebeu mensagem.
- Nenhum workflow foi ativado.
- Nenhum webhook Meta foi alterado.
- Nenhuma configuração de produção foi alterada.
