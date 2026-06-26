# Receipt — correção de fluxo LKGOC: descrição de coleção

Data: 2026-06-15T15:00:51.720862+00:00

Correção aplicada após feedback do Lucas sobre descrição fraca da coleção Salomon XT-6.

Arquivos alterados/criados:
- Criado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-DESCRICAO-COLECAO-QUALITY-GATE-20260615.md`
- Atualizado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/full-lkgoc-rebuild.md`
- Atualizado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/REGRA-LKGOC-TEXTOS-E-SELECAO-DE-IMAGENS.md`

Novo gate:
- Todo LKGOC exige Description Packet antes de write Shopify.
- Descrição genérica bloqueia status de LKGOC.
- Placeholder pode existir apenas marcado como bloqueado, sem publish/approval.

Status: FLOW_PATCHED_LOCAL_BRAIN
