# Elle Brain v2 — canonicalização, regression candidates e gate de autonomia

**Data:** 2026-06-26  
**Pedido:** “fazer do 1 ao 4” após a recomendação: reconciliar runtime/fonte canônica, garantir aprendizado→regressão, medir v2 e só expandir autonomia se qualidade confirmar.  
**values_printed:** false

## 1. Runtime/fonte canônica reconciliados

Problema encontrado:

```text
check_drift.sh: status=fail reason=source_runtime_drift image=elle-chatwoot:canonical-20260623
```

Causa:

- `check_drift.sh` compara `/opt/elle-chatwoot/app/app.py` com runtime `/app/app.py`;
- runtime e `/opt/elle-chatwoot/app.py` estavam atualizados;
- `/opt/elle-chatwoot/app/app.py` estava antigo;
- Dockerfile canônico não copiava `elle_brain_v2.py`.

Correção:

- `/opt/elle-chatwoot/app/app.py` sincronizado com runtime atual;
- `/opt/elle-chatwoot/app/elle_brain_v2.py` criado/sincronizado;
- Dockerfile atualizado para copiar `app/elle_brain_v2.py`;
- não recriado o container porque `docker-compose.yml` não declara envs e recriar poderia perder runtime env/secrets.

Validação:

```text
status=ok image=elle-chatwoot:canonical-20260623 compose=/opt/elle-chatwoot/docker-compose.yml workdir=/opt/elle-chatwoot values_printed=false
```

## 2. Aprendizado vira regression candidates

Criado script:

```text
/opt/elle-chatwoot/scripts/export_v2_regression_candidates.py
/app/scripts/export_v2_regression_candidates.py
```

Função:

- lê lessons e avaliações;
- gera `/data/supervised_learning/regression_candidates.jsonl`;
- sanitiza shape;
- não salva raw PII;
- não autoaplica em produção;
- marca `auto_apply=false` e `candidate_pending_review`.

Resultado inicial:

```json
{
  "status": "ok",
  "mode": "v2_regression_candidate_export",
  "lessons_seen": 14,
  "evaluations_candidate_seen": 10,
  "candidates_added": 14,
  "candidates_total": 14,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

Learner wrapper agora também reporta regression candidates:

```json
{
  "status": "ok",
  "mode": "v2_supervised_learning_health",
  "lessons_total": 14,
  "evaluations_total": 10,
  "v2_lessons_loaded": 8,
  "v2_context_probe_ok": true,
  "regression_candidates_total": 14,
  "regression_candidates_added": 0,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

## 3. Medição v2 contínua

Verificador OpenRouter 1h atualizado e validado:

```text
✅ Elle OpenRouter 1h: OK
processed=9 | openrouter=9 | v2_used=3 | v2_skipped=5 | v2_errors=0 | provider_errors=0
values_printed=false
```

Observer remoto agora mostra:

```text
- v2/canary status: elle_brain_v2_canary_skipped: 5, elle_brain_v2_canary_used: 3
- decision_source processed: rule_guardrail_after_llm: 34, llm_final: 7, elle_brain_v2_canary: 3
- ai_used processed: False: 34, True: 10
- valid_json processed: False: 24, True: 20
- v2 autonomy gate: hold (eval_bad=5, eval_medium_high=1, handoff_violations=0)
```

## 4. Gate de autonomia por qualidade

Criado script:

```text
/opt/elle-chatwoot/scripts/check_v2_autonomy_gate.py
/app/scripts/check_v2_autonomy_gate.py
```

Resultado 24h:

```json
{
  "status": "hold",
  "scope": "autonomy_expansion_gate",
  "processed": 44,
  "v2_canary_used": 3,
  "v2_canary_skipped": 5,
  "v2_canary_error": 0,
  "ai_provider_error": 0,
  "eval_bad": 5,
  "eval_medium_high": 1,
  "handoff_violations": 0,
  "recommendation": "do_not_expand_autonomy",
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

Interpretação:

- v2/canary tecnicamente saudável: sem erro v2/provider e sem violação de handoff;
- **autonomia não deve ser expandida agora** porque o evaluator detectou qualidade ruim/risco em parte da janela;
- isso cumpre a regra: expandir só se relatórios confirmarem qualidade.

## Verificações finais

```text
check_drift.sh: OK
regression suite: 38 OK
learner smoke: OK
OpenRouter verifier: OK
v2 autonomy gate: HOLD por qualidade
```

## Backup / rollback

Backup:

```text
/opt/data/backups/elle-v2-canonical-learning-gates/20260626T194417Z
```

Rollback rápido de customer-facing v2:

```bash
docker exec elle-chatwoot sh -lc 'python3 - <<PY
import json
p="/data/elle_brain_v2_canary.json"
c=json.load(open(p)); c["enabled"]=False
open(p,"w").write(json.dumps(c, ensure_ascii=False, indent=2))
PY'
docker restart elle-chatwoot
```

Rollback completo: restaurar arquivos do backup acima.

## Próximo passo

Manter v2 em 100% safe-only, mas **não ampliar autonomia** até `v2 autonomy gate` sair de `hold` para `go_review_only` em uma janela operacional limpa.
