# Receipt — Hermes Task OS convenção Lucas Cimino 2026-06-25

- Data/hora: 2026-06-25T14:31:54.158843+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: operacoes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas disse seguir após reconciliação; executar próximo card Task OS para definir convenção de campos e statuses.
- Classificação: local-write
- Fontes usadas:
- Card Kanban t_5e84b76c; relatório de reconciliação boards; rotina inicial hermes-task-os-kanban-interno; política Lucas de approval gates e Telegram silent-OK.
- O que foi feito:
- Criada convenção Lucas/Cimino para Hermes Task OS: campos obrigatórios, risco A0-A4, tipos de card, status Kanban, política de assignee, integração Mesa COO e fechamento de cards.
- Output/artefato:
- Documento em areas/operacoes/rotinas/hermes-task-os-convencao-lucas-cimino-20260625.md; índice de rotinas atualizado; sem assignee/dispatch/worker.
- Aprovação: Aprovação no Telegram: seguir.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Se assignee for usado em card ready com dispatch_in_gateway=true, pode disparar execução; convenção bloqueia isso sem approval packet.
- Rollback/mitigação: Remover documento e linha do índice se a convenção for substituída; nenhum runtime ou board executor foi alterado.
- Próximos passos: Comentar e completar card t_5e84b76c; próximo card sugerido t_1ed3d96d para Mesa COO + Kanban sem spam.
- Onde foi documentado no Brain: areas/operacoes/rotinas/hermes-task-os-convencao-lucas-cimino-20260625.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
