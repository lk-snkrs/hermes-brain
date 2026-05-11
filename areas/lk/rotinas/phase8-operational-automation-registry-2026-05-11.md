# LK Phase 8 Operational Automation Registry, 2026-05-11

Generated at: `2026-05-11T22:34:07.834767+00:00`

## Veredito

A Fase 8 agora tem um registro operacional reconciliado: Daily e Weekly são entregas obrigatórias; SEO/CRO weekly já existe como cron read-only de preview; ledger, Klaviyo e sourcing continuam manuais/bloqueados conforme risco.

## P0/P1 em linguagem simples

- P0: Urgente hoje; pode exigir ação no mesmo dia.
- P1: Importante acompanhar/decidir; não é necessariamente incêndio.
- Regra de envio: Daily e Weekly são enviados sempre na cadência aprovada; P0/P1 só priorizam a leitura.

## Resumo

- Automações rastreadas: 6
- Cronjobs ativos: 3
- Entregas obrigatórias: 2
- Crons read-only de preview: 1
- Manual-only ou bloqueadas: 3
- n8n flows criados: 0
- Writes produtivos permitidos: 0

## Automações

### LK-AUTO-001 · Daily Sales Brief read-only mandatory delivery

- Status: `active_cron_mandatory_delivery`
- Risco: `low`
- Cadência: daily 08:00 BRT
- Job ID: `7c688553e293`
- Entrega: origin/Telegram
- Contrato: Always deliver the generated daily report; P0/P1 only prioritize content.
- Próximo gate: Monitor first scheduled delivery on 2026-05-12 08:00 BRT.

### LK-AUTO-002 · Weekly CEO Review read-only mandatory delivery

- Status: `active_cron_mandatory_delivery`
- Risco: `low`
- Cadência: weekly Monday 09:00 BRT
- Job ID: `953b9055458e`
- Entrega: origin/Telegram
- Contrato: Always deliver the generated weekly report; P0/P1 only prioritize content.
- Próximo gate: Monitor first scheduled delivery on 2026-05-18 09:00 BRT.

### LK-AUTO-003 · SEO/CRO weekly Claude SEO improvement loop

- Status: `active_existing_agent_cron_readonly_preview`
- Risco: `low`
- Cadência: weekly Monday 10:00 BRT
- Job ID: `15777e3416dc`
- Entrega: origin/Telegram
- Contrato: Generate read-only SEO/CRO queue and previews; writes require explicit approval.
- Próximo gate: Keep as read-only preview loop; do not auto-apply Shopify/Merchant/theme changes.

### LK-AUTO-004 · Approval Learning Ledger refresh

- Status: `manual_post_action_only`
- Risco: `low`
- Cadência: after approval/correction/execution artifacts, manual
- Job ID: `none`
- Entrega: Brain artifact/PR only
- Contrato: Regenerate after meaningful decisions; do not auto-approve or auto-execute.
- Próximo gate: Stay manual until pattern stabilizes; possible post-PR hook later with separate approval.

### LK-AUTO-005 · Klaviyo CRM draft watcher

- Status: `blocked_manual_readiness_only`
- Risco: `medium`
- Cadência: manual only
- Job ID: `none`
- Entrega: preview only
- Contrato: No send/schedule; only readiness and risk packet with verified IDs/links.
- Próximo gate: Needs Klaviyo read-only implementation and explicit Lucas approval.

### LK-AUTO-006 · On-demand sourcing router

- Status: `manual_per_item_approval_only`
- Risco: `medium`
- Cadência: manual/event only
- Job ID: `none`
- Entrega: preview only
- Contrato: Run only for named approved item; no full-sync, supplier contact, purchase, price or stock write.
- Próximo gate: Needs explicit Lucas/Júlio approval per item and real lead-time/cost parameters.

## Guardrails

- Nenhum n8n criado.
- Nenhum write em Shopify/Tiny/Merchant/GSC.
- Nenhuma campanha/envio para cliente/fornecedor.
- Medium risk permanece manual com aprovação específica.
