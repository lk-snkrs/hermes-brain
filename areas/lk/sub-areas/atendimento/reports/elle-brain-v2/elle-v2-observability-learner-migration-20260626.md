# Elle Brain v2 — migração de observabilidade + learner

**Data:** 2026-06-26  
**Escopo:** migrar observabilidade e learner para semântica Elle Brain v2 / canary 100% safe-only.  
**Sem envio manual a cliente.**  
**values_printed:** false

## O que foi migrado

### 1. Elle Brain v2 consome supervised lessons

Patch em `/app/elle_brain_v2.py`:

- adicionada função `load_recent_supervised_lessons()`;
- `decide_shadow()` e `decide_live_shadow()` agora passam `supervised_lessons` para `build_context()` quando não fornecido explicitamente;
- loader sanitiza shape e não retorna raw customer text/secrets;
- regression suite aumentada de 36 para 38 testes.

Verificação:

```json
{"ok": true, "tests": 38, "values_printed": false}
```

### 2. Observer remoto agora é v2-aware

Patch em `/opt/elle-chatwoot/elle_observer_summary.py` no VPS:

- adiciona `v2/canary status`;
- adiciona `decision_source processed`;
- adiciona `ai_used processed`;
- adiciona `valid_json processed`;
- cria seção `## Elle Brain v2 / canary`.

Smoke 24h usando caminho real `/opt/elle-chatwoot/logs/events.jsonl`:

```text
v2/canary status: elle_brain_v2_canary_skipped: 4, elle_brain_v2_canary_used: 2
decision_source processed: rule_guardrail_after_llm: 33, llm_final: 7, elle_brain_v2_canary: 2
```

### 3. Relatório 07h passa a destacar v2/canary

Patch em `lk_elle_atendimento_morning_24h.py`:

- parseia `elle_brain_v2_canary_used/skipped/error`;
- adiciona leitura executiva quando v2 assumiu decisões;
- alerta se houver canary error;
- inclui `v2/canary status` e `decision_source processed` nos sinais rápidos.

### 4. Learner cron corrigido

Causa da falha anterior:

- cron `lk-elle-customer-correction-learner` chamava `/opt/elle-chatwoot/scripts/run_customer_correction_learner.sh`;
- wrapper não existia no VPS.

Correção:

- criado `/opt/elle-chatwoot/scripts/run_customer_correction_learner.sh` local e no VPS;
- wrapper roda dentro do container `elle-chatwoot` com `PYTHONPATH=/app`;
- valida lessons/evaluations e se v2 carrega lessons;
- não envia cliente e não escreve sistemas externos.

Smoke do learner:

```json
{
  "status": "ok",
  "mode": "v2_supervised_learning_health",
  "lessons_total": 14,
  "evaluations_total": 10,
  "v2_lessons_loaded": 8,
  "v2_context_probe_ok": true,
  "lessons_added": 0,
  "customer_send_executed": false,
  "writes_external": 0,
  "values_printed": false
}
```

### 5. Verificador OpenRouter 1h ajustado para semântica v2

Patch em `lk_elle_openrouter_1h_verification.py`:

- adiciona contadores v2 canary used/skipped/error;
- adiciona `elle_brain_v2_canary_decision_source`;
- separa `legacy_openrouter_full_coverage` de health v2;
- smoke aceita guardrail correto em casos de risco, sem exigir que todos sejam `llm_final`.

Resultado do smoke:

- `traffic_ok=true`;
- `live_smoke.ok=true`;
- `elle_brain_v2_canary_used=2`;
- `elle_brain_v2_canary_skipped=4`;
- `elle_brain_v2_canary_error=0`.

## Bloqueio/dívida restante

`/opt/elle-chatwoot/scripts/check_drift.sh` ainda retorna:

```text
status=fail reason=source_runtime_drift image=elle-chatwoot:canonical-20260623
```

Leitura: runtime atual difere da imagem canônica após os patches v2/canary. Isso não impede o runtime, mas impede dizer que a fonte canônica/docker image foi reconciliada.

## Backups

Backup principal:

`/opt/data/backups/elle-v2-observability-learner/20260626T193108Z`

## Segurança

- `customer_send_executed=false` nos smokes;
- `writes_external=0` nos smokes de learner;
- sem Shopify/Tiny/stock writes;
- secrets não impressos;
- `values_printed=false`.

## Próximo passo recomendado

1. Rodar próximo cron learner naturalmente; o último status no `jobs.json` só será limpo no próximo tick.
2. Monitorar relatório 07h seguinte para confirmar métricas v2/canary.
3. Reconciliar source/runtime drift criando imagem/canonicalização do estado atual, com backup/rollback, antes de declarar a plataforma totalmente higienizada.
