# LK Growth — Cron Delivery Watchdog — 2026-06-12

- Execução watchdog: 2026-06-12T21:02:16Z.
- Fonte de configuração: `/opt/data/profiles/lk-growth/cron/jobs.json`.
- Fonte de outputs: `/opt/data/profiles/lk-growth/cron/output/`.
- Janela de auditoria: últimas 36h desde 2026-06-11T09:02:16Z.
- Modo: read-only; nenhum job/cron/sistema externo alterado.
- values_printed=false; nenhum secret/token impresso.

## Inventário

- Jobs no `jobs.json`: 11.
- Ativos (`enabled=true`): 10.
- Pausados/inventário (`enabled=false`): 1 — `d4c26da4cd48` / LK GMC Review read-only mandatory delivery, pausado por duplicidade e substituído.
- Ativos com entrega Telegram Lucas OK: 9/10.
- Ativos com problema de configuração/execução: 2 jobs com ação necessária.

## Configuração de entrega Telegram

Critério: `deliver=origin`, `origin.platform=telegram`, `origin.chat_id=171397651`, `origin.chat_name=Lucas Cimino`.

- OK: `1240644c5f3f` — LK GMC/Product Data + Local Inventory Review.
- OK: `de3a45d36040` — LK Experiment Ledger + Impact Review.
- OK: `6cdd70fcec80` — LK Storefront QA Light Monitor.
- OK: `738d3deabaeb` — LK Growth Weekly Command Center.
- OK: `4edbacaf43ff` — LK SEO/GSC + GEO Opportunities Review.
- OK: `9a34dea6ee4b` — LK CRO/PDP Funnel Review read-only.
- OK: `f0993178730a` — LK D+7 impact review — SEO GSC P1 + hotfix Samba Jane.
- OK: `aiendpointsab01` — LK AI/GEO Endpoints Monitor.
- OK: `lkdeliverywd01` — LK Growth Cron Delivery Watchdog; primeira execução atual ainda não refletida em `last_run_at` durante a própria execução.
- FALHA CONFIG: `lkprodcleanD14` — LK Growth D+14 impact review — product operational copy cleanup; job ativo one-shot com `delivery=origin`, porém sem bloco `origin` no registro lido. Ação necessária: corrigir/confirmar configuração Telegram antes do run previsto de 2026-06-19 19:00 UTC.

## Execuções nas últimas 36h

- `1240644c5f3f` — 2026-06-11 11:43 UTC — `last_status=ok`, sem `last_delivery_error`; output grande, mas com seção `## Response` e resumo executivo.
- `de3a45d36040` — 2026-06-12 11:39 UTC — `last_status=ok`, sem `last_delivery_error`; output grande, mas com seção `## Response` e resumo executivo.
- `aiendpointsab01` — 2026-06-11 09:10, 17:10; 2026-06-12 09:10 OK; 2026-06-12 17:10 falhou com alerta legível; sem `last_delivery_error`.
- Output recente órfão/inventário: `12b96a478751` em 2026-06-12 19:25 UTC, não presente no `jobs.json` atual; output tem `## Response` e resumo executivo. Recomendação: confirmar se foi one-shot removido/renomeado ou se deveria constar no inventário.

## Problemas detectados

1. `aiendpointsab01` — `last_status=error` em execução recente (2026-06-12 17:10 UTC). O script retornou alerta por termos operacionais proibidos em `/llms.txt` e `/llms-full.txt`; output é curto e legível, sem erro de entrega. Ação necessária: revisar conteúdo/baseline dos endpoints AI/GEO; qualquer ajuste público exige aprovação escopada.
2. `lkprodcleanD14` — job ativo previsto para 2026-06-19 sem bloco `origin` Telegram no `jobs.json`. Ação necessária: corrigir configuração de entrega antes da execução; não alterado por este watchdog.

## Jobs previstos que não rodaram

- Nenhum job ativo vencido sem execução foi confirmado nesta janela.
- `f0993178730a` e `lkprodcleanD14` são one-shots futuros.
- `lkdeliverywd01` está em primeira execução; `last_run_at` ainda não aparece no arquivo durante a própria execução.

## Veredito

- Entrega Telegram geral está majoritariamente configurada, sem `last_delivery_error` nos jobs recentes.
- Não está 100% OK por dois pontos: falha recente do monitor AI/GEO e configuração incompleta do one-shot D+14 `lkprodcleanD14`.
- Writes externos: nenhum.
