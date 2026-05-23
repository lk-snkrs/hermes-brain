---
name: brain-sync
description: DEPRECATED historical OpenClaw-era sync notes. Do not execute; use Hermes Brain safe allowlist sync and runtime cron records instead.
tags: [memory, brain, sync, deprecated]
---

# Brain Sync — legado / não executar

> **Status 2026-05-22:** arquivo preservado apenas como histórico. Não executar comandos antigos daqui.

## Fonte canônica atual

- Brain atual: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Runtime Hermes principal: `/opt/data` com perfis em `/opt/data/profiles/*`
- Credenciais: Doppler `lc-keys/prd`; nunca colocar senha/token em comando, arquivo ou log.
- Fechamento/sync atual: cron `Hermes Brain Fechamento Ágil 23h + Brain Sync` (`3fc45b0830c6`), com allowlist documental segura.

## Por que este arquivo foi desativado

A versão antiga citava paths legados de root, Mem0 e comandos de cópia SSH com senha inline. Isso não representa o runtime atual e cria risco operacional/segurança se copiado.

## Regra atual

1. Para saber se uma rotina roda, verificar `cronjob list` e o script real.
2. Para consolidar documentação, usar o fluxo do Brain com allowlist (`reports/brain-sync-safe-dry-run-*` como evidência) e sem mover secrets/config/runtime sensível.
3. Para fatos duráveis, salvar em Brain/skill/ledger apropriado — não em arquivos locais soltos nem Mem0 legado.
4. Qualquer alteração em VPS/Docker/SSH/produção exige aprovação explícita de Lucas com backup/rollback.
