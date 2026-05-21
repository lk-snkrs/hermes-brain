# LK Crisp — patch BODY.text documentado + canary interno — 2026-05-21

## Contexto

Lucas autorizou seguir após diagnóstico de que mensagens via Crisp devem aparecer na Inbox. Objetivo: alinhar o payload do checkout abandonado LK com a documentação Crisp para `crisp_options.type = "text"`, mantendo o shape híbrido LK que já havia funcionado.

## Ações executadas

### 1. Snapshot antes de write

- Workflow: `kWQbmEMuvdipcGjd`
- Nome: `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`
- Snapshot raw local, fora do Brain público: `/opt/data/hermes_bruno_ingest/n8n_snapshots/kWQbmEMuvdipcGjd_pre_crisp_body_component_text_20260521T015921Z.json`

### 2. Patch no n8n

Node alterado: `Preparar payload Crisp`.

Antes:

```js
{ type: 'BODY', parameters: bodyParams }
```

Depois:

```js
{ type: 'BODY', parameters: bodyParams, text: fallbackText }
```

Mantido o shape híbrido que já era o melhor baseline LK:

```js
crisp_options: { as: 'text', type: 'text', new_session: false }
BODY: { text: fallbackText }
```

### 3. Readback/validação

- Workflow ativo: `true`
- `versionId`: `05b65439-470f-47ac-92b0-d75dd57665e1`
- `activeVersionId`: `05b65439-470f-47ac-92b0-d75dd57665e1`
- `BODY.text` dentro do componente verificado: `true`
- `crisp_options` híbrido verificado: `true`

### 4. Canary interno Lucas

- Destino: Lucas interno, final `3361`
- Sem clientes/terceiros
- Template: `lk_checkout_abandonado_30min_v4`
- Marker: `FIX020030`
- Payload: `HEADER IMAGE` + `BODY.parameters` + `BODY.text` no componente + `crisp_options { as:text, type:text, new_session:false }`
- Imagem pública usada para header:
  - HTTP HEAD: `200`
  - Content-Type: `image/png`
  - Content-Length: `46674`
- Crisp HTTP: `200`
- Crisp reason: `request_accepted`
- Request ID: `acc30152-c26b-4c83-88fc-1c1d597349c5`

## Callback/readback pós-canary

- Supabase `lk_crisp_whatsapp_receipts`: `0` registros para o request id após primeira janela curta de espera.
- n8n callback executions pesquisadas nos workflows conhecidos (`HTTOStvvzcz0sELN`, `8heG4ZyRp85p0MQj`): nenhum hit para `acc30152-c26b-4c83-88fc-1c1d597349c5` ou `FIX020030` entre execuções recentes.

## Interpretação

- O patch de produção foi aplicado e lido de volta com sucesso.
- O canary foi aceito pela Crisp, mas `request_accepted` ainda não comprova entrega no aparelho nem visibilidade na Inbox.
- A confirmação final depende de Lucas verificar se recebeu `FIX020030` no WhatsApp e se a mensagem apareceu no Crisp Inbox.

## Rollback

Restaurar o snapshot:

`/opt/data/hermes_bruno_ingest/n8n_snapshots/kWQbmEMuvdipcGjd_pre_crisp_body_component_text_20260521T015921Z.json`

ou remover `text: fallbackText` do componente `BODY` mantendo o restante do payload anterior.

## Não executado

- Nenhum envio a clientes.
- Nenhum replay/backfill.
- Nenhuma alteração de Meta template, campanha, preço, cupom ou Shopify.
