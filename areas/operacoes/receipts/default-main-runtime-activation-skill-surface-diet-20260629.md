# Receipt — Default Main runtime activation Skill Surface Diet

- Data/hora: 2026-06-29T15:51:04.494622+00:00
- Agente/profile/cron: Hermes default
- Empresa/área: Operações Hermes / Runtime
- Responsável humano: Hermes
- Pedido original: Lucas aprovou ativar em runtime a Skill Surface Diet do default/Main
- Classificação: infra-sensitive
- Fontes usadas:
- Runner detached; logs do gateway; proc roster; API health; config readback
- O que foi feito:
- Ativação controlada do default/Main executada; comando retornou race rc=1, mas logs confirmaram parada e startup; Telegram/API/webhook conectados; menu Telegram reduzido ativo; roster especialista preservado
- Output/artefato:
- /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/default-main-runtime-activation-skill-surface-diet-2026-06-29.md
- Aprovação: Aprovação explícita de Lucas neste chat: Pode restart; escopo default/Main Skill Surface Diet; sem Docker/VPS/Traefik/produção
- Envio/publicação: Telegram resumo executivo; artefatos locais no Brain
- Writes externos: 0
- Riscos/bloqueios: Main/default activation interrompeu a sessão ativa e usou drain/interruption; sem Docker/VPS/Traefik; rollback por config backup e ativação controlada
- Rollback/mitigação: Restaurar /opt/data/config.yaml do backup skill-surface-diet-default-20260629T153033Z/config.yaml.before e repetir ativação controlada; ou apenas repetir ativação se não houver rollback de config
- Próximos passos: Monitorar warnings de webhooks/zombie workers como frente separada; não repetir ativação se health e roster seguirem OK
- Onde foi documentado no Brain: Relatório de ativação, run dir com pre/post state, receipt
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
