# Configured vs Active Scorecard

Status: rotina local/read-only v0.1
Criado em: 2026-06-10T14:13:27Z

## Objetivo

Separar o que está documentado/configurado do que está ativo e verificado no runtime vivo.

## Entidades

- profile
- gateway process
- platform/Telegram
- provider/model
- toolsets/MCP
- cron registry
- watchdog
- dashboard/API/webhook exposure
- Brain docs/owner

## Estados

- `documented`: aparece em Brain/skill/PRD.
- `configured`: existe em config/env/registry local.
- `active`: há processo/cron/gateway vivo ou estado local atual.
- `verified`: prova fresca por health, log, readback ou round-trip proporcional.
- `stale_or_conflicting`: docs e runtime divergem.

## Fontes read-only

- `hermes status` / wrapper sanitizado.
- `hermes cron list --all` / registry local quando tool bloqueado.
- `/proc/<pid>/environ` com booleans, sem secrets.
- `gateway_state.json`.
- Brain reports: Runtime Truth Reconciler, Memory OS, receipts.
- `hermes prompt-size --platform telegram --json`.

## Saída recomendada

Um relatório local por dia com:

- profiles vivos vs preparados/parados;
- cron active/paused/non-ok;
- watchdog silent-OK/anômalo;
- model configured vs provider ativo;
- toolset Telegram vs CLI;
- docs drift;
- ações locais seguras;
- ações que requerem aprovação.

## Guardrails

- Não imprimir previews de API keys/tokens.
- Não reiniciar nada.
- Não mudar cron delivery.
- Não testar round-trip externo sem aprovação quando gerar mensagem.
