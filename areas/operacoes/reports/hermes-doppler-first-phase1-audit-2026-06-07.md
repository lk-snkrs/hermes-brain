# Relatório — Doppler-first Fase 1/2 auditoria read-only

Data: 2026-06-07

Escopo aprovado: auditoria read-only + helper universal; sem restart, sem Docker/VPS, sem copiar valores de secrets, sem escrita externa.

## Resultado executivo

- `values_printed`: `False`
- `writes_performed_external`: `False`
- `runtime_restarts`: `False`
- `docker_vps_changes`: `False`
- Doppler API download: `True`
- Doppler CLI: `v3.76.0`
- Token source: `file`, file mode OK: `True`
- Secret count em `lc-keys/prd`: `272`
- Perfis auditados: `14`
- Perfis com todos os secrets esperados presentes: `14`
- Perfis com algum secret esperado ausente: `0`
- Perfis sem skill comum Doppler: `2`
- Perfis sem menção Doppler em docs de identidade raiz: `13`
- Perfis com evidência antiga de cron sem token Doppler: `1`

## Helper universal criado/validado

Arquivo: `/opt/data/scripts/hermes_doppler.py`

Comandos validados:
- `doctor` — conectividade sanitizada, `values_printed=false`.
- `exists` — presença/ausência por nome, sem valor.
- `inventory --profile ... --verbose` — matriz por perfil com booleans, sem valor.
- `run` — preparado para executar comando com env Doppler via processo, não usado nesta auditoria para escrever nada.

Também atualizei o mapa não-secreto `/opt/data/hermes_bruno_ingest/doppler_map.md` para apontar para o helper universal.

## Matriz por perfil

### brain-process
- Path: `/opt/data/profiles/brain-process`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `33`
- Expected secrets: `3`; present: `3`; missing: `0`

### default
- Path: `/opt/data`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `161`
- Expected secrets: `6`; present: `6`; missing: `0`

### hermes-ops-readonly
- Path: `/opt/data/profiles/hermes-ops-readonly`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `33`
- Expected secrets: `5`; present: `5`; missing: `0`

### lc-claude-cli
- Path: `/opt/data/profiles/lc-claude-cli`
- Common Doppler skill: `False`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `0`
- Expected secrets: `2`; present: `2`; missing: `0`

### lk-analyst-readonly
- Path: `/opt/data/profiles/lk-analyst-readonly`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `33`
- Expected secrets: `6`; present: `6`; missing: `0`

### lk-collection-optimizer
- Path: `/opt/data/profiles/lk-collection-optimizer`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `122`
- Expected secrets: `5`; present: `5`; missing: `0`

### lk-content
- Path: `/opt/data/profiles/lk-content`
- Common Doppler skill: `False`
- Identity docs with Doppler mention: `MEMORY.md`
- Skill files with Doppler mention: `2`
- Expected secrets: `6`; present: `6`; missing: `0`
- Known cron outputs with Doppler token-missing evidence:
  - `cron/output/e8db49cf916e/2026-06-07_14-49-04.md`

### lk-content-reviewer
- Path: `/opt/data/profiles/lk-content-reviewer`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `33`
- Expected secrets: `4`; present: `4`; missing: `0`

### lk-growth
- Path: `/opt/data/profiles/lk-growth`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `122`
- Expected secrets: `9`; present: `9`; missing: `0`

### lk-ops
- Path: `/opt/data/profiles/lk-ops`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `153`
- Expected secrets: `8`; present: `8`; missing: `0`

### lk-shopify
- Path: `/opt/data/profiles/lk-shopify`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `124`
- Expected secrets: `6`; present: `6`; missing: `0`

### lk-trends
- Path: `/opt/data/profiles/lk-trends`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `120`
- Expected secrets: `6`; present: `6`; missing: `0`

### mordomo
- Path: `/opt/data/profiles/mordomo`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `123`
- Expected secrets: `6`; present: `6`; missing: `0`

### spiti
- Path: `/opt/data/profiles/spiti`
- Common Doppler skill: `True`
- Identity docs with Doppler mention: `none`
- Skill files with Doppler mention: `117`
- Expected secrets: `5`; present: `5`; missing: `0`

## Lacunas de Fase 3 candidatas

- Instalar/replicar skill comum Doppler: `lc-claude-cli, lk-content`
- Adicionar seção Doppler-first em docs raiz/AGENTS: `brain-process, default, hermes-ops-readonly, lc-claude-cli, lk-analyst-readonly, lk-collection-optimizer, lk-content-reviewer, lk-growth, lk-ops, lk-shopify, lk-trends, mordomo, spiti`
- Revisar crons com histórico de token missing: `lk-content`

## Próxima etapa

Fase 3 deve ser proposta como patch local em skills/AGENTS por perfil, ainda sem restart e sem valores de secrets. Runtime/env/launcher só com nova aprovação escopada.
