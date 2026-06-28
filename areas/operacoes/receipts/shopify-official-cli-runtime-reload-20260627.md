# Receipt — Shopify official CLI specialist runtime reload

- Data/hora: 2026-06-27T15:44:40.625970+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / runtime / Shopify CLI
- Responsável humano: Hermes default
- Pedido original: Recarregar gateways especialistas para ativar em runtime a regra de Shopify CLI oficial.
- Classificação: infra-sensitive
- Fontes usadas:
- Lucas aprovou de forma escopada no Telegram: Pode reiniciar, para ativar a regra Shopify CLI oficial nos agentes.
- O que foi feito:
- Recarregados 11 gateways especialistas gerenciados: mordomo, lk-growth, spiti, spiti-atendimento, lk-ops, lk-shopify, lk-trends, lk-collection-optimizer, lk-stock, lk-finance, lk-content. Watchdog pós-ação silent-OK; Shopify CLI smoke OK.
- Output/artefato:
- reports/governance/shopify-official-cli-gateway-restart-2026-06-27.md
- Aprovação: Aprovação explícita e escopada de Lucas no Telegram: Pode reiniciar, logo após o pedido de ativar a regra Shopify CLI oficial nos agentes.
- Envio/publicação: Resposta Telegram com resumo e bloqueio técnico do main/default.
- Writes externos: 0
- Riscos/bloqueios: Main/default não foi recarregado porque Hermes bloqueia essa ação feita de dentro do próprio gateway; requer comando de controle pelo usuário ou shell externo.
- Rollback/mitigação: Rerun /opt/data/scripts/hermes_all_gateway_watchdog.py para restaurar o roster especialista esperado; nenhum estado externo Shopify foi modificado.
- Próximos passos: Se Lucas quiser reload do main/default, usar o comando de controle do Telegram principal ou executar o comando Hermes de controle em shell externo.
- Onde foi documentado no Brain: reports/governance/shopify-official-cli-gateway-restart-2026-06-27.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
