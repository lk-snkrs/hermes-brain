# LKGOC Config Audit — 20260627T164535Z

## Escopo
Auditoria local/read-only da configuração LKGOC no profile `lk-collection-optimizer`.

## Verificações executadas
- Skill local: `/opt/data/profiles/lk-collection-optimizer/skills/lk-superpowers-collection-optimizer/SKILL.md`
- Skill Brain: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md`
- Brain Collection Optimizer: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/`
- Canônicos LKGOC em `growth/LKGOC-*`
- Profile `AGENTS.md`, `SOUL.md`, `MAPA.md`, Task OS, Honcho, CLI/Doppler-first e Shopify policy
- Smoke: `/opt/data/home/.hermes/profiles/lk-collection-optimizer/scripts/lkgoc_boot_smoke.py`

## Evidência resumida
- `LKGOC_BOOT_SMOKE=PASS`
- Skill local existe: 15.543 bytes, sha256 prefix `cc856f5280ee0d86`
- Skill Brain existe: 29.587 bytes, sha256 prefix `d87d4c5a58f9e23d`
- `growth/` contém 12 arquivos top-level `LKGOC-*`
- `collection-optimizer/` contém 0 arquivos top-level `LKGOC-*`
- `collection-optimizer/` possui OS estruturado: MAPA, AGENTS, SOUL, work, receipts, approval-packets, qa, impact-reviews, rules, standards, templates

## Status executivo
Configuração funcional e identidade correta, mas não 100% limpa/canônica.

## Achados priorizados
1. P0 — Skill local diverge da skill Brain canônica apontada pelo README.
2. P0 — Canônicos principais `LKGOC-*` ainda vivem fisicamente em `growth/`, não no diretório dono `collection-optimizer/`.
3. P0 — Conflito documental: Contract Lock/DEV write vs regra mais nova de DEV/unpublished permitido e Production bloqueado.
4. P1 — Política Shopify GitHub-first/no Admin writes conflita com registros antigos de DEV Admin write/standing approval.
5. P1 — MAPA do collection-optimizer não indexa toda a suite LKGOC operacional: PRD, input, evidence, workflow, scorecard, ledger, QA standard.
6. P1 — Skill LKGOC não explicita dentro dela dois guardrails já presentes no profile: Shopify GraphQL via CLI oficial e estoque sempre via `lk-stock`.
7. P2 — Tags/paths com `lk-growth` podem causar drift de ownership, embora o hard lock do profile mitigue.
8. P2 — Índices de projeto/artefatos ainda têm ruído de scanner e precisam curadoria.
9. P2 — Namespaces antigos `lk-204l-*`/`lk-collection-v2` coexistem com regra nova `lk-goc-*`; precisa wording de compatibilidade.

## Recomendação
Executar uma normalização local em três blocos:
1. Canon/índice: criar `collection-optimizer/canon/INDEX.md` ou espelhar `LKGOC-*` para o diretório dono.
2. Regras: consolidar DEV/unpublished, Contract Lock, GitHub-first/Admin writes e Production approval em uma única precedência.
3. Skill: atualizar skill local para ser wrapper canônico ou cópia sincronizada da Brain skill, adicionando CLI oficial Shopify e handoff `lk-stock`.

## Writes externos
Nenhum.

## Writes locais
Este report foi salvo em Brain local.

## Approval necessário
Não para correções locais/Brain/skill. Necessário apenas se a próxima etapa tocar Shopify, produção, secrets, deploy, VPS ou writes externos.
