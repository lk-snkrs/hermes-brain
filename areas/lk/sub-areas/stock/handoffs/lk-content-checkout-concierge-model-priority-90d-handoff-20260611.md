# Handoff para [LK] Estoque Loja Física / lk-stock

Data: 2026-06-11
Origem: LK Content
Projeto: Klaviyo — Checkout Concierge / abandono de checkout por modelo
Solicitante: Lucas

## Pedido

Precisamos de um ranking sanitizado de famílias/modelos para priorizar os splits do Email 2 no flow de checkout abandonado.

## Janela

Últimos 90 dias.

## Escopo de dados solicitado

Agrupar vendas por família/modelo, não por SKU isolado.

Famílias iniciais para mapear:

1. New Balance 9060
2. New Balance 530
3. Onitsuka Tiger Mexico 66
4. Onitsuka Tiger Mexico 66 Sabot
5. Nike Vomero / Vomero Premium
6. Nike Mind 001 / Mind 002
7. Adidas low-profile / terrace: Samba, Gazelle, Campus, Taekwondo, SL 72
8. Outros modelos relevantes que aparecerem no top 90d

## Formato ideal do retorno

Para cada família/modelo:

- canonical_group
- aliases/matching_rules usados
- units_sold_90d
- distinct_orders_90d
- gross_revenue_context, se disponível
- representative_products/handles
- confidence_level
- observações de matching

## Restrições

- Não incluir PII de cliente.
- Não incluir dados sensíveis.
- Não concluir estoque/disponibilidade/pronta entrega a menos que seja explicitamente validado pelo stock owner.
- Shopify/Tiny/controle de estoque continuam sob responsabilidade do `lk-stock`; LK Content só vai usar o ranking para ordem de branch e copy.

## Uso pelo LK Content

Ordenar os Conditional Splits do Klaviyo Checkout Concierge e calibrar copy editorial por modelo.

## Status

Pendente retorno do `lk-stock`.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: waiting_event; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/lk-content-checkout-concierge-model-priority-90d-handoff-20260611.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Content / profile lk-content
- Reminder OS next action: Produzir somente copy/brief/preview interno para wishlist CRM; não enviar nem ativar Klaviyo/SWYM sem aprovação explícita.
- Reminder OS review trigger: Revisar quando Lucas pedir pacote CRM ou antes de qualquer Klaviyo/SWYM/customer-facing write.
- Evidence: areas/lk/sub-areas/stock/handoffs/lk-content-checkout-concierge-model-priority-90d-handoff-20260611.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
