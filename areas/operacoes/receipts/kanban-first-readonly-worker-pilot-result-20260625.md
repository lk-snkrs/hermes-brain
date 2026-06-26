# Receipt — Kanban first read-only worker pilot result 2026-06-25

- Data/hora: 2026-06-25T15:34:25.840738+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: operacoes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas aprovou Opção A do approval packet para executar primeiro worker read-only Kanban.
- Classificação: local-write
- Fontes usadas:
- Kanban runs/log/show/diagnostics do card hermes-task-os/t_6d995d67; approval packet kanban-first-readonly-worker-20260625.md.
- O que foi feito:
- Executado precheck dry-run; atribuído t_6d995d67 para hermes-ops-readonly; gateway dispatcher tentou 2 runs; card bloqueou por repeated_failures; relatório local criado.
- Output/artefato:
- Piloto falhou de forma controlada: profile hermes-ops-readonly recebeu HTTP 401 token_expired no provider antes de tool calls; card t_6d995d67 ficou blocked; nenhum write externo, Telegram, cron ou gateway mutation.
- Aprovação: Aprovação explícita no Telegram: aprovar A.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Worker readiness bloqueada por autenticação do profile hermes-ops-readonly; corrigir auth/profile é mudança separada e não foi executada.
- Rollback/mitigação: Card já está blocked; para retry, requer novo approval packet para auth/profile ou reassign/reclaim. Nenhuma mutação externa precisa rollback.
- Próximos passos: Decidir entre corrigir auth do hermes-ops-readonly, reatribuir a outro profile funcional com novo packet, ou manter Task OS manual.
- Onde foi documentado no Brain: reports/governance/kanban-first-readonly-worker-pilot-result-2026-06-25.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
