# Handoff LK Content → lk-stock — grupos/modelos mais vendidos 90d

Data: 2026-06-10
Origem: LK Content / Lucas
Destino obrigatório: `[LK] Estoque Loja Física` / `lk-stock`

## Correção de roteamento

Lucas corrigiu: consultas relacionadas a vendas, estoque, disponibilidade e base operacional de produto devem ser terceirizadas ao agente especialista `lk-stock`. LK Content não deve puxar Shopify/Tiny/vendas diretamente para produzir ranking operacional; deve consumir o resultado validado pelo especialista e transformar em estratégia de conteúdo/CRM.

## Pedido para lk-stock

Gerar um relatório read-only dos **grupos/famílias de produtos mais vendidos nos últimos 90 dias**, sem dados de cliente e sem prometer estoque/disponibilidade.

Objetivo do LK Content: usar o ranking para definir quais modelos merecem branch próprio no flow de checkout abandonado por modelo.

## Grupos/modelos citados inicialmente

- New Balance 9060
- New Balance 530
- Onitsuka Tiger Mexico 66
- Onitsuka Tiger Mexico 66 Sabot
- Nike Vomero / Vomero Premium
- Nike Mind 001
- Nike Mind 002
- Outros grupos relevantes que aparecerem nos dados

## Saída desejada do lk-stock

Para cada grupo/modelo:

- nome canônico do grupo;
- aliases/regras de matching usadas;
- unidades vendidas nos últimos 90 dias;
- pedidos distintos aproximados;
- receita bruta contextual, se disponível;
- produtos/handles representativos;
- observação de confiança do agrupamento;
- aviso explícito: `estoque/disponibilidade não inferidos`.

## Guardrails

- Não incluir PII/dados de cliente.
- Não usar estoque como critério para LK Content.
- Não responder disponibilidade, pronta entrega ou tamanho.
- Tiny / `LK | CONTROLE ESTOQUE` continua sendo fonte de verdade para disponibilidade.
- Shopify pode ser usado como superfície de vendas/contexto se for o padrão do lk-stock.

## Como LK Content vai usar

Depois do retorno do lk-stock, LK Content vai montar a recomendação de branches no Klaviyo:

1. quais modelos entram como branch próprio;
2. ordem dos conditional splits;
3. quais modelos entram em fallback;
4. copy editorial do Email 2 por modelo;
5. sem envio/ativação de flow sem aprovação dupla.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: waiting_event; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/lk/sub-areas/stock/handoffs/lk-content-request-product-model-sales-groups-90d-20260610.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: [LK] Content / profile lk-content
- Reminder OS next action: Produzir somente copy/brief/preview interno para wishlist CRM; não enviar nem ativar Klaviyo/SWYM sem aprovação explícita.
- Reminder OS review trigger: Revisar quando Lucas pedir pacote CRM ou antes de qualquer Klaviyo/SWYM/customer-facing write.
- Evidence: areas/lk/sub-areas/stock/handoffs/lk-content-request-product-model-sales-groups-90d-20260610.md

## Reminder OS closure — 2026-06-12

- Status: expired/closed by Lucas request.
- Reason: conservative backfill loop reviewed; no longer treated as active pending work.
- Writes externos: 0.
- Reminder OS loop needed: no
- Evidence: areas/operacoes/reminder-os/reminders.jsonl
