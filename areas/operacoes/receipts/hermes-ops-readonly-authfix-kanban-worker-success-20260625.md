# Receipt — Hermes ops readonly auth fix and Kanban worker success 2026-06-25

- Data/hora: 2026-06-25T15:43:48.553268+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: operacoes
- Responsável humano: Lucas Cimino
- Pedido original: Lucas escolheu A para corrigir auth/model do hermes-ops-readonly e tentar novamente o primeiro worker read-only Kanban.
- Classificação: local-write
- Fontes usadas:
- Auth status/smoke profile-local; default auth smoke; Kanban dry-run/dispatch/show/runs/log/diagnostics; card hermes-task-os/t_6d995d67.
- O que foi feito:
- Backup de auth/config do profile hermes-ops-readonly; sincronizado credential_pool openai-codex do default para o profile sem imprimir valores; removido provider stale openai-codex profile-local; smoke OK; unblocked e dispatch controlado do card t_6d995d67; worker concluiu no terceiro run.
- Output/artefato:
- Card t_6d995d67 done; diagnostics=0; relatório durável em reports/governance/task-os-dashboard-telegram-ux-recommendation-2026-06-25.md; guardrails preservados.
- Aprovação: Aprovação explícita no Telegram: A.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: 0
- Riscos/bloqueios: Correção local de auth profile-local; artifact original do worker em scratch era efêmero, por isso foi preservado em relatório Brain.
- Rollback/mitigação: Restaurar /opt/data/profiles/hermes-ops-readonly/auth.json e config.yaml a partir de /opt/data/backups/hermes-ops-readonly-auth-fix-*/ se necessário; card já finalizado sem external writes.
- Próximos passos: Manter Kanban como backoffice e Mesa COO Telegram como superfície principal; qualquer dashboard/API/comando Telegram novo exige approval packet separado.
- Onde foi documentado no Brain: reports/governance/task-os-dashboard-telegram-ux-recommendation-2026-06-25.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
