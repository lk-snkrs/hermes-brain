# LK Daily + Weekly Silent Cron Activation, 2026-05-11

Generated at: `2026-05-11T22:17:37.043836+00:00`

## Veredito

Daily Sales Brief e Weekly CEO Review foram ativados como cronjobs read-only, `no_agent`. O texto original chamava o contrato de `silent-OK`, mas isso foi superseded em 2026-05-15: o contrato atual é **entrega obrigatória** do report na cadência aprovada, sem n8n, sem envio imediato e sem write produtivo.

## Snapshot

- Cronjobs criados: 2
- Jobs no_agent: 2
- n8n flows criados: 0
- Telegram sends imediatos: 0
- Envios externos agora: 0
- Writes produtivos agora: 0

## Jobs

### LK-AUTO-001 · LK Daily Sales Brief read-only silent watchdog

- Job ID: `7c688553e293`
- Agenda UTC: `0 11 * * *`
- Agenda BRT: daily 08:00 BRT
- Script: `/opt/data/scripts/lk_daily_sales_brief_watchdog.py`
- no_agent: `True`
- Próxima execução: `2026-05-12T11:00:00+00:00`
- Silent-OK: superseded em 2026-05-15. Contrato atual é entrega obrigatória: rc=0 + stdout entrega report; rc!=0 alerta falha.
- Report inclui P0/P1 quando houver, mas P0/P1 são prioridade de leitura, não condição de entrega.

### LK-AUTO-002 · LK Weekly CEO Review read-only silent watchdog

- Job ID: `953b9055458e`
- Agenda UTC: `0 12 * * 1`
- Agenda BRT: weekly Monday 09:00 BRT
- Script: `/opt/data/scripts/lk_weekly_ceo_review_watchdog.py`
- no_agent: `True`
- Próxima execução: `2026-05-18T12:00:00+00:00`
- Silent-OK: superseded em 2026-05-15. Contrato atual é entrega obrigatória: rc=0 + stdout entrega report; rc!=0 alerta falha.
- Report inclui P0/P1 quando houver, mas P0/P1 são prioridade de leitura, não condição de entrega.

## Rollback

- Pause/remove job_id 7c688553e293 for Daily.
- Pause/remove job_id 953b9055458e for Weekly.
- Cron scripts are local at /opt/data/scripts and can be edited/disabled without touching Shopify/Tiny/GA4.

## Não realizado

- Nenhum n8n flow criado.
- Nenhum envio imediato executado.
- Nenhuma campanha enviada/agendada.
- Nenhum write em Shopify/Tiny/Merchant/GSC/produção.
