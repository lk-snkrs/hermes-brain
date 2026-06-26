# Fix — LK report external delivery cron — 2026-06-26

## Pedido

Lucas pediu corrigir o erro encontrado no audit Task OS: cron `LK 09h previous-day sales report external delivery` (`e3279babbc4a`) falhava com:

```text
generated payload missing message/html/email_meta
```

## Root cause

A camada de delivery `/opt/data/scripts/lk_report_external_delivery.py` espera que o gerador Brain retorne contrato completo:

- `message`
- `html`
- `email_meta`
- `email.report_type`

O checkout operacional atual do Brain tinha uma versão regressiva/truncada do gerador:

```text
scripts/lk_os_sales_reports_whatsapp_email_designmd_20260516.py
```

Tamanho/sha curto antes:

```text
24172 bytes / sha256 015a84798ec624d6
```

Essa versão gerava apenas:

```text
json, whatsapp, html, message
```

Além disso, o config esperado pelo delivery estava ausente no checkout atual:

```text
config/lk-report-delivery-targets.json
```

O backup pré-switch para `main` preservava a versão funcional do gerador e o config.

## Correção aplicada

Backup criado:

```text
/opt/data/backups/lk-report-external-delivery-fix-20260626T125749Z
```

Restaurado de:

```text
/opt/data/hermes_bruno_ingest/hermes-brain.backup-pre-main-switch-20260626T102451Z/scripts/lk_os_sales_reports_whatsapp_email_designmd_20260516.py
/opt/data/hermes_bruno_ingest/hermes-brain.backup-pre-main-switch-20260626T102451Z/config/lk-report-delivery-targets.json
```

Para:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_os_sales_reports_whatsapp_email_designmd_20260516.py
/opt/data/hermes_bruno_ingest/hermes-brain/config/lk-report-delivery-targets.json
```

Tamanho/sha curto do gerador restaurado:

```text
77658 bytes / sha256 b438ae9d46dba0f2
```

## Verificação sem envio externo

Não rodei `--send`; nenhum WhatsApp/e-mail foi enviado nesta correção.

Dry-runs da camada de delivery:

| Report | Resultado | Subject |
|---|---|---|
| `previous-day-09h` | `dry_run_ok` | `LK OS · Fechamento de ontem — 25/06` |
| `pulse-finance-16h` | `dry_run_ok` | `LK OS · Pulso financeiro 16h — ritmo do dia` |
| `store-close-1930` | `dry_run_ok` | `LK OS · Fechamento loja física — 19h30` |

Audit operacional:

```text
/opt/data/scripts/lk_os_status_audit.py --run-generation
status=ok
warnings=[]
```

## Guardrails

- WhatsApp/email send: `0` nesta correção.
- Shopify/Tiny/GMC/Klaviyo write: `0`.
- Secrets impressos: `0`; reporta apenas status/paths.
- Próximo envio real fica para o cron aprovado ou para execução manual apenas se Lucas pedir explicitamente reenvio agora.

## Status

Localmente corrigido e validado. O campo `last_status` do cron ainda pode aparecer como `error` até a próxima execução real do cron, porque não disparei o envio externo manualmente.
