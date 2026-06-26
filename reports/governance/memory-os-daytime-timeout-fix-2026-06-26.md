# Fix — Memory OS daytime checker timeout

Data UTC: 2026-06-26T11:32Z

## Veredito

Erro corrigido. O job `Hermes Memory OS daytime checker/router — 30min alert-only` (`bc96bb03d2b0`) voltou para `last_status=ok` em execução manual/cron.

## Sintoma

O cron estava com:

- `last_status=error`
- causa: `subprocess.TimeoutExpired`
- comando interno: `hermes_memory_os_daytime_checker.py --json --since-minutes 240 --adoption-auto-heal-limit 10`
- timeout: 240s

## Root cause

O checker tinha lógica de auto-size em `recommended_adoption_auto_heal_limit()`: mesmo quando o wrapper pedia `--adoption-auto-heal-limit 10` (ou menor), se havia backlog de adoption gaps ele elevava o lote para `gap_count` inteiro, até 250.

Isso é seguro como rotina governada/manual, mas perigoso no loop daytime de 30min sob timeout do wrapper: um backlog de hooks/writer pode exceder 240s e fazer o wrapper terminar com traceback bruto e `last_status=error`.

Durante a investigação, o linter mostrava 27 gaps. Um run manual do checker curou esses 27 gaps, mas a causa arquitetural permanecia: o daytime loop podia voltar a expandir lote automaticamente e estourar o timeout.

## Correção aplicada localmente

Backups:

```text
/opt/data/backups/memory-os-timeout-fix-20260626T113214Z/
```

Arquivos alterados:

```text
/opt/data/scripts/hermes_memory_os_daytime_checker.py
/opt/data/scripts/hermes_memory_os_daytime_alerting_watchdog.py
```

Mudanças:

1. `recommended_adoption_auto_heal_limit()` agora respeita o limite pedido por padrão.
2. Auto-size grande só fica habilitado quando `HERMES_MEMORY_OS_AUTOSIZE_ADOPTION_AUTOHEAL=1` estiver setado explicitamente para run manual/governado.
3. O wrapper passou a capturar `subprocess.TimeoutExpired` e emitir alerta sanitizado sem traceback bruto, retornando `rc=0` para preservar contrato de watchdog local/actionable.

## Verificação

Comandos/evidências:

- `py_compile` dos dois scripts: OK.
- Regressão da função de limite:
  - sem env: `gap_count=27`, requested `1` → `1`; requested `10` → `10`.
  - com env `HERMES_MEMORY_OS_AUTOSIZE_ADOPTION_AUTOHEAL=1`: requested `1` → `27`.
- `hermes_memory_os_daytime_checker.py --json --since-minutes 240 --adoption-auto-heal-limit 10`: OK.
- `hermes_memory_os_daytime_alerting_watchdog.py`: `rc=0`, stdout vazio, stderr vazio.
- Cron manual `bc96bb03d2b0`: `last_status=ok`, `last_run_at=2026-06-26T11:32:57Z`, `last_error=null`.
- Brain health: OK.
- Strict-runtime guard: `fail_count=0`.
- Focused secret scan nos scripts: `secret_literal_hits=0`, `values_printed=false`.

## Estado atual dos crons relacionados

- Brain Sync `3fc45b0830c6`: OK.
- Strict-runtime guard `d9badcd83411`: OK.
- Memory OS daytime `bc96bb03d2b0`: OK.

## Não-ações

- Nenhum cron schedule/delivery/prompt foi alterado.
- Nenhum Docker/VPS/Traefik/gateway/runtime sensível foi alterado.
- Nenhum Shopify/Tiny/sistema externo foi alterado.
- Nenhum secret foi impresso.

## Pendência / follow-up

Os scripts corrigidos vivem em `/opt/data/scripts` e não entram no Brain Sync allowlist. A correção foi documentada neste report e no receipt. Se quisermos versionar runtime scripts em repo canônico no futuro, isso deve virar uma frente separada de governança de scripts.
