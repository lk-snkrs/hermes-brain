# Receipt — Main/default gateway Shopify CLI activation packet prepared

- Data/hora: 2026-06-28T10:47:03.223840+00:00
- Agente/profile/cron: default / Mesa COO follow-through
- Empresa/área: Operações Hermes / Gateway principal
- Responsável humano: Hermes Agent
- Pedido original: Lucas clicou Fazer na decisão Mesa COO 1/3 para preparar ativação controlada do gateway principal para carregar a política Shopify CLI oficial.
- Classificação: infra-sensitive
- Fontes usadas:
- reports/daily-consolidation/2026-06-28.md
- reports/governance/shopify-official-cli-gateway-restart-2026-06-27.md
- reports/governance/main-default-gateway-shopify-cli-activation-approval-packet-2026-06-28.md
- O que foi feito:
- Preparado approval packet com comando exato, escopo permitido/bloqueado, readback e rollback; capturado snapshot sanitizado do pré-estado e atualizado ledger da Mesa.
- Output/artefato:
- reports/governance/main-default-gateway-shopify-cli-activation-approval-packet-2026-06-28.md
- reports/governance/main-default-gateway-shopify-cli-activation-prestate-2026-06-28.json
- empresa/contexto/decision-sequences/2026-06-28.jsonl
- Aprovação: Fazer autorizou preparar o packet/readback; restart main/default ainda bloqueado até aprovação escopada separada.
- Envio/publicação: Telegram: resposta curta com packet preparado e pedir aprovação separada se quiser executar.
- Writes externos: 0; sem Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/e-mail/WhatsApp/customer writes.
- Riscos/bloqueios: Restart do main/default pode interromper Telegram/API/webhook/cron e afetar roster de especialistas; packet exige execução fora do gateway e validação pós-restart.
- Rollback/mitigação: Sem runtime mutation executada; para execução futura, rollback/contenção é reenumerar /proc/gateway status e restaurar somente especialistas vivos no pré-estado via /opt/data/scripts/hermes_all_gateway_watchdog.py.
- Próximos passos: Aguardar aprovação separada de Lucas para executar o restart controlado, ou manter lacuna documentada.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
