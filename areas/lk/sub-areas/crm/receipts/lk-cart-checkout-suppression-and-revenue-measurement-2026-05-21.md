# LK CRM — Supressão checkout > cart + mensuração de receita

Data UTC: 2026-05-21T00:55Z

## Aprovação

Lucas aprovou no turno atual:

- Fazer item 1: checkout abandonado suprime cart intent.
- Fazer item 4: mensuração fim-a-fim por receita.

Lucas recusou/dispensou:

- Quiet hours.
- Fallback por e-mail/Klaviyo — já existente.

## Mudanças executadas

### 1) Supressão checkout > cart

Workflow atualizado:

- `XLODECE4MvNRNCQ9`
- `LK - Cart Intent 30min Full Funnel - Crisp (ATIVO)`

Patch aplicado:

- Inserido node `Supabase Load Active Checkout Suppression` depois de `Filtrar cart intent elegíveis`.
- Inserido node `Aplicar supressão checkout > cart` antes de `Preparar payload Crisp Cart`.
- Nova ordem crítica:
  - `Filtrar cart intent elegíveis`
  - `Supabase Load Active Checkout Suppression`
  - `Aplicar supressão checkout > cart`
  - `Preparar payload Crisp Cart`

Regra ativa:

- Se o telefone tiver uma sequência de checkout abandonado ativa nos últimos 96h (`pending`, `sent`, `request_accepted`, `delivered`, `read`) em `lk_crm_checkout_sequences`, o cart intent é suprimido.
- A sequência de checkout tem prioridade sobre carrinho/cart intent.
- O patch não dispara mensagem; apenas altera o roteamento para próximos eventos elegíveis.

Readback:

- Workflow ativo: `true`
- `versionId == activeVersionId`: `true`
- Edge verificada: `Filtrar cart intent elegíveis -> Supabase Load Active Checkout Suppression -> Aplicar supressão checkout > cart -> Preparar payload Crisp Cart`

Backup raw com potencial conteúdo sensível:

- `/opt/data/hermes_bruno_ingest/.secrets/lk-cart-checkout-suppression-metrics-20260521T005405Z/`

## 2) Mensuração fim-a-fim por receita

Script read-only criado:

- `/opt/data/hermes_bruno_ingest/scripts/lk_crm_recovery_funnel_report.py`

Relatório latest gerado:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/reports/lk-crm-recovery-funnel-latest.md`

O relatório cruza:

- Supabase `lk_crm_cart_intent_events` para captura e identidade.
- Supabase `lk_crm_checkout_sequences` para sequências/disparos.
- Supabase `lk_crm_event_log` para resultados provider.
- Shopify Orders para pedidos e receita.

Atribuição de receita:

- Alta confiança: `exact_checkout_id` quando `order.checkout_id` bate com `checkout_id` da sequência CRM.
- Média confiança: `phone_window_7d` quando o mesmo telefone compra em até 7 dias após envio CRM.
- Telefones são exibidos apenas como last4.

Snapshot inicial do relatório 7d:

- Cart intent events: 101.
- Product view: 69.
- Identity update: 27.
- Cart event: 5.
- Identidade nos eventos: phone 0, email 0, Crisp 46, Klaviyo 75, Meta 96.
- Sequências checkout abandonado: 5 sent, todas 30min.
- Shopify janela 7d: 67 pedidos, R$ 193.255,55.
- Receita atribuída ao CRM no snapshot: R$ 0,00.

Interpretação:

- O sistema já mede captura → identidade → sequências → provider → pedido/receita.
- No snapshot atual ainda não há pedido atribuído aos envios de CRM.
- O cart intent continua sem telefone/e-mail direto nos eventos recentes; os sinais de Meta/Klaviyo/Crisp estão presentes, mas WhatsApp segue dependendo de telefone resolvido.

## Rollback

Para rollback do item 1:

- Restaurar workflow `XLODECE4MvNRNCQ9` a partir do backup raw em `.secrets`.
- Ou reconectar `Filtrar cart intent elegíveis` diretamente para `Preparar payload Crisp Cart` e remover/desconectar os nodes:
  - `Supabase Load Active Checkout Suppression`
  - `Aplicar supressão checkout > cart`

## Observação de segurança

Nenhum envio de WhatsApp foi disparado por esses scripts. Nenhum segredo foi impresso ou salvo no Brain.
