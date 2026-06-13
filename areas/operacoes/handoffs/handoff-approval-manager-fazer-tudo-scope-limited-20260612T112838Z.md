# Handoff — Approval Manager: “Fazer tudo” com escopo limitado

Criado em: `2026-06-12T11:28:38Z`
Status: `active_rule_verified`

## Destinatários

- Hermes Geral / Mesa COO
- Approval Manager / Learning Loop
- Multiempresa Routing
- LK OS / LK Stock / LK Shopify / LK Growth / LK Trends
- Qualquer agente/script que consuma aprovações amplas de Lucas

## Decisão aprovada

Lucas aprovou: transformar “Fazer tudo” em regra de escopo limitado, não autorização ampla.

## Regra para agentes

Quando Lucas disser `Fazer tudo`, `seguir tudo`, `continuar tudo`, `todos os restantes` ou equivalente:

1. Verificar qual pacote/preview/approval estava imediatamente em vigor.
2. Continuar somente alvos pré-validados dentro do mesmo escopo.
3. Manter os mesmos campos, sistemas, exclusões, rollback/readback e risco.
4. Pular alvos ambíguos ou fora do escopo.
5. Registrar receipt/readback.
6. Preparar novo approval packet para qualquer expansão.

## Bloqueios sem nova aprovação

- Novo campo ou alvo.
- Preço, estoque, título, tema, produto, cliente, fornecedor.
- Tiny write.
- Shopify write fora do campo já aprovado.
- WhatsApp/e-mail/campanha/envio externo.
- Produção, infra/runtime, banco, cron, secrets, integrações.

## Artefatos atualizados

- Brain rotina: `areas/lk/rotinas/lk-os-fazer-tudo-scope-limited-approval-guardrail-2026-06-12.md`
- SQLite local: `lk_approval_manager_rules`, `lk_approval_decision_ledger`, `lk_approval_router_tests`
- Skill central LK: `lk-operational-intelligence`
- Routing central: `multiempresa-routing-lucas`
- Learning loop: `empresa/gestao/hermes-learning-loop.md`
- Rotinas index: `empresa/rotinas/_index.md`

## Writes executados

- Local/Brain/SQLite/skills only.
- External writes: `0`.
- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/cliente/fornecedor/produção/infra/cron/secrets: `0`.

## Verificação

- Regras ativas no SQLite: `7`.
- Ledger total: `7`.
- Router tests total/passando: `11/11`.
- Nova regra: `LK-APPROVAL-BROAD-CONTINUATION-SCOPE-LIMIT-20260612`.

## Backfill funcional — Handoff + Reminder OS (2026-06-12T19:01:04Z)

- Agente/profile: Hermes Agent default / backfill local de handoff funcional
- Pedido original: Corrigir handoffs recentes que estavam como documentação passiva, sem transferência operacional verificável.
- Status: done; handoff normalizado retroativamente para contrato funcional.
- Fontes/evidência: `areas/operacoes/handoffs/handoff-approval-manager-fazer-tudo-scope-limited-20260612T112838Z.md`; `reports/handoff-functionality/handoff-functionality-2026-06-12.json`; ledger Reminder OS quando aplicável.
- Output artifact: este próprio handoff atualizado com bloco canônico de continuidade.
- Aprovação Lucas: autorização explícita no Telegram — “CORRIGIR POR FAVOR” — limitada a correção local/documental e Reminder OS; sem aprovação para writes externos/runtime.
- Writes externos: nenhum; 0 Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/prod/runtime writes.
- Reminder OS loop needed: no
- Reminder OS owner: Hermes Geral
- Reminder OS next action: Manter escopo de Approval Manager apenas local/documental; qualquer automação externa segue bloqueada até aprovação escopada.
- Reminder OS review trigger: Reabrir somente se Lucas pedir nova fase do Approval Manager ou se regressão de roteamento aparecer.
- Evidence: areas/operacoes/handoffs/handoff-approval-manager-fazer-tudo-scope-limited-20260612T112838Z.md
