# Runtime Truth Reconciler — 2026-05-24

Timestamp UTC: 2026-05-24 11:21

## Escopo

Reconciliação read-only entre evidência viva do scheduler Hermes e a documentação do Hermes Brain.

## Fonte viva usada

- Comando preferido `cronjob list`: indisponível neste container/runtime (`cronjob` não está no PATH).
- Fallback canônico usado com sucesso: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

## Sumário da evidência viva

- Total de jobs listados: 23.
- Ativos: 23.
- Pausados/disabled listados: 0.
- `last_status` não-ok: 0.
- Erros explícitos de delivery na listagem: 0.
- Jobs ativos sem `Last run`: 1.

## Jobs ativos sem `Last run`

- `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) — ativo, delivery `origin`, semanal; primeira execução esperada em 2026-05-25 12:15 UTC.

## Delivery observado

### `origin` sem erro explícito

- `LK Daily Sales Brief read-only mandatory delivery` (`7c688553e293`).
- `LK Weekly CEO Review read-only mandatory delivery` (`953b9055458e`).
- `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`).
- `Mesa COO diária Telegram` (`749ee30b51eb`).
- `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`).
- `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`).

### `local` confirmado para watchdogs/silent-OK

- `Hermes runtime + cron watchdog no_agent` (`edd06fe19397`).
- `Hermes compression failure self-heal watchdog` (`4bb4e2223fd3`).
- `LK WhatsApp Hermes responder watchdog` (`71b2636add5d`).
- `Mordomo Telegram gateway watchdog` (`ac0b440e2643`).
- `LK Growth Telegram gateway watchdog` (`876d54c62ccd`).
- `SPITI Telegram gateway watchdog` (`663e3e6a148c`).
- `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`).
- `Hermes Brain Runtime Truth Reconciler` (`2404c0766d33`).
- `LK WhatsApp Hermes responder regression watchdog` (`a5d7a392eed9`).
- `Hermes Brain strict-runtime guard watchdog` (`d9badcd83411`).

## Drift / gaps documentais

1. Contagem viva se manteve igual ao snapshot de 2026-05-23/05:01: `23 ativos / 0 pausados listados`; snapshots mais antigos com jobs pausados devem continuar tratados como histórico até nova evidência viva.
2. `Lucas Brain weekly Learning Loop report` continua ativo sem primeira execução registrada; acompanhar após 2026-05-25 12:15 UTC.
3. Seções antigas do inventário ainda citam alguns watchdogs como `origin`; a evidência viva atual confirma `local` para runtime+cron, compression self-heal, Mordomo, LK Growth, SPITI, Operating Layer, strict-runtime guard e responder regression. A nova seção datada do inventário deve ser tratada como fonte viva mais recente.
4. Jobs com `origin` listados acima não apresentam erro; qualquer redução de ruído/delivery deve continuar exigindo aprovação explícita de Lucas e não foi feita neste reconciliador.

## Verificação

- Health check executado: `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-24-runtime-truth-reconciler.json`.
- Resultado: `All checks passed` (`FAIL=0 / WARN=0`).
- Secret scan escopado aos 3 arquivos tocados: `possible_secrets 0`.
- `git diff --check` escopado aos arquivos tocados: sem problemas.

## Não alterado

Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, container, rede, sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email, banco ou secret foi alterado.
