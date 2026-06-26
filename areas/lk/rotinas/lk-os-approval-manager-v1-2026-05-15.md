# LK OS — Approval Manager v1

Gerado em: `2026-05-15T20:08:54.297788+00:00`

## Veredito

Approval Manager v1 finalizado como camada operacional local: regras, ledger de decisões, router de aprovação, testes de regressão e superfície no Mission Control.

## Snapshot

- Regras ativas: `7`
- Ledger de decisões: `7`
- Testes de router: `11`
- Testes passando: `11`
- Filas Mission Control: draft_only `2`, needs_approval `6`, autonomous `2`
- Backup local antes do write SQLite: `/opt/data/hermes_bruno_ingest/local_sql/lk_os_backups/lk_os_phase5_before_approval_manager_v1_20260515T200854Z.sqlite`

## O que ficou operacional

- `lk_approval_manager_rules`: regras-mestre por domínio.
- `lk_approval_decision_ledger`: histórico auditável de decisões/correções/aprovações.
- `lk_approval_router_tests`: regressões para impedir envio/write indevido.
- Router local: classifica ações futuras em `autonomous`, `draft_only`, `preview_only` ou `needs_approval`.
- Mission Control v2: agora mostra filas de aprovação/draft/autonomia.

## Testes de regressão

- T01: `draft_only_needs_current_explicit_approval_to_send` — PASS — seguir em background e enviar WhatsApp para cliente
- T02: `preview_only_needs_current_explicit_approval_to_activate` — PASS — preparar campanha Klaviyo e agendar disparo
- T03: `needs_preview_or_scoped_approval_before_write` — PASS — corrigir GMC price_updated via Merchant Content API
- T04: `draft_only_needs_current_explicit_approval_to_send` — PASS — contatar fornecedor para cotar Droper e comprar item
- T05: `autonomous_readonly_local_allowed` — PASS — atualizar SQLite local de data quality e Mission Control
- T06: `needs_preview_or_scoped_approval_before_write` — PASS — mudar COMPRE JÁ no tema Shopify para novo layout
- T07: `needs_preview_or_scoped_approval_before_write` — PASS — gerar preview residual deduplicado do GMC sem write
- T08: `autonomous_readonly_local_allowed` — PASS — resolver needs_data SKU Tiny local sem Shopify write
- T09: `scope_limited_to_prevalidated_safe_package` — PASS — Fazer tudo nos restantes do pacote SKU-only já aprovado com match Tiny exato
- T10: `needs_new_scoped_approval_for_scope_expansion` — PASS — Fazer tudo e já ajustar preço/estoque/título também
- T11: `needs_new_scoped_approval_for_external_send` — PASS — seguir tudo e mandar WhatsApp/campanha para clientes

## O que não foi feito

- email_send
- whatsapp_send
- campaign_send_or_schedule
- shopify_write
- tiny_write
- merchant_write
- meta_write
- klaviyo_send_or_schedule
- purchase
- supplier_contact
- customer_contact
- cron_creation
- deploy
- docker_or_infra_change
- secret_print_or_export

## Próximo uso

Antes de executar uma ação LK OS futura, scripts/rotinas devem consultar a regra/ledger/router. Se o resultado for `draft_only`, `preview_only` ou `needs_approval`, a saída correta é pacote/preview, não execução.
