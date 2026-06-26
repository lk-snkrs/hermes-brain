# Receipt — Main/default Docker restart — Task OS dispatcher activation

- Data/hora: 2026-06-25T20:23:27.994332+00:00
- Agente/profile/cron: default
- Empresa/área: Hermes runtime / Task OS / Kanban dispatcher
- Responsável humano: Hermes
- Pedido original: Lucas autorizou: então pode restart.
- Classificação: infra-sensitive
- Fontes usadas:
- Docker restart log; PID 1 process start time; API health; webhook health; runtime import inspection; Kanban diagnostics; Brain health; gateway_state.json.
- O que foi feito:
- Restart do container Main/default executado via Docker daemon; PID 1 iniciou após mtime do patch; dispatcher runtime expõe readiness preflight, worker_readiness_fn e readiness_blocked; API/webhook/Telegram conectados; diagnostics limpo.
- Output/artefato:
- PID 1 start Thu Jun 25 20:16:04 2026; main_api_health=ok; webhook_health=ok; telegram state=connected; kanban_diagnostics_count=0; Brain All checks passed.
- Aprovação: Aprovação explícita e escopada de Lucas para restart do Main/default: 'então pode restart', após o assistente declarar que o Main/default ainda precisava de restart para carregar o dispatcher patchado.
- Envio/publicação: Resumo pós-restart no Telegram.
- Writes externos: 0 business writes; Docker container restart only, approved.
- Riscos/bloqueios: Restart interrompeu sessão por alguns segundos; log do script não registrou finished_at porque o próprio container foi reiniciado durante docker restart; validação pós-boot confirmou sucesso. Warnings atuais de invalid signature em rota webhook foram rejeitados pelo gateway e não bloqueiam o restart.
- Rollback/mitigação: Reverter patches a partir dos backups já documentados e reiniciar container novamente; para apagar symlinks de skill, usar /opt/data/backups/kanban-worker-skill-propagation-20260625T200720Z/created_symlinks.json.
- Próximos passos: Monitorar somente se surgirem erros atuais; investigar invalid signature lk-shopify-tiny-stock-sync separadamente se persistir como degradação real.
- Onde foi documentado no Brain: Sim: receipt pós-restart.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
