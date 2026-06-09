# Handoff para execução — Agente LC Hermes

Data/hora: 2026-06-09T01:11:30+00:00
Origem: Mordomo (`mordomo`)
Destino: **Agente LC Hermes Central / Hermes Geral**
Solicitante: Lucas Cimino
Prioridade: Governança sistêmica / próxima ação recomendada
Risco: A1 — documentação local/read-only, sem runtime, sem deploy, sem secrets, sem dados vivos

## Instrução de Lucas

> Fazer Handoff para o LCHermes executar.

## Execução solicitada ao Agente LC Hermes

Criar e consolidar a rotina canônica de governança:

`areas/operacoes/rotinas/brain-fonte-viva-e-dados-grandes.md`

A rotina deve transformar em regra operacional do LC Hermes a fronteira:

> Brain guarda contexto, decisões, resumos, índices, governança e receipts. Bases grandes e dados vivos ficam em fonte viva consultável — banco/API/runtime — e o Brain aponta para elas, não replica tudo.

## Contexto/handoff base

Usar como base:

- `areas/operacoes/handoffs/handoff-lc-hermes-brain-fonte-viva-governance-20260609T000522Z.md`
- `areas/operacoes/handoffs/request-lc-hermes-execute-brain-fonte-viva-governance-20260609T000522Z.md`
- `areas/operacoes/MAPA.md`
- `AGENTS.md` do Hermes Brain

## Entregáveis esperados

1. Criar `areas/operacoes/rotinas/brain-fonte-viva-e-dados-grandes.md`.
2. Incluir matriz por tipo de dado:
   - guardar completo no Brain;
   - guardar resumo/índice no Brain;
   - consultar fonte viva;
   - proibido persistir bruto.
3. Incluir checklist para:
   - novos PRDs;
   - ingestões de material externo;
   - subagentes;
   - Mission Control;
   - skills;
   - rotinas/cron/watchers.
4. Incluir política de freshness/source confidence.
5. Incluir exemplos por domínio:
   - LK: Shopify/Tiny/GA4/Meta/Klaviyo;
   - Zipper: Supabase, WhatsApp/e-mail, PDFs/artistas/obras;
   - SPITI: lotes, lances, leilões, Hub;
   - Mordomo: WhatsApp pessoal, CRM, follow-ups, Decision Packets;
   - Hermes/infra: runtime, crons, logs, deploys.
6. Atualizar `areas/operacoes/MAPA.md` com a nova rotina.
7. Criar receipt curto em `areas/operacoes/receipts/`.
8. Só depois sugerir promoção para skills relevantes; não misturar patch de skills nesta execução.

## Guardrails

- Não copiar dumps de dados vivos para o Brain.
- Não mover/apagar dados existentes.
- Não consultar ou expor secrets.
- Não alterar runtime, crons, Docker, deploy, banco, APIs produtivas ou integrações externas.
- Não transformar a regra em burocracia para documentos pequenos/estáticos; o alvo são bases grandes, vivas, sensíveis ou rapidamente obsoletas.

## Critério de pronto

- Rotina existe e está indexada no MAPA.
- Handoff base fica referenciado ou resolvido.
- Pendência em `memories/pending.md` pode ser marcada como concluída.
- Receipt documenta o que foi feito e o que não foi feito.

## Observação de roteamento

Este é um handoff **para o agente LC Hermes executar**. O Brain é o mecanismo de continuidade e passagem de contexto; não é o destino final conceitual. O dono da execução é o Agente LC Hermes Central.
