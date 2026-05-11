# Índice de Rotinas — Hermes Brain

Este índice aponta para rotinas business-readable documentadas no Brain. Ele não prova que todos os crons estão ativos; sempre verificar cron real na VPS/ambiente antes de afirmar execução.

## Rotinas cross-área / operações

| Rotina | Caminho | Função |
|--------|---------|--------|
| Brain Sync | `areas/operacoes/rotinas/brain-sync.md` | Sincronização do Brain e versionamento |
| Heartbeat | `areas/operacoes/rotinas/heartbeat.md` | Checagens periódicas operacionais |
| Brain Health Check | `areas/operacoes/rotinas/brain-health-check.md` | Validação de secrets, links, agentes, rotinas e skills |
| Hermes Release Watch | `areas/operacoes/rotinas/hermes-release-watch.md` | Monitorar releases do Hermes Agent e avaliar melhorias aplicáveis |
| Hermes Runtime Observability | `areas/operacoes/rotinas/hermes-runtime-observability.md` | Inventário read-only de versão, containers, gateway, cron e logs Hermes |
| Material Ingest to PRD | `areas/operacoes/rotinas/material-ingest-to-prd.md` | Ingestão segura de material externo até documentação, matriz de decisão e PRD |
| Brain Improvement Score | `areas/operacoes/rotinas/brain-improvement-score.md` | Score executivo de saúde/maturidade do Hermes Brain após rodadas de melhoria |
| Retomada de Planos e PRDs | `areas/operacoes/rotinas/retomada-planos-prds.md` | Recupera estado de planos, PRDs, branches e análises pausadas antes de seguir |
| Revisão Operacional Multiempresa | `areas/operacoes/rotinas/revisao-operacional-multiempresa.md` | Leitura executiva sob demanda de LK, Zipper, SPITI e Operações usando Brain versionado |
| Higiene de Memória e Pendências | `areas/operacoes/rotinas/memory-hygiene-pendencias.md` | Organiza pendências, decisões, lições e memória durável sem misturar log de sessão |
| Security Checkup | `areas/operacoes/rotinas/security-checkup.md` | Revisão de secrets, permissões, prompt injection, integrações e ações sensíveis |
| Decisão Área/Skill/Subagent/Agente | `areas/operacoes/rotinas/area-skill-subagent-agent-decision.md` | Decide a menor estrutura suficiente antes de criar agentes, canais, crons ou skills |
| Hermes v0.13 Operacionalização | `areas/operacoes/rotinas/hermes-v013-operacionalizacao.md` | Converter novidades v0.13 em uso diário seguro: `/goal`, Kanban, no_agent, documentos e guardrails |
| Hermes v0.13 Watchdogs no_agent | `areas/operacoes/rotinas/hermes-v013-watchdogs-no-agent.md` | Propostas de watchdogs script-only silenciosos/read-only para Hermes/LK |
| Kanban LK Growth Ops v0.13 | `areas/operacoes/rotinas/hermes-v013-kanban-lk-growth-ops.md` | Desenho inicial de Mission Control LK em Kanban, sem ativar workers de produção |
| Hermes Approval Learning Loop | `areas/operacoes/rotinas/hermes-approval-learning-loop.md` | Registro de aprovações/correções de Lucas para virar guardrails, skills e rotinas |
| Hermes v0.13 Próximas Melhorias | `areas/operacoes/rotinas/hermes-v013-next-improvements-plan-2026-05-10.md` | Plano de melhorias v0.13 classificadas por risco e aprovação necessária |
| Revisão Semanal Multiempresa | `areas/operacoes/rotinas/revisao-semanal-multiempresa.md` | Revisão executiva LK/Zipper/SPITI/Hermes pelo Hermes Chief of Staff, sem ações externas |
| Hermes Gateway Remediation Plan | `areas/operacoes/rotinas/hermes-gateway-remediation-plan.md` | Plano seguro para diagnóstico/correção do gateway Telegram sem mudança não aprovada |
| Hermes Gateway Read-only Diagnostic 2026-05-04 | `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` | Diagnóstico read-only do warning gateway/cron e conflito Telegram, sem alteração de VPS/Docker |
| Hermes Runtime Update Plan | `areas/operacoes/rotinas/hermes-runtime-update-plan.md` | Plano de update v0.9.0 → v0.12.0 com backup/rollback e aprovação |
| Hermes Runtime Update Attempt 2026-05-05 | `areas/operacoes/rotinas/hermes-runtime-update-attempt-2026-05-05.md` | Registro da tentativa segura de pull/update Docker; imagem Hostinger latest permaneceu em v0.9.0 |
| Hermes Runtime Upgrade Options 2026-05-05 | `areas/operacoes/rotinas/hermes-runtime-upgrade-options-2026-05-05.md` | Matriz de decisão para v0.9.0 → v0.12.0 sem ação automática em Docker/VPS |
| Cron Inventory | `areas/operacoes/rotinas/cron-inventory.md` | Inventário de crons/VPS e status real das rotinas |
| n8n Inventory | `areas/operacoes/rotinas/n8n-inventory.md` | Inventário read-only de workflows n8n na VPS |
| Integration Secret Validation | `areas/operacoes/rotinas/integration-secret-validation.md` | Validação de nomes de secrets no Doppler sem imprimir valores |
| Shopify LK Read-only Sync | `areas/operacoes/rotinas/shopify-readonly-sync.md` | Consulta segura de Shopify LK sem alterações na loja |
| Supabase Audit Read-only | `areas/operacoes/rotinas/supabase-audit-readonly.md` | Auditoria read-only nas bases LK, Zipper e SPITI |
| Evolution Approval Flow | `areas/operacoes/rotinas/evolution-send-approval-flow.md` | Fluxo obrigatório de preview/aprovação para WhatsApp |
| Klaviyo Campaign Approval | `areas/operacoes/rotinas/klaviyo-campaign-approval-flow.md` | Separação entre análise/draft e envio real de campanha |
| Meta Ads Reporting Read-only | `areas/operacoes/rotinas/meta-ads-reporting-readonly.md` | Relatórios de mídia paga sem alterar campanhas/orçamentos |
| Hostinger/VPS Inventory Read-only | `areas/operacoes/rotinas/hostinger-vps-inventory-readonly.md` | Inventário seguro de VPS/Docker sem modificar produção |

