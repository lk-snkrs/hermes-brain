# Receipt — Main/default gateway Shopify CLI activation done

- Data/hora: 2026-06-28T10:54:27.504224+00:00
- Agente/profile/cron: default / Operações Hermes
- Empresa/área: Operações Hermes / Gateway principal
- Responsável humano: Hermes Agent
- Pedido original: Lucas aprovou explicitamente: Pode restart, para ativar no main/default a política Shopify CLI oficial.
- Classificação: infra-sensitive
- Fontes usadas:
- reports/governance/main-default-gateway-shopify-cli-activation-approval-packet-2026-06-28.md
- reports/governance/main-default-gateway-shopify-cli-activation-post-validation-20260628T105319Z/summary.json
- O que foi feito:
- Executado restart controlado do main/default; primeira tentativa retornou corrida com PID 1 ainda vivo, depois o gateway principal reiniciou e foi validado por start time novo, health, cron, roster, watchdog e smoke Shopify CLI oficial.
- Output/artefato:
- reports/governance/main-default-gateway-shopify-cli-activation-run-20260628T104941Z
- reports/governance/main-default-gateway-shopify-cli-activation-post-validation-20260628T105319Z
- empresa/contexto/decision-sequences/2026-06-28.jsonl
- Aprovação: Aprovação escopada recebida de Lucas no Telegram: 'Pode restart'. Escopo limitado ao restart/readback do main/default gateway para carregar política Shopify CLI oficial; Docker/VPS/Traefik, cron mutation, secrets e writes externos permaneceram bloqueados.
- Envio/publicação: Telegram: reportar conclusão objetiva; sem valores sensíveis.
- Writes externos: 0; sem Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/e-mail/WhatsApp/customer writes.
- Riscos/bloqueios: Restart do gateway principal causou corrida não fatal com PID 1; validação final OK, especialistas preservados e watchdog silent-OK.
- Rollback/mitigação: Se regressão aparecer, usar snapshot/validation dirs e restaurar apenas especialistas esperados via /opt/data/scripts/hermes_all_gateway_watchdog.py; não escalar para Docker/VPS/Traefik sem nova aprovação.
- Próximos passos: Monitorar se algum agente volta a usar raw/wrapper Shopify; corrigir localmente se aparecer regressão.
- Onde foi documentado no Brain: Receipt final e ledger Mesa atualizados; values_printed=false.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
