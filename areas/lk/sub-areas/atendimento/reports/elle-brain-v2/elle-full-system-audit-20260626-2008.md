# Elle — auditoria completa de runtime, crons, scripts e coerência operacional

**Data:** 2026-06-26 20:08 UTC  
**Escopo:** auditoria read-only do sistema Elle/Chatwoot/Elle Brain v2, crons, scripts, logs, learner, observabilidade e guardrails.  
**Sem alteração em produção nesta auditoria.**  
**values_printed:** false

## Veredito executivo

**Não está 100%.**  
O runtime está saudável e a Elle Brain v2 está ativa em **100% safe-only**, mas o sistema como um todo não deve ser considerado 100% porque o gate de autonomia está em **HOLD** por qualidade e há gaps operacionais de infraestrutura/limpeza.

Classificação atual:

| Camada | Status |
|---|---|
| Container/runtime | OK |
| Health endpoint | OK |
| Drift fonte/runtime | OK |
| Elle Brain v2 safe-only | OK, 100% elegível |
| OpenRouter 1h | OK |
| Regression suite | OK, 38 testes |
| Learner | OK |
| Observer/relatórios v2-aware | OK |
| Lifecycle Chatwoot | OK |
| Autonomia ampla | **HOLD** |
| Compose/env reprodutível | **Gap** |
| Qualidade 24h | **Atenção** |

## 1. Runtime Elle

Container:

```text
elle-chatwoot elle-chatwoot:canonical-20260623 Up 32 minutes
```

Health endpoint:

```json
{
  "ok": true,
  "dry_run": false,
  "write_enabled": true,
  "kill_switch": false,
  "public_reply_enabled": true,
  "ai_enabled": true,
  "ai_provider": "openrouter",
  "ai_model": "deepseek/deepseek-v4-pro",
  "elle_brain_v2_canary_enabled": true,
  "elle_brain_v2_canary_percent": 100,
  "values_printed": false
}
```

Canary config:

```json
{
  "exists": true,
  "enabled": true,
  "percent": 100,
  "legacy_handoff_guard": true,
  "scope": "100_percent_safe_non_handoff_only",
  "values_printed": false
}
```

Drift:

```text
status=ok image=elle-chatwoot:canonical-20260623 compose=/opt/elle-chatwoot/docker-compose.yml workdir=/opt/elle-chatwoot values_printed=false
```

## 2. Testes / learner / autonomia

Regression suite:

```json
{"ok": true, "tests": 38, "values_printed": false}
```

Learner:

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
  "lessons_added": 0,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

Autonomy gate 24h:

```json
{
  "status": "hold",
  "processed": 45,
  "v2_canary_used": 4,
  "v2_canary_skipped": 7,
  "v2_canary_error": 0,
  "ai_provider_error": 0,
  "eval_bad": 4,
  "eval_medium_high": 1,
  "handoff_violations": 0,
  "recommendation": "do_not_expand_autonomy",
  "values_printed": false
}
```

Interpretação: a v2 está tecnicamente saudável, sem erro provider/canary e sem violação de handoff, mas o avaliador ainda detecta respostas ruins/risco na janela. Portanto **não expandir autonomia**.

## 3. Logs 24h

Resumo observer 24h:

```text
- eventos totais no log: 2671
- processed: 45
- v2/canary status: elle_brain_v2_canary_skipped: 7, elle_brain_v2_canary_used: 4
- decision_source processed: rule_guardrail_after_llm: 34, llm_final: 7, elle_brain_v2_canary: 4
- ai_used processed: False: 34, True: 11
- valid_json processed: False: 25, True: 20
- v2 autonomy gate: hold (eval_bad=4, eval_medium_high=1, handoff_violations=0)
```

Categorias processadas 24h:

```json
[
  ["human_handoff", 19],
  ["product_clear", 12],
  ["stock_handoff", 7],
  ["greeting", 5],
  ["coupon", 2],
  ["institutional", 1]
]
```

Nota: `valid_json=false` aparece muito porque vários casos vencem por guardrail determinístico após probe, não necessariamente erro OpenRouter; ainda assim o relatório diferencia `decision_source`.

## 4. OpenRouter / v2 1h

Verificador 1h:

```text
✅ Elle OpenRouter 1h: OK
processed=11 | openrouter=11 | v2_used=4 | v2_skipped=7 | v2_errors=0 | provider_errors=0
values_printed=false
```

## 5. Crons e scripts

Crons Elle/Chatwoot encontrados:

