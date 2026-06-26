# Receipt — LK Weekly Collection Sort Rule B recorrente APPLY ativado

Data: `2026-06-04T09:50:06Z`
Status: `activated`

## Aprovação

Lucas aprovou explicitamente no Telegram:

> APROVO RULE B APPLY RECORRENTE

Observação de UX registrada: próximos approvals operacionais devem usar botões/choices quando possível, não exigir frase digitada.

## Mudança realizada

- Cron job: `787134d4ac5c` — `LK Weekly Collection Sort Rule B`.
- Agenda preservada: `0 9 * * 5` — sexta-feira 09:00 UTC.
- Delivery preservado: `local`.
- `no_agent` preservado: `true`.
- Script anterior: `lk_weekly_collection_sort_ruleB.sh`.
- Script novo: `lk_weekly_collection_sort_ruleB_apply_recurring.sh`.

## Wrapper criado

Arquivo: `/opt/data/scripts/lk_weekly_collection_sort_ruleB_apply_recurring.sh`

Comportamento:

1. `export LK_WEEKLY_COLLECTION_SORT_APPLY=1`
2. `exec /bin/bash /opt/data/scripts/lk_weekly_collection_sort_ruleB.sh`

A lógica Rule B não foi alterada; apenas o cron recorrente passa a chamar o dispatcher existente com opt-in APPLY.

## O que NÃO foi feito

- Não rodei APPLY manual imediato.
- Não alterei produtos, preços, estoque, tags, SEO, GMC, tema, campanhas ou clientes.
- Não mexi em Docker, VPS, Traefik, gateway, providers ou secrets.
- Não alterei outros crons.

## Rollback

Para voltar a dry-run recorrente:

1. Atualizar o job `787134d4ac5c` para `script=lk_weekly_collection_sort_ruleB.sh`.
2. Verificar `cronjob list`.
3. Se alguma execução APPLY futura já tiver rodado e precisar reversão, usar o `rollback-snapshot-pre-write.json` do respectivo receipt de execução.

## Verificações feitas

- Wrapper escrito em `/opt/data/scripts/lk_weekly_collection_sort_ruleB_apply_recurring.sh`.
- `bash -n` do wrapper: OK.
- Permissão do wrapper: `750 root:root`.
- Cron update retornou `success=true` e script novo no job `787134d4ac5c`.

## Próxima execução esperada

- `2026-06-05T09:00:00+00:00`
