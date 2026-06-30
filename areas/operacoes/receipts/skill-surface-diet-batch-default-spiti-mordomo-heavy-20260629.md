# Receipt — Skill Surface Diet batch default spiti mordomo heavy skills

- Data/hora: 2026-06-29T15:35:44.327371+00:00
- Agente/profile/cron: Hermes default
- Empresa/área: Operações Hermes / Skill Surface Diet
- Responsável humano: Hermes
- Pedido original: Lucas aprovou fazer do 1 ao 4: default, spiti, mordomo e curadoria global de skills pesadas
- Classificação: local-write
- Fontes usadas:
- Relatório batch Skill Surface Diet; configs dos profiles; runtime readback spiti/mordomo; QA independente; backups locais
- O que foi feito:
- Aplicada Skill Surface Diet em default, spiti e mordomo; spiti e mordomo migrados para config v30 e reiniciados; spiti-atendimento restaurado após interrupção acidental; 3 skills globais pesadas compactadas com conteúdo completo preservado em references
- Output/artefato:
- /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/skill-surface-diet-batch-default-spiti-mordomo-heavy-2026-06-29.md; /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/skill-surface-diet-batch-default-spiti-mordomo-heavy-2026-06-29.json
- Aprovação: Lucas: Fazer do 1 ao 4; e também sugeriu curar skills globais pesadas
- Envio/publicação: Telegram resumo executivo; artefatos locais no Brain
- Writes externos: 0
- Riscos/bloqueios: Default configurado mas não ativado em runtime porque Main/PID1/container não foi reiniciado; rollback por backups; sem Docker/VPS/Traefik/Main restart
- Rollback/mitigação: Restaurar backups em areas/operacoes/backups/skill-surface-diet-default-20260629T153033Z, areas/spiti/backups/skill-surface-diet-spiti-20260629T153033Z, areas/operacoes/backups/skill-surface-diet-mordomo-20260629T153033Z e areas/operacoes/backups/global-heavy-skill-curation-20260629T153033Z; reiniciar somente profiles afetados se necessário
- Próximos passos: Se Lucas quiser ativar default runtime, fazer restart controlado do Main/container com packet próprio; senão continuar com lk-ops/lk-growth ou medir latência pós-dieta
- Onde foi documentado no Brain: Relatório batch, JSON, backups, QA e receipt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
