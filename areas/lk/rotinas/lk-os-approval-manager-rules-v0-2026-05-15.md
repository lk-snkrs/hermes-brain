# LK OS — Approval Manager Rules v0

Gerado em: `2026-05-15T19:47:39.003558+00:00`
Status: `active_local_rule_layer`

## Veredito

Materializei o Approval Manager em SQLite local e Brain: agora os gates principais do LK OS são regras consultáveis, não apenas texto solto.

## Snapshot

- Regras ativas: `7`
- Regras que exigem aprovação: `6`
- Regras autônomas read-only/local: `1`
- Backup local antes do write SQLite: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups/lk_os_phase5_before_approval_manager_rules_v0_20260515T194739Z.sqlite`

## Regras vivas

### LK-APPROVAL-EXTERNAL-SEND-DRAFT-ONLY-20260515

- Domínio: `external_contact`
- Estado default: `draft_only`
- Exige aprovação: `True`
- Contrato de aprovação: Current-turn explicit approval with named recipient + exact payload. Background/seguir never authorizes send.
- Exemplo: Paulo/Zipper correction: should have generated draft, not sent email.

### LK-APPROVAL-COMPRE-JA-VISUAL-BASELINE-20260515

- Domínio: `theme_cro_visual`
- Estado default: `visual_preview_or_reversible_fix`
- Exige aprovação: `True`
- Contrato de aprovação: Visual/theme changes require preview or exact scoped approval; if correcting a regression to original, keep parity and verify live/readback.
- Exemplo: COMPRE JÁ returned to white background, light-gray border, no shadow/double stroke; preserve original visual parity.

### LK-APPROVAL-CAMPAIGN-GATE-20260515

- Domínio: `campaign_crm_paid`
- Estado default: `preview_only`
- Exige aprovação: `True`
- Contrato de aprovação: Inline packet with audience, copy/creative, timing, budget/flow, expected action, rollback/stop plan; Lucas approval before send/activate/schedule.
- Exemplo: Klaviyo/LK CRM can be draft/readiness only until Lucas approves send/schedule.

### LK-APPROVAL-SOURCING-GATE-20260515

- Domínio: `sourcing_purchase_supplier`
- Estado default: `decision_preview_only`
- Exige aprovação: `True`
- Contrato de aprovação: Exact product/SKU/size, cost logic, price/margin, source, lead time, risk, and whether action is quote/contact/purchase. Lucas approval before external contact or purchase.
- Exemplo: Sourcing uses Droper, exact StockX/GOAT, import cost FX*1.05, ideal cost*2; action remains preview until approved.

### LK-APPROVAL-GMC-GATE-20260515

- Domínio: `gmc_merchant_feed`
- Estado default: `read_only_or_preview`
- Exige aprovação: `True`
- Contrato de aprovação: Exact offer/product IDs, fields, source ownership, before snapshot/rollback, no bulk wildcard, post-apply verification. Price/source writes require special caution.
- Exemplo: GMC residual/preço remains blocked until UI/manual Google & YouTube/Shopify/Merchant checklist and exact preview.

### LK-APPROVAL-DATA-QUALITY-AUTONOMY-20260515

- Domínio: `data_quality_local_readonly`
- Estado default: `autonomous_readonly_local`
- Exige aprovação: `False`
- Contrato de aprovação: Read-only/local/reversible data quality fixes may proceed; source-of-truth writes remain gated.
- Exemplo: Tiny stock snapshot and lk_variant_commercial_state can update locally; final commercial action waits for coverage/approval.

### LK-APPROVAL-BROAD-CONTINUATION-SCOPE-LIMIT-20260612

- Domínio: `broad_continuation_approval`
- Estado default: `scope_limited_to_prevalidated_safe_package`
- Exige aprovação: `True`
- Contrato de aprovação: “Fazer tudo” / `seguir tudo` / `continuar tudo` só continua o mesmo pacote seguro já aprovado. Qualquer novo campo, alvo, envio externo, preço, estoque, cliente, fornecedor, produção, infra, banco, cron, secret ou integração exige novo approval packet escopado.
- Exemplo: LK Stock second pass continuou apenas SKU-only comprovável e manteve bloqueados alvos ambíguos.

## O que não foi feito

- email_send
- whatsapp_send
- campaign_send
- shopify_write
- tiny_write
- merchant_write
- meta_write
- klaviyo_send_or_schedule
- purchase
- supplier_contact
- cron_creation

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: tratar estas regras como camada local de governança do LK OS, sem transformar o documento em autorização para ações produtivas.
- Ação proposta se aprovado em wave futura: usar as regras como checklist/gate para approval packets, previews e blockers dos domínios listados.

### Escopo permitido
- Escopo permitido neste artefato: consulta local/read-only das regras, documentação, validação de packets e geração de previews/rascunhos.
- Pode fazer: classificar ações por domínio, apontar exigência de aprovação e bloquear execução quando faltar approval packet escopado.

### O que continua bloqueado
- Não pode enviar e-mail/WhatsApp/campanha, fazer Shopify/Tiny/Merchant/Meta/Klaviyo writes, compra, contato com fornecedor, criação de cron ou qualquer execução externa/produtiva apenas com base neste documento.
- `seguir`, `fazer tudo` ou aprovação genérica continuam limitados ao pacote seguro já validado; novo alvo exige novo approval packet.

### Risco
- Risco principal: interpretar regras de governança como permissão de execução. Mitigação: fail-closed, approval packet específico e receipt/readback antes de qualquer write sensível.
- Risco adicional: regra desatualizada; mitigar com revisão periódica e evidência viva antes de agir.

### Opções de aprovação
- Aprovar uso local/read-only das regras como checklist/gate.
- Aprovar uma regra específica para virar teste/validator local.
- Pedir ajuste em uma regra antes de adoção.
- Bloquear qualquer uso além de referência histórica.

### Secret hygiene
- Não armazenar nem imprimir tokens, API keys, passwords, refresh tokens, service-account JSON ou connection strings nas regras, relatórios ou receipts.
- Quando houver validação com integrações, usar Doppler/wrapper seguro e registrar apenas `values_printed=false`.
