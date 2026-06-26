# Verificação — Task Router / Fase 2

Data: 2026-05-24
Status: concluído documentalmente
Escopo: atualizar regras do Hermes Geral para consultar a matriz antes de executar tarefas com especialista dono.

## Arquivos atualizados

- `START-HERE.md`
  - Adicionada regra de roteamento antes de executar.
  - Referências canônicas adicionadas para organograma de tarefas, matriz e task-router.
  - Regra anti-erro: conteúdo/blog/source page/copy SEO/GEO/CRO da LK pertence a `lk-growth`.

- `AGENTS.md`
  - Boot mínimo passou a exigir tipo de tarefa, risco A0-A4 e consulta à matriz.
  - Criada seção `Roteamento obrigatório`.
  - Rotas críticas documentadas: `lk-growth-content`, `mordomo-personal-intake`, `spiti-os`, `zipper-os-readonly-comm-crm`.

- `agentes/hermes-geral/AGENTS.md`
  - Hermes Geral definido como orquestrador central, não executor universal.
  - Criada seção `Task Router` com ações possíveis: executar aqui, delegar especialista, preparar packet, bloquear por aprovação, perguntar clarificação.
  - Reforço de que conteúdo editorial LK deve ser roteado para `/opt/data/profiles/lk-growth`.

- `empresa/contexto/organograma-agentes-hermes.md`
  - Atualizado para 2026-05-24.
  - Adicionado complemento de orquestrador/tarefa/executor/approval/handoff.
  - Links para organograma de tarefas, matriz e algoritmo operacional.

- Skill `multiempresa-routing-lucas`
  - Atualizada para consultar os documentos canônicos do Task Router no Hermes Brain.

## Verificação executada

Checklist por string nos arquivos principais: PASS.

Cobertura mínima verificada:

- `START-HERE.md`: contém regra de roteamento antes de executar e referência à matriz.
- `AGENTS.md`: contém seção `Roteamento obrigatório` e rotas críticas.
- `agentes/hermes-geral/AGENTS.md`: contém `Task Router`, `delegar_especialista` e regra `lk-growth`.
- `organograma-agentes-hermes.md`: contém atualização 2026-05-24 e referências ao Task Router.

## Guardrails preservados

- Nenhum runtime alterado.
- Nenhum Docker/gateway/Traefik/VPS alterado.
- Nenhum cron criado ou editado.
- Nenhuma publicação em Shopify/GMC/Klaviyo/Meta/Supabase.
- Nenhum contato externo executado.

## Próxima fase recomendada

Fase 3 — Inventário read-only de runtime:

- listar profiles existentes;
- listar crons por profile;
- listar bots/canais conhecidos;
- comparar runtime real com organograma documental;
- gerar `reports/governance/runtime-vs-organograma-2026-05-24.md`.

A Fase 3 deve ser somente leitura. Qualquer correção em cron, gateway, Docker, profile ou canal fica bloqueada até aprovação explícita.