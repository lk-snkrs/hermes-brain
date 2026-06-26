# Receipt — compactação boot memory Mordomo

Data UTC: 2026-06-06T11:17:57Z

## Escopo aprovado

Lucas aprovou a Decisão 4/4 da Mesa COO: compactar boot memories do profile Mordomo antes de saturar.

## Diagnóstico do erro

O alerta da madrugada das 02h15 deveria ter sido evitado por auto-compaction se o Mordomo estivesse coberto pela regra de auto-compactação de especialistas.

Root cause confirmado: o script `/opt/data/scripts/hermes_memory_hygiene_watchdog.py` só tinha templates de auto-compaction para:

- default profile;
- `lk-ops`;
- `lk-shopify`.

Ele verificava `profiles/mordomo/memories/MEMORY.md` e `profiles/mordomo/memories/USER.md`, mas não tinha template autorizado para compactá-los. Resultado: reportou `attention` em vez de compactar automaticamente.

## Correção feita

- Adicionados templates boot-minimum do Mordomo ao `SPECIALIST_BOOT_TEMPLATES` do watchdog.
- Compactados arquivos locais:
  - `profiles/mordomo/memories/MEMORY.md`: 2156 → 963 chars.
  - `profiles/mordomo/memories/USER.md`: 1334 → 601 chars.
- Backups criados:
  - `memories/backups/auto-compact/MEMORY.md.20260606T111757Z.before`
  - `memories/backups/auto-compact/USER.md.20260606T111757Z.before`
- Atualizada a skill `hermes-brain-governance` para registrar que Mordomo também entra na cobertura aprovada.

## Verificação

- Watchdog manual: `rc=0`.
- `reports/memory-hygiene/latest.json` após a execução:
  - `status=ok`
  - `auto_compaction_count=2`
  - `near_saturation_count=0`
  - `over_limit_count=0`
  - `alert_count=0`
- Readback dos arquivos compactados OK.
- `py_compile` do watchdog: PASS.
- Focused secret scan: PASS.

## Não tocado

- Sem restart de gateway.
- Sem Docker/VPS/SSH/Traefik.
- Sem alteração de cron registry/schedule/delivery.
- Sem provider/memória externa/Mem0.
- Sem Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/envio externo.
