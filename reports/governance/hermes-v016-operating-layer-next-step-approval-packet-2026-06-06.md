# Approval Packet — Próximo passo do board Hermes v0.16 Operating Layer

Data: 2026-06-06T16:59:02Z
Owner: Hermes Geral / Operações Hermes
Board: `hermes-operating-layer-v016`
Status: decisão solicitada; nenhuma execução automática, worker, cron, runtime/config/infra change realizada

## Contexto

Lucas pediu para preparar um approval packet após a conclusão manual/local do card:

- `t_cfef0a8d` — `[R1] Pilotar receipt/handoff padrão entre agentes` — status `done`.

O board ainda contém quatro cards `ready`, todos `unassigned`:

- `t_171bd02c` — `[R2] Preparar smoke test de fast lane/model routing`
- `t_b1d4b9e4` — `[R2] Definir primeiro piloto Kanban controlado`
- `t_5a0bca56` — `[R3] Preparar threat model OIDC/Dashboard`
- `t_e5273358` — `[R1] Auditoria de noise/receipts para Telegram`

## Decisão solicitada

Escolher qual próximo passo avançar e qual nível de autorização vale.

Este packet **não** autoriza por si só:

- atribuir worker;
- rodar `dispatch`;
- criar cron;
- enviar Telegram automático;
- mudar modelo/provider;
- reiniciar gateway;
- alterar Docker/Traefik/Dashboard/OIDC;
- mexer em secrets;
- fazer write externo.

## Opções

### Opção A — Continuar R1 local/documental: Telegram noise/receipts

Card sugerido:

- `t_e5273358` — `[R1] Auditoria de noise/receipts para Telegram`

Escopo aprovado se Lucas escolher A:

- execução manual/local por Hermes Geral;
- ler crons/rotinas/receipts somente de forma read-only quando necessário;
- criar matriz de ruído no Brain;
- não alterar cron delivery;
- não enviar mensagens automáticas;
- completar o card manualmente com receipt.

Risco: A1/A2.

Prós:

- maior ganho operacional imediato;
- reduz chance de Telegram virar log técnico;
- não exige runtime change.

Contras:

- ainda não melhora performance/model routing;
- pode gerar recomendações futuras que precisarão de novo approval.

Rollback:

- se o relatório ficar ruim, arquivar/substituir o artefato Brain;
- nenhum runtime para reverter.

Minha recomendação: **aprovar esta opção primeiro**.

---

### Opção B — Preparar smoke test de fast lane/model routing

Card sugerido:

- `t_171bd02c` — `[R2] Preparar smoke test de fast lane/model routing`

Escopo aprovado se Lucas escolher B:

- criar suite documental/local de smoke tests simples-vs-deep por perfil;
- mapear prompts de teste e critérios;
- não alterar `config.yaml`;
- não trocar modelo/provider;
- não reiniciar gateway;
- não ativar router.

Risco: A2 enquanto for só preparação. Sobe para A3 se houver mudança real de runtime/config/modelo.

Prós:

- prepara ganho de performance;
- reduz risco antes de ativar fast lane;
- permite comparar qualidade antes/depois.

Contras:

- não muda latência ainda;
- ativação futura exigirá novo packet específico.

Rollback:

- remover/arquivar artefatos de teste;
- nenhum runtime para reverter.

---

### Opção C — Definir piloto Kanban controlado com possível worker futuro

Card sugerido:

- `t_b1d4b9e4` — `[R2] Definir primeiro piloto Kanban controlado`

Escopo aprovado se Lucas escolher C:

- escolher um piloto A0/A1 local/read-only;
- definir owner/profile candidato;
- definir critérios de sucesso, kill criteria e verificação;
- **não** atribuir worker ainda;
- **não** rodar dispatch ainda;
- preparar packet separado caso o próximo passo seja worker real.

Risco: A2 nesta fase; A3 quando envolver assignee/worker/dispatch.

Prós:

- amadurece uso real do Kanban;
- prepara multiagente com controle;
- mantém execução humana/manual nesta fase.

Contras:

- se avançar rápido demais, pode virar swarm barulhento;
- exige disciplina de receipt por card.

Rollback:

- arquivar card/piloto;
- manter board sem dispatch.

---

### Opção D — Threat model OIDC/Dashboard

Card sugerido:

- `t_5a0bca56` — `[R3] Preparar threat model OIDC/Dashboard`

Escopo aprovado se Lucas escolher D:

- análise documental de ameaça/rollback;
- comparar basic auth, OIDC/SSO e túnel/VPN;
- não alterar Traefik, Docker, DNS, secrets, Dashboard ou auth.

Risco: A2/A3 documental; A4 se virar mudança real de auth/infra.

Prós:

- prepara segurança de longo prazo;
- reduz risco de lockout se um dia migrar auth.

Contras:

- menor ganho imediato;
- basic auth atual já funciona.

Rollback:

- nenhum runtime para reverter nesta fase;
- se um dia houver execução real, rollback deve restaurar basic auth previamente validado.

---

### Opção E — Bloquear por enquanto

Escopo:

- não avançar nenhum card;
- manter board como backlog local;
- nenhuma alteração.

## Recomendação do Hermes Geral

Recomendo a sequência:

1. **A — R1 Telegram noise/receipts**: maior ganho e menor risco.
2. **B — Fast lane smoke tests**: prepara performance sem tocar runtime.
3. **C — Kanban piloto controlado**: só depois que mais um R1 validar o processo.
4. **D — OIDC/Dashboard threat model**: importante, mas não urgente enquanto basic auth está funcional.

## Aprovação solicitada

Escolher uma das opções:

- **Aprovar A** — fazer `t_e5273358` manual/local/read-only.
- **Aprovar B** — fazer `t_171bd02c` manual/local, preparando smoke tests sem ativar runtime.
- **Aprovar C** — fazer `t_b1d4b9e4` manual/local, escolhendo piloto sem worker.
- **Aprovar D** — fazer `t_5a0bca56` documental, threat model sem mudar infra.
- **Bloquear** — manter board parado.
- **Ajustar** — Lucas define outro escopo.

## Critérios gerais de verificação para qualquer opção aprovada

Antes de concluir:

- card Kanban comentado/completado manualmente;
- nenhum card `running` inesperado;
- `by_assignee` continua vazio se não houver approval explícito para worker;
- `notify-list=[]`;
- `diagnostics=[]`;
- artefato Brain criado;
- receipt criado;
- secret scan `possible_secrets=0`;
- Brain Health `All checks passed`.
