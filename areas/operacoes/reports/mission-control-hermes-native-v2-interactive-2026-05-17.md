# Mission Control Hermes-native v2 — ação antes de informação

Data: 2026-05-17  
Produção: https://mission.lucascimino.com/  
Marker: `hermes-native-v2-interactive-2026-05-17`  
Commit: `b4e3e50 feat: make mission control action-first`

## Correção de produto aplicada

Lucas apontou cinco lacunas corretas:

1. A v1 não tinha usado Impeccable como workflow suficiente.
2. A v1 não cobria todas as possibilidades do Hermes Workspace/Hermes Agent.
3. Informação sem botão não opera nada.
4. Mission Control precisa mapear features de gestão: goal, kanban, tasks, routines, crons, etc.
5. Chat e terminal são superfícies centrais.

A v2 foi publicada para corrigir a topologia inicial: a home passou de dashboard informativo para Decision Inbox com action rails.

## O que foi adicionado

- `PRODUCT.md`: contexto Impeccable do produto Mission Control.
- `DESIGN.md`: direção visual/UX, produto minimal, preview-first, action-first.
- `src/components/mission/MissionActionRail.tsx`: botões de pacote/chat/terminal por decisão.
- `src/app/chat/page.tsx`: primeira superfície de chat contextual, ainda preview/copy-prompt, sem envio real à API Hermes.
- `src/data/mission-control.ts`: matriz ampliada de capabilities Hermes, queue e roadmap.
- Home `/`: redesenhada como Mesa COO interativa.
- Terminal `/terminal`: quick commands removendo resquícios OpenClaw e apontando para Mission/Hermes Brain.

## Features Hermes mapeadas na v2

- Chat contextual: não iniciado, P0, agora com página inicial `/chat`.
- Terminal read-only: parcial, P0, já existe e foi reposicionado.
- Goals / Missions: não iniciado, P0.
- Kanban / Tasks: não iniciado, P0.
- Todo / Lucas Queue: parcial, P0.
- Approval Center: conceitual, P0.
- Cron / Routines: parcial, P1.
- Memory / Brain: parcial, P1.
- Skills: parcial, P1.
- Sessions: parcial, P1.
- Agents / Delegation: parcial, P1.
- Files / Artifacts: parcial, P1.
- Git / PR workflow: parcial, P1.
- Search, Reports, Analytics, MCP, Browser/Web, Webhooks, Notifications, Costs, Logs, Calendar, Voice/Media: mapeados por status e próximo botão.

## Interatividade entregue agora

Cada item da Decision Inbox tem:

- pacote copiável para Hermes/Telegram;
- link para chat contextual;
- link para terminal ou rota operacional;
- fonte, frescor e confiança;
- ação segura agora;
- ação bloqueada;
- gate A0-A4.

Exemplo LK:

- decisão: revisar descrições de coleção com evidência SEO/CRO;
- botão: `Preparar pacote`;
- botão: `Abrir chat LK`;
- botão: `Diagnóstico read-only`;
- bloqueio: publicar Shopify/campanha sem aprovação.

## Validações

- `npx impeccable detect --fast --json ...`: `[]`.
- ESLint nos arquivos alterados: 0 erros.
- `npm run build`: passou.
- Secret scan simples nos arquivos alterados: ok.
- Local `/`: HTTP 200 e marker presente.
- Produção `/`: HTTP 200 e marker presente.
- Produção `/chat` e `/terminal`: redirecionam para login, esperado por auth.
- Browser produção: title `Mission Control Hermes-native`, marker v2, 12 primeiros botões detectados.
- Browser console produção: sem JS errors.
- Browser vision produção: confirma Decision Inbox com botões, chat/terminal/goals/kanban, sem overflow horizontal óbvio.

## Limites ainda honestos

- Chat real com Hermes API ainda não está conectado. `/chat` prepara prompt e pacote.
- Goals/Kanban persistente ainda não foi construído. A v2 explicita que é P0 não iniciado.
- Approval Center real ainda não executa payloads. A v2 só prepara e roteia.
- Terminal ainda é uma página legada parcial, mas seus comandos rápidos foram alinhados ao Mission/Hermes.

## Próximo bloco recomendado

Bloco 3: construir o núcleo vivo de gestão:

1. Modelo `goals` por empresa.
2. Modelo `kanban_items` com estados: não iniciado, em andamento, bloqueado, feito.
3. Modelo `decision_packets` persistente.
4. Chat real conectado ao Hermes API Server ou fluxo seguro Telegram.
5. Approval Center com estados pendente/aprovado/negado/executado e evidência.
