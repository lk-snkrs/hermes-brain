# Handoff — Governança de Organograma, LK Ops e Zipper Runtime

Data/hora: 2026-05-26  
Agente/profile: Hermes Geral  
Empresa/área: Operações Hermes / LK / Zipper  
Responsável humano: Lucas Cimino

## Pedido original

Lucas aprovou seguir após a auditoria do organograma vs Amora, confirmou que o Mordomo completo está correto e sinalizou seguir com a preparação de LK Ops/Atendimento e Zipper runtime.

## O que foi feito

- Criado contrato operacional de LK Ops/Atendimento.
- Atualizado MAPA de LK Atendimento/Ops com fonte de verdade Tiny e limite com LK Growth.
- Criado documento de gatilhos, guardrails e plano de promoção para Zipper Runtime.
- Atualizado critério anterior de promoção Zipper para apontar para o documento novo.
- Nenhum cron, scheduler, gateway, Docker, VPS, profile, bot, Shopify, Tiny ou delivery foi alterado.

## Fontes usadas

- `areas/lk/MAPA.md`
- `areas/lk/sub-areas/atendimento/MAPA.md`
- `areas/zipper/contrato-operacional-readonly.md`
- `areas/zipper/operacoes/zipper-profile-promotion-criteria-2026-05-25.md`
- Relatórios de governança criados em 2026-05-26 sobre donos de crons e organograma.

## Output/artefato

- `areas/lk/sub-areas/atendimento/contrato-operacional-lk-ops-atendimento-2026-05-26.md`
- `areas/lk/sub-areas/atendimento/MAPA.md`
- `areas/zipper/operacoes/zipper-runtime-gatilhos-e-guardrails-2026-05-26.md`
- `areas/zipper/operacoes/zipper-profile-promotion-criteria-2026-05-25.md`

## Aprovação

Aprovado por Lucas para preparação documental. Não houve aprovação para runtime/profile/bot/cron/write externo.

## Envio/publicação

Nenhum envio externo.

## Writes externos

Nenhum.

## Riscos/bloqueios

- Registry do Mordomo tem bytes/trailing data inválidos; sanear com backup antes de qualquer edição.
- Zipper provavelmente precisará de runtime se o volume continuar, mas ainda requer medição e approval packet.
- LK Ops/Atendimento deve ser separado de LK Growth para evitar execução por conveniência.

## Próximos passos

1. Medir volume Zipper por 1–2 semanas antes de propor runtime.
2. Sanear registry do Mordomo com backup antes de qualquer migração.
3. Classificar rotinas LK Ops/Zipper que hoje rodam em Main/Mordomo.
4. Só depois preparar approval packet para migração de cron/profile, se necessário.

## Onde foi documentado no Brain

Este handoff fica em `empresa/contexto/handoffs/2026-05-26-governanca-lk-ops-zipper-runtime.md`.