## LK Sneakers

| Rotina | Caminho | Função |
|--------|---------|--------|
| Full Sync | `areas/lk/rotinas/full-sync.md` | Sincronização LK |
| Morning Briefing | `areas/lk/rotinas/morning-briefing.md` | Briefing matinal LK |
| Playbook LK Comando Diário | `areas/lk/rotinas/playbook-comando-diario.md` | Roteiro executivo para diagnóstico/prioridades LK com dados vivos |
| Sync Log | `areas/lk/rotinas/sync-log.md` | Auditoria de início/fim de sync |
| Consequence Tracker | `areas/lk/rotinas/consequence-tracker.md` | Registro de efeitos de ações |
| LK Stock Action Queue 2026-05-11 | `areas/lk/rotinas/stock-action-queue-2026-05-11.md` | Fila read-only de ruptura, baixo estoque, mapear SKU Tiny e sem SKU Shopify por influencer/produto/SKU/tamanho |
| LK Stock Saneamento B + Preview A 2026-05-11 | `areas/lk/rotinas/stock-sku-saneamento-b-e-preview-a-2026-05-11.md` | Execução read-only: primeiro saneia Fila B SKU Shopify↔Tiny, depois prepara preview P0/P1 de sourcing/reposição e cards Mission Control |
| LK Shopify SKU Padronizado para Tiny 2026-05-11 | `areas/lk/rotinas/shopify-sku-padronizacao-tiny-execution-2026-05-11.md` | Execução aprovada: 8 SKUs de variants Shopify alinhados exatamente ao `codigo` Tiny, com backup/rollback e verificação live |
| LK Shopify SKU Padronizado para Tiny — Catálogo 2026-05-11 | `areas/lk/rotinas/shopify-sku-padronizacao-tiny-catalogo-2026-05-11.md` | Execução aprovada no catálogo completo: 505 variants divergentes seguras alinhadas ao `codigo` Tiny, 505/505 verificadas live |
| LK Fila B Residual Pós-Saneamento 2026-05-11 | `areas/lk/rotinas/shopify-tiny-fila-b-residual-pos-saneamento-2026-05-11.md` | Classificação read-only dos 1.282 variants pulados por segurança: 857 com SKU sem match Tiny, 374 sem SKU, 51 ambíguos por título+tamanho |
| LK Fila B Residual Priorizada 2026-05-11 | `areas/lk/rotinas/shopify-tiny-fila-b-residual-priorizada-2026-05-11.md` | Fila curta de revisão manual antes da nova Fila A: 15 residuais cruzam com venda/ruptura; P1 ambíguos, P2 sem SKU, P3 com SKU sem Tiny seguro |
| LK P0 Residual Live Lookup 2026-05-11 | `areas/lk/rotinas/lk-p0-residual-live-lookup-enriched-2026-05-11.md` | Lookup read-only dos 15 P0 contra Shopify atual + Tiny; nenhuma linha segura para SKU-only automático sem confirmação/código canônico |
| LK P0 Residual Correction Queue 2026-05-11 | `areas/lk/rotinas/lk-p0-residual-correction-queue-2026-05-11.md` | Fila acionável para decisão humana/correção SKU/Tiny dos 15 P0 antes de qualquer Fila A/sourcing |
| LK P0 Tiny Code Correction Preview 2026-05-11 | `areas/lk/rotinas/lk-p0-tiny-code-correction-preview-2026-05-11.md` | Preview de correção Tiny `codigo`: 2 candidatas com alvo definido, 4 pendentes de decisão Lucas/Júlio |
| LK P0 Tiny Code Correction Execution 2026-05-11 | `areas/lk/rotinas/lk-p0-tiny-code-correction-execution-2026-05-11.md` | Execução aprovada: 2/2 códigos Tiny preenchidos e verificados ao vivo, sem Shopify/preço/estoque/produto |
| LK P0 Remaining Tiny Code Preview 2026-05-11 | `areas/lk/rotinas/lk-p0-remaining-tiny-code-preview-2026-05-11.md` | Lookup read-only dos 13 P0 restantes: 7 candidatos a preencher `codigo` Tiny via SKU Shopify, 6 bloqueados por decisão/cadastro |
| LK P0 Remaining Tiny Code Execution 2026-05-11 | `areas/lk/rotinas/lk-p0-remaining-tiny-code-execution-2026-05-11.md` | Execução aprovada: 7/7 códigos Tiny preenchidos e verificados ao vivo, sem Shopify/preço/estoque/produto |
| LK P0 Blocked Six Correction Queue 2026-05-11 | `areas/lk/rotinas/lk-p0-blocked-six-correction-queue-2026-05-11.md` | Recheck read-only dos 6 P0 restantes; por decisão Lucas ficam stand by/pending de baixa venda |
| LK OS Next Stage Fila A Sourcing Preview 2026-05-11 | `areas/lk/rotinas/lk-os-next-stage-fila-a-sourcing-preview-2026-05-11.md` | Próxima etapa LK OS: preview read-only de sourcing/reposição, 39 SKU/tamanho agregados e top 15 executivos, sem compra/contato/write |
| LK Fila A Sourcing Validation + Quote Preview 2026-05-11 | `areas/lk/rotinas/lk-fila-a-sourcing-validation-and-quote-preview-2026-05-11.md` | Continuação da Fila A: tetos de margem, gate de lead time e fila de cotação agrupada, sem envio/compra/write |
| LK SEO/CRO Weekly Improvement Loop | `areas/lk/rotinas/seo-cro-weekly-improvement-loop.md` | Rotina semanal read-only com Claude SEO: nota, meta e fila priorizada de melhorias de PDP/páginas |
| LK Search Console Read-only Router 2026-05-11 | `areas/lk/rotinas/search-console-readonly-router-2026-05-11.md` | Fase 6: GSC real como `fact_gsc`, queries/páginas/CTR/posição virando fila SEO/CRO sem writes |
| LK Merchant Center Feed Read-only Router 2026-05-11 | `areas/lk/rotinas/merchant-center-feed-readonly-router-2026-05-11.md` | Fase 6: Merchant real como `fact_merchant_center`, issues/destinos/feed virando fila de correção sem writes |
| LK PDP Low-conversion Priority Router 2026-05-11 | `areas/lk/rotinas/pdp-low-conversion-priority-router-2026-05-11.md` | Fase 6: GA4 + GSC + Merchant priorizando PDP/collection com tráfego alto e baixa conversão, sem writes |
| LK P1 SEO/CRO Approval Packets 2026-05-11 | `areas/lk/rotinas/p1-seo-cro-approval-packets-2026-05-11.md` | Fase 6: pacotes de aprovação top P1 com title/meta exatos e CRO visível separado, sem writes |
| LK Approved P1 SEO Fields Execution 2026-05-11 | `areas/lk/rotinas/approved-p1-seo-fields-execution-2026-05-11.md` | Execução aprovada: 8 SEO title/meta aplicados no Shopify e verificados live, com backup/rollback e sem mudanças visíveis |
| LK Data Spine Read-only | `areas/lk/rotinas/data-spine-readonly-2026-05-11.md` | Fase 1 do LK OS: fonte da verdade, entidades canônicas, reconciliação, credenciais por nome e lacunas sem writes |
| LK Daily Sales Brief Read-only 2026-05-11 | `areas/lk/rotinas/daily-sales-brief-readonly-2026-05-11.md` | Primeiro briefing diário real do LK OS com Shopify + GA4 + Tiny, local/read-only, sem cron/envio |
| LK Weekly CEO Review Read-only 2026-05-11 | `areas/lk/rotinas/weekly-ceo-review-readonly-2026-05-11.md` | Revisão semanal executiva com Shopify + GA4 + Tiny + Meta/Metricool como sinais, preview Telegram e contrato de silêncio, sem cron/envio |
| LK Weekly Stock/SKU Action Plan Read-only 2026-05-11 | `areas/lk/rotinas/weekly-stock-sku-action-plan-readonly-2026-05-11.md` | Fila operacional P0/P1 derivada do Weekly CEO Review: ruptura, baixo estoque e SKU/Tiny desconhecido, sem compra/contato/write |
| LK Weekly Quote Validation Preview Read-only 2026-05-11 | `areas/lk/rotinas/weekly-quote-validation-preview-readonly-2026-05-11.md` | Preview interno de validação/cotação dos P0/P1 semanais: tetos de custo, gate de lead time e grupos por família, sem fornecedor/compra/write |
| LK Supplier Quote Approval Packet Read-only 2026-05-11 | `areas/lk/rotinas/supplier-quote-approval-packet-readonly-2026-05-11.md` | Pacote de aprovação para decidir envio de cotação a fornecedores, com briefs preview e status approved/rejected/needs_data, sem envio/compra/write |
| LK Approval Decision Log + Router Read-only 2026-05-11 | `areas/lk/rotinas/approval-decision-log-router-readonly-2026-05-11.md` | Registro roteável das decisões pendentes de cotação, com status needs_approval/needs_data e próximos passos bloqueados até aprovação |
| LK On-demand Sourcing Router Read-only 2026-05-11 | `areas/lk/rotinas/on-demand-sourcing-router-readonly-2026-05-11.md` | Router de sourcing sob demanda para GOAT/Droper/StockX/KicksDev por decisão específica, sem full-sync de preços externos |
| Cross-sell Monitor | `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md` | Oportunidades pós-pedido |
| Playbook Campanha CRM Aprovada | `areas/lk/sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md` | Segmentação, preview e aprovação Lucas antes de campanha externa |
| LK Klaviyo P1 Draft Campaign | `areas/lk/sub-areas/crm/rotinas/klaviyo-p1-draft-campaign-2026-05-11.md` | Primeira execução P1 CRM/Klaviyo em Draft, sem envio/agendamento, com template/lista/campanha documentados |
| LK CRM Phase 5 Next Decision Router 2026-05-11 | `areas/lk/sub-areas/crm/rotinas/phase5-next-decision-router-readonly-2026-05-11.md` | Router de próxima decisão CRM: manter P1 Draft, bloquear repetição WhatsApp e preparar P2 preview ou refresh Data Spine |
| RFM Semanal | `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md` | Segmentação RFM e relatório |
| Outcomes Tracker | `areas/lk/sub-areas/crm/rotinas/outcomes-tracker.md` | Status de sugestões Hermes |
| Creative Pipeline | `areas/lk/sub-areas/trafego-pago/rotinas/creative-pipeline.md` | Hipótese → criativo → teste → learning |
| LK Ads Intelligence | `areas/lk/sub-areas/trafego-pago/rotinas/lk-ads-intelligence-metricool-meta-20260509.md` | Fonte validada para Google Ads via Metricool, Meta direto e leitura de influencer/product fit |
| Campaign Attribution Dictionary | `areas/lk/sub-areas/trafego-pago/rotinas/campaign-attribution-dictionary.md` | Dicionário de campanha/influencer/produto |
| LK Influencer Identity Bridge Read-only 2026-05-11 | `areas/lk/sub-areas/trafego-pago/rotinas/influencer-identity-bridge-readonly-2026-05-11.md` | Fila de handles/cupons/ad_id/UTM oficiais por influencer, com ponte Shopify/Tiny e Meta como platform_signal |
| Product Dashboard | `areas/lk/sub-areas/ecommerce/rotinas/product-dashboard.md` | Saúde de PDPs |
| Weekly Influencer Sales Email | `areas/lk/sub-areas/trafego-pago/rotinas/weekly-influencer-sales-email.md` | E-mail semanal aprovado com vendas por influencer, Meta canônico e comparação WoW |
| LK Weekly Internal Influencer Email Preview 2026-05-11 | `areas/lk/sub-areas/trafego-pago/rotinas/weekly-internal-influencer-email-preview-2026-05-11.md` | Preview interno de e-mail semanal, sem envio/cron, separando mídia, Shopify/Tiny e decisões bloqueadas |
| LK Creative Visual Approval Gate 2026-05-11 | `areas/lk/sub-areas/trafego-pago/rotinas/creative-visual-approval-gate-readonly-2026-05-11.md` | Gate visual de criativos: imagem só entra em e-mail/relatório depois de qualidade automática e aprovação humana |
| Pareto-Compatible Monthly Reconciliation | `areas/lk/sub-areas/trafego-pago/rotinas/pareto-monthly-reconciliation.md` | Conferência mensal com lógica Maicon/Pareto, tolerância 99%+ e leitura Lucas-operacional separada |
| LK Pareto vs Lucas Operational Split Read-only 2026-05-11 | `areas/lk/sub-areas/trafego-pago/rotinas/pareto-operational-split-readonly-2026-05-11.md` | Fronteira de uso entre relatório Pareto-compatible e decisão operacional Lucas por Shopify/Tiny bridge |
| Consolidar FAQ | `areas/lk/sub-areas/atendimento/rotinas/consolidar-faq.md` | Loop FAQ/suporte/bot |

