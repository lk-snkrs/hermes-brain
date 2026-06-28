# Elle v2 — auditoria 3h pós-correção (atenção)

Gerado: 20260627T133404Z

## Resumo

- Processados: 5
- v2 used/skipped/error: 3/2/0
- eval_bad: 1
- eval médio/alto: 1
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 12

## Issues

- qualidade ainda tem eval_bad=1 e risco médio/alto=1
- autonomy gate continua HOLD

## Exemplos de risco sanitizados

- conv=2393 msg=58143 quality=bad risk=medium issue=misclassification expected=None

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
    "events_total": 304,
    "processed": 5,
    "response_evaluated": 5,
    "eval_bad": 1,
    "eval_medium_high": 1,
    "v2_used": 3,
    "v2_skipped": 2,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 3,
    "decision_llm_final": 1,
    "decision_guardrail_after_llm": 1,
    "stock_handoff": 0,
    "human_handoff": 2,
    "product_clear": 0
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
    "events_total": 3049,
    "processed": 45,
    "v2_canary_used": 13,
    "v2_canary_skipped": 15,
    "v2_canary_error": 0,
    "ai_provider_error": 0,
    "eval_bad": 4,
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
