# Índice de Rotinas — Hermes Brain

Este índice aponta para rotinas business-readable documentadas no Brain. Ele não prova que todos os crons estão ativos; sempre verificar cron real na VPS/ambiente antes de afirmar execução.

## Rotinas cross-área / operações

| Rotina | Caminho | Função |
|--------|---------|--------|
| Brain Sync | `areas/operacoes/rotinas/brain-sync.md` | Sincronização do Brain e versionamento |
| Heartbeat | `areas/operacoes/rotinas/heartbeat.md` | Checagens periódicas operacionais |

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
