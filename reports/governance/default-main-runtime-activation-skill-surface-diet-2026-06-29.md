# Default/Main runtime activation — Skill Surface Diet

Data: 2026-06-29T15:47–15:49 UTC

## Escopo

Ativar em runtime a Skill Surface Diet já configurada no `default` / Hermes Geral.

## Comportamento observado

- A execução foi feita por runner detached para não depender do subprocess da sessão ativa.
- O comando retornou `rc=1` por race/already-running, mas o log vivo confirma parada planejada, drain/interrupção do agente ativo e startup subsequente do gateway default.
- O gateway principal voltou em polling mode, webhook/API conectados e Telegram conectado.

## Evidência runtime

- Log: `Received SIGTERM as a planned gateway stop` às 15:47:04.
- Log: `Starting Hermes Gateway` às 15:48:29.
- Log: `Telegram menu: 30 commands registered, 72 hidden` às 15:48:31 — evidência de superfície reduzida ativa.
- Log: `Connected to Telegram (polling mode)` às 15:48:31.
- Local API health: `http://127.0.0.1:8642/health` → HTTP 200, version `0.17.0`.
- Config default: `_config_version=30`, `skills.platform_disabled.telegram=150`.

## Roster pós-ativação

Especialistas esperados preservados com API/webhook fechados:

- `lk-growth`
- `lk-ops`
- `lk-shopify`
- `lk-trends`
- `lk-collection-optimizer`
- `lk-stock`
- `mordomo`
- `spiti`
- `spiti-atendimento`
- `lk-finance`
- `lk-content`
- `lc-claude-cli`

## Caveat

O comando retornou não-zero por race de PID 1/already-running, mas a validação viva mostrou que o default efetivamente parou, iniciou novamente e está saudável. Não foi usado Docker/VPS/Traefik/compose.

## Arquivos de evidência

Run dir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/runtime/default-restart-skill-surface-diet-20260629T154618Z/`

Contém:

- `pre_roster.json`
- `restart_command.txt`
- `restart_output.json`
- `post_state.json`
- `DONE`

## Rollback

Se a dieta do default precisar ser revertida, restaurar `/opt/data/config.yaml` do backup `/opt/data/hermes_bruno_ingest/hermes-brain/areas/operacoes/backups/skill-surface-diet-default-20260629T153033Z/config.yaml.before` e repetir ativação controlada do default/Main. Para rollback runtime sem mudança de config, repetir ativação controlada e validar health/Telegram/roster.
