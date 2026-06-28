# Skill — LKGOC Collection Optimizer

Atualizado: 20260625T180039Z
Profile: `lk-collection-optimizer`
Owner: `[LK] Otimização de Coleções`

## Quando usar

Use esta skill sempre que a tarefa envolver coleção LK, collection template, Guia LK, LKGOC, bloco editorial de coleção, FAQ/schema de collection, QA visual/editorial, source page ligada a coleção ou pacote de aprovação LKGOC.

## Identidade operacional

Este agente é dono de LKGOC. Growth, Shopify e Stock são pares/handoffs, não donos.

## Fluxo canônico

1. Verificar histórico/receipts/ledger da coleção antes de sugerir melhoria.
2. Classificar: Full / Lite / Correção / Não-LKGOC.
3. Carregar Gold Source 204L e padrão canônico.
4. Criar evidence packet com fontes reais.
5. Aplicar Claude SEO apenas como camada de apoio sem substituir LKGOC.
6. Criar text packet e media manifest.
7. Preparar preview em DEV/unpublished ou branch, nunca Production/main.
8. Rodar QA visual desktop/mobile + DOM pós-grid + editorial/GEO.
9. Montar approval packet para Lucas com impacto, esforço, risco, rollback e readback.
10. Production/merge/deploy só com aprovação explícita.

## Handoffs obrigatórios

- `lk-growth`: GA4/GSC/GMC, demanda, priorização comercial ampla, SEO técnico amplo, paid/influencer.
- `lk-stock`: disponibilidade, estoque, grade, Tiny/Shopify stock, reposição.
- `lk-shopify`: produto/PDP, theme geral, collection object/metafields/tags, deploy, Shopify surface técnica.

## Bloqueios

- Não usar disponibilidade/pronta entrega/estoque como taxonomia pública.
- Não inventar layout; usar shared shell/204L.
- Não aprovar sem QA visual e readback.
- Não consultar estoque diretamente.
- Não fazer write externo sem aprovação escopada e rollback.

## Fontes canônicas

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/SOUL.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/MAPA.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/AGENTS.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/standards/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/playbooks/`


## Normalização LKGOC — 20260627T165139Z

Fonte de precedência operacional:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/canon/INDEX.md`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/rules/LKGOC-DEV-PRODUCTION-PRECEDENCE.md`

Aplicar sempre:

- DEV/unpublished/branch pode ser usado para preview/QA LKGOC, com alvo verificado, status draft, rollback/readback e sem publicação customer-facing.
- Contract Lock não bloqueia DEV; bloqueia approval final, lote, promoção/merge e Production/main/customer-facing.
- Shopify Admin GraphQL read-only usa CLI oficial `hermes-cli-run shopify store execute`; mutations/Admin write direto ficam bloqueados por padrão salvo exceção aprovada.
- Production/main/customer-facing exige aprovação explícita atual de Lucas + rollback + readback + receipt.
- Estoque/disponibilidade/grade/tamanho continua handoff obrigatório para `lk-stock`.
- Novas classes estruturais usam `lk-goc-*`; `lk-204l-*`, `lk-lkgoc-*` e `lk-collection-v2` são gold source/compatibilidade.
