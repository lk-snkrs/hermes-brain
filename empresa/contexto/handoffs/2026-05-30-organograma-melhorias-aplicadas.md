# Handoff — Melhorias no organograma vivo Hermes/Amora

Data: 2026-05-30
Origem: Lucas / Telegram
Owner: Hermes Geral / Governança Brain

## Pedido limpo

Melhorar o que ainda faltava melhorar no organograma documentado após a auditoria Hermes vs Bruno/Amora.

## Ação executada

Foram aplicadas melhorias locais/documentais no Brain para fechar as lacunas de maturidade operacional:

- matriz de crons por dono lógico;
- critérios de promoção para profiles auxiliares e Zipper;
- rotina de revisão do organograma vivo;
- atualização da matriz agente/profile/bot/cron/status;
- atualização do organograma canônico.

## Arquivos criados

- `empresa/contexto/matriz-crons-dono-logico-status.md`
- `empresa/contexto/criterios-promocao-agentes-auxiliares.md`
- `areas/operacoes/rotinas/revisao-organograma-vivo-amora-bruno.md`
- `reports/governance/organograma-melhorias-aplicadas-2026-05-30.md`

## Arquivos atualizados

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`

## Não executado

Nenhuma migração de cron, criação de cron, restart, alteração de gateway, Docker/VPS/Traefik, Shopify/Tiny/CRM/WhatsApp ou write externo.

## Próximo passo se Lucas quiser avançar runtime

Preparar pacote de aprovação separado para inventário/migração de crons históricos por lote, com backup e rollback.
