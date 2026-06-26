# Kanban Task OS — all-readiness activation follow-up — 2026-06-25

## Pedido

Lucas pediu “fazer TUDO” sobre a integração direta dos guards no Task OS / Kanban dispatcher.

## O que faltava depois da primeira integração

A integração direta no dispatcher estava em disco e ativa nos dispatchers LK reiniciados, mas havia dois gaps práticos:

1. **Skill preload universal** — vários profiles não conseguiam carregar `kanban-worker` com `--skills kanban-worker`.
2. **Stale block no goal-mode fallback** — o caminho de fallback do goal-mode em `cli.py` bloqueava sem `expected_run_id`, deixando uma rota teórica para block stale se uma tentativa antiga tentasse fechar uma tentativa nova.

## Correções executadas

### 1. `kanban-worker` visível para todos os profiles relevantes

Criei symlinks de profile para o skill global:

```text
/opt/data/skills/devops/kanban-worker
```

Profiles verificados com preflight OK:

| Profile | Preflight `kanban-worker` |
|---|---|
| default | OK |
| mordomo | OK |
| spiti | OK |
| spiti-atendimento | OK |
| lk-growth | OK |
| lk-ops | OK |
| lk-collection-optimizer | OK |
| lk-stock | OK |
| lk-finance | OK |
| lk-content | OK |
| lk-shopify | OK |
| lk-trends | OK |
| hermes-ops-readonly | OK |
| lk-analyst-readonly | OK |
| lk-content-reviewer | OK |
| brain-process | OK |
| lc-claude-cli | OK |

Resultado final:

```text
all_ok=true
values_printed=false
```

### 2. Corrigida colisão de skill no `lk-shopify`

Problema encontrado pelo novo preflight:

```text
Skill name collision for 'kanban-worker'
```

Causa: arquivo arquivado dentro de outro skill:

```text
/opt/data/profiles/lk-shopify/skills/devops/kanban-workflows/references/kanban-worker.md
```

Correção:

```text
references/kanban-worker.md → references/archived-kanban-worker-source.md
```

E frontmatter arquivado deixou de declarar `name: kanban-worker`.

### 3. Guard anti-stale no goal-mode fallback

Patch no runtime ativo:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/cli.py
```

Antes:

```python
_kb.block_task(c, task_id, reason=reason)
```

Depois:

```python
_kb.block_task(..., expected_run_id=HERMES_KANBAN_RUN_ID)
```

Se o run estiver stale, o block é recusado e logado, em vez de mutar o card novo.

## O que já estava ativo antes e foi mantido

- `dispatch_once()` com `worker_readiness_fn`.
- `_default_worker_readiness_preflight()` antes de `claim_task()`/spawn real.
- `DispatchResult.readiness_blocked`.
- LK dispatchers com `dispatch_in_gateway=true` reiniciados após patch:
  - `lk-growth`
  - `lk-ops`
  - `lk-collection-optimizer`
  - `lk-stock`
  - `lk-finance`
  - `lk-content`

## Verificação final

### Testes runtime/source

```text
4 passed
```

Cobriu:

- stale run não completa tentativa nova;
- stale run não bloqueia/heartbeat tentativa nova;
- dispatcher bloqueia readiness failure antes de spawn;
- dispatcher spawna quando readiness OK.

### Scripts de guard de handoff

```text
Ran 3 tests
OK
```

Cobriu:

- status guard anti-stale;
- readiness helper;
- preservação de evidência durável.

### Compile

```text
py_compile OK
```

Arquivos:

- `hermes_cli/kanban_db.py`
- `cli.py`
- `tools/kanban_tools.py`

### Health

```text
Kanban diagnostics: 0
Brain health: FAIL=0 WARN=0
Main API health: ok
Webhook health: ok
secret scan: 0 high-confidence hits
```

## Limite honesto: Main/default

O Main/default PID 1 **não foi self-restarted** neste turno.

Motivo: ele é o gateway foreground do container atual. Sinalizar/reiniciar PID 1 daqui poderia derrubar a sessão Telegram/container antes da confirmação final. Isso é um limite operacional real, não falta de patch.

Estado Main:

- código patchado em disco;
- API health OK;
- webhook health OK;
- `kanban-worker` preload OK para `default`;
- novo dispatcher será carregado no próximo restart seguro do Main/container.

## Writes externos

0.

Sem Shopify/Tiny/GMC/Klaviyo/WhatsApp/email. Sem secrets impressos. Sem Docker/VPS/Traefik.

## Backups

```text
/opt/data/backups/kanban-dispatcher-readiness-integration-20260625T194726Z/
/opt/data/backups/kanban-dispatcher-readiness-integration-runtime-20260625T195152Z/
/opt/data/backups/kanban-cli-stale-block-guard-20260625T200247Z/
/opt/data/backups/lk-shopify-kanban-worker-skill-collision-20260625T200509Z/
/opt/data/backups/kanban-worker-skill-propagation-20260625T200720Z/
```

## Veredito

Tudo que era seguro executar **sem derrubar o Main PID 1** foi feito:

- dispatcher endurecido;
- workers conseguem carregar `kanban-worker` em todos os profiles relevantes;
- stale completion/block/heartbeat protegido por run id;
- evidência e tests registrados;
- LK dispatchers ativos carregaram patch;
- Main fica preparado para ativação no próximo restart seguro.
