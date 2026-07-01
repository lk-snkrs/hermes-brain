# Approval packet — limpar variável webhook herdada em gateways secundários

Data: 2026-06-30
Status: superseded/resolvido por execução 2026-06-30T10:17Z e revalidação viva 2026-07-01T09:38:47Z
Risco: A3 runtime local de gateways secundários
values_printed=false

## Problema
O watchdog global de gateways Telegram encontrou dois perfis secundários vivos com `WEBHOOK_SECRET` presente no ambiente do processo, apesar de API/webhook estarem configurados para ficar desligados em perfis especialistas:

- `spiti-atendimento`: gateway conectado, `HERMES_HOME` correto, `bad_keys=[WEBHOOK_SECRET]`.
- `lk-finance`: gateway conectado, `HERMES_HOME` correto, `bad_keys=[WEBHOOK_SECRET]`.

Não há evidência de valores impressos. O problema é de superfície runtime herdada, não de secret ausente.

## Por que não auto-corrigi neste cron
Este relatório era o preflight inicial. A correção escopada foi posteriormente aprovada/executada em 2026-06-30T10:17Z e revalidada em 2026-07-01T09:38:47Z. Não tratar este arquivo como bloqueio ativo sem novo readback vivo.

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


## Revalidação 2026-07-01

Readback vivo atual confirmou `WEBHOOK_SECRET` ausente, `API_SERVER_KEY` ausente, `DOPPLER_TOKEN` ausente, API/webhook desligados e Telegram OK para `spiti-atendimento` e `lk-finance`. Ver `reports/governance/webhook-secret-secondary-gateways-revalidation-2026-07-01.md`.
