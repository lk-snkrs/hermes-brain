# Receipt — PRD lk-stock: arquitetura Gate B base local

Data UTC: 2026-06-08T17:18:29Z

## Continuação

Lucas mandou seguir após incluir base local com sync live via webhook e sync diário via cron.

## Alterações feitas

Arquivo PRD atualizado:

- `areas/lk/sub-areas/stock/PRD.md`

Template/schema criado:

- `areas/lk/sub-areas/stock/templates/base-local-gate-b-schema.md`

## O que foi detalhado

### Arquitetura mínima da base local — Gate B

O PRD agora define a base local como simples, auditável e reversível, preferencialmente SQLite ou equivalente local, com schema versionado antes de runtime.

Entidades mínimas registradas:

1. `products`
2. `variants`
3. `stock_snapshots`
4. `sales_velocity`
5. `demand_signals`
6. `scores`
7. `event_ledger`
8. `receipts`

Fluxos mínimos registrados:

- backfill inicial read-only;
- webhook live assinado;
- cron diário de reconciliação;
- consulta do agente com confirmação Tiny/fonte viva antes de afirmar disponibilidade/ruptura/P0/P1.

## Segurança registrada

- Webhook público deve preferir `hermes-webhooks` no Vercel quando houver provedor externo.
- Secrets ficam em Doppler/ambiente autorizado, nunca no Brain.
- Idempotência obrigatória por provider/event_id/hash.
- Ledger appendável/auditável.
- Sem write externo a partir da base local.

## Writes externos

0.

## Runtime ativado

Nenhum. PRD/documentação apenas.
