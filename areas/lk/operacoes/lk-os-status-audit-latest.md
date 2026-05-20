# LK OS — Status audit operacional

Atualizado: 2026-05-18T20:48:56.796955+00:00

Status: `ok`

## Segurança

- Writes externos executados por este audit: `0`
- Este audit é read-only/local; não envia WhatsApp/e-mail e não escreve em Shopify/Tiny/GMC.

## Destinos aprovados de reports

- WhatsApp: `Grupo LK Vendas` / `[LK] Vendas/Trocas/Envios` / `120363314625506305@g.us` / conta `hermes`
- E-mail: `lk@lksneakers.com.br`
- External auto send enabled para reports aprovados: `True`

## Reports canônicos

### `previous-day-09h`

- Escopo: Fechamento do dia anterior com leitura estrutural, incluindo performance/interesse do site quando disponível.
- Watchdog script existe: `True` — `/opt/data/scripts/lk_previous_day_09h_sales_report_watchdog.py`
- Último receipt: status `dry_run_ok` em `2026-05-18T13:55:27.068677+00:00`
- Sent state conhecido: `False`
- Secret hits nos últimos artefatos: `0`
- Dry-run generation: exit `0`, status `dry_run_ok`
  - json: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-previous-day-09h-20260518T090000-0300.json`
  - whatsapp: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-whatsapp-previous-day-09h-20260518T090000-0300.txt`
  - html: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-designmd-previous-day-09h-20260518T090000-0300.html`
  - email_meta: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-meta-previous-day-09h-20260518T090000-0300.json`

### `pulse-finance-16h`

- Escopo: Pulso financeiro do dia corrente até 16h, separando loja física vs e-commerce quando disponível.
- Watchdog script existe: `True` — `/opt/data/scripts/lk_financial_pulse_16h_watchdog.py`
- Último receipt: status `duplicate_skipped` em `2026-05-18T19:06:45.314035+00:00`
- Sent state conhecido: `True`
- Secret hits nos últimos artefatos: `0`
- Dry-run generation: exit `0`, status `dry_run_ok`
  - json: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-pulse-finance-16h-20260518T160000-0300.json`
  - whatsapp: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-whatsapp-pulse-finance-16h-20260518T160000-0300.txt`
  - html: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-designmd-pulse-finance-16h-20260518T160000-0300.html`
  - email_meta: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-meta-pulse-finance-16h-20260518T160000-0300.json`

### `store-close-1930`

- Escopo: Fechamento POS/loja física only; sem online/e-commerce/GA4 no escopo do report.
- Watchdog script existe: `True` — `/opt/data/scripts/lk_store_close_1930_watchdog.py`
- Último receipt: status `dry_run_ok` em `2026-05-18T13:55:33.917620+00:00`
- Sent state conhecido: `False`
- Secret hits nos últimos artefatos: `0`
- Dry-run generation: exit `0`, status `dry_run_ok`
  - json: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-store-close-1930-20260518T105530-0300.json`
  - whatsapp: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-whatsapp-store-close-1930-20260518T105530-0300.txt`
  - html: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-designmd-store-close-1930-20260518T105530-0300.html`
  - email_meta: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-sales-reports/lk-sales-reports-email-meta-store-close-1930-20260518T105530-0300.json`

## Atenção

- Nenhum alerta crítico no audit local.
