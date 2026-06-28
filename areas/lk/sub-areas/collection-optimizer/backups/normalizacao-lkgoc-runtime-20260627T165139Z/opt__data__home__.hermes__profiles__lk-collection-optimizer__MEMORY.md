## 2026-06-06 10:04:50Z — Standing approval Lucas: publish em DEV LKGOC
Lucas autorizou standing approval para publicar em Shopify DEV/unpublished quando ele pedir para "refazer", "fazer" ou equivalente em contexto LKGOC/tema/guia/collection. Escopo permitido: aplicar/publicar preview em tema DEV com role `unpublished`, fazer readback e QA. Continua bloqueado sem aprovação explícita atual: production/main, promoção/merge para produção, alterações customer-facing finais, preço/estoque/desconto/campanha/envios externos. Sempre verificar `role: unpublished`; se `role: main`, abortar.

## 2026-06-06T12:53:24Z — LKGOC: sempre mapear já feito antes de sugerir próxima
Lucas corrigiu: Onitsuka Tiger e New Balance 9060 já tinham sido trabalhadas. Antes de sugerir “próxima” frente LKGOC, consultar obrigatoriamente `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/LKGOC-MAPA-JA-FEITO.md` + `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md` e buscar no Brain pelo candidato. Não tratar como nova frente: 204L, 9060, 530, Onitsuka, Adidas Samba/Samba Jane/Sambae, Nike Mind, Moon Shoe sem checar escopo; classificar como refino/QA/impact review se já otimizada.

## 2026-06-25 — LKGOC runtime hardening
Lucas mandou executar correção 1-4: identidade runtime do profile deve ser Collection Optimizer puro; skill local LKGOC criada; smoke de boot criado; memory-context/Honcho fora de LKGOC deve ser ignorado. Growth/Stock/Shopify/CRO geral são handoffs.
