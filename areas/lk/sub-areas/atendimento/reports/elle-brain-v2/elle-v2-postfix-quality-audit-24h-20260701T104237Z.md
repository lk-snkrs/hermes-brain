# Elle v2 — auditoria 24h pós-correção (atenção)

Gerado: 20260701T104237Z

## Resumo

- Processados: 36
- v2 used/skipped/error: 3/33/0
- eval_bad: 3 (resolvidos: 0; não resolvidos: 3)
- eval médio/alto: 3 (resolvidos: 0; não resolvidos: 3)
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 20

## Issues

- qualidade ainda tem eval_bad_unresolved=3 e risco médio/alto unresolved=3
- autonomy gate continua HOLD por issue não resolvido

## Exemplos de risco sanitizados

- conv=1673 msg=59296 quality=bad risk=high issue=possible_availability_promise expected=None
- conv=2451 msg=59356 quality=bad risk=low issue=context_loss expected=None
- conv=2451 msg=59361 quality=bad risk=high issue=possible_availability_promise expected=None
- conv=1481 msg=28625 quality=ok risk=medium issue=context_incomplete expected=None

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
    "events_total": 2350,
    "processed": 36,
    "response_evaluated": 36,
    "eval_bad": 3,
    "eval_medium_high": 3,
    "eval_bad_resolved": 0,
    "eval_medium_high_resolved": 0,
    "eval_bad_unresolved": 3,
    "eval_medium_high_unresolved": 3,
    "v2_used": 3,
    "v2_skipped": 33,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 3,
    "decision_llm_final": 1,
    "decision_guardrail_after_llm": 32,
    "stock_handoff": 6,
    "human_handoff": 21,
    "product_clear": 8
  },
  "autofix_counts": {
    "autofix_regression_drafts": 20,
    "autofix_patch_suggestions": 20,
    "regression_candidates": 22,
    "eval_risk_candidates": 10
  },
  "autonomy_gate": {
    "status": "hold",
    "scope": "autonomy_expansion_gate",
    "window_hours": 24.0,
    "events_total": 2350,
    "processed": 36,
    "v2_canary_used": 3,
    "v2_canary_skipped": 33,
    "v2_canary_error": 0,
    "ai_provider_error": 0,
    "eval_bad": 3,
    "eval_medium_high": 3,
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
