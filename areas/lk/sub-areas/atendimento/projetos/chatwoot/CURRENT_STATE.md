# Current State — Chatwoot / Elle / LK Atendimento

Atualizado em: `2026-06-10T18:33:50Z`

## Resumo em uma frase

O projeto Chatwoot da LK está documentado no Brain como frente de **atendimento interno/copiloto/pós-venda**, com várias integrações diagnosticadas/planejadas e algumas ações executadas com receipts; a pasta canônica consolida leitura e continuidade, mas qualquer write externo segue approval-gated.

## Frentes já trabalhadas

### 1. Elle conectada ao Chatwoot

- PRD principal: `prd-elle-chatwoot-shopify-whatsapp-transbordo-20260602.md`.
- Implementação/planejamento: `implementation-plan-elle-mvp1c-chatwoot-20260602.md`.
- Approval packets para writes internos e webhook.
- Receipts de token/Doppler, conexão, correção, dry-run, smoke test, canário e observação de evento real.

### 2. Shopify → Chatwoot

- Diagnóstico de importação de contato Shopify.
- PRD de event sync / CRM inteligente.
- Receipts de OAuth/app config/feature flag/hook/integration connected/population audit.
- Reports de dry-run/backfill de telefone.
- Regra: Shopify é gatilho/superfície; estoque continua Tiny.

### 3. WhatsApp / Evolution API / templates

- Intake Evolution API + Chatwoot.
- Guidance Evolution API → Chatwoot LK Flagship.
- PRD e plano para WhatsApp Template Builder.
- Receipts de capability check, feature enabled, builder local customization/deploy e availability check.
- Guardrail: campanhas/mensagens externas exigem aprovação escopada.

### 4. Chatwoot UI/sidebar/templates

- PRD de sidebar “Templates”.
- Implementation handoff, PR package handoff e live validation.
- Patch package preservado em `pr-packages/chatwoot-sidebar-templates/`.

### 5. Chatwoot Cloud / migração / inbox / data services

- Diagnósticos read-only de Chatwoot/Elle, data services e Cloud.
- Migration pack Elle → Chatwoot Cloud.
- Config dual-target preparada.
- Direcionamento de bot de atendimento LK no Chatwoot Cloud.

### 6. Pós-venda POS — PÓS VENDA LK FLAGSHIP

- Receipt principal: `receipts/lk-chatwoot-pos-venda-flagship-layer-20260610.md`.
- Script operacional: `/opt/data/scripts/lk_pos_postsale_chatwoot_layer.py`.
- State local: `state/lk_pos_postsale_chatwoot_state.json`.
- Report apply: `reports/lk_pos_postsale_chatwoot_layer_20260610T154557Z_apply.json`.
- Resultado documentado: 10 pedidos POS registrados como conversas/notas internas; mensagens ao cliente pelo Chatwoot: 0.

### 7. Motor de recuperação de carrinho + journeys WhatsApp (NOVO — 10/jun)

- Frente construída pelo Lucas com Claude (Cowork) no fork `lk-chatwoot` (produção `v2-recovery17`).
- Pacote canônico: `recovery-engine/` (README, ARQUITETURA, ESTADO-ATUAL, RUNBOOK, AUDIT-FIXES-2026-06-10).
- Estado: motor pronto e testado; fluxos automáticos DESLIGADOS por decisão do Lucas; templates preenchidos (8, tom LK) com interpolação; resposta de agente na inbox LK Flagship CONSERTADA (webhook Evolution); audit completo com todos os críticos corrigidos.
- Guardrail: delays ainda demo (1,2,3 min) — trocar para 60,1440,2880 AO LIGAR.

## Estado POS registrado

`processed_orders=10; updated_at_utc=2026-06-10T15:45:57.370898+00:00; guardrail=internal Chatwoot records only; no customer-visible Chatwoot messages`

## Inventário por categoria

- approval-packets: 2
- evaluation: 4
- plans: 2
- pr-packages: 3
- prds: 4
- receipts: 42
- reports: 8
- research: 2
- root-docs: 6
- scripts: 3
- state: 1
