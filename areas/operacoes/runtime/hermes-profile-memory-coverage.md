# Hermes profile memory coverage

Atualizado: 2026-06-09T00:00Z UTC

## Regra canônica

Todo agente/profile Hermes que tiver `memories/MEMORY.md` e/ou `memories/USER.md` deve estar coberto pela higiene diária de memória.

- Boot memory = índice mínimo injetado no prompt.
- Memória rica = Brain, dailies, hot, reports, skills, context files e session history.
- Se boot memory passa de 85% do limite e existe template seguro, o watchdog deve compactar automaticamente com backup antes de alertar Lucas.
- Telegram só deve receber alerta se houver risco/falha/decisão real: arquivo ausente relevante, over-limit, secret locator, provider externo indevido ou impossibilidade de compactar com segurança.

## Cobertura atual do watchdog

Script: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`

Profiles com arquivos de memória e cobertura de template:

- `brain-process` — coberto.
- `hermes-ops-readonly` — coberto.
- `lk-analyst-readonly` — coberto.
- `lk-collection-optimizer` — coberto; agente permanente independente `[LK] Otimização de Coleções`, não subagente de Growth/Shopify.
- `lk-content` — coberto; conteúdo/CRM/Klaviyo/editorial LK, sem envio/publicação externa sem aprovação escopada.
- `lk-content-reviewer` — coberto.
- `lk-growth` — coberto.
- `lk-ops` — coberto.
- `lk-shopify` — coberto.
- `lk-stock` — coberto; fonte viva Tiny para estoque/pronta entrega/availability, sem dado inventado.
- `lk-trends` — coberto.
- `mordomo` — coberto.
- `spiti` — coberto.

Profile existente sem arquivos de boot memory no momento:

- `lc-claude-cli` — profile existe, mas `memories/MEMORY.md` e `memories/USER.md` não existem; não entra no compactor até existir boot memory.

## Estado após Fase 1 Memory OS v1 — 2026-06-09

- `lk-content` e `lk-stock` adicionados à cobertura por template.
- Próxima verificação esperada: `coverage_missing_for_existing_memory=[]` em `reports/memory-hygiene/latest.json` após execução manual do watchdog.
- Verificação 2026-06-09: `latest.json.status=ok`, `template_coverage_missing_count=0`, `over_limit_count=0`, `near_saturation_count=0`.
- Qualquer compactação deve manter backup local e não tocar runtime, provider, cron, Docker/VPS ou sistemas externos.

## Estado após compactação geral 2026-06-06

- `brain-process`: MEMORY 21.9%, USER 19.3%.
- `hermes-ops-readonly`: MEMORY 19.8%, USER 16.4%.
- `lk-analyst-readonly`: MEMORY 19.0%, USER 14.9%.
- `lk-collection-optimizer`: MEMORY 27.3%, USER 18.4%.
- `lk-content-reviewer`: MEMORY 18.2%, USER 14.7%.
- `lk-growth`: MEMORY 26.4%, USER 15.4%.
- `lk-ops`: MEMORY 40.1%, USER 56.6%.
- `lk-shopify`: MEMORY 44.2%, USER 52.6%.
- `lk-trends`: MEMORY 19.1%, USER 14.8%.
- `mordomo`: MEMORY 43.8%, USER 43.7%.
- `spiti`: MEMORY 25.0%, USER 13.7%.

## Backups

Compactação geral de 2026-06-06:

- Manifest: `reports/governance/memory-backups/20260606T112954Z-all-agents-boot-compact/manifest.json`

Compactação inicial Mordomo da Mesa COO:

- `memories/backups/auto-compact/MEMORY.md.20260606T111757Z.before`
- `memories/backups/auto-compact/USER.md.20260606T111757Z.before`

## Verificação exigida

Ao alterar esta cobertura ou templates:

1. Rodar `python3 -m py_compile /opt/data/scripts/hermes_memory_hygiene_watchdog.py`.
2. Rodar o watchdog manualmente.
3. Confirmar `coverage_missing_for_existing_memory=[]` no bloco `auto_template_coverage` de `reports/memory-hygiene/latest.json`.
4. Confirmar `reports/memory-hygiene/latest.json` com `status=ok` ou explicar alertas.
5. Rodar focused secret scan nos arquivos alterados/receipts.
6. Rodar Brain health check.
7. Salvar receipt em `reports/governance/receipts/`.

## Lição registrada

A falha da Mesa COO 2026-06-06 não foi a detecção: o cron detectou. O erro foi a cobertura parcial de auto-compaction. A regra correta é cobertura por roster: todo profile/agente com boot memory deve estar no compactor, não apenas os profiles que já tiveram incidente anterior.

## Reauditoria Bruno 2026-06-06

Relatório: `reports/governance/02h15-memory-lkgoc-watchdog-bruno-reaudit-2026-06-06.md`.

Conclusão: o 02h15 está certo como watchdog/receipt local, mas não deve ser tratado como agente de operação. Bruno recomenda que o 02h seja o supervisor de auto-melhoria que consome receipts, enquanto o 02h30 só resume decisões/exceções. O receipt agora expõe cobertura de templates por roster para impedir novo ponto cego.

Além disso, `[LK] Otimização de Coleções` precisa ser tratado como especialista vivo quando autorizado a responder: memória/documentação não basta. O watchdog global de gateways foi atualizado para supervisionar `lk-collection-optimizer` como managed local gateway com API/webhook off.
