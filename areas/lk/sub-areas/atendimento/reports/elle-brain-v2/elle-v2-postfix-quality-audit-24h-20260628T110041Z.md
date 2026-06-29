# Elle v2 — auditoria 24h pós-correção (atenção)

Gerado: 20260628T110041Z

## Resumo

- Processados: 21
- v2 used/skipped/error: 8/13/0
- eval_bad: 2
- eval médio/alto: 1
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 13

## Issues

- qualidade ainda tem eval_bad=2 e risco médio/alto=1
- autonomy gate continua HOLD

## Exemplos de risco sanitizados

- conv=2393 msg=58143 quality=bad risk=medium issue=misclassification expected=None
- conv=2408 msg=58681 quality=bad risk=low issue=ignored_request expected=None

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
    "events_total": 2184,
    "processed": 21,
    "response_evaluated": 21,
    "eval_bad": 2,
    "eval_medium_high": 1,
    "v2_used": 8,
    "v2_skipped": 13,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 8,
    "decision_llm_final": 1,
    "decision_guardrail_after_llm": 12,
    "stock_handoff": 1,
    "human_handoff": 12,
    "product_clear": 5
  },
  "autofix_counts": {
    "autofix_regression_drafts": 13,
    "autofix_patch_suggestions": 13,
    "regression_candidates": 18,
    "eval_risk_candidates": 6
  },
  "autonomy_gate": {
    "status": "hold",
    "scope": "autonomy_expansion_gate",
    "window_hours": 24.0,
    "events_total": 2184,
    "processed": 21,
    "v2_canary_used": 8,
    "v2_canary_skipped": 13,
    "v2_canary_error": 0,
    "ai_provider_error": 0,
    "eval_bad": 2,
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
