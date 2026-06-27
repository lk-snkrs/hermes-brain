# Elle Brain v2 — token budget gate 100 — 2026-06-26

**Modo:** shadow/live OpenRouter classify-only.  
**Sem canary, sem envio para cliente, sem alteração do `app.py` produtivo.**  
**values_printed:** false

## Resultado

```json
{
  "live_used": 100,
  "valid_json": 99,
  "invalid_or_error": 1,
  "valid_json_rate": "99%",
  "writes_external": 0,
  "values_printed": false
}
```

## Diagnóstico sanitizado

```json
{
  "finish_reason": [["stop", 96], ["length", 4]],
  "content_len_bucket": [["101-500", 79], ["501+", 19], ["0", 1], ["21-100", 1]],
  "parse_failure": [["none", 99], ["json_parse_none", 1]],
  "error_class": [["", 100]],
  "attempt": [[1, 99], [2, 1]]
}
```

## Leitura

A Elle Brain v2 passou o gate técnico de structured output (`>=95% valid_json`): `99/100`.

Ainda não é produção/canary automático porque restam duas etapas antes de aprovação:

1. revisão qualitativa dos diffs vs legado;
2. approval packet de canary com escopo limitado, kill-switch e rollback.

## Segurança

- `customer_send_executed=false`
- `writes_external=0` para Chatwoot/WhatsApp/Shopify/Tiny
- OpenRouter apenas classify-only/shadow
- sem restart/cutover/canary
- `values_printed=false`

## Raw

- `areas/lk/sub-areas/atendimento/reports/elle-brain-v2/tokenbudget-gate-100-raw-20260626/shadow-report.json`
- `areas/lk/sub-areas/atendimento/reports/elle-brain-v2/tokenbudget-gate-100-raw-20260626/shadow-report.md`
