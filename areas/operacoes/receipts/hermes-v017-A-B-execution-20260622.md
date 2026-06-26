# Receipt — Hermes v0.17 A+B execution: profile delegation activation and cron Telegram contract hardening

- Data/hora: 2026-06-22T13:38:48.380876+00:00
- Agente/profile/cron: hermes-geral/default
- Empresa/área: operacoes
- Responsável humano: Hermes Geral
- Pedido original: Lucas aprovou Fazer o A e o B
- Classificação: local-write
- Fontes usadas:
- Approval packets v0.17 A/B; live profile roster; cron registry backups; sentinel; Brain health; independent tester
- O que foi feito:
- Reiniciados 11 perfis gerenciados para ativar delegation/toolsets; patchados 13 crons origin com contrato Telegram v0.17 apenas no prompt; preservados schedule/delivery/enabled/state/script; rodado sentinel e tester PASS
- Output/artefato:
- sentinel status ok; profile_gap_count=0; origin_without_explicit_contract_count=0; 11 perfis running/connected; global watchdog silent-OK
- Aprovação: Lucas disse Fazer o A e o B; escopo aplicado somente aos packets A/B
- Envio/publicação: Telegram conciso
- Writes externos: nenhum
- Riscos/bloqueios: lk-ops e lk-stock precisaram SIGKILL após drain mas voltaram com 1 PID e Telegram connected; cron runtime metadata pode mudar naturalmente pelo scheduler
- Rollback/mitigação: A: restaurar configs de /opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/ e reiniciar perfis; B: restaurar registries de /opt/data/backups/hermes-v017-A-B-20260622T132911Z/cron-backups/
- Próximos passos: Monitorar sentinel; não há próximo passo obrigatório para A/B; canais/dashboard/MCP/model default continuam approval-gated
- Onde foi documentado no Brain: areas/operacoes/reports/hermes-v017-A-B-execution-20260622.md; lucas-runtime-operations reference hermes-v017-A-B-activation-20260622.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
