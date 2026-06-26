# Patch Plan — LKGOC Zero-Base Superpowers v2

Data UTC: 20260606T180811Z
Status: **DRAFT — depende das respostas de Lucas**

## Objetivo

Transformar o PRD em regra operacional canônica do LKGOC.

## Patches propostos

1. Criar regra `REGRA-LKGOC-PRD-ANTES-DE-REBUILD.md`.
2. Atualizar `AGENTS.md` com Gate -2 PRD obrigatório.
3. Atualizar `playbooks/full-lkgoc-rebuild.md` com fluxo v2 completo.
4. Atualizar Skill Superpowers com workers obrigatórios e veto documentado.
5. Atualizar QA checklist com status finais:
   - `FAIL_NO_PRD`
   - `FAIL_NO_QUESTIONS`
   - `FAIL_VISUAL_CONTRACT_204L`
   - `PASS_204L_VISUAL_CONTRACT`
6. Criar template `lkgoc-prd-template.md`.
7. Criar template `lkgoc-worker-verdicts-template.md`.
8. Criar template `lkgoc-side-by-side-qa-template.md`.
9. Fazer rollback/zero-base da Puma DEV atual ou sobrescrever com snapshot, conforme resposta de Lucas.
10. Rebuild Puma do zero a partir do shell 204L.

## Não executar ainda

- Não escrever Production.
- Não fazer merge.
- Não declarar PASS sem side-by-side.
- Não reconstruir Puma antes das respostas bloqueantes.
