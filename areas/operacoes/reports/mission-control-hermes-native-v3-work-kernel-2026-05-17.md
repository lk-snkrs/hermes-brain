# Mission Control Hermes-native v3 — Work Kernel local

Data: 2026-05-17
URL: https://mission.lucascimino.com/
Marker: `hermes-native-v3-work-kernel-2026-05-17`
Commit: `6e38117 feat: add Mission Control work kernel`

## Objetivo

Dar sequência à correção de Lucas de que Mission Control não pode ser apenas informativo. A v3 inicia um núcleo de trabalho interativo para Goals, Kanban, Decision Packets e Approval States, mantendo o modelo preview-first e bloqueando writes externos.

## O que foi feito

- Criado `src/components/mission/MissionWorkKernel.tsx` com estado local em `localStorage`.
- Adicionados modelos em `src/data/mission-control.ts`:
  - `operatingGoals` por empresa/domínio;
  - `kanbanItems` com estados `backlog`, `doing`, `blocked`, `done`;
  - `decisionPackets` derivados da Lucas Queue;
  - `approvalStates` com `draft`, `pending`, `approved`, `denied`, `executed`.
- Reescrita `/workflows` para abandonar workflows herdados e virar COO Kernel Hermes-native.
- Reescrita `/actions` para deixar de ser Quick Actions Hub genérico e virar Approval Center preview-first.
- Home atualizada com seção `Gestão local iniciada`, métricas v3 e roadmap ajustado.
- `/chat` agora respeita `?topic=` para abrir contexto de decisão específico.

## Estado honesto

### Feito

- Kernel local interativo para mover tarefas e marcar estados de aprovação.
- Packets copiáveis com fonte, risco, gate, payload e rollback.
- Goals/Kanban/Approval Center deixam de ser apenas “não iniciado” e passam a `parcial` na matriz Hermes.
- Produção atualizada e verificada no domínio principal.

### Parcial

- Persistência ainda é `localStorage`, não backend compartilhado.
- Chat ainda prepara prompt; não envia para Hermes API Server.
- Terminal continua protegido/legado; precisa hardening de allowlist e auditoria.
- Rotas internas `/workflows`, `/actions`, `/chat` seguem atrás do login em produção, esperado pelo auth atual.

### Falta

- API autenticada para persistir goals, kanban, packets e approval events.
- Runner seguro para transformar aprovação explícita em execução auditada.
- Integração Telegram/Hermes para approval packets.
- Snapshots vivos read-only de GA4/GSC/GMC/Shopify/Tiny/Supabase/Meta.

## Validação

- `npx impeccable detect --fast --json` nos arquivos alterados: `[]`.
- `npx eslint` nos arquivos alterados: passou.
- `npm run build`: passou.
- Local `/`: HTTP 200 e marker v3 encontrado.
- Produção `/`: HTTP 200, marker v3 encontrado.
- Browser produção:
  - título: `Mission Control Hermes-native`;
  - marker: `hermes-native-v3-work-kernel-2026-05-17`;
  - textos verificados: `Mesa COO interativa com kernel local`, `KERNEL DE TRABALHO LOCAL`, `Approval Center preview-first`, `Kernel local v3`;
  - overflow horizontal: falso;
  - console: sem erros JS.

## Guardrails preservados

- Nenhum write externo foi conectado.
- Nenhuma mensagem WhatsApp/e-mail/cliente/fornecedor foi enviada.
- Nenhum Shopify/GMC/Tiny/ads/Supabase produtivo foi alterado.
- Nenhum Docker/VPS/Traefik/volume/network foi modificado.
- O deploy Mission Control foi feito via Vercel com token carregado sem impressão.

## Próximo bloco recomendado

Bloco 4: persistência e contrato Hermes API.

1. Definir schema server-side para `goals`, `kanban_items`, `decision_packets`, `approval_events` e `evidence_receipts`.
2. Criar rotas API autenticadas para leitura/gravação local do Mission.
3. Ligar chat contextual a um endpoint Hermes seguro, inicialmente sem ferramentas de write.
4. Criar allowlist auditada para terminal read-only contextual.
5. Preparar integração Telegram para pedir aprovação com payload exato e registrar evidência.
