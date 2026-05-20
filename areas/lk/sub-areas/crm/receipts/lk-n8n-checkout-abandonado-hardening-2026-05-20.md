# Receipt — hardening n8n checkout abandonado LK

Data: 2026-05-20  
Área: LK CRM / WhatsApp / Crisp / n8n / Shopify  
Workflow: `kWQbmEMuvdipcGjd` — `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`

## Aprovação

Lucas aprovou seguir no turno atual: “Aprovado seguir”.

## Backup / rollback

Snapshots raw do workflow foram salvos fora do Brain por poderem conter Authorization headers:

- Pré-hardening: `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-hardening-20260520-174228.json`
- Pós-hardening: `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-post-hardening-20260520-174526.json`

Rollback: restaurar o JSON pré-hardening pelo n8n API/UI e verificar `activeVersionId == versionId` após restauração.

## Mudanças aplicadas

1. **Paginação/volume Shopify**
   - `abandonedCheckouts` passou de `first: 100` para `first: 250`.
   - Objetivo: reduzir risco de perder checkout elegível em dias de maior volume.

2. **Frequency cap premium por telefone**
   - Adicionado `staticData.phoneSequences`.
   - Regra: 1 sequência ativa por telefone/checkouts diferentes em janela de 96h.
   - Mesma sequência/checkouts iguais continuam podendo avançar 30min → 24h → 72h.
   - Skip reason novo: `phone_frequency_cap_active_sequence_96h`.

3. **Audit log operacional no staticData**
   - Adicionado `staticData.auditLog` com retenção dos últimos 100 ticks.
   - Registra quantidade retornada pela Shopify e quantidade elegível enviada para próxima etapa.

4. **Tratamento de erro Crisp mais seguro**
   - Node `Crisp Send checkout touchpoint` recebeu `onError: continueRegularOutput`.
   - Objetivo: permitir que o node seguinte registre falha no dedup/manual review em vez de deixar `pending` silencioso quando o HTTP Request falhar.

5. **Remoção de fallback inseguro no payload Crisp**
   - `Preparar payload Crisp` não usa mais `originals[0]` quando `pairedItem` está ausente.
   - Agora falha explicitamente com erro de pareamento, evitando associar resposta/payload ao checkout errado em execuções multi-item.

6. **Workflow version marker**
   - `lkWorkflowVersion` atualizado para `checkout_abandonado_polling_graphql_30min_24h_72h_coupon_v2_hardened`.

## Verificação

Readback n8n após update:

- `active`: true
- `versionId`: `549acdb5-482a-475f-80d7-c5d217b752d9`
- `activeVersionId`: `549acdb5-482a-475f-80d7-c5d217b752d9`
- `triggerCount`: 1

Syntax check com `node --check`:

- `Filtrar elegíveis + dedup`: OK
- `Marcar enviado no dedup`: OK
- `Preparar payload Crisp`: OK

Execução real agendada pós-update:

- Execução `11255` — status `success`, modo `trigger`, iniciou `2026-05-20T17:45:04.032Z`, finalizou `2026-05-20T17:45:06.792Z`.

StaticData após verificação:

- `sent`: 3
- `failed`: 0
- `skipped`: 339
- `phoneSequences`: 0
- `auditLog`: 1

## O que não foi feito nesta rodada

Não foi implementada ainda a camada ideal Supabase/Postgres para dedup/event log. Motivo: é uma mudança maior de arquitetura e exige definir tabela/constraint, credencial e migração de estado. O hardening aplicado reduz risco no MVP sem trocar o storage.

Também não foi criado um Error Workflow separado nesta rodada. Parte da segurança foi adicionada diretamente no fluxo ativo via `onError` + mark failed. Um Error Workflow/alerta Telegram ainda é recomendado como próxima etapa.

## Próximos passos recomendados

1. Criar tabela Supabase/Postgres para `checkout_recovery_events` com unique key por `touchpoint + checkoutId + phone`.
2. Persistir `request_id` Crisp e reconciliar callback de entrega/falha/read.
3. Criar Error Workflow/alerta Telegram para falhas críticas.
4. Mover Basic Auth Crisp para credential n8n dedicada.
5. Testar primeira execução real de 24h e 72h com cupom.
