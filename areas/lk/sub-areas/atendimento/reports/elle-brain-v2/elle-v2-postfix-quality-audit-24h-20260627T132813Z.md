# Elle v2 — auditoria 24h pós-correção (atenção)

Gerado: 20260627T132813Z

## Resumo

- Processados: 45
- v2 used/skipped/error: 13/15/0
- eval_bad: 4
- eval médio/alto: 1
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 12

## Issues

- qualidade ainda tem eval_bad=4 e risco médio/alto=1
- autonomy gate continua HOLD

## Exemplos de risco sanitizados

- conv=2362 msg=56927 quality=bad risk=low issue=misinterpreted_intent expected=None
- conv=2381 msg=57720 quality=bad risk=low issue=irrelevant_response expected=None
- conv=2389 msg=58034 quality=bad risk=low issue=inappropriate_response expected=None
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
    "events_total": 3074,
    "processed": 45,
    "response_evaluated": 45,
    "eval_bad": 4,
    "eval_medium_high": 1,
    "v2_used": 13,
    "v2_skipped": 15,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 13,
    "decision_llm_final": 5,
    "decision_guardrail_after_llm": 27,
    "stock_handoff": 6,
    "human_handoff": 18,
    "product_clear": 11
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
    "events_total": 3074,
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
