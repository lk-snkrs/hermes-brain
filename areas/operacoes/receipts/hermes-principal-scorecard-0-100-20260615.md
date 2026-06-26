# Receipt — Hermes Principal Scorecard 0-100 no digest 03h

- Data/hora: 2026-06-15T01:18:45.742524+00:00
- Agente/profile/cron: Hermes Geral / Nightly Ops Audit / Digest 03h
- Empresa/área: Operações / Hermes Runtime Governance
- Responsável humano: Hermes Agent
- Pedido original: Lucas pediu criar um sistema de score de 0 a 100 e dar uma nota no cron digest de 03h para tudo que for principal no Hermes.
- Classificação: local-write
- Fontes usadas:
- /opt/data/scripts/hermes_nightly_ops_audit.py; /opt/data/cron/jobs.json; reports/nightly-ops-audit/latest.json; cron 98478b820720
- O que foi feito:
- Adicionado scorecard determinístico 0-100 ao Nightly Ops Audit; espelhado script no Brain; atualizado prompt/nome do digest 03h para incluir Nota Hermes geral e por área; criado contrato runtime/hermes-principal-scorecard-0-100.md e MAPA.
- Output/artefato:
- reports/nightly-ops-audit/latest.json agora contém scorecard.overall_score e componentes; digest 03h consumirá a nota e notas por área; values_printed=false.
- Aprovação: Aprovado por Lucas nesta conversa para criar score 0-100 no digest 03h.
- Envio/publicação: Sem envio externo nesta execução; próximo envio normal pelo cron 03h já existente.
- Writes externos: nenhum
- Riscos/bloqueios: Score é operacional e não autoriza mutações; critical/attention limitam a nota geral; watch desconta pouco.
- Rollback/mitigação: Restaurar /opt/data/cron/jobs.json pelo backup /opt/data/backups/cron-digest-scorecard-20260615T011734Z/jobs.default.before.json e reverter script /opt/data/scripts/hermes_nightly_ops_audit.py pela versão anterior no histórico/backup.
- Próximos passos: Observar o primeiro digest real das 03h e ajustar pesos se a leitura executiva ficar otimista/punitiva demais.
- Onde foi documentado no Brain: areas/operacoes/runtime/hermes-principal-scorecard-0-100.md; areas/operacoes/MAPA.md; areas/operacoes/scripts/hermes_nightly_ops_audit.py
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
