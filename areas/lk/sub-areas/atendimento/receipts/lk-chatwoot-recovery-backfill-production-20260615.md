# LK Chatwoot Recovery — backfill produção caso recovered legado

Data: 2026-06-15
Agente: lk-ops
Área: LK / Atendimento / Chatwoot Recovery
Tipo: write produção aprovado por Lucas

## Aprovação

Lucas autorizou explicitamente: "Pode fazer write na produção".

Escopo executado: reconciliar o único caso legado identificado na auditoria anterior em que havia compra posterior detectada, mas o checkout ainda não estava com status `recovered`.

## Backup antes do write

Backup criado na VPS antes da alteração:

`/root/chatwoot-rollbacks/recovery-backfill-20260615T130123Z/`

Arquivos:
- `shopify_recovery_checkouts_before.sql`
- `recovery_event_logs_before.sql`
- `readback_before_sanitized.txt`

Nenhum PII foi copiado para o Brain.

## Write executado

Transação SQL em produção:

- alvo: `shopify_recovery_checkouts.id=5`
- condição: status diferente de `recovered` e existência de compra posterior em `recovery_event_logs`
- alteração:
  - `status='recovered'`
  - `recovered_at=<timestamp da primeira compra posterior detectada>`
  - `updated_at=now()`

Resultado do update:

- linhas atualizadas: 1
- row pós-update sanitizada:
  - id: 5
  - status: `recovered`
  - touches_sent: 0
  - checkout_created_at: 2026-05-07 17:18:11
  - recovered_at: 2026-06-10 19:34:26.430406
  - updated_at: 2026-06-15 13:01:46.416341

## Verificação pós-write

Auditoria geral após o write:

- Total `recovered`: 91
- Total `notified`: 4
- Total `pending`: 532
- `purchase_after_not_recovered`: 0 em 24h, 7d, 30d e all-time

Estado final do problema auditado:

- Antes: 1 compra posterior sem `recovered`
- Depois: 0 compras posteriores sem `recovered`

## Non-actions

- Nenhum envio WhatsApp/canary.
- Nenhuma alteração em Shopify, Tiny, Klaviyo, Meta ou templates.
- Nenhum dado pessoal registrado no Brain.

## Rollback

Se necessário, usar o backup em:

`/root/chatwoot-rollbacks/recovery-backfill-20260615T130123Z/`

Rollback pontual possível restaurando a linha `shopify_recovery_checkouts.id=5` a partir do dump antes do write.
