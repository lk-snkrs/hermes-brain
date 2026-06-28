## 2026-06-06 10:04:50Z — Standing approval Lucas: publish em DEV LKGOC
Lucas autorizou standing approval para publicar em Shopify DEV/unpublished quando ele pedir para "refazer", "fazer" ou equivalente em contexto LKGOC/tema/guia/collection. Escopo permitido: aplicar/publicar preview em tema DEV com role `unpublished`, fazer readback e QA. Continua bloqueado sem aprovação explícita atual: production/main, promoção/merge para produção, alterações customer-facing finais, preço/estoque/desconto/campanha/envios externos. Sempre verificar `role: unpublished`; se `role: main`, abortar.

## 2026-06-06T12:53:24Z — LKGOC: sempre mapear já feito antes de sugerir próxima
Lucas corrigiu: Onitsuka Tiger e New Balance 9060 já tinham sido trabalhadas. Antes de sugerir “próxima” frente LKGOC, consultar obrigatoriamente `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/LKGOC-MAPA-JA-FEITO.md` + `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md` e buscar no Brain pelo candidato. Não tratar como nova frente: 204L, 9060, 530, Onitsuka, Adidas Samba/Samba Jane/Sambae, Nike Mind, Moon Shoe sem checar escopo; classificar como refino/QA/impact review se já otimizada.

## 2026-06-25 — LKGOC runtime hardening
Lucas mandou executar correção 1-4: identidade runtime do profile deve ser Collection Optimizer puro; skill local LKGOC criada; smoke de boot criado; memory-context/Honcho fora de LKGOC deve ser ignorado. Growth/Stock/Shopify/CRO geral são handoffs.


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
