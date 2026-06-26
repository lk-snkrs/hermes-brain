# Approval Packet — Primeiro worker read-only no Hermes Task OS

- Data: 2026-06-25
- Preparado por: Hermes Geral
- Card que preparou este packet: `hermes-task-os/t_6d7720a2`
- Status: **pendente de aprovação Lucas**
- Execução deste packet: nenhuma; documento local apenas
- generated_at_utc: `2026-06-25T15:25:05.347216+00:00`
- values_printed: `false`

## Decisão pedida

Aprovar ou não o primeiro teste real de worker Kanban read-only no board `hermes-task-os`.

## Recomendação Hermes

Aprovar **um único piloto read-only**, com escopo documental/local, usando o card:

```text
Board: hermes-task-os
Task: t_6d995d67 — Task OS — dashboard/Telegram UX de acompanhamento
Assignee candidato: hermes-ops-readonly
Risco: A3-prep / A1 se executado exatamente como read-only local
```

Por que este card:

- é sobre UX/observabilidade, não sobre Shopify/Tiny/prod;
- resultado esperado é relatório/decisão local;
- não exige credenciais externas;
- não deve tocar Docker/VPS/gateway/cron;
- testa o lifecycle Kanban worker com baixo risco operacional.

## Escopo permitido se Lucas aprovar

O worker poderá:

1. ler o próprio card Kanban;
2. ler documentos Brain relacionados a Task OS, Mesa COO e Kanban;
3. produzir um relatório local no Brain com recomendação de UX para acompanhamento;
4. comentar o card com o caminho do relatório;
5. bloquear para review ou completar se o artefato for suficiente.

## Fora de escopo / bloqueado

Mesmo com aprovação deste packet, continua bloqueado:

- Shopify/Tiny/GMC/Meta/Klaviyo/Google writes;
- Telegram outbound/probe/spam;
- alteração de cron/delivery;
- gateway restart/reload;
- Docker/VPS/Traefik;
- secrets/Doppler/env;
- dashboard público/API/porta nova;
- dispatch de múltiplos cards;
- assignee em qualquer outro card.

## Comandos pretendidos após aprovação

Pré-check read-only:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os show t_6d995d67 --json
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os diagnostics
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os notify-list
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os dispatch --dry-run --max 1 --json
```

Execução mínima aprovada, se o dry-run mostrar exatamente o card esperado:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os assign t_6d995d67 hermes-ops-readonly
```

Observação: como `kanban.dispatch_in_gateway=true`, **o assign pode ser suficiente para execução pelo dispatcher do gateway**. Por isso este packet pede aprovação explícita antes de qualquer assignee.

Verificação pós-execução:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os runs t_6d995d67
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os log t_6d995d67
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os show t_6d995d67 --json
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os diagnostics
```

## Rollback / abortar

Se o worker travar, executar algo fora do escopo, ou o card errado for selecionado:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os reclaim t_6d995d67
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os block t_6d995d67 "rollback: piloto worker interrompido; aguardando revisão Lucas"
```

Depois verificar:

```bash
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os stats
HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes kanban --board hermes-task-os diagnostics
```

## Critério de sucesso

O piloto passa se:

- apenas `t_6d995d67` tiver run novo;
- nenhum outro card for atribuído/executado;
- nenhum write externo ocorrer;
- worker produzir relatório local/Brain ou bloquear pedindo review claro;
- logs não expuserem secrets;
- Brain health continuar FAIL=0;
- Telegram não receber ruído automático.

## Critério de falha

Falha se:

- outro card rodar;
- houver tentativa de external write;
- houver Telegram/probe não solicitado;
- houver erro de spawn/path/profile;
- worker passar do escopo ou ficar preso;
- logs contiverem segredo/PII sensível.

## Opções para Lucas

### Opção A — Aprovar piloto read-only recomendado

Autoriza somente o assign/execução de `t_6d995d67` com `hermes-ops-readonly` e verificações acima.

### Opção B — Não executar worker ainda

Mantém Task OS em modo manual/local. Próximo passo seria finalizar o card `t_6d995d67` manualmente como documentação.

### Opção C — Escolher outro card/profile

Requer novo packet com novo alvo. Nenhuma execução por inferência.

## Estado atual antes de aprovação

- `hermes-task-os`: 2 ready, 3 done.
- Cards ready: `t_6d7720a2`, `t_6d995d67` antes do fechamento deste packet.
- Assigned ready: 0.
- Running: 0.
- Diagnostics: 0.
- Notify subscriptions: 0.

## Decisão recomendada

Recomendação: **Opção A**, mas somente quando Lucas responder explicitamente aprovando este packet.
