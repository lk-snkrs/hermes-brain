# Handoff — Fase 1 documental pós-aprovação organograma

Data: 2026-05-26  
Owner: Hermes Geral / COO  
Escopo: execução local/read-only da Fase 1 aprovada por Lucas após auditoria organograma vs Amora.  
Produção/runtime: nenhuma alteração; sem migração de cron, sem restart, sem writes externos.

## Pedido limpo

Lucas aprovou “fazer” a fase local de alinhamento documental: atualizar organograma, matriz de agentes/profiles/bots/crons/status, docs de LK Shopify/LK Trends, status SPITI e checklist de handoff/receipt.

## Arquivos alterados/criados

- Atualizado: `empresa/contexto/organograma-agentes-hermes.md`
- Criado: `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`
- Criado: `areas/lk/sub-areas/shopify/MAPA.md`
- Criado/atualizado: `areas/lk/sub-areas/trends/MAPA.md`
- Criado: `areas/spiti/cron-status-2026-05-26.md`
- Criado: `areas/operacoes/rotinas/checklist-handoff-receipt-obrigatorio-2026-05-26.md`

## Decisões registradas

- Agentes podem fazer write quando Lucas aprovar de forma explícita e escopada.
- Aprovação ampla não vira cheque em branco permanente.
- Zipper permanece documental/read-only até gatilho real de runtime.
- LK Ops é dono lógico de atendimento/estoque/preço/disponibilidade; Growth não deve absorver Ops.
- Shopify/Tiny writes exigem snapshot, preview, readback, receipt e rollback.
- SPITI sem cron registry local é estado observado, não erro automático.

## Próximo passo recomendado

Preparar pacote específico para Fase 2 se Lucas quiser mexer em runtime:

1. backup e saneamento do registry Mordomo;
2. verificação launcher/env/max_iterations;
3. restart controlado profile a profile;
4. receipt por alteração.

## Rollback

Como esta fase foi documental/local, rollback é reverter os arquivos listados para a versão anterior via backup/git/diff do Brain, sem impacto em produção.
