# Brain/GMC governance approved package — final report 2026-05-22

## Veredito

Pacote aprovado por Lucas executado. O Brain ficou com guardrail ampliado, scripts legados neutralizados, skill LK corrigida, crons pausados/orfãos removidos e evidência final verde.

## Escopo executado

- GMC: mantido em modo governado/read-only; nenhuma escrita externa no GMC/Content API nesta etapa.
- Brain docs/runtime local: saneamento local em `/opt/data/hermes_bruno_ingest/hermes-brain/`.
- Scheduler: removidos somente os 5 jobs que já estavam pausados/orfãos, com aprovação explícita; jobs ativos não foram pausados/removidos.
- Docker/VPS/containers/volumes/redes/Traefik: não tocados.
- WhatsApp/email/Shopify/Tiny/Crisp/externos: sem mutação nesta etapa.

## Mudanças principais

1. `scripts/operational_docs_guard.py`
   - Adicionado modo `--strict-runtime` para varrer root docs, `skills/`, `scripts/`, executáveis `.py/.sh` e relatórios de governança.
   - Guard passou a diferenciar instrução viva perigosa de evidência histórica/scanners/redaction regex.

2. Scripts legados neutralizados como stubs inertes `DEPRECATED / DO NOT RUN`
   - `monitor_daemon.py`
   - `alert_system.py`
   - `scripts/hermes_consolidation_weekly.py`
   - `scripts/session_end_summary.py`

3. Skill LK corrigida
   - `skills/lk-crosssell/SKILL.md`: removida referência operacional a `/root/lk-price/`; fonte operacional agora exige caminho/runtime atual verificado.

4. Docs históricos marcados
   - `lessons.md`
   - `areas/operacoes/rotinas/hermes-runtime-update-attempt-2026-05-05.md`
   - `reports/governance/hermes-brain-runtime-docs-audit-2026-05-22.md`

5. Crons pausados/orfãos removidos
   - `c214051f7780` — LK weekly influencer sales email
   - `15777e3416dc` — LK SEO/CRO weekly Claude SEO improvement loop
   - `4ced266825f0` — Mordomo WhatsApp pessoal resumo 17h BRT
   - `051f05ce17c1` — Mordomo WhatsApp pessoal realtime scan
   - `a7e883edd200` — LK SEO/CRO impact review — SEO title/meta P1 packets

6. Brain Sync skipped artifacts classificados
   - Criado `reports/governance/brain-sync-skipped-artifact-classification-2026-05-22.md`.

## Evidência final

### Brain health

```text
secrets: FAIL=0 WARN=0
links: FAIL=0 WARN=0
required_files: FAIL=0 WARN=0
agent_files: FAIL=0 WARN=0
area_maps: FAIL=0 WARN=0
decisions_index: FAIL=0 WARN=0
routines_index: FAIL=0 WARN=0
skill_references: FAIL=0 WARN=0

All checks passed.
```

### Operational docs guard — default

- Mode: `default-docs`
- Scanned files: `180`
- Fail count: `0`

### Operational docs guard — strict runtime

- Mode: `strict-runtime`
- Scanned files: `1059`
- Fail count: `0`

### Brain Sync safe dry-run

- Branch: `consolidation/brain-filesystem-git-hygiene-20260516`
- Allowed files: `78`
- Skipped files: `306`
- External sync/push: não executado; dry-run apenas.

### Secret scan focado

- Files scanned: `11`
- Fail count: `0`

### Cron registry após remoções

- Live scheduler confirmado após remoções: 22 jobs.
- Scheduled/ativos: 22.
- Pausados/orfãos: 0.

## Política resultante

- Recriar qualquer job removido somente com rotina `.md`, owner, fonte, delivery, kill criteria e approval packet novo.
- Scripts continuam locais e fora do Brain Sync por design, salvo revisão explícita.
- Relatórios/raw JSON/receipts gerados ficam locais ou são resumidos em `.md` durável quando útil.
- Guard default continua rápido para docs vivos; `--strict-runtime` vira gate para auditoria profunda.

## Pendências não bloqueantes

- Consolidar o relatório Telegram 02h30 com Mesa COO se continuarem duplicando decisões.
- Promover para allowlist apenas relatórios de governança realmente duráveis; não versionar scripts/runtime cru por impulso.
