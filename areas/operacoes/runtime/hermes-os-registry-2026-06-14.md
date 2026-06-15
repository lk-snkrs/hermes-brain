# Hermes OS Registry — 2026-06-14

Snapshot UTC: `2026-06-14T23:50:47Z`

Escopo: mapa canônico dos “OS” e camadas operacionais hoje observadas no Hermes de Lucas. Este arquivo separa **OS/camada operacional**, **profile especialista**, **crons/watchdogs**, **delivery**, **fonte de verdade**, **autoheal permitido** e **limites de aprovação**.

Fonte viva usada neste snapshot:

- `/proc/*/environ` + `cmdline` para gateways Hermes por `HERMES_HOME`.
- `/opt/data/cron/jobs.json`.
- `/opt/data/profiles/*/cron/jobs.json`.

Non-actions deste snapshot:

- Nenhum cron foi criado, removido, pausado ou alterado.
- Nenhum gateway/profile foi reiniciado.
- Nenhum Docker/VPS/Traefik/API/webhook/runtime foi alterado.
- Nenhuma integração externa foi chamada para write.
- Nenhum secret foi impresso; `values_printed=false`.

## Legenda

- **OS oficial**: tem PRD/rotina/camada explícita como sistema operacional interno.
- **Camada operacional**: rotina central recorrente, com função executiva ou de continuidade, mesmo sem profile dedicado.
- **Profile especialista vivo**: profile Hermes com gateway vivo; pode atuar como “OS” de área, mas status operacional específico ainda depende de crons/fonte viva.
- **Silent-OK**: deve ficar quieto quando saudável e alertar só exceção/ação.
- **Origin/Telegram**: entrega ao chat/canal Telegram configurado.

## Registry resumido

### 1. Memory OS

- Tipo: OS oficial / camada de memória e contexto.
- Runtime principal: `default` + scripts locais.
- Crons ativos:
  - `Hermes Memory OS daytime checker/router — 30min alert-only` — `deliver=origin`, `last_status=ok`.
  - `Hermes Memory OS weekly observability local/silent` — `deliver=local`, `last_status=ok`.
- Fonte de verdade:
  - `areas/operacoes/rotinas/hermes-memory-os-v1.md`
  - `areas/operacoes/projetos/memory-os/`
  - `reports/memory-hygiene/latest.json`
  - `memories/hot.md`, `memories/daily/`, `context/current/`, `context/packs/`
- Autoheal permitido:
  - Sim, para A0/A1 local/documental/secret-free: compactação segura, templates de coverage, daily/hot/context repair, receipts.
- Aprovação necessária:
  - runtime/gateway restart, provider externo de memória, alteração sensível de cron/delivery, secrets, produção ou writes externos.

### 2. Brain OS

- Tipo: OS oficial / camada de organização canônica do Brain.
- Runtime principal: `default` + scripts locais.
- Cron ativo:
  - `Brain OS silent-OK health/scanner watchdog` — `deliver=origin`, `last_status=ok`.
- Fonte de verdade:
  - `areas/operacoes/projetos/brain-os/`
  - `areas/operacoes/MAPA.md`
  - `scripts/brain_health_check.py`
  - scanners/reports Brain OS em `reports/`.
- Autoheal permitido:
  - Sim, para documentação, scanners, manifests, receipts, índices e hubs locais quando A0/A1.
- Aprovação necessária:
  - GitHub publish quando fora do pacote previamente aprovado, runtime/cron mutation, Docker/VPS/Traefik, produção, banco, integrações ou deletes amplos.

### 3. Mordomo OS

- Tipo: OS oficial / Lucas pessoal + Zipper/WhatsApp/email/calendar/CRM local.
- Profile vivo:
  - `mordomo` — gateway vivo em `/opt/data/profiles/mordomo`.
