# Handoff — Check de documentação do organograma Hermes vs Amora

Data: 2026-05-30
Origem: pedido de Lucas por Telegram/voz
Destino: Hermes Geral / Governança Brain

## Pedido limpo

Verificar se o organograma está bem documentado, usando a lógica do Bruno/Amora como referência, e apontar se falta alguma coisa.

## Resultado

O organograma está bem documentado e estruturalmente correto. A lógica central está alinhada com Bruno/Amora: organograma vivo, agentes com identidade/escopo, roteamento, permissões, handoffs e Brain como fonte de verdade.

Foram corrigidas/atualizadas lacunas documentais locais sobre:

- watchdog global dos gateways Telegram;
- cobertura dos agentes ativos;
- pacote documental mínimo completo para especialistas ativos;
- não auto-start de profiles prepared/read-only com token.

## Arquivos alterados

- `empresa/contexto/organograma-agentes-hermes.md`
- `empresa/contexto/matriz-agentes-profiles-bots-crons-status-2026-05-26.md`

## Relatório

- `reports/governance/organograma-documentacao-amora-check-2026-05-30.md`

## Lacunas pendentes

- rotinas antigas em Main/Mordomo com dono lógico LK Ops/Zipper continuam documentadas como pendência;
- crons próprios de LK Ops/LK Shopify/LK Trends/SPITI precisam ser escolha explícita ou pendência formal antes de qualquer migração;
- Zipper continua documental/read-only, sem bot por simetria;
- manter revisão periódica para evitar drift.

## Segurança

Nenhuma alteração em Docker, VPS, Traefik, gateways, cron runtime, Shopify, Tiny, SPITI Hub, CRM, WhatsApp ou sistema externo.
