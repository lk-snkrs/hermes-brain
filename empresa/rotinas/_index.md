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
| Sync Log | `areas/lk/rotinas/sync-log.md` | Auditoria de início/fim de sync |
| Consequence Tracker | `areas/lk/rotinas/consequence-tracker.md` | Registro de efeitos de ações |
| Cross-sell Monitor | `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md` | Oportunidades pós-pedido |
| RFM Semanal | `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md` | Segmentação RFM e relatório |
| Outcomes Tracker | `areas/lk/sub-areas/crm/rotinas/outcomes-tracker.md` | Status de sugestões Hermes |
| Creative Pipeline | `areas/lk/sub-areas/trafego-pago/rotinas/creative-pipeline.md` | Hipótese → criativo → teste → learning |
| Consolidar FAQ | `areas/lk/sub-areas/atendimento/rotinas/consolidar-faq.md` | Loop FAQ/suporte/bot |

## Zipper Galeria

| Rotina | Caminho | Função |
|--------|---------|--------|
| Consulta de Vendas de Obras | `areas/zipper/rotinas/consulta-vendas-obras.md` | Análise comercial com `vendas_tango` |
| Abordagem de Colecionadores | `areas/zipper/rotinas/abordagem-colecionadores.md` | Rascunhos e aprovação comercial |
| Planejamento de Feiras | `areas/zipper/rotinas/planejamento-feiras.md` | Checklists, responsáveis e execução |

## SPITI Auction

| Rotina | Caminho | Função |
|--------|---------|--------|
| Verificação de Lances | `areas/spiti/rotinas/verificacao-lances.md` | Checagem segura de lances/lotes |
| Alerta de Lances | `areas/spiti/rotinas/alerta-lances.md` | Alertas, deduplicação e falhas conhecidas |
| Relatório de Leilão | `areas/spiti/rotinas/relatorio-leilao.md` | Relatório interno com fonte e ressalvas |

## Regras

- Secrets via Doppler `lc-keys/prd`.
- Rotina documentada ≠ cron confirmado.
- Mensagens externas, campanhas, posts e contato com cliente/colecionador exigem aprovação Lucas.
