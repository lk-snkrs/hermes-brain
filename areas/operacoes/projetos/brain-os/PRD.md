# PRD — Hermes Brain OS v1

## 1. Problema

O Brain contém grande volume de evidência útil, mas a inteligência executiva fica espalhada em receipts, reports, PRDs, work files e logs/documentos históricos. Isso aumenta o risco de:

- responder com estado antigo;
- confundir fonte viva com documentação;
- perder decisões importantes em receipts antigos;
- repetir trabalho já feito;
- criar agentes/rotinas sem saber o dono real;
- acionar sistemas externos sem enxergar guardrails completos.

## 2. Objetivo

Criar o **Hermes Brain OS**, uma camada canônica de inteligência por projeto, onde cada frente relevante possui:

- estado atual;
- fonte da verdade;
- decisões válidas;
- guardrails;
- índice de evidências;
- timeline;
- próximos passos;
- manifest verificável;
- vínculo com MAPAs/skills/rotinas.

## 3. Não-escopo v1

- Não reorganizar movendo ou apagando históricos.
- Não ativar runtime, cron, gateway, Docker, VPS ou APIs externas.
- Não sincronizar para GitHub sem aprovação explícita.
- Não substituir sistemas vivos como Tiny, Shopify, GMC ou Chatwoot.
- Não copiar secrets, payloads brutos ou dados sensíveis para hubs.

## 4. Pesquisa incorporada

### Hermes oficial

- Memória persistente do Hermes é curta/curada e congelada no início da sessão; deve ser boot mínimo, não Brain completo.
- Skills são memória procedural sob demanda; Brain OS deve apontar para skills quando houver procedimento reutilizável.
- Profiles isolam identidade, memória, skills, cron e estado; Brain OS deve separar dono lógico de runtime.
- Cron roda em sessões frescas; rotinas futuras devem carregar contexto suficiente por skill/workdir/profile.
- Kanban é a camada durável para trabalho multiagente e handoffs, quando necessário.

### Boas práticas externas

- PARA/Second Brain: projetos, áreas, recursos e arquivos; foco em ação e organização just-in-time.
- Diátaxis: separar how-to, referência, explicação e tutoriais.
- ADRs: decisões importantes devem ser preservadas e marcadas como superseded quando mudam.
- Docs-as-code: markdown versionado, validado, com scans.
- Runbooks: agentes precisam de procedimentos operáveis, não só contexto solto.

## 5. Produto

Brain OS v1 entrega:

1. Padrão de hub canônico.
2. Scanner local/read-only de candidatos.
3. Índice central de candidatos e ondas.
4. Primeiros hubs de alto impacto.
5. Verificações de segurança e sanidade.

## 6. Critérios de sucesso

- O agente consegue responder “onde está o estado atual?” para projetos grandes.
- O agente distingue histórico de estado atual.
- O agente sabe qual fonte é viva e qual arquivo é evidência.
- Hubs têm manifest válido e índice de artefatos.
- Nenhum histórico é apagado.
- Nenhum secret é copiado.
- Scanner gera candidatos e scores reproduzíveis.
- Health/docs/secret gates passam.

## 7. Modelo de hub

Ver `PROJECT_HUB_STANDARD.md`.

## 8. Rollout

Ver `ROLL_OUT_PLAN.md`.
