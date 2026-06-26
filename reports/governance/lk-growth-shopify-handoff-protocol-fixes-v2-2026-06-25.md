# LK Growth ↔ LK Shopify handoff protocol fixes v2 — 2026-06-25

## Pedido

Lucas pediu “melhor 1 2 e 3” após a primeira correção dos três pontos do incidente `t_ae530570`.

## Melhorias aplicadas

### 1. Status guard melhorado

Script:

```text
/opt/data/scripts/hermes_kanban_task_status_guard.py
```

Melhorias v2:

- adiciona `recommended_report`;
- adiciona `human_summary`;
- decodifica payload JSON de eventos;
- permite teste com `HERMES_KANBAN_ROOTS`;
- mantém detecção de status stale quando houve `gave_up` histórico seguido por retry/complete.

Verificação real no caso `t_ae530570`:

```text
ok=true
status=done
latest_run=18 completed
stale_blocked_report_risk=true
recommended_report=report_done_with_latest_summary_and_receipt
values_printed=false
```

### 2. Worker readiness melhorado

Script:

```text
/opt/data/scripts/hermes_kanban_worker_readiness.py
```

Melhorias v2:

- respeita `HERMES_BIN` para teste/portabilidade;
- verifica skill por CLI e filesystem;
- adiciona `--deep-skill-load-check`, que roda um smoke read-only `hermes chat --ignore-rules --skills ...` para provar que o preload da skill funciona;
- retorna `deep_skill_load_check` com `rc`, `skill_preload_error` e `stdout_contains_ready`, sem secrets.

Verificação real no `lk-shopify`:

```text
ok=true
skills_found.kanban-worker=true
deep_skill_load_check.rc=0
deep_skill_load_check.skill_preload_error=false
values_printed=false
```

### 3. Preservação de evidência virou ferramenta

Novo script:

```text
/opt/data/scripts/hermes_kanban_preserve_evidence.py
```

Função:

- copia evidências finais para diretório durável;
- valida JSON antes de copiar;
- gera `manifest.json` com bytes + sha256;
- falha se arquivo esperado estiver ausente, salvo `--allow-missing`;
- não lê secrets nem faz API call.

Rodado no caso `t_ae530570`; nova evidência durável:

```text
areas/lk/sub-areas/shopify/evidence/adidas-samba-marrom-guarded-20260625T193435Z/
```

## Testes adicionados

```text
/opt/data/scripts/test_kanban_handoff_guards.py
```

Cobertura:

- status guard detecta `gave_up` histórico seguido por `completed` e recomenda reportar done;
- evidence preserve copia JSON e escreve manifest;
- readiness script expõe `--deep-skill-load-check` e respeita configuração de binário.

Resultado:

```text
Ran 3 tests in 0.234s
OK
```

## Verificação final

- `py_compile`: OK para os 3 scripts.
- Testes unitários: 3/3 OK.
- Status guard real `t_ae530570`: OK.
- Readiness deep real `lk-shopify`: OK.
- Evidence preserve real: OK.
- Brain health: `FAIL=0 WARN=0`.
- Secret scan escopado: `high_confidence_secret_hits=0`.

## Writes externos

Nenhum. Apenas scripts locais, Brain docs/evidence/receipts e skill docs.

## Próximo passo opcional

Integrar estes scripts diretamente ao dispatcher Kanban para bloquear spawn de business task quando readiness falhar. Isso seria patch runtime + testes + restart controlado, não foi feito nesta etapa.
