# Hermes Task OS — rotina operacional Lucas/Cimino

- Data: 2026-06-25
- Board canônico: `hermes-task-os`
- generated_at_utc: `2026-06-25T16:01:03.283468+00:00`
- values_printed: `false`

## Objetivo

Consolidar o Hermes Kanban nativo como Linear interno operacional sem virar ruído no Telegram nem bypass de aprovação.

## Rotina diária/on-demand

1. Criar ou manter cards no `hermes-task-os` quando a frente precisa sobreviver à sessão, ter owner, approval, evidência ou worker.
2. Cards novos de backlog seguro devem começar `ready` sem assignee ou `blocked` sem assignee. **Não usar `--triage` para backlog em produção**, porque o specifier/decomposer pode transformar o card em `todo`, atribuir `default` e gerar child tasks.
3. `assignee` só entra quando houver approval packet claro ou quando for A0/A1 local/read-only seguro.
4. Mesa COO só puxa cards que exigem decisão real, bloqueio, A3/A4, falha atual ou prazo relevante.
5. `done` exige evidência: summary, artifact/receipt/report quando aplicável.
6. Boards antigos não são fonte executiva; viram origem histórica/migração/revalidação.

## Status policy

- `triage`: backlog ainda não especificado; nunca executar.
- `ready`: pronto para execução, mas se tiver assignee pode disparar worker; usar com cuidado.
- `blocked`: precisa input humano ou correção antes de seguir.
- `running`: worker em andamento; monitorar se travar.
- `done`: concluído e evidenciado.
- `archived`: histórico consolidado, não executar.

## Regra de Telegram

Telegram não recebe backlog bruto. O canal humano é:

- Mesa COO para decisões/alertas acionáveis;
- consulta sob demanda local/Telegram futura para resumo curto;
- nunca feed automático de todos os cards.

## Comandos locais seguros

Script local/read-only:

```bash
HERMES_HOME=/opt/data /opt/data/scripts/hermes_task_os_summary.py agora
HERMES_HOME=/opt/data /opt/data/scripts/hermes_task_os_summary.py decisoes
HERMES_HOME=/opt/data /opt/data/scripts/hermes_task_os_summary.py bloqueios
```

Esses comandos não fazem dispatch, não enviam Telegram e não escrevem externo.

## Linear externo

Linear externo fica opcional/parado. Só reabrir se Lucas quiser integração externa; token atual já foi diagnosticado como inválido/revogado/sem acesso.
