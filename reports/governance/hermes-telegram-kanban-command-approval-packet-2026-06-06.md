# Approval Packet — Ativar/validar `/kanban` no Telegram

Data: 2026-06-06
Dono: Hermes / infra / operating layer
Pedido: Lucas perguntou se dá para fazer PRD e comando `/kanban` no Telegram e implementar.

## Resumo executivo
O comando `/kanban` já está implementado no código do gateway e no venv ativo. A próxima etapa segura não é escrever código novo; é validar no Telegram real e, se necessário, fazer restart controlado do gateway para garantir que o processo ativo carregou o handler.

## Opção recomendada — A: validação read-only agora
Aprovar apenas teste Telegram read-only:

1. Lucas envia ou Hermes orienta envio de `/kanban stats` neste chat.
2. Se responder, feature está ativa.
3. Salvar receipt no Brain com evidência.

Escopo permitido:
- `/kanban stats`
- `/kanban boards`
- `/kanban list` com limite curto, se suportado.

Bloqueado:
- create/comment/complete/block/unblock/dispatch/assign/reassign.
- restart gateway.
- alterações de config/runtime/secrets.

Risco: A1/A2, read-only.
Rollback: nenhum.

## Opção B: validação + restart controlado se não responder
Aprovar:

1. Teste read-only `/kanban stats`.
2. Se o Telegram não reconhecer ou mandar para LLM, verificar processo/versionamento ativo.
3. Fazer restart controlado do gateway conforme runbook, sem mudar código/config.
4. Validar pós-restart com `/status` e `/kanban stats`.
5. Registrar receipt.

Risco: A3 por restart de gateway.
Rollback: novo restart/retorno à versão anterior conforme runbook.

## Opção C: hardening code-level antes de ativar
Aprovar criação de testes adicionais no repo para:

- `/kanban` cold-path Telegram.
- `/kanban` mid-run bypass.
- truncamento de resposta longa.
- auto-subscribe em create.

Risco: A2 local/code-only; A3 se houver deploy/restart.
Rollback: git revert dos patches.

## Recomendação
Escolher A primeiro. Se A falhar, pedir aprovação explícita para B.

## Evidências técnicas já verificadas
- Runtime instalado contém `gateway/run.py::_handle_kanban_command`.
- Runtime instalado contém dispatch `if canonical == "kanban"`.
- Runtime instalado contém registry `CommandDef("kanban", ..., cli_only=False)`.
- Candidate v0.16: `resolve_command('kanban')` OK e `/kanban` aparece no gateway help.
- Teste sintético local isolado: `/kanban stats --json` retornou JSON válido.
- Teste targeted: `tests/hermes_cli/test_commands.py` → `144 passed`.

## Decisão solicitada
Aprovar uma das opções:

- **Aprovar A** — testar `/kanban stats` read-only no Telegram agora.
- **Aprovar B** — permitir teste read-only e restart controlado se falhar.
- **Aprovar C** — criar testes/hardening code-level antes de validação real.
- **Bloquear** — não ativar/validar agora.