| Job | Enabled | Deliver | Último status | Leitura |
|---|---:|---|---|---|
| LK Elle atendimento diário seg-sex 17h10 | true | local | ok | faz sentido; relatório local/silencioso |
| LK Elle atendimento diário sábado 17h10 | true | local | ok | faz sentido |
| LK Elle semanal sábado 17h00 | false | origin | n/a | desativado; manter arquivado ou remover depois |
| Domingo teste 1 semana | false | origin | ok | stale/desativado; candidato a arquivar |
| Revisão trial 2026-06-21 | false | origin | n/a | stale; candidato a arquivar |
| Elle 07h últimas 24h | true | origin | ok | faz sentido; alerta executivo |
| Chatwoot lifecycle exception 17h03 | true | origin | ok | faz sentido; cobre lifecycle, não Elle v2 |
| Elle learner 15min | true | local | ok | faz sentido; agora v2-aware |

Scripts Elle compilam:

```text
compile_ok=true
```

Scripts relevantes:

- `lk_elle_atendimento_morning_24h.py` — v2-aware.
- `lk_elle_atendimento_observer_report.py` — usa log correto `/opt/elle-chatwoot/logs/events.jsonl`.
- `lk_elle_conversion_monitor.py` — ainda não está plenamente v2-attribution-aware; usa log correto, mas precisa atribuir conversão por `decision_source`.
- `lk_elle_customer_correction_learner.py` — OK; wrapper v2-aware.
- `lk_elle_openrouter_1h_verification.py` — OK; v2-aware.
- `lk_chatwoot_lifecycle_exception_monitor.py` — OK para lifecycle.

## 6. Lifecycle Chatwoot

Último monitor lifecycle:

```text
Status: ok
order_created: total=11, entregues/lidas=11, failed=0, blank=0
approved: total=11, entregues/lidas=11, failed=0, blank=0
delivered: total=9, entregues/lidas=8, sent=1, failed=0, blank=0
Blank content 48h: 0
Sem ação necessária.
```

## 7. Gaps / riscos atuais

### P0 — nenhum bloqueio crítico imediato

Não há erro v2, provider error, drift, container down ou falha lifecycle atual.

### P1 — autonomia ainda não pode ampliar

Autonomy gate em HOLD:

- `eval_bad=4`;
- `eval_medium_high=1`;
- recomendação automática: `do_not_expand_autonomy`.

Manter v2 em 100% safe-only, sem aumentar autonomia.

### P1 — compose/env não é plenamente reprodutível

`docker-compose.yml` não tem `environment:` nem `env_file:` mas o container depende de envs runtime:

```text
CHATWOOT_*, ELLE_*, OPENROUTER_API_KEY, PORT
```

Isso explica por que a decisão anterior foi não recriar o container. Para ficar 100%, precisa plano de canonicalização env/Doppler sem imprimir secrets.

### P2 — jobs desativados/stale

Existem jobs desativados de trial/review antigos. Não quebram nada, mas poluem a governança:

- `lk-elle-daily-sunday-trial`
- `lk-elle-daily-trial-review-20260621`
- weekly sábado desativado

### P2 — conversion monitor ainda não atribui bem por v2

`lk_elle_conversion_monitor.py` existe e faz sentido, mas deve ganhar separação por:

- `decision_source=elle_brain_v2_canary`;
- `llm_final`;
- humano;
- handoff/stock.

### P2 — observer tag noise

O observer mostra tags estranhas como `a`, `o`, `e`, `r`, `_`. Isso sugere parsing/contagem de tag string como iterável em algum ponto. Não parece quebrar decisão, mas suja relatório.

## Conclusão

**O sistema está operacional e bem melhor, mas não está 100%.**

Estado correto para comunicar:

- Elle Brain v2 está ativa em **100% safe-only**.
- Runtime, drift, OpenRouter, learner, lifecycle e testes estão OK.
- Crons principais fazem sentido e estão OK.
- Não expandir autonomia porque o gate de qualidade está em HOLD.
- Antes de dizer “100%”, corrigir/env canonical, limpar stale crons, ajustar conversion attribution e limpar tag noise.

## Recomendações

1. **Manter v2 100% safe-only** — não rollback.
2. **Não expandir autonomia** até gate limpo.
3. **P1:** criar plano Doppler/env canonical para compose/recreate seguro.
4. **P2:** arquivar jobs stale/desativados depois de aprovação.
5. **P2:** atualizar conversion monitor para atribuição v2/humano/handoff.
6. **P2:** corrigir tag noise do observer.
7. **P2:** revisar amostras `eval_bad` e `eval_medium_high` para criar lessons/regressions específicas.
