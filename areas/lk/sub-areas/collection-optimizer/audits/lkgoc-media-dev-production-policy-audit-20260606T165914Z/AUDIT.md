# Audit — Correção LKGOC mídia editorial, DEV write e Production

Data: 20260606T165914Z
Status: **PASS**

## Correção solicitada por Lucas

1. O LKGOC deve sempre retirar/buscar as imagens principais dos principais veículos de moda, como Vogue, quando forem relevantes.
2. Todo write Shopify deve ser sempre no tema DEV/unpublished e não precisa de autorização de Lucas.
3. A autorização de Lucas é necessária para merge/promoção para Production.
4. Write direto no tema Production/main é extremamente proibido.

## O que estava errado

A documentação anterior misturava três coisas:

- asset/licença como bloqueio de DEV;
- Contract Lock como bloqueio de DEV;
- cautela sobre imagens editoriais como se elas não pudessem entrar no LKGOC.

Isso foi corrigido com uma regra canônica explícita.

## Nova regra canônica criada

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-MIDIA-DEV-PRODUCTION-POLICY.md`

## Arquivos reforçados

- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-HERO-PESSOAS-E-GUIA-PADRAO-BLOQUEANTE.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/templates/lkgoc-contract-lock-template.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md
- /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md

## Checks por arquivo

- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-MIDIA-DEV-PRODUCTION-POLICY.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-CONTRACT-LOCK-ANTES-DE-WRITE.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-HERO-PESSOAS-E-GUIA-PADRAO-BLOQUEANTE.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/templates/lkgoc-contract-lock-template.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md
- ✅ /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md

## Resultado operacional

- DEV/unpublished: write liberado sem autorização.
- Production/main: write direto proibido; abortar se `role: main`.
- Merge/promoção: só com aprovação explícita Lucas.
- Mídia: buscar/usar imagens principais editoriais dos veículos de moda relevantes; registrar fonte/URL no receipt.
