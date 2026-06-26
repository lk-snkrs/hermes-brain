# LK Crisp WhatsApp Image Canary Battery — 2026-05-21

## Contexto

Lucas aprovou no turno atual: “Fazer”, após corrigir que recebeu um WhatsApp com imagem/header. Objetivo: testar envio interno para o número pessoal de Lucas (final 3361), sem clientes, variando uma dimensão por vez para isolar como entregar WhatsApp com imagem via Crisp.

## Guardrails

- Target: Lucas pessoal, final 3361.
- Sem envio a clientes.
- Sem alteração em workflow de produção.
- Sem exposição de secrets.
- Crisp `request_accepted` não é prova de entrega; callback/recebimento humano ainda necessários.

## Imagem usada

URL pública Shopify validada antes do envio:

- HTTP 200
- content-type: image/png
- content-length: 139787

## Envios

### A

- Marker: `IMGA013129`
- Template: `lk_checkout_abandonado_30min_v3`
- Variante: `v3 note lowercase — shape que teve callback sent externo`
- Component case: lower
- crisp_options: `{ "type": "note", "new_session": false }`
- HTTP: 200
- reason: `request_accepted`
- request_id: `3e74eb87-0504-4f15-9ce2-f928a4dfa893`

### B

- Marker: `IMGB013129`
- Template: `lk_checkout_abandonado_30min_v4`
- Variante: `v4 hybrid uppercase — shape atual produção`
- Component case: upper
- crisp_options: `{ "as": "text", "type": "text", "new_session": false }`
- HTTP: 200
- reason: `request_accepted`
- request_id: `0eba23e5-5b45-4694-a09e-96c88275a8c8`

### C

- Marker: `IMGC013129`
- Template: `lk_checkout_abandonado_30min_v4`
- Variante: `v4 note lowercase — isola opções Crisp`
- Component case: lower
- crisp_options: `{ "type": "note", "new_session": false }`
- HTTP: 200
- reason: `request_accepted`
- request_id: `c6d07e05-0ea0-4098-aa4b-4a0a4afbc277`

### D

- Marker: `IMGD013129`
- Template: `lk_checkout_abandonado_30min_v3`
- Variante: `v3 hybrid uppercase — compara com print recebido`
- Component case: upper
- crisp_options: `{ "as": "text", "type": "text", "new_session": false }`
- HTTP: 200
- reason: `request_accepted`
- request_id: `318d64db-005f-4acf-9998-32d271fd2261`

## Callback check inicial

Foram pesquisados os workflows de callback conhecidos:

- `HTTOStvvzcz0sELN`
- `8heG4ZyRp85p0MQj`

Resultado inicial: nenhum dos quatro `request_id` apareceu nos callbacks recentes até a primeira checagem pós-envio.

## Resultado reportado por Lucas

Lucas informou que não recebeu nenhuma das quatro mensagens (`IMGA013129`, `IMGB013129`, `IMGC013129`, `IMGD013129`).

## Verificação pós-docs Crisp

Fonte consultada: `https://docs.crisp.chat/guides/messaging-apis/whatsapp-api/` e `.../configuration/`.

Pontos confirmados nos docs:

- `crisp_options.type = "note"` é o padrão e pode não aparecer na Inbox até o usuário responder.
- Para a mensagem aparecer imediatamente para operadores na Inbox, deve ser enviada como `crisp_options.type = "text"`.
- Para `type = "text"`, o campo `text` é obrigatório em pelo menos um componente do `message_template.components[]` e recomendado em todos os componentes aplicáveis.
- O retorno inicial `request_accepted` gera um `request_id` e só significa que a Crisp aceitou/enfileirou a tentativa; o status final deve vir pelo Callback URL.
- O Callback URL deveria receber sucesso ou erro por tentativa aceita; em sucesso, deve conter `crisp_fingerprint`, `whatsapp_message_id` e `session_id`; em erro, deve explicar por que o template não foi enviado.

## Verificação técnica pós não-recebimento

- Callback workflows ativos: `HTTOStvvzcz0sELN` e `8heG4ZyRp85p0MQj`.
- Supabase `lk_crisp_whatsapp_receipts`: nenhum registro para os quatro request_ids da bateria.
- n8n executions recentes dos callbacks: nenhum hit para os quatro request_ids ou marcadores.
- Workflow de produção `kWQbmEMuvdipcGjd` está ativo e publicado, mas nos ticks recentes inspecionados não houve itens elegíveis no node `Filtrar elegíveis + dedup`, então não disparou novas mensagens automáticas nessa janela.

## Interpretação revisada

A bateria A/C com `note` não atende ao requisito de Lucas de aparecer na Inbox. B/D usaram `type:text`, mas ainda sem confirmação de callback/entrega; além disso, o payload atual da automação usa fallback `BODY.text` em nível top-level/compatibilidade LK, enquanto a documentação Crisp recomenda/define `text` dentro dos componentes do template.

Próximo ajuste seguro antes de novo envio: corrigir o payload para `type:text` com `text` documentado dentro do componente `BODY` do `message_template.components[]`, manter `new_session:false`, e não usar `note` para mensagens que precisam aparecer na Inbox.
