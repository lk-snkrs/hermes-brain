# Receipt — Daily Intelligence auto-heal lk-stock watchdog — 2026-06-09

Escopo: A1 local watchdog/source parity.

Mudança aplicada:
- `/opt/data/scripts/hermes_runtime_cron_watchdog.py`: adicionou `/opt/data/profiles/lk-stock` a `REQUIRED_GATEWAY_HOMES`.
- `areas/operacoes/scripts/hermes_runtime_cron_watchdog.py`: espelho Brain atualizado.

Motivo: `hermes_all_gateway_watchdog.py` já gerencia `lk-stock`, e o preflight confirmou o perfil ativo; o runtime watchdog ainda alertava HERMES_HOME inesperado.

Verificação:
- `py_compile`: ok.
- execução manual do runtime watchdog: `rc=0`, stdout vazio.

Rollback:
- remover as duas linhas de `lk-stock` dos dois arquivos alterados se Lucas desativar esse perfil e mover o perfil para estado dormant.

Bloqueios respeitados:
- nenhum Docker/VPS/gateway restart;
- nenhuma alteração de cron registry;
- nenhum write externo/source-of-truth;
- nenhum secret impresso ou persistido.

values_printed=false
