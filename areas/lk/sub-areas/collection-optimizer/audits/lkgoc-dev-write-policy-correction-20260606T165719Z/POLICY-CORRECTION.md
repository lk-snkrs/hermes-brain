# LKGOC DEV Write Policy Correction — 20260606T165719Z

## Status

**PASS**

## Correção recebida de Lucas

O Contract Lock não deve bloquear write em tema DEV. Write em DEV/unpublished é sempre liberado para construir, testar, previewar e fazer QA.

O Contract/approval é gate para write direto em Production/main, promoção, merge ou qualquer mudança customer-facing.

## Política atualizada

- DEV/unpublished: write liberado para build/preview/QA.
- DEV com placeholder/asset pendente: permitido, desde que marcado.
- Production/main: bloqueado sem Contract/approval explícito.
- Falta de asset lifestyle: bloqueia Production, não bloqueia DEV.

## Arquivos atualizados

- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/templates/lkgoc-contract-lock-template.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md

## Checks

- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md — DEV write liberado
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/templates/lkgoc-contract-lock-template.md — DEV sempre permitido
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md — Contract não bloqueia DEV
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md — DEV-first sempre liberado
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md — DEV write permitido
