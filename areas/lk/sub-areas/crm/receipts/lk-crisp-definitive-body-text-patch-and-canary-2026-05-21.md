# LK Crisp — patch BODY.text documentado + canary interno — 2026-05-21

## Contexto

Lucas autorizou seguir após diagnóstico de que mensagens via Crisp devem aparecer na Inbox. Objetivo: alinhar o payload do workflow ativo com o padrão documentado pela Crisp, preservando o shape híbrido LK que já havia funcionado em teste texto.

## Patch aplicado

Workflow n8n:

- ID: `kWQbmEMuvdipcGjd`
- Nome: `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`

Snapshot rollback criado antes do patch:

- `/opt/data/hermes_bruno_ingest/n8n_snapshots/kWQbmEMuvdipcGjd_pre_crisp_body_component_text_20260521T015921Z.json`

Alteração no node `Preparar payload Crisp`:

- Antes, componente `BODY` do template era montado assim:
  - `{ type: 'BODY', parameters: bodyParams }`
- Depois:
  - `{ type: 'BODY', parameters: bodyParams, text: fallbackText }`

Mantido:

- `crisp_options.as = text`
- `crisp_options.type = text`
- `crisp_options.new_session = false`
- fallback legado `BODY.text`

Motivo:

- Documentação Crisp para Inbox/text mode pede `text` no componente do template.
- LK já tinha baseline melhor com shape híbrido `as:text + type:text + new_session:false`.

## Verificação readback

Readback do n8n após update:

- `active: true`
- `versionId == activeVersionId`
- Code node contém `BODY` com `text: fallbackText`
- Code node contém shape híbrido `as:'text'`, `type:'text'`, `new_session:false`

## Canary interno enviado

Destino interno de Lucas:

- final: `3361`

Payload:

- Template: `lk_checkout_abandonado_30min_v4`
- Header image: sim
- Marker: `FIX020030`
- Body text: `Oi Lucas, teste LK FIX020030 com imagem.`

Resposta síncrona Crisp:

- HTTP: `200`
- Crisp error: `false`
- Crisp reason: `request_accepted`
- Request ID: `acc30152-c26b-4c83-88fc-1c1d597349c5`

## Confirmação humana

Lucas informou em seguida:

- não recebeu no WhatsApp;
- não viu no Inbox.

## Auditoria pós-non-receipt

### Callback / Supabase

- Supabase `lk_crisp_whatsapp_receipts`: nenhum registro para `acc30152-c26b-4c83-88fc-1c1d597349c5`.
- n8n callbacks conhecidos (`HTTOStvvzcz0sELN`, `8heG4ZyRp85p0MQj`): nenhum hit com `acc30152...` ou `FIX020030` nas execuções recentes.

### Crisp REST / conversa do telefone final 3361

Consulta read-only via Crisp REST Website Token encontrou a conversa WhatsApp do número final `3361`:

- `session_a706e297-863a-452b-9b73-c845f7c42467`
- origin: `urn:crisp.im:whatsapp:0`

Mensagens recentes na conversa mostram que as tentativas de teste foram registradas como notas/picker internos e seguidas de erro de WhatsApp.

Erro recorrente encontrado, inclusive no horário do canary final:

```text
The message was not delivered because WhatsApp limited the number of marketing messages sent to this user, especially if they are less likely to engage with them. Please try again at a later time to send this message.
```

A própria nota aponta para a documentação Meta:

- Per-User Marketing Template Message Limits

Interpretação técnica:

- Isso é bloqueio Meta/WhatsApp por limite per-user de templates de Marketing, equivalente ao erro de ecossistema/engajamento observado antes (`131049`).
- Não é prova de que a imagem, o template `v4`, ou o `BODY.text` estejam errados.
- Como o destino de teste recebeu várias tentativas de Marketing em sequência, o número de Lucas ficou inadequado para validar entrega nesse momento.

## Conclusão atualizada

O canary `FIX020030` não chegou porque a entrega foi bloqueada pelo WhatsApp/Meta para esse usuário/recipient, por limite de templates Marketing. A Crisp registrou um erro interno na conversa, mas isso não equivale a mensagem enviada nem a visibilidade normal como mensagem de atendimento no Inbox.

## Decisão operacional

- Não reenviar mais templates Marketing para o número final `3361` agora.
- Próximo teste decision-grade deve usar:
  1. outro número interno/controlado com opt-in, ou
  2. aguardar cooldown da Meta para o número de Lucas, ou
  3. testar apenas recebimento/Inbox com mensagem não-template dentro de janela de atendimento, se houver janela aberta e aprovação explícita.

## Risco produção

- Clientes reais não devem ser avaliados pelo comportamento do número de Lucas após vários canaries.
- Porém, em produção, cada falha por limite per-user deve ser tratada como `failed/blocked`, não como `sent`, e deve entrar em monitoramento.
