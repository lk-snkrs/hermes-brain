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
| Cross-sell Monitor | `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md` | Oportunidades pós-pedido |
| Playbook Campanha CRM Aprovada | `areas/lk/sub-areas/crm/rotinas/playbook-campanha-crm-aprovada.md` | Segmentação, preview e aprovação Lucas antes de campanha externa |
| RFM Semanal | `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md` | Segmentação RFM e relatório |
| Outcomes Tracker | `areas/lk/sub-areas/crm/rotinas/outcomes-tracker.md` | Status de sugestões Hermes |
| Creative Pipeline | `areas/lk/sub-areas/trafego-pago/rotinas/creative-pipeline.md` | Hipótese → criativo → teste → learning |
| LK Ads Intelligence | `areas/lk/sub-areas/trafego-pago/rotinas/lk-ads-intelligence-metricool-meta-20260509.md` | Fonte validada para Google Ads via Metricool, Meta direto e leitura de influencer/product fit |
| Campaign Attribution Dictionary LK | `areas/lk/sub-areas/trafego-pago/rotinas/campaign-attribution-dictionary.md` | Dicionário canônico campanha/influencer → UTM/cupom/produto/SKU/tamanho/estoque |
| Weekly Influencer Sales Email | `areas/lk/sub-areas/trafego-pago/rotinas/weekly-influencer-sales-email.md` | E-mail semanal aprovado com vendas por influencer, Meta canônico e comparação WoW |
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

## Regras
## Documentos de gestão relacionados

- `empresa/gestao/hermes-learning-loop.md` — regra global para registrar aprovações/correções e atualizar Brain/skills/PRDs/memória quando um padrão se repetir.


- Secrets via Doppler `lc-keys/prd`.
- Rotina documentada ≠ cron confirmado.
- Mensagens externas, campanhas, posts e contato com cliente/colecionador exigem aprovação Lucas.

