# Zipper OS — implementação do report diário de vendas (2026-05-18)

## Status

Implementado e agendado.

## Job

- Nome: `Zipper OS vendas 09h WhatsApp/email`
- Job ID: `357d40a5863e`
- Schedule: `0 12 * * 1-5` UTC = 09:00 BRT
- Script cron: `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py`
- Delivery layer: `/opt/data/scripts/zipper_sales_report_external_delivery.py`

## Fonte

- Supabase Zipper Vendas: `pcstqxpdzibheuopjkas`
- Tabela: `vendas_tango`
- Credenciais via Doppler `lc-keys/prd`; nenhum secret salvo/impresso.

## Destinos aprovados no PRD

- WhatsApp: `[ZPR] IA Bot` via account `hermes`, JID validado localmente.
- E-mail: `lucas@zippergaleria.com.br`, `osmar@zippergaleria.com.br`, `fabio@zippergaleria.com.br`.

## Validações executadas

- `python3 -m py_compile` nos scripts: OK.
- Dry-run default em 2026-05-18: período `2026-05-15..2026-05-17`, 2 linhas, total R$ 41.500,00.
- Artefatos gerados:
  - `/opt/data/hermes_bruno_ingest/local_sql/zipper_sales_report/artifacts/2026-05-15_2026-05-17/report.json`
  - `/opt/data/hermes_bruno_ingest/local_sql/zipper_sales_report/artifacts/2026-05-15_2026-05-17/whatsapp.txt`
  - `/opt/data/hermes_bruno_ingest/local_sql/zipper_sales_report/artifacts/2026-05-15_2026-05-17/email.html`
- Marker presente: `zipper-os-sales-report-v1-2026-05-18`.
- PII sanity nos artefatos visíveis: 0 e-mails/telefones detectados.
- WhatsApp target validado read-only: account autenticado e grupo `[ZPR] IA Bot` encontrado.
- Gmail Zipper validado: remetente `lucas@zippergaleria.com.br`.

## Segurança

- Script lê Supabase read-only.
- Não escreve em Supabase/CRM.
- Não faz follow-up, draft ou contato com clientes/artistas/colectores.
- Anti-duplicidade por idempotency key de período + destinatários.
- Report sempre consolida vendas do mês corrente até ontem; não usa D-1/fim de semana como período padrão.
- Sucesso duplicado fica silencioso; falha alerta a origem com erro sanitizado.

## Observação

Não foi feito envio manual imediato no momento da implementação. O primeiro envio automático está agendado para o próximo dia útil às 09:00 BRT.

## Hardening pós-LK 16h — 2026-05-18

Após o falso negativo de verificação Gmail no report LK 16h, o report Zipper foi revisado preventivamente antes do primeiro envio automático.

Mudanças aplicadas:

- `/opt/data/scripts/zipper_sales_report_external_delivery.py` agora decodifica headers MIME (`Subject`/`To`) antes de verificar o e-mail enviado.
- A verificação Gmail agora também exige pelo menos 1 parte HTML no MIME.
- Limpeza de duplicidade interna na montagem dos filtros de data Supabase; o filtro continua sendo `pedido_data >= start` e `pedido_data <= end`.
- `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py` ganhou `--dry-run` para validar o fluxo completo sem WhatsApp/e-mail externo.

Validação fresca:

- `python3 -m py_compile /opt/data/scripts/zipper_sales_report_external_delivery.py /opt/data/scripts/zipper_weekday_sales_report_watchdog.py`: OK.
- `/opt/data/scripts/zipper_sales_report_external_delivery.py`: dry-run OK, período `2026-05-15..2026-05-17`, 2 linhas, total R$ 41.500,00.
- WhatsApp target read-only: OK para `[ZPR] IA Bot` via account `hermes`.
- Gmail Zipper read-only: OK, sender `lucas@zippergaleria.com.br`.
- Local MIME subject decode test: OK.
- `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py --dry-run`: exit 0, nenhum envio externo.
- Artefatos visíveis: 0 secret hits; marker no HTML OK.
