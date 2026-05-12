# LK Sneakers — Mapa

Fonte resumida atual: `memories/lk.md`. Data contract atual: `contexto/data-spine-v0.1.md`.

## Sub-áreas

- `sub-areas/crm/` — recompra, RFM, cross-sell, leads esfriando, sugestões e consequências.
- `sub-areas/trafego-pago/` — hipóteses, criativos, testes, dados e learnings de performance.
- `sub-areas/ecommerce/` — Shopify, produtos, estoque, pedidos, UX e catálogo.
- `sub-areas/atendimento/` — FAQ, dúvidas, suporte e consolidação para bot.

## Projeto estratégico aprovado

- `projetos/lk-operating-system-prd.md` — PRD v0.1 do LK Operating System no Hermes: CEO/Chief of Staff da LK com curadoria, estoque, Shopify, CRM, conteúdo, SEO, pricing, sourcing acionado por sinal, Google/Meta/influencers, approval flow e learning loop.
- `projetos/lk-os-implementation-control.md` — plano mestre vivo de implementação do Projeto LK OS, com fases, definição de pronto, todo-list, próximos passos e frase canônica de retomada: `Seguir Projeto LK OS`.

## Design e comunicação visual

- `design/DESIGN.md` — DesignMD v0.1 da LK, derivado dos últimos e-mails enviados no Klaviyo.
- `design/previews/lk-designmd-pdp-preview.html` — HTML visual de PDP/produto para aprovação de layout.

## Equipe e roteamento

- `equipe/README.md` — matriz inicial de funções, aprovações e roteamento de relatórios do LK OS. Inclui Lucas, Renan, Júlio e Danilo com limites de envio; ainda exige validação antes de crons ou envios recorrentes.

## Rotinas LK globais

