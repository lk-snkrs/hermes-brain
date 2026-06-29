# Elle v2 — auditoria 24h pós-correção (ok)

Gerado: 20260628T133503Z

## Resumo

- Processados: 17
- v2 used/skipped/error: 5/12/0
- eval_bad: 1 (resolvidos: 1; não resolvidos: 0)
- eval médio/alto: 0 (resolvidos: 0; não resolvidos: 0)
- provider_error: 0
- autonomy_gate: hold
- auto-fix drafts: 13

## Issues

- Nenhum issue acionável automático.

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
    "events_total": 1956,
    "processed": 17,
    "response_evaluated": 17,
    "eval_bad": 1,
    "eval_medium_high": 0,
    "eval_bad_resolved": 1,
    "eval_medium_high_resolved": 0,
    "eval_bad_unresolved": 0,
    "eval_medium_high_unresolved": 0,
    "v2_used": 5,
    "v2_skipped": 12,
    "v2_error": 0,
    "provider_error": 0,
    "handoff_violations": 0,
    "decision_elle_v2": 5,
    "decision_llm_final": 0,
    "decision_guardrail_after_llm": 12,
    "stock_handoff": 1,
    "human_handoff": 11,
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
    "events_total": 1956,
    "processed": 17,
    "v2_canary_used": 5,
    "v2_canary_skipped": 12,
    "v2_canary_error": 0,
    "ai_provider_error": 0,
    "eval_bad": 1,
    "eval_medium_high": 0,
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
