# Kanban first read-only worker pilot — resultado

- Data: 2026-06-25
- Aprovação Lucas: `aprovar A`
- Board: `hermes-task-os`
- Card executado: `t_6d995d67` — Task OS — dashboard/Telegram UX de acompanhamento
- Assignee aprovado: `hermes-ops-readonly`
- generated_at_utc: `2026-06-25T15:34:10.792954+00:00`
- values_printed: `false`

## Resultado executivo

O piloto **não completou o trabalho**. O dispatcher tentou rodar o worker `hermes-ops-readonly` duas vezes, mas ambas as tentativas falharam antes de qualquer tool call do worker.

Causa verificada: autenticação Codex/OAuth do profile `hermes-ops-readonly` expirou/rejeitou com HTTP 401.

O Kanban auto-bloqueou o card após 2 falhas consecutivas.

## Estado final do card

- Task: `t_6d995d67`
- Status: `blocked`
- Assignee: `hermes-ops-readonly`
- Runs: 2
- Outcome: `crashed` / protocol violation porque o agent process saiu sem `kanban_complete` ou `kanban_block`
- Diagnóstico ativo: `repeated_failures`

## Evidência local

- Runs: `/tmp/kanban_t_6d995d67_runs.txt`
- Log: `/tmp/kanban_t_6d995d67_log.txt`
- Monitor: `/tmp/kanban_t_6d995d67_monitor.json`

Trecho sanitizado da causa:

```text
HTTP 401: Provided authentication token is expired.
Codex OAuth token was rejected (HTTP 401).
```

## Guardrails preservados

- Nenhum write externo executado pelo worker.
- Nenhuma mensagem Telegram/probe enviada.
- Nenhum Docker/VPS/gateway/cron alterado.
- Nenhum outro card foi atribuído/executado.
- Falha ocorreu antes de tool calls do worker.

## Próximas opções

### Opção A — Corrigir autenticação do profile e tentar novamente

Escopo: reautenticar/ajustar `hermes-ops-readonly` para um provider/model funcional e fazer novo dry-run antes de reclaim/unblock.

Risco: A3/A4 dependendo se envolver auth/config/profile/gateway. Exige approval separado.

### Opção B — Reatribuir para outro profile já funcional

Escopo: escolher outro profile read-only comprovadamente funcional, preparar novo approval packet e só então reassign/reclaim.

Risco: A3-prep; exige approval separado.

### Opção C — Fechar o piloto como falha controlada e seguir manual

Escopo: manter o Task OS manual/local até resolver perfis workers.

Risco: A1.

## Recomendação Hermes

Recomendação: **Opção A**, mas como novo packet específico de auth/profile, não como continuidade automática. O piloto cumpriu seu papel: revelou que o worker `hermes-ops-readonly` não está pronto por auth, sem causar efeito externo.