- `rotinas/data-spine-readonly-2026-05-11.md` — Fase 1 do LK OS: inventário de fontes, matriz Doppler sem valores, entidades canônicas, reconciliação, lacunas e primeiro snapshot read-only multi-fonte em `reports/lk-os-data-spine-snapshot-2026-05-11.md`.
- `rotinas/search-console-readonly-router-2026-05-11.md` — Fase 6 do LK OS: Search Console real como `fact_gsc`, queries/páginas/CTR/posição e oportunidades SEO/CRO sem writes.
- `rotinas/merchant-center-feed-readonly-router-2026-05-11.md` — Fase 6 do LK OS: Merchant Center real como `fact_merchant_center`, diagnóstico de feed/issues/destinos e fila de correção sem writes.
- `rotinas/pdp-low-conversion-priority-router-2026-05-11.md` — Fase 6 do LK OS: GA4 + GSC + Merchant em fila de PDP/collection com tráfego alto e baixa conversão, sem writes.
- `rotinas/p1-seo-cro-approval-packets-2026-05-11.md` — Fase 6 do LK OS: pacotes de aprovação para top P1 com title/meta exatos e recomendações CRO visíveis separadas, sem writes.
- `rotinas/approved-p1-seo-fields-execution-2026-05-11.md` — execução aprovada por Lucas: 8 SEO title/meta aplicados no Shopify e verificados live, com backup/rollback e sem mudanças visíveis.
- `rotinas/visible-cro-pending-future-2026-05-11.md` — decisão Lucas: CRO visível dos 8 P1 fica `pending_future`; nenhuma mudança de H1/body/layout/tema foi aplicada.
- `rotinas/approval-learning-ledger-2026-05-11.md` — Fase 7 do LK OS: ledger operacional de aprovações/aprendizados com 24 registros roteáveis (`executed_verified`, `pending_future`, `needs_approval`, `needs_data`) e 0 writes liberados.
- `rotinas/safe-automation-readiness-registry-2026-05-11.md` — Fase 8 do LK OS: catálogo safe-by-default de 6 automações candidatas em `dry_run_only`, com risco, rollback, contrato silent-OK e aprovação antes de ativação.
- `rotinas/daily-weekly-dry-run-validation-2026-05-11.md` — Fase 8: dry-run manual aprovado para `LK-AUTO-001` Daily Sales Brief e `LK-AUTO-002` Weekly CEO Review, elegíveis para decisão futura de cadência/destino, sem cron/n8n/envio/write.
- `rotinas/daily-weekly-silent-cron-activation-2026-05-11.md` — Fase 8: ativação dos cronjobs `no_agent` Daily 08:00 BRT e Weekly segunda 09:00 BRT, silent-OK, sem n8n/envio imediato/write produtivo.
- `rotinas/daily-weekly-mandatory-report-delivery-2026-05-11.md` — correção Lucas: Daily e Weekly devem ser enviados obrigatoriamente na cadência aprovada; P0/P1 são rótulos de prioridade, não gatilhos de entrega.
- `rotinas/phase8-operational-automation-registry-2026-05-11.md` — Fase 8 reconciliada: 6 automações rastreadas, 3 cronjobs ativos (`LK-AUTO-001/002/003`), 3 manual-only/bloqueadas e 0 n8n/writes produtivos.
- `rotinas/approval-ledger-refresh-guard-2026-05-11.md` — `LK-AUTO-004` guard manual pós-ação: regenera ledger, valida contradições e gera readiness; 24 registros, 0 fails/warnings, 0 cron/n8n/write.
- `rotinas/klaviyo-crm-draft-readiness-watcher-2026-05-11.md` — `LK-AUTO-005` watcher manual/read-only do rascunho Klaviyo: 10 checks, Draft confirmado, sem schedule/send/PII/deep link chutado.
- `rotinas/full-sync.md` — sincronizações LK.
- `rotinas/morning-briefing.md` — briefing matinal.
- `rotinas/sync-log.md` — auditoria de syncs.
- `rotinas/consequence-tracker.md` — consequências e aprendizados de ações.
- `rotinas/stock-action-queue-2026-05-11.md` — primeira fila operacional read-only do Stock Intelligence Center: ruptura, baixo estoque, mapear SKU Tiny e sem SKU Shopify por influencer/produto/SKU/tamanho, com preview de aprovação antes de sourcing/reposição.
- `rotinas/stock-sku-saneamento-b-e-preview-a-2026-05-11.md` — execução do bloco B antes do A: saneamento SKU Shopify↔Tiny read-only, candidatos de mapeamento, preview P0/P1 de sourcing/reposição e cards Mission Control unassigned.
- `rotinas/shopify-sku-padronizacao-tiny-execution-2026-05-11.md` — execução aprovada por Lucas para padronizar 8 SKUs de variants Shopify para ficarem idênticos ao `codigo` Tiny, com backup/rollback por variant e verificação live pós-write.
- `rotinas/shopify-sku-padronizacao-tiny-catalogo-2026-05-11.md` — execução aprovada para o catálogo completo: 505 variants Shopify com SKU divergente seguro foram alinhadas ao `codigo` Tiny, 505/505 verificadas live, com backup/rollback e pulos por ambiguidade/sem código.
- `rotinas/templates/` — templates read-only v0.1/v0.2/v0.3 do LK Operating System: `Daily Sales Brief`, `Stock Intelligence Center` e `Weekly CEO Review`, com exemplos fictícios em `rotinas/templates/examples/`, primeiro relatório real agregado/read-only com GA4 em `reports/lk-daily-sales-brief-real-2026-05-08-ga4-v02.md` e primeiro relatório real agregado/read-only de atribuição paga/influencers em `reports/lk-paid-attribution-brief-real-2026-05-08-v03.md`, primeiro Stock Intelligence + Influencer/Product Audit em `reports/lk-stock-influencer-audit-readonly-2026-05-10.md`, rotina/template de dicionário canônico em `sub-areas/trafego-pago/rotinas/campaign-attribution-dictionary.md`, dicionário operacional v0.2 em `sub-areas/trafego-pago/contexto/campaign-attribution-dictionary-v0.2.md` e ROAS operacional provisório por influencer em `reports/lk-influencer-operational-roas-v02-2026-05-10.md`.

## Playbooks operacionais

- `rotinas/playbook-comando-diario.md` — roteiro executivo para briefing/prioridades LK sem inventar dados.
- `sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md` — campanha CRM com segmentação, preview e aprovação Lucas antes de envio.
- `sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` — primeira campanha P1 CRM/Klaviyo colocada em Draft com lista/template/campanha, pendente de revisão final.
- `sub-areas/crm/rotinas/phase5-next-decision-router-readonly-2026-05-11.md` — próxima decisão Fase 5: P1 Klaviyo Draft, WhatsApp sem repetição automática, P2 preview ou refresh Data Spine.

## Ferramentas principais

Shopify, Supabase LK, Klaviyo, GA4/GSC, Meta Ads, Judge.me, Frenet, Tiny ERP, Evolution Clo e Telegram.

## Skills canônicas LK

- `skills/lk-shopify-readonly/SKILL.md` — Shopify LK em modo leitura, com Doppler e bloqueio de writes/envios sem aprovação.
- `skills/lk-crosssell/SKILL.md` — oportunidades de cross-sell pós-pedido.
- `skills/lk-leads-esfriando/SKILL.md` — leads/clientes em risco de esfriar.

## Regras permanentes

- Dados antes de afirmação.
- Copy LK sem travessão, sem “compre agora”, sem “melhor do Brasil”.
- Preview no Telegram antes de campanha, WhatsApp, contato com cliente ou ação externa.
- Doppler `lc-keys/prd` é a fonte de credenciais; nunca versionar valores.
