# Bruno/OpenClaw gap closure follow-up — 2026-05-22

Status: **concluído em modo Brain/local/documental**.

## Objetivo

Após a auditoria Bruno/OpenClaw do Hermes Brain, fechar pendências seguras que não exigem aprovação externa:

1. Criar auditoria formal de skills com owner/status/risco/última revisão/verificação.
2. Criar ponte canônica mínima para Mordomo/Lucas pessoal.
3. Registrar backlog de revisão de ruído em watchdogs e one-shots pausados.
4. Verificar health, operating layer, diff, secret scan e Brain Sync safe dry-run.

## O que foi criado/alterado

### Skills

- `empresa/skills/status-risco-2026-05-22.md`
  - Baseline formal das skills canônicas.
  - Campos: owner, status, risco, última revisão, última verificação e observação.
- `empresa/skills/_index.md`
  - Adicionado link para o baseline de status/risco.

### Mordomo / Lucas pessoal

- `areas/operacoes/mordomo/MAPA.md`
  - Ponte canônica mínima para Mordomo sem mover arquivos históricos.
  - Define escopo, guardrails, arquivos atuais, crons relacionados e critério futuro para virar `agentes/mordomo/` ou `areas/lucas-pessoal/`.
- `areas/operacoes/MAPA.md`
  - Adicionado link para `mordomo/MAPA.md`.
- `MAPA.md`
  - Adicionado atalho global: Mordomo / Lucas pessoal.

### Ruído / jobs pausados

- `reports/governance/runtime-noise-and-paused-jobs-backlog-2026-05-22.md`
  - Backlog documental dos watchdogs `origin` que merecem revisão de ruído.
  - Backlog de one-shots pausados/antigos.
  - Nenhum cron foi alterado.

## Verificação final

Comandos executados em `/opt/data/hermes_bruno_ingest/hermes-brain`:

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-22-final-gap-closure.json`
  - Resultado: `FAIL=0`, `WARN=0`, `issues=0`.
- `python3 /opt/data/scripts/brain_operating_layer_audit.py`
  - Resultado: exit `0`, stdout vazio.
- `git diff --check`
  - Resultado: ok.
- Secret scan direcionado nos arquivos tocados:
  - Resultado: `0` hits.
- `python3 /opt/data/scripts/brain_sync_safe.py --dry-run > reports/brain-sync-safe-dry-run-2026-05-22-gap-closure.txt`
  - Resultado: `allowed_files=36`, `skipped_files=282`.
  - Interpretação: esperado; arquivos não allowlisted continuam bloqueados.

## Limites respeitados

Não houve:

- alteração de cron/schedule/delivery;
- Docker/VPS/gateway/Traefik/container/network;
- Shopify/GMC/API write;
- WhatsApp/e-mail/campanha/envio externo;
- mudança de secrets;
- deleção/arquivamento destrutivo.

## Próximos passos que exigem decisão ou rotina separada

1. Revisar delivery dos watchdogs `origin` um por um, com leitura do script e rollback.
2. Decidir se one-shots pausados antigos podem ser removidos/arquivados.
3. Se o volume do Mordomo continuar crescendo, aprovar criação de `agentes/mordomo/` ou `areas/lucas-pessoal/` como estrutura formal.
4. Automatizar auditoria mensal de skills contra o baseline de owner/status/risco.
