# Execução A+B — Hermes v0.17 delegated tests + crons Telegram

Data: 2026-06-22
Responsável: Hermes Geral/default
Status: A e B executados com backup, verificação e sem secrets impressos.

## Pedido

Lucas disse: “Fazer o A e o B”.

Interpretação aplicada:

- **A** = ativar delegated tests v0.17 nos perfis especialistas já configurados.
- **B** = hardening dos crons `deliver=origin` que ainda não tinham contrato Telegram/noise/actionability explícito.

## Escopo permitido pela aprovação

- Restart controlado dos perfis especialistas gerenciados para carregar configs de delegação.
- Patch de `prompt` dos crons `deliver=origin` detectados pelo sentinel como sem contrato explícito.
- Backups locais, readback, sentinel, Brain health, secret scan, receipt.

## Escopo não executado

- Não reiniciei Docker/VPS/Traefik/Main Hermes via infra.
- Não alterei cron schedule/delivery/enabled/state/script.
- Não ativei dashboard/API público.
- Não ativei WhatsApp Cloud, Photon/iMessage, Raft ou SimpleX.
- Não instalei MCP.
- Não troquei modelo default.
- Não fiz writes externos/prod.

## Backups

Run dir:

`/opt/data/backups/hermes-v017-A-B-20260622T132911Z`

Backups de cron registries:

`/opt/data/backups/hermes-v017-A-B-20260622T132911Z/cron-backups/`

Backups prévios das configs dos perfis já existiam em:

`/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`

## A — delegated tests ativado nos perfis gerenciados

Perfis reiniciados/controlados:

- `mordomo`
- `lk-growth`
- `spiti`
- `spiti-atendimento`
- `lk-ops`
- `lk-shopify`
- `lk-trends`
- `lk-collection-optimizer`
- `lk-stock`
- `lk-finance`
- `lk-content`

Resultado pós-restart:

- perfis checados: 11
- cada perfil com exatamente 1 gateway vivo
- todos com `gateway_state=running`
- todos com Telegram `connected`
- todos com API/webhook fechados (`false`)
- todos com token presente como booleano, sem imprimir valor
- watchdog global pós-restart: stdout `0`, stderr `0`

Observação operacional:

- `lk-ops` e `lk-stock` precisaram de SIGKILL após janela de drain; ambos voltaram saudáveis pelo watchdog com 1 PID vivo e Telegram conectado.

## B — hardening dos 13 crons `origin`

Foram patchados 13 jobs em 5 cron registries.

Mudança aplicada:

- prepend no `prompt` com contrato Telegram v0.17/actionability;
- sem mudar `schedule`, `deliver`, `enabled`, `state`, `script`, `no_agent` ou `repeat`.

Verificação:

- JSON parse errors: 0
- prompt_changed_jobs: 13
- jobs com diff fora de `prompt`: 0

## Sentinel final

Comando:

`python3 /opt/data/scripts/hermes_v017_adoption_sentinel.py --json`

Resumo:

- `status: ok`
- `profile_gap_count: 0`
- `origin_without_explicit_contract_count: 0`
- `scripts_delegated_done_count: 1`
- `values_printed=false`

## Default/main health

- API health local: `status=ok`, `version=0.17.0`
- Cron status: gateway running; 39 active jobs

## Brain health

Arquivo:

`reports/brain-health-check-2026-06-22-v017-A-B.json`

Resumo:

- secrets `FAIL=0/WARN=0`
- links `FAIL=0/WARN=0`
- required_files `FAIL=0/WARN=0`
- agent_files `FAIL=0/WARN=0`
- area_maps `FAIL=0/WARN=0`
- routines_index `FAIL=0/WARN=0`
- skill_references `FAIL=0/WARN=0`

## Secret scan

Escopo: 16 artefatos/backups relevantes da execução A+B.

Resultado:

- Telegram bot token pattern: 0
- private key: 0
- generic secret assignment: 0
- `values_printed=false`

## Rollback

### Rollback A

1. Restaurar configs dos perfis de:
   `/opt/data/backups/hermes-v017-system-audit-20260622T120610Z/config-backups/`
2. Reiniciar apenas os perfis afetados.
3. Rodar `hermes_all_gateway_watchdog.py` e verificar 1 PID por profile.

### Rollback B

1. Restaurar cron registries de:
   `/opt/data/backups/hermes-v017-A-B-20260622T132911Z/cron-backups/`
2. Validar JSON.
3. Rodar sentinel novamente.

## Tester review independente

Subagente tester read-only retornou **PASS**.

Resumo do tester:

- sentinel current/final `status=ok`, `findings=[]`, `values_printed=false`;
- 11 perfis gerenciados com 1 PID vivo, `HERMES_HOME` correto, `gateway_state=running`, Telegram `connected`, API/webhook `false`;
- 13 mudanças de prompt em cron registries; sem diff estático em `schedule`, `schedule_display`, `deliver`, `enabled`, `state`, `script` ou `no_agent`;
- Brain report coerente;
- secret scan em 23 arquivos relevantes: token Telegram `0`, private key `0`, generic secret assignment `0`.

Caveat do tester: metadados de runtime de cron podem mudar naturalmente enquanto o scheduler roda (`last_run_at`, `next_run_at`, `repeat.completed`, `last_status/last_error`); isso não foi tratado como regressão porque os campos estáticos protegidos permaneceram inalterados.

## Conclusão

A+B concluídos.

A v0.17 agora está mais próxima de “adotada no sistema”, não só instalada:

- delegated tests/background delegation preparados e runtime-active nos 11 perfis gerenciados;
- contratos Telegram v0.17 aplicados aos 13 crons que estavam sem contrato explícito;
- sentinel final/current verde (`status=ok`);
- tester independente retornou PASS.

`values_printed=false`
