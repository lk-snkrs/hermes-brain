# Linear externo opcional; Hermes Task OS canônico

- Data: 2026-06-25
- values_printed: `false`

## Decisão

O Hermes não depende de Linear externo para operar. O sistema canônico interno de tarefas é o Hermes Kanban board `hermes-task-os`.

## Quando usar Linear externo

Somente se Lucas quiser integração com ferramenta externa para visibilidade fora do Hermes.

## Estado de credencial

Diagnóstico anterior: secret `LINEAR_API_KEY` existe no Doppler, mas smoke GraphQL retornou `401`; aliases `LINEAR_API_TOKEN` e `LINEAR_TOKEN` ausentes. Nenhum valor foi impresso.

## Regra operacional

Não tentar corrigir/reconectar Linear externo por padrão. Se Lucas pedir, preparar novo approval packet para token válido/read-only smoke.
