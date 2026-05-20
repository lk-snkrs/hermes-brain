# LK — Checkout abandonado n8n: Supabase, callbacks Crisp e Error Workflow

Data: 2026-05-20
Agente: Hermes LK Growth

## Escopo aprovado por Lucas

Implementar no fluxo ativo de checkout abandonado:

1. migrar dedup/event log para Supabase/Postgres;
2. reconciliar `request_id` Crisp com callback real de entrega/falha;
3. criar Error Workflow/alerta Telegram separado;
4. mover Basic Auth Crisp para credential n8n dedicada.

## Workflows envolvidos

- Produção: `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`
- Callback Crisp ativo: `8heG4ZyRp85p0MQj` — `LK - Crisp WhatsApp Callback Capture (ATIVO)`
- Error workflow novo: `C4v2U9qbfhlVSPCF` — `LK - n8n Error Alert → Telegram + Supabase`
- Callback arquivado ignorado: `HTTOStvvzcz0sELN` — workflow arquivado, não atualizado.

## Snapshot / rollback

Snapshot pré-write salvo fora do Brain por conter potencialmente headers/credenciais:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-next-hardening-20260520-175911.json`
- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/8heG4ZyRp85p0MQj-pre-next-hardening-20260520-175911.json`
- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/HTTOStvvzcz0sELN-pre-next-hardening-20260520-175911.json`

Rollback: restaurar o JSON pré-write correspondente via API/UI n8n e revalidar `activeVersionId == versionId`.

## Alterações aplicadas

### 1. Persistência externa Supabase

Criadas/confirmadas tabelas Supabase:

- `public.lk_crm_checkout_sequences`
- `public.lk_crm_event_log`
- `public.lk_crisp_whatsapp_receipts`
- `public.lk_n8n_error_log`

Criadas funções RPC PostgREST:

- `public.lk_crm_record_checkout_send(jsonb,jsonb)`
- `public.lk_crm_record_crisp_receipt(jsonb)`
- `public.lk_n8n_record_error(jsonb)`

Observação técnica: o Postgres node direto do n8n falhou por SSL/IPv6/Supabase pool. O fluxo foi ajustado para usar Supabase REST/PostgREST com credential HTTP Header Auth n8n dedicada, evitando expor service key no workflow.

### 2. Dedup/event log

No workflow de produção:

- `Postgres Load CRM State` agora lê `lk_crm_checkout_sequences` via Supabase REST.
- `Filtrar elegíveis + dedup` passa a considerar histórico externo para `dedup_key` e frequency cap por telefone.
- `Postgres Persist CRM Result` agora chama RPC `lk_crm_record_checkout_send` para gravar sequência e log.
- `staticData` foi mantido como fallback/compatibilidade enquanto o banco assume como fonte persistente.

### 3. Reconciliar `request_id` Crisp

No callback ativo `8heG4ZyRp85p0MQj`:

- Webhook recebe payload do Crisp.
- `Prepare Callback Receipt SQL` normaliza `request_id`, evento e status.
- `Postgres Store Crisp Receipt` chama RPC `lk_crm_record_crisp_receipt`.
- A função grava receipt em `lk_crisp_whatsapp_receipts`, registra evento em `lk_crm_event_log`, e atualiza `lk_crm_checkout_sequences.status` quando há `request_id` correspondente.

### 4. Error Workflow / alerta Telegram

Criado workflow `C4v2U9qbfhlVSPCF`:

- `Error Trigger`
- `Prepare Error Alert`
- `Postgres Store Error`
- `Telegram Alert Lucas`

O workflow de produção foi configurado com `settings.errorWorkflow = C4v2U9qbfhlVSPCF`.

### 5. Basic Auth Crisp dedicada

O node `Crisp Send checkout touchpoint` foi migrado de header Authorization hardcoded para credential n8n dedicada:

- Credential: `Crisp WhatsApp Plugin Basic Auth - LK`
- Readback confirmou ausência de header `Authorization` hardcoded no node.

## Validação

### Readback n8n

Produção após patch:

- Workflow: `kWQbmEMuvdipcGjd`
- `active: true`
- `versionId: e3e34127-7741-4bfd-b11d-a2cacb2af950`
- `activeVersionId: e3e34127-7741-4bfd-b11d-a2cacb2af950`
- `errorWorkflow: C4v2U9qbfhlVSPCF`

Callback ativo após patch:

- Workflow: `8heG4ZyRp85p0MQj`
- `active: true`
- `versionId: 4cc4ba56-1161-4fe7-998f-3dff6a47d2f0`
- `activeVersionId: 4cc4ba56-1161-4fe7-998f-3dff6a47d2f0`

Error workflow após patch:

- Workflow: `C4v2U9qbfhlVSPCF`
- `active: true`
- `versionId: 1dd6ebbd-1290-4a80-8505-2057e1f17fa3`
- `activeVersionId: 1dd6ebbd-1290-4a80-8505-2057e1f17fa3`

### Syntax checks

Code nodes verificados com `node --check`:

- Produção: `Filtrar elegíveis + dedup`, `Marcar enviado no dedup`, `Preparar payload Crisp` — OK.
- Callback: `Prepare Callback Receipt SQL` — OK.
- Error workflow: `Prepare Error Alert` — OK.

### Callback sintético

Enviado callback sintético interno sem disparo WhatsApp para cliente:

- HTTP webhook: 200
- Execução callback: `11274`, status `success`
- Supabase: `synthetic_receipts = 1`, `synthetic_events = 1`

### Execução real após correção REST

Produção:

- Execução `11277`
- `status: success`
- `startedAt: 2026-05-20T18:20:25.031Z`
- `stoppedAt: 2026-05-20T18:20:27.205Z`

## Observações / incidentes durante patch

- Duas execuções intermediárias de produção (`11268`, `11272`) falharam durante tentativa de uso do Postgres node direto por erro de SSL/IPv6/Supabase. Corrigido migrando para Supabase REST RPC.
- Duas execuções intermediárias do callback (`11266`, `11270`) falharam pelo mesmo motivo. Corrigido e validado com execução `11274`.
- Error workflow também teve falhas intermediárias enquanto usava Postgres node direto (`11269`, `11273`). Foi migrado para Supabase REST RPC; não foi disparado teste sintético para não gerar alerta Telegram desnecessário ao Lucas.

## Compra concluída / supressão

O workflow usa Shopify GraphQL `abandonedCheckouts` e o Code node classifica `completedAt` como `purchaseStatus = purchased`. Se `completedAt` existir, o checkout é marcado como `purchased_before_touchpoint` e não entra nos touchpoints seguintes.

Limitação: não foi adicionado nesta rodada um recheck separado por pedido/order ID fora do payload de `abandonedCheckouts`; a proteção atual depende do `completedAt`/estado vindo do GraphQL de abandoned checkout e da ausência de item elegível no polling.

## Próximos pontos recomendados

- Monitorar os próximos ciclos reais com sends efetivos para confirmar gravação de `lk_crm_checkout_sequences` quando houver item elegível.
- Validar receipt real do Crisp quando chegar um callback de mensagem real, não apenas callback sintético.
- Opcional: adicionar recheck Shopify específico por checkout/order antes de cada touchpoint como proteção extra além do `completedAt` do abandoned checkout.
