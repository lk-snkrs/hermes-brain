# Receipt — Hermes Central Auth Broker — runtime activation/restart validation

- Data/hora: 2026-06-28T17:10:50.367466+00:00
- Agente/profile/cron: Hermes default / runtime operations
- Empresa/área: Operações Hermes / Central Integration Auth Broker
- Responsável humano: Hermes Agent
- Pedido original: Lucas perguntou se deveria reiniciar os agentes para ativar a regra obrigatória do Hermes Central Integration Auth Broker; havia aprovação prévia para reiniciar se necessário.
- Classificação: infra-sensitive
- Fontes usadas:
- lucas-runtime-operations; gateway-post-restart-validation; /proc live roster; watchdog; API health; CLI smoke; unit tests.
- O que foi feito:
- Recarreguei 12 gateways especialistas gerenciados via watchdog; reiniciei main/default de forma controlada; recuperei/validei roster completo e smoke do broker.
- Output/artefato:
- 13/13 gateways esperados vivos (main + 12 managed); especialistas com API/webhook fechados; health 200 Hermes 0.17.0; cron status OK com 40 jobs; broker smoke OK sem Linear; tests do broker 5/5 OK.
- Aprovação: Lucas aprovou reiniciar caso necessário e perguntou sobre ativação por restart; ação restrita ao runtime Hermes local, sem Docker/VPS/Traefik.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Pequena interrupção temporária dos bots durante reload; nenhum secret alterado; nenhum write externo.
- Rollback/mitigação: Watchdog global pode restaurar managed gateways; artefatos/pre-state em reports/governance/default-gateway-restart-all-agents-policy-2026-06-28/; reverter AGENTS via backup central-auth-broker-mandatory-skill-propagation-20260628T165621Z se necessário.
- Próximos passos: Nenhum obrigatório. Opcional: auditoria de higiene para scripts/crons antigos hardcoded.
- Onde foi documentado no Brain: reports/governance/default-gateway-restart-all-agents-policy-2026-06-28/post_validation_recovered.json; receipt atual.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
