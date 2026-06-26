# Memory OS v1.17 — rollout profile-local do contrato Memory OS

Gerado: 2026-06-09T21:15:55.379287+00:00

## Pedido

Lucas respondeu `Seguir` após a recomendação de fazer rollout escopado do contrato Memory OS nos especialistas vivos, sem restart/runtime.

## Escopo executado

- Patch mínimo em `AGENTS.md` profile-local dos 9 especialistas vivos detectados.
- Backup timestamped antes de alterar cada profile-local instruction file.
- Nenhum restart, kill, gateway mutation, Docker/VPS/Traefik ou write externo.
- Nenhum segredo lido/impresso.

## Perfis alterados

- `lk-collection-optimizer` → `/opt/data/profiles/lk-collection-optimizer/AGENTS.md`
- `lk-content` → `/opt/data/profiles/lk-content/AGENTS.md`
- `lk-growth` → `/opt/data/profiles/lk-growth/AGENTS.md`
- `lk-ops` → `/opt/data/profiles/lk-ops/AGENTS.md`
- `lk-shopify` → `/opt/data/profiles/lk-shopify/AGENTS.md`
- `lk-stock` → `/opt/data/profiles/lk-stock/AGENTS.md`
- `lk-trends` → `/opt/data/profiles/lk-trends/AGENTS.md`
- `mordomo` → `/opt/data/profiles/mordomo/AGENTS.md`
- `spiti` → `/opt/data/profiles/spiti/AGENTS.md`

## Backup/Rollback

Backup root:

- `/opt/data/backups/memory-os-v117-profile-local-rollout/20260609T211502Z`

Rollback manual por perfil: restaurar o `AGENTS.md.bak` correspondente, ou remover `AGENTS.md` quando o marcador `.missing` indicar que o arquivo não existia antes.

## Contrato aplicado

Cada perfil recebeu regra mínima para:

- criar receipts novos via `/opt/data/scripts/hermes_memory_os_receipt_writer.py`;
- registrar receipts legados/existentes via `--register-existing` ou `hermes_memory_os_worker_receipt_guard.py`;
- usar `hermes_memory_os_event_hook.py` para handoffs e approval packets;
- manter `values_printed=false` para secrets;
- preservar Telegram silent-OK;
- bloquear writes sensíveis e restarts sem aprovação escopada, backup/rollback e verificação.

## Verificação profile-local

- Perfis verificados: `9`.
- Todos com contrato: `True`.
- Processos Hermes observados após patch: `43`.
- Bad rows: `0`.

## Não-ações

- Não reiniciei gateway/profile.
- Não matei processos.
- Não alterei crons.
- Não toquei Docker/VPS/Traefik.
- Não alterei Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/database.

## Próximo passo

Aguardar maturação real 21/21 ciclos. Se Lucas quiser, a próxima fronteira é uma auditoria read-only de pós-restart readiness ou ativação pública/Mission Control, ambas com aprovação própria.