## Zipper Galeria

| Rotina | Caminho | Função |
|--------|---------|--------|
| Consulta de Vendas de Obras | `areas/zipper/rotinas/consulta-vendas-obras.md` | Análise comercial com `vendas_tango` |
| Abordagem de Colecionadores | `areas/zipper/rotinas/abordagem-colecionadores.md` | Rascunhos e aprovação comercial |
| Playbook Abordagem Obra/Colecionador | `areas/zipper/rotinas/playbook-abordagem-obra-colecionador.md` | Abordagem sofisticada por obra/artista/colecionador sem hard sell |
| Planejamento de Feiras | `areas/zipper/rotinas/planejamento-feiras.md` | Checklists, responsáveis e execução |
| Playbook Execução de Feira | `areas/zipper/rotinas/playbook-feira-execucao.md` | Plano de feira com checklist por responsável e comunicação aprovada |
| Template Consulta Vendas Tango | `areas/zipper/sub-areas/vendas-obras/templates/consulta-vendas-tango.md` | Consulta read-only padronizada para vendas reais Zipper |
| Template Registro Pós-contato | `areas/zipper/sub-areas/colecionadores/templates/registro-pos-contato.md` | Registro factual após contato aprovado com colecionador |
| Template Checklist Feira por Fase | `areas/zipper/sub-areas/feiras/templates/checklist-feira-por-fase.md` | Checklist de feira com status confirmado/a confirmar |
| Template Briefing Publicação Obra/Artista | `areas/zipper/sub-areas/comunicacao/templates/briefing-publicacao-obra-artista.md` | Briefing de comunicação com tom Zipper e aprovação |

