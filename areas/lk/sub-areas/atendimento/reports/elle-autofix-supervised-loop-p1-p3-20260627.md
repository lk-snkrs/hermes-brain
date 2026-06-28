# Elle — correção P1/P2/P3 + auto-fix supervisionado

Data: 2026-06-27
Escopo: corrigir erros qualitativos identificados na auditoria e implementar loop automático supervisionado `eval_bad/eval_medium_high → regression draft → patch suggestion → validação`, sem autoeditar produção sem gate.

## Mudanças

- Finalizado ajuste de objeção de preço com português imperfeito (`valor estar certo`, `tem lugares q`, `ela estar`).
- Corrigidos padrões na Elle Brain v2:
  - produto não relacionado em baixa confiança;
  - navegação segura não vira pós-venda;
  - localização/endereço;
  - objeção de preço/curadoria.
- Corrigida camada produtiva `app.py` com os mesmos guardrails leves.
- Criado `/app/scripts/elle_supervised_autofix_loop.py` no container.
- Integrado ao wrapper `/opt/elle-chatwoot/scripts/run_customer_correction_learner.sh`.
- Dockerfile atualizado para copiar o script ao runtime.
- Build/recreate Doppler-safe executado.

## Verificação

### Smokes produtivos classify-only

- `price_typo`: `product_clear`, sem handoff, resposta segura de valor/curadoria.
- `price_nb`: `product_clear`, sem handoff.
- `location`: `institutional`, sem handoff, endereço aprovado.
- `browse`: `product_clear`, sem pós-venda.
- `stock`: `stock_handoff`, handoff correto.

### Regressões v2

```json
{"ok": true, "tests": 42, "values_printed": false}
```

### Auto-fix loop

```json
{
  "status": "ok",
  "evaluations_seen": 12,
  "risk_evaluations_seen": 12,
  "regression_drafts_added": 12,
  "regression_drafts_total": 12,
  "patch_suggestions_added": 12,
  "patch_suggestions_total": 12,
  "auto_apply": false,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

### Learner wrapper

```json
{
  "status": "ok",
  "lessons_total": 15,
  "evaluations_total": 12,
  "v2_lessons_loaded": 8,
  "v2_context_probe_ok": true,
  "regression_candidates_total": 17,
  "eval_risk_candidates_total": 5,
  "writes_external": 0,
  "values_printed": false
}
```

### Drift / runtime

```text
status=ok image=elle-chatwoot:canonical-20260623 compose=/opt/elle-chatwoot/docker-compose.yml workdir=/opt/elle-chatwoot values_printed=false
```

Health:

```json
{
  "ok": true,
  "write_enabled": true,
  "kill_switch": false,
  "public_reply_enabled": true,
  "ai_enabled": true,
  "hmac_secret_present": true,
  "legacy_path_webhook_enabled": false,
  "elle_brain_v2_canary_enabled": true,
  "elle_brain_v2_canary_percent": 100,
  "values_printed": false
}
```

OpenRouter 1h:

```text
processed=5 | openrouter=5 | v2_used=3 | v2_skipped=2 | v2_errors=0 | provider_errors=0
values_printed=false
```

Autonomy gate:

```json
{
  "status": "hold",
  "processed": 46,
  "v2_canary_used": 13,
  "v2_canary_skipped": 15,
  "v2_canary_error": 0,
  "ai_provider_error": 0,
  "eval_bad": 4,
  "eval_medium_high": 1,
  "handoff_violations": 0,
  "recommendation": "do_not_expand_autonomy",
  "writes_external": 0,
  "values_printed": false
}
```

## Segurança

- Sem envio para cliente durante correção.
- Sem estoque/Tiny.
- Sem Shopify write.
- Sem secrets impressos.
- `auto_apply=false`: o loop gera drafts/suggestions e alimenta validação, mas não autoedita produção nem expande autonomia.

## Status

Correções aplicadas em produção safe-only. Auto-fix supervisionado criado e rodando junto ao learner. Autonomia ampla permanece HOLD corretamente.
