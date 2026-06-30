# Receipt — LK Trends config migration v23 to v30

- Data/hora: 2026-06-29T11:38:15.636983+00:00
- Agente/profile/cron: Hermes default
- Empresa/área: Operações Hermes / LK Trends
- Responsável humano: Operações Hermes
- Pedido original: Lucas disse 'Migrar' após caveat de config version 23 -> 30 no profile lk-trends.
- Classificação: local-write
- Fontes usadas:
- Backup em areas/lk/sub-areas/trends/backups/config-migrate-v23-v30-20260629T113552Z; hermes config migrate; hermes config check; get_disabled_skills; gateway_state; /proc runtime evidence; Brain health; credential scan.
- O que foi feito:
- Migrado somente o config.yaml do profile lk-trends de _config_version 23 para 30; preservada a Skill Surface Diet; reiniciado somente o gateway lk-trends; runtime verificado com PID novo e Telegram connected.
- Output/artefato:
- Config version 30; PID lk-trends 698358; Telegram connected; API/webhook false; 208 skills disabled e 28 enabled no Telegram; protected_disabled=[]
- Aprovação: Aprovação explícita de Lucas: 'Migrar'.
- Envio/publicação: Telegram summary
- Writes externos: nenhum
- Riscos/bloqueios: Migração adicionou novos defaults do Hermes v30 e manteve model_catalog.ttl_hours=1/curator.consolidate=false; optional API keys ausentes aparecem como nomes apenas, sem valores; nenhum Docker/VPS/Traefik/Main tocado.
- Rollback/mitigação: Restaurar backups config.yaml.before e gateway_state.before.json se necessário; reiniciar apenas lk-trends; verificar config check, Skill Surface Diet e Telegram connected.
- Próximos passos: Monitorar LK Trends em tarefa real; repetir migração/config-check em outros profiles P0 apenas com novo escopo.
- Onde foi documentado no Brain: Receipt, backup, config-check before/after, migration output, runtime evidence local.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