- Crons ativos:
  - `LC Mordomo OS post-cutover healthcheck` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS local-only scheduler` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS WhatsApp daily digest 17h` — `deliver=origin`, `last_status=ok`.
  - `LC Mordomo OS Calendar watcher` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS zipper_lead_intake` — `deliver=origin`, `last_status=ok`.
  - `LC Mordomo OS zipper_email_monitor` — `deliver=origin`, `last_status=ok`.
  - `LC Mordomo OS whatsapp_context_engine` — `deliver=origin`, `last_status=ok`.
  - `LC Mordomo OS crm_sync` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS pdf_knowledge_ingest` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS email_draft_engine local runner` — `deliver=local`, `last_status=ok`.
  - `LC Mordomo OS observability drift monitor` — `deliver=local`, `last_status=ok`.
- Crons pausados/replaced:
  - `LC Mordomo OS critical cron watchdog` — `enabled=false`, `last_status=ok`.
  - `LC Mordomo OS email_draft_engine` — `enabled=false`, substituído pelo local runner.
- Fonte de verdade:
  - `/opt/data/profiles/mordomo/cron/jobs.json`
  - `areas/operacoes/projetos/mordomo-os/`
  - `areas/operacoes/mordomo/`
- Autoheal permitido:
  - Sim para correções locais, dedupe, receipts, health local, parsing/ledger e silent-OK.
- Aprovação necessária:
  - WhatsApp pairing/reconnect, envio externo, resposta a cliente/lead, negociação, proposta, preço, logística, banco/prod, cron/delivery sensível ou credenciais.

### 4. Stock OS / LK Stock

- Tipo: OS oficial / estoque, Tiny, Shopify sales reconcile read-only.
- Profile vivo:
  - `lk-stock` — gateway vivo em `/opt/data/profiles/lk-stock`.
- Crons ativos:
  - `LK Stock Gate B daily freshness reconcile read-only` — `deliver=origin`, `last_status=ok`.
  - `LK Stock Tiny sharded full sync nightly read-only` — `deliver=origin`, `last_status=ok`.
  - `LK Shopify Sales OS nightly full reconcile read-only` — `deliver=origin`, `last_status` ainda ausente no registry lido.
- Fonte de verdade:
  - Profile `lk-stock`.
  - Stock OS DB/local reconciliation artifacts.
  - Tiny é fonte de verdade de estoque; Shopify é superfície/event trigger.
- Autoheal permitido:
  - Sim para reconciliadores/read-only/local DB, freshness checks, dashboards e receipts.
- Aprovação necessária:
  - qualquer write Tiny/Shopify, alteração de estoque, preço/disponibilidade, produção, campanha, cliente ou fornecedor.

### 5. Reminder OS

- Tipo: OS oficial / continuidade anti-stand-by cross-agent.
- Runtime principal: `default` + ledger/Kanban/scripts locais.
- Cron ativo:
  - `Reminder OS — 2h open-loop watchdog` — `deliver=origin`, `last_status=ok`.
- Fonte de verdade:
  - `areas/operacoes/rotinas/reminder-os-v0-2026-06-12.md`
  - `areas/operacoes/prds/reminder-os-prd-v1-2026-06-12.md`
  - `reports/reminder-os/`
  - ledger/Kanban `reminder-os`.
- Autoheal permitido:
  - Sim para ledger schema, ingress local, template audit, canonical status e noise suppression.
- Aprovação necessária:
  - executar a tarefa lembrada, write externo/prod, contato, campanha, banco, cron/runtime mutation.

### 6. Mesa COO

- Tipo: camada operacional executiva / ritual de decisões Telegram.
- Runtime principal: `default` cron agent.
- Cron ativo:
  - `Mesa COO diária Telegram` — `deliver=origin`, `last_status=ok`.
- Fonte de verdade:
  - `areas/operacoes/projetos/mesa-coo/`
  - `areas/operacoes/rotinas/mesa-coo-telegram-quality-audit.md`
  - Decision ledger / Approval ledger.
- Autoheal permitido:
  - Sim para UX/documentação/formatos/receipts locais e validações silent-OK.
- Aprovação necessária:
  - alterar cadência/delivery, executar decisões, integrar writes externos ou mudar runtime/gateway.

### 7. Zipper OS vendas

- Tipo: camada operacional comercial Zipper.
- Runtime principal: `default` cron + Mordomo/Zipper local stores.
- Cron ativo:
  - `Zipper OS vendas 09h WhatsApp/email` — `deliver=local`, `last_status=ok`.
- Fonte de verdade:
  - `areas/zipper/`
  - `areas/zipper/projetos/email-crm-intake/`
  - Mordomo OS stores/receipts quando o canal passa por Mordomo.
- Autoheal permitido:
  - Sim para relatório local, readiness, partial delivery classification e receipts.
- Aprovação necessária:
  - envio WhatsApp/e-mail, contato externo, proposta, preço, logística, CRM/Supabase write, reconexão WhatsApp.

### 8. LK Shopify Sales OS

- Tipo: camada operacional read-only de vendas/reconciliação Shopify.
- Runtime principal: profile `lk-stock`.
- Cron ativo:
  - `LK Shopify Sales OS nightly full reconcile read-only` — `deliver=origin`, `last_status` ausente no registry lido.
- Fonte de verdade:
  - `lk-stock` para reconciliação/estoque.
  - Shopify para pedidos/superfície; Tiny para estoque.
- Autoheal permitido:
  - Sim para read-only reconcile, local DB/report/receipt.
- Aprovação necessária:
  - qualquer write Shopify/Tiny, alteração de pedido/estoque/preço, contato cliente ou produção.

## Profiles especialistas vivos que funcionam como OS de área

Estes têm gateway vivo hoje. Nem todos têm “OS” formal no nome, mas operam como superfícies permanentes por domínio.

### LK Growth OS

- Profile vivo: `lk-growth`.
- Crons relevantes:
  - `LK Growth Cron Delivery Watchdog` — `deliver=origin`, `last_status=ok`.
  - `LK Growth D+14 impact review — product operational copy cleanup` — `deliver=origin`, `last_status` ausente no registry lido.
- Escopo: SEO/GEO/CRO/GMC/conteúdo/analytics/oportunidades.
- Writes externos: bloqueados sem aprovação escopada.

### LK Shopify OS

- Profile vivo: `lk-shopify`.
- Escopo: superfície Shopify, previews, QA, readback, receipts e execuções escopadas quando aprovadas.
- Writes Shopify/theme/produto/menu/tag: bloqueados sem aprovação escopada.

### LK Trends

- Profile vivo: `lk-trends`.
- Crons relevantes:
  - `LK-TRENDS · Notícias sneaker/fashion da semana` — `deliver=telegram`, `last_status=ok`.
  - `LK-TRENDS · Cloudflare email delivery` — `deliver=local`, `last_status=ok`.
- Escopo: tendências, pesquisa, notícias e insumos para Growth/Content/Collection.
- Writes externos/campanhas/envios: bloqueados sem aprovação escopada.

### LK Finance

- Profile vivo: `lk-finance`.
- Escopo: gastos, recebimentos, caixa e conciliação.
- Writes bancários/financeiros/ERP: bloqueados sem aprovação escopada.

### LK Content

- Profile vivo: `lk-content`.
- Crons relevantes:
  - `LK Content — Calendário mensal v0` — `deliver=origin`, `last_status` ausente no registry lido.
  - `LK Content — Planejamento semanal` — `deliver=origin`, `last_status=ok`.
  - `LK Content — Radar Growth Trends` — `deliver=origin`, `last_status=ok`.
  - `LK Content — Klaviyo sent watchdog` — `deliver=origin`, `last_status=ok`.
- Escopo: calendário, conteúdo, Klaviyo-first, insumos Growth/Trends.
- Sends Klaviyo/e-mail/social: bloqueados sem aprovação/double-confirm quando aplicável.

### LKGOC / LK Collection Optimizer

- Profile vivo: `lk-collection-optimizer`.
- Escopo: otimização de coleções, rebuilds, scorecards, previews e approvals.
- Fonte canônica: `areas/lk/sub-areas/collection-optimizer/` + skill local.
- Writes Shopify/theme/produção: bloqueados sem aprovação escopada.

### LK Ops

- Profile vivo: `lk-ops`.
- Escopo: operações LK, execução operacional, stock/ops interfaces quando não for caso exclusivo `lk-stock`.
- Writes externos/prod: bloqueados sem aprovação escopada.

### SPITI

- Profile vivo: `spiti`.
- Escopo: Hub, leilões, lotes, CRM, Financial e Growth SPITI.
- Writes CRM/admin/leilão/financeiro: bloqueados sem aprovação escopada.

### SPITI Atendimento

- Profile vivo: `spiti-atendimento`.
- Escopo: atendimento/triagem SPITI.
- Contato externo/resposta a cliente: bloqueado sem fonte/aprovação quando sensível.

## Profiles existentes não classificados como OS ativo neste snapshot

Perfis existentes no filesystem que não apareceram como gateway vivo neste snapshot:

- `brain-process`
- `hermes-ops-readonly`
- `lc-claude-cli`
- `lk-analyst-readonly`
- `lk-content-reviewer`

Interpretação: são suporte/read-only/dormant ou perfis de uso sob demanda; não contar como OS rodando sem nova verificação viva.

## Regras de governança para este registry

1. Este registry é snapshot; estado vivo deve ser revalidado antes de afirmar “rodando agora”.
2. `last_status=ok` em cron não prova entrega útil ao Lucas; prova apenas último status registrado pelo scheduler.
3. Profile vivo não autoriza writes do domínio.
4. OS/camada pode autoheal somente em A0/A1 local/read-only/documental/script-safe.
5. A2/A3/A4 exigem approval packet específico com alvo, risco, rollback, verificação e secret hygiene.
6. Telegram deve obedecer silent-OK: alertar só quando houver ação, decisão, exceção ou falha atual.
7. Secrets sempre Doppler-first/wrapper seguro; reports devem manter `values_printed=false`.

## Próxima melhoria sugerida

Transformar este snapshot em rotina `hermes-os-registry.md` atualizada por um watchdog read-only/silent-OK que compara:

- profiles configurados vs gateways vivos;
- crons OS enabled/paused;
- last_status atual vs stale;
- delivery local/origin/telegram;
- owner/fonte de verdade;
- approval boundary.

Não criar esse cron automaticamente sem aprovação de cadência/kill criteria.
