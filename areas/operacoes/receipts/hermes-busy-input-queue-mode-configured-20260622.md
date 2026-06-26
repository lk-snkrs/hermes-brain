# Receipt — Hermes busy input queue mode configured

- Data/hora: 2026-06-22T20:58:32.999496+00:00
- Agente/profile/cron: hermes-geral/default
- Empresa/área: operacoes-hermes
- Responsável humano: Hermes Geral
- Pedido original: Lucas corrigiu que mensagens sequenciais em agentes Telegram devem entrar em fila e não cancelar/substituir a tarefa anterior
- Classificação: local-write
- Fontes usadas:
- gateway/run.py busy_input_mode; /proc live env; default and specialist config.yaml
- O que foi feito:
- Configurado display.busy_input_mode=queue no default e em 11 perfis especialistas gerenciados; backups criados; WACLI auth process anterior encerrado para não deixar QR solto
- Output/artefato:
- Config parse OK em 12 configs; live gateways ainda mostram interrupt até restart; values_printed=false
- Aprovação: Pedido direto do Lucas para corrigir comportamento de cancelamento por fila
- Envio/publicação: Telegram
- Writes externos: nenhum
- Riscos/bloqueios: Ativação runtime exige restart escopado dos gateways; sem restart, fica apenas configured
- Rollback/mitigação: Restaurar config.yaml de /opt/data/backups/hermes-busy-queue-mode-20260622T205735Z/config-backups/
- Próximos passos: Executar restart controlado dos gateways afetados quando aprovado para tornar HERMES_GATEWAY_BUSY_INPUT_MODE=queue live
- Onde foi documentado no Brain: hermes-agent reference gateway-busy-input-queue-mode-lucas-20260622.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
