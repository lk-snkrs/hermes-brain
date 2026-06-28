# Elle v2 — auditoria 3h pós-correção (atenção)

Gerado: 20260627T163340Z

## Resumo

- Processados: 2
- v2 used/skipped/error: 1/1/0
- eval_bad: 0
- eval médio/alto: 0
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 12

## Issues

- autonomy gate continua HOLD

## Exemplos de risco sanitizados

- nenhum

## Gates

```json
{
  "health": {
    "ok": true,
    "write_enabled": true,
    "kill_switch": false,
    "public_reply_enabled": true,
    "ai_enabled": true,
    "ai_provider": "openrouter",
    "hmac_secret_present": true,
    "legacy_path_webhook_enabled": false,
    "elle_brain_v2_canary_enabled": true,
    "elle_brain_v2_canary_percent": 100
  },
  "counts": {
    "events_total": 624,
    "processed": 2,
    "response_evaluated": 2,
    "eval_bad": 0,
    "eval_medium_high": 0,
    "v2_used": 1,
    "v2_skipped": 1,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 1,
    "decision_llm_final": 0,
    "decision_guardrail_after_llm": 1,
    "stock_handoff": 0,
    "human_handoff": 1,
    "product_clear": 1
  },
  "autofix_counts": {
    "autofix_regression_drafts": 12,
    "autofix_patch_suggestions": 12,
    "regression_candidates": 17,
    "eval_risk_candidates": 5
  },
  "autonomy_gate": {
    "status": "hold",
    "scope": "autonomy_expansion_gate",
    "window_hours": 24.0,
    "events_total": 3105,
    "processed": 38,
    "v2_canary_used": 14,
    "v2_canary_skipped": 16,
    "v2_canary_error": 0,
    "ai_provider_error": 0,
    "eval_bad": 3,
    "eval_medium_high": 1,
    "handoff_violations": 0,
    "recommendation": "do_not_expand_autonomy",
    "customer_send_executed": false,
    "writes_external": 0,
    "values_printed": false
  },
  "drift_ok": true,
  "regression_ok": true,
  "openrouter_ok": true,
  "values_printed": false
}
```

Sem estoque/Tiny, sem WhatsApp/backfill, sem secrets. values_printed=false
