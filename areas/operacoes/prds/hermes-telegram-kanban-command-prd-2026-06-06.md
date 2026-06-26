# PRD — Comando `/kanban` no Telegram Hermes

Data: 2026-06-06
Dono operacional: Hermes / infra / operating layer
Risco: A2 se apenas leitura/teste; A3 se exigir restart/deploy do gateway ativo.

## Problema
Lucas quer controlar o Kanban diretamente pelo Telegram, sem depender do Dashboard/CLI, mantendo Telegram como canal executivo e o Brain como trilha durável.

## Resultado desejado
Permitir que mensagens como `/kanban stats`, `/kanban list`, `/kanban show <task>`, `/kanban comment <task> ...`, `/kanban block/unblock/complete ...` funcionem no Telegram com resposta curta e acionável.

## Descoberta técnica
O runtime Hermes v0.16 candidate e o venv ativo já contêm implementação de `/kanban` no gateway:

- Registry: `hermes_cli/commands.py` registra `CommandDef("kanban", ...)` com `cli_only=False`.
- Dispatcher cold-path: `gateway/run.py` chama `_handle_kanban_command(event)` quando `canonical == "kanban"`.
- Dispatcher mid-run: `/kanban` bypassa o running-agent guard e chama `_handle_kanban_command(event)`.
- Handler: `_handle_kanban_command` delega para `hermes_cli.kanban.run_slash`, executa em thread, trunca saída longa e auto-inscreve notificações em `/kanban create`.

Conclusão: não há necessidade inicial de nova feature code-level; o trabalho é validação/ativação operacional no gateway Telegram ativo.

## Escopo MVP
1. Confirmar que `/kanban` aparece no help/menu do gateway.
2. Confirmar localmente que `_handle_kanban_command` processa `/kanban stats --json` em ambiente isolado.
3. Se Lucas aprovar, validar no Telegram real com comando read-only:
   - `/kanban stats`
   - opcional: `/kanban list --limit 5`
4. Se não responder no Telegram real, executar activation path aprovado:
   - verificar processo/versionamento do gateway;
   - restart controlado do gateway, sem alterar código/config sensível;
   - validação pós-restart.

## Fora de escopo sem nova aprovação
- Criar/remover cards reais.
- Dispatch de workers.
- Atribuir assignee.
- Alterar cron, provider, model, Docker, Traefik, secrets, Dashboard ou deploy externo.
- Mudar permissões/admin de slash commands.

## Comandos esperados
- `/kanban stats` — resumo do board atual.
- `/kanban boards` — boards disponíveis.
- `/kanban list` ou `/kanban ls` — lista cards.
- `/kanban show <task_id>` — detalhe.
- `/kanban comment <task_id> <texto>` — comentário.
- `/kanban complete <task_id> --summary <texto>` — conclusão.

## Critérios de aceite
- `/kanban` é reconhecido no registry gateway.
- Handler local responde com JSON válido em teste isolado.
- Telegram real responde a `/kanban stats` sem acionar LLM e sem iniciar worker.
- Se restart for necessário, `/status` e `/kanban stats` funcionam após o restart.
- Receipt salvo no Brain com evidências e sem secrets.

## Riscos
- Resposta longa demais no Telegram: mitigado por truncamento no handler.
- Mutação acidental: primeiro teste deve ser read-only.
- Gateway ativo ainda não carregou a versão com handler: mitigado por restart controlado com aprovação.
- Comando em chat/tópico errado: validar source/destino antes de teste mutável.

## Rollback
- Se apenas teste read-only: nenhum rollback necessário.
- Se houver restart: rollback operacional é reiniciar novamente para versão/serviço anterior conforme runbook Hermes gateway.
- Se `/kanban create` auto-subscrever notificação indevida: usar `/kanban notify-unsubscribe <task_id>`.

## Evidência já coletada
- `resolve_command('kanban')` retorna `CommandDef(... cli_only=False ...)`.
- `gateway_help_lines()` inclui `/kanban`.
- Teste sintético local do handler `/kanban stats --json` em `HERMES_KANBAN_DB` temporário retornou JSON válido com `by_status.ready = 1`.
- Suite targeted `tests/hermes_cli/test_commands.py`: `144 passed`.
