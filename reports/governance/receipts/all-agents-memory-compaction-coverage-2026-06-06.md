# Receipt — compactação e cobertura de memória para todos os agentes

Data UTC: 2026-06-06T11:29Z

## Correção recebida de Lucas

Lucas corrigiu que a higiene de memória não deve cobrir só profiles específicos que já deram problema. Todo agente/profile com boot memory deve estar documentado e coberto pela rotina diária de compactação.

## Root cause

O watchdog `/opt/data/scripts/hermes_memory_hygiene_watchdog.py` tinha duas partes desalinhadas:

- varredura: checava todos os `profiles/*/memories/MEMORY.md` e `USER.md` existentes;
- auto-compaction: só tinha templates para default, `lk-ops`, `lk-shopify` e, após a Mesa COO 4/4, `mordomo`.

Isso criava cobertura parcial: o sistema detectava saturação de qualquer profile, mas só conseguia corrigir automaticamente alguns.

## Correção feita

1. Adicionados templates de boot-minimum ao watchdog para todos os profiles com arquivos de memória existentes:
   - `brain-process`
   - `hermes-ops-readonly`
   - `lk-analyst-readonly`
   - `lk-collection-optimizer`
   - `lk-content-reviewer`
   - `lk-growth`
   - `lk-ops`
   - `lk-shopify`
   - `lk-trends`
   - `mordomo`
   - `spiti`
2. Executada compactação/alinhamento geral one-time em todos os profiles com boot memory existente.
3. Corrigido conteúdo do `lk-collection-optimizer` para refletir ownership independente de `[LK] Otimização de Coleções`, não LK Growth.
4. Criada documentação canônica de cobertura:
   - `areas/operacoes/runtime/hermes-profile-memory-coverage.md`
5. Backups salvos em:
   - `reports/governance/memory-backups/20260606T112954Z-all-agents-boot-compact/manifest.json`

## Estado final por profile

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

Profile existente sem boot memory:

- `lc-claude-cli`: `MEMORY.md` e `USER.md` ausentes; documentado como fora do compactor até existir boot memory.

## Verificação

- Watchdog manual: `rc=0`.
- Cobertura: `coverage_missing_for_existing_memory=[]`.
- `reports/memory-hygiene/latest.json`: `status=ok`, `near_saturation_count=0`, `over_limit_count=0`, `alert_count=0`.

## Não tocado

- Sem restart de gateway.
- Sem Docker/VPS/SSH/Traefik.
- Sem alteração de cron registry/schedule/delivery.
- Sem provider/Mem0/memória externa.
- Sem Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/envio externo.
