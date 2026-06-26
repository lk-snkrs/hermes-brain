# Packet — Refinamento de guardrails para inspeção administrativa read-only

Status: proposta local; nenhuma alteração de runtime/código aplicada  
Owner: Hermes Geral / COO  
Risco: médio se implementado sem testes, baixo enquanto documental  
Writes externos: não

## Problema

Durante a auditoria Hermes vs Amora, a ferramenta de cron foi bloqueada mesmo para `list`. A auditoria precisava apenas inspecionar o registry em modo read-only; o bloqueio foi seguro, mas grosseiro demais. A alternativa usada foi terminal read-only com CLI e redaction.

## O que está correto no bloqueio atual

- Fail-closed para criação/edição/remoção/execução de crons.
- Proteção contra runtime mutation em modo approval/handoff.
- Evita que um agente use ferramenta de cron como bypass de approval.

## O que precisa melhorar

Separar verbos read-only de verbos mutáveis.

### Read-only admin permitido em auditoria local

- cron list/status;
- gateway/process status;
- read logs sanitizados;
- list profiles/config path sem secrets;
- health checks;
- file readback;
- git status/diff local.

### Mutável/bloqueado sem approval

- cron create/update/pause/resume/remove/run;
- gateway restart/stop/start;
- Docker/compose/network/volume/root/VPS;
- config/env writes;
- delivery target changes;
- secrets exposure;
- production/external writes.

## Preview de regra desejada

```text
Se action_mode=approval/handoff e tool=cronjob:
  permitir apenas action=list/status quando não houver deliver/send/run/mutation;
  bloquear create/update/pause/resume/remove/run;
  registrar que foi inspeção read-only.
```

## Testes necessários antes de qualquer patch de código

1. `cronjob(action=list)` permitido em auditoria local/read-only.
2. `cronjob(action=create)` bloqueado.
3. `cronjob(action=update)` bloqueado.
4. `cronjob(action=run)` bloqueado.
5. Nenhum `decision_json`, route id ou preflight metadata vaza para resposta Lucas-facing.
6. Logs de ferramenta não imprimem secrets.

## Rollback se implementado futuramente

- Reverter patch do dispatcher/guardrail.
- Rodar testes de preflight e scheduler.
- Confirmar gateway/scheduler ainda fail-closed para mutações.

## Decisão atual

Não implementar código agora. Manter como packet/documentação para próxima rodada de melhoria do runtime.
