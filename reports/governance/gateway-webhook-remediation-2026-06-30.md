# Approval packet — limpar variável webhook herdada em gateways secundários

Data: 2026-06-30
Status: aguardando aprovação escopada
Risco: A3 runtime local de gateways secundários
values_printed=false

## Problema
O watchdog global de gateways Telegram encontrou dois perfis secundários vivos com `WEBHOOK_SECRET` presente no ambiente do processo, apesar de API/webhook estarem configurados para ficar desligados em perfis especialistas:

- `spiti-atendimento`: gateway conectado, `HERMES_HOME` correto, `bad_keys=[WEBHOOK_SECRET]`.
- `lk-finance`: gateway conectado, `HERMES_HOME` correto, `bad_keys=[WEBHOOK_SECRET]`.

Não há evidência de valores impressos. O problema é de superfície runtime herdada, não de secret ausente.

## Por que não auto-corrigi neste cron
A correção real exige parar/reiniciar processos de gateway secundários ou matar processos inseguros após substituição por processo limpo. Isso é mutação de runtime/gateway e está bloqueado dentro do Daily Intelligence sem aprovação atual.

## Escopo de aprovação recomendado
Aprovar somente:

1. Reiniciar `spiti-atendimento` e `lk-finance` via launcher/watchdog local já existente, com API/webhook forçados off.
2. Verificar `/proc/<pid>/environ` dos novos PIDs apenas por booleans/nomes de variáveis, sem imprimir valores.
3. Verificar `gateway_state.json`, Telegram connected e logs sanitizados.
4. Não tocar Main Hermes, Docker, VPS, Traefik, portas, volumes, secrets no Doppler, cron schedule, Shopify/Tiny/GMC/WhatsApp/email.

## Rollback
Se o novo processo não conectar ou herdar superfície indevida, parar somente o processo recém-criado e manter o estado anterior documentado; não reiniciar Docker/Main.

## Evidência desta rodada
- Preflight 2026-06-30 02h BRT: `nightly_self_improvement_regression.status=attention`, issue `gateway_watchdog_not_silent_ok`.
- Watchdog all Telegram gateways 05:01 UTC: alerta para `spiti-atendimento` e `lk-finance` com `WEBHOOK_SECRET`.
- Probe local read-only deste run confirmou os dois PIDs vivos, `HERMES_HOME` correto e `bad_keys=['WEBHOOK_SECRET']`.
