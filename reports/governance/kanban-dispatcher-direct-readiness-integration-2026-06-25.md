# Kanban dispatcher direct readiness integration — 2026-06-25

## Resposta curta

Sim, isso é diretamente relacionado ao **Hermes Task OS**.

O Task OS é a política/processo; o Kanban nativo é o mecanismo de execução; o dispatcher é a peça que transforma card `ready + assignee` em worker real. Integrar o guard no dispatcher significa endurecer o coração do Task OS, não apenas um script auxiliar.

## O que foi integrado diretamente

Arquivo runtime ativo:

```text
/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/hermes_cli/kanban_db.py
```

Arquivo source também patchado para testes/regressão:

```text
/opt/hermes/hermes_cli/kanban_db.py
/opt/hermes/tests/hermes_cli/test_kanban_db.py
```

Mudanças:

1. `DispatchResult` ganhou:

```text
readiness_blocked: list[str]
```

2. `dispatch_once()` ganhou parâmetro testável:

```text
worker_readiness_fn=None
```

3. No modo real do dispatcher (`spawn_fn is None`), antes de `claim_task()` e antes de spawn, roda:

```text
_default_worker_readiness_preflight(task)
```

4. Se o worker não consegue carregar `kanban-worker` ou skills extras da task, o dispatcher agora:

- não faz spawn;
- não cria crash loop;
- bloqueia o card antes de executar;
- escreve razão `worker-readiness: ...`;
- registra o id em `DispatchResult.readiness_blocked`.

## Segurança do preflight

O preflight é local e sanitizado:

- não chama modelo;
- não faz write externo;
- não toca Shopify/Tiny/GMC/Klaviyo/WhatsApp/email;
- não imprime secrets;
- usa subprocess Python local com `HERMES_HOME` do profile alvo;
- chama `agent.skill_commands.build_preloaded_skills_prompt()` para validar preload de skills.

Emergency kill-switch:

```text
HERMES_KANBAN_WORKER_PREFLIGHT=0
```

## Testes e verificação

### Testes source

```text
4 passed
```

Inclui:

- `test_dispatch_worker_readiness_blocks_before_spawn`
- `test_dispatch_worker_readiness_success_spawns`
- regressões de spawn/promoção existentes

### Smoke ativo site-packages

Resultado:

```text
active_site_packages_behavior=ok
```

Provou que, no runtime importado por `/opt/hermes/.venv/bin/python`, uma readiness failure bloqueia card sem chamar spawn.

### Scripts auxiliares anteriores

```text
/opt/data/scripts/test_kanban_handoff_guards.py -v
Ran 3 tests
OK
```

### Health

```text
Kanban diagnostics: 0
Brain health: FAIL=0 WARN=0
Main API health: ok
values_printed=false
```

## Ativação runtime

Reiniciei os gateways LK com `kanban.dispatch_in_gateway=true` para eles carregarem o patch:

| Profile | Novo PID | API/Webhook |
|---|---:|---|
| lk-growth | 160733 | off/off |
| lk-ops | 160792 | off/off |
| lk-collection-optimizer | 160892 | off/off |
| lk-stock | 161049 | off/off |
| lk-finance | 161143 | off/off |
| lk-content | 161225 | off/off |

Todos os processos acima iniciaram depois do `kanban_db.py` patchado.

## Limite honesto

Main/default permaneceu vivo e saudável, mas não foi self-restarted dentro deste turno para não matar o gateway da conversa. Portanto:

- `lk-growth` e demais dispatchers LK com `dispatch_in_gateway=true`: patch ativo em runtime agora.
- Main/default: código patchado em disco e API saudável; dispatcher Main carrega no próximo restart seguro do Main/container.

## Writes externos

0. Sem Shopify/Tiny/GMC/Klaviyo/WhatsApp/email. Sem Docker/VPS/Traefik/secrets.

## Backup

```text
/opt/data/backups/kanban-dispatcher-readiness-integration-20260625T194726Z/
/opt/data/backups/kanban-dispatcher-readiness-integration-runtime-20260625T195152Z/
```
