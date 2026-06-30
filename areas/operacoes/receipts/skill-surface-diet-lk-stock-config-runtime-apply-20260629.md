# Receipt — Skill Surface Diet lk-stock config/runtime apply

- Data/hora: 2026-06-29T15:24:02.055723+00:00
- Agente/profile/cron: Hermes default / lk-stock
- Empresa/área: Operações Hermes / LK Stock
- Responsável humano: Hermes
- Pedido original: Lucas pediu continuar melhorando skills e escolheu aplicar Skill Surface Diet no lk-stock
- Classificação: local-write
- Fontes usadas:
- Inventário Skill Surface Diet 2026-06-29; dry-run lk-stock; config/readback do profile; gateway_state; QA independente
- O que foi feito:
- Aplicada dieta por skills.platform_disabled.telegram; AGENTS.md e lk-stock/SKILL.md receberam política de tier; config migrada 27→30; gateway lk-stock reiniciado localmente; 175 skills desabilitadas no Telegram, 51 preservadas, 0 protegidas desabilitadas
- Output/artefato:
- /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/skill-surface-diet-lk-stock-config-runtime-apply-2026-06-29.md; /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/skill-surface-diet-lk-stock-apply-dry-run-2026-06-29.md; backup em /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/backups/skill-surface-diet-apply-20260629T151923Z/
- Aprovação: Lucas escolheu: Aplicar Skill Surface Diet no lk-stock
- Envio/publicação: Telegram: resposta executiva; artefatos locais no Brain
- Writes externos: 0
- Riscos/bloqueios: Mudança local de superfície de skills no Telegram; rollback por backup; API/webhook/Docker/VPS/Traefik/Main não tocados
- Rollback/mitigação: Restaurar AGENTS.md.before, lk-stock.SKILL.md.before e config.yaml.before do backup skill-surface-diet-apply-20260629T151923Z e reiniciar somente lk-stock
- Próximos passos: Continuar com próximo P0/P1 apenas se Lucas pedir; possível próxima frente: default com approval mais cuidadoso ou split global de skills pesadas
- Onde foi documentado no Brain: Relatório apply, dry-run, backup e receipt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