## SPITI Auction

| Rotina | Caminho | Função |
|--------|---------|--------|
| Verificação de Lances | `areas/spiti/rotinas/verificacao-lances.md` | Checagem segura de lances/lotes |
| Playbook Pregão ao Vivo | `areas/spiti/rotinas/playbook-pregao-ao-vivo.md` | Resposta segura durante pregão com hierarquia de fontes |
| Alerta de Lances | `areas/spiti/rotinas/alerta-lances.md` | Alertas, deduplicação e falhas conhecidas |
| Monitor Health | `areas/spiti/rotinas/monitor-health.md` | Health check read-only do monitor SPITI/lances antes de confiar em alertas |
| Playbook Divergência de Lances | `areas/spiti/rotinas/playbook-divergencia-lances.md` | Investigação quando email/site/banco/monitor não fecham |
| Relatório de Leilão | `areas/spiti/rotinas/relatorio-leilao.md` | Relatório interno com fonte e ressalvas |
| Pós-leilão e Lessons | `areas/spiti/rotinas/pos-leilao-lessons.md` | Fechamento de leilão com decisions, lessons e memória executiva |
| Template Relatório Interno SPITI | `areas/spiti/templates/relatorio-interno-matriz-evidencia.md` | Matriz de evidência por lote para relatório interno |

## Documentos de gestão relacionados

- `empresa/gestao/hermes-learning-loop.md` — regra global para registrar aprovações/correções e atualizar Brain/skills/PRDs/memória quando um padrão se repetir.

## Regras

- Secrets via Doppler `lc-keys/prd`.
- Rotina documentada ≠ cron confirmado.
- Mensagens externas, campanhas, posts e contato com cliente/colecionador exigem aprovação Lucas.
