# LK GMC residual corrections — 2026-05-14

Status: `executado_com_rollback_e_monitoramento`

## Autorização

Lucas aprovou no Telegram: seguir/corrigir itens 1, 3, 4 e 5; usar Kicks.dev para GTINs faltantes quando houvesse match seguro; seguir.

## Escopo executado

- Preço/salePrice: correção via Merchant API ProductInputs v1, copiando somente preço/compare-at/price de variante Shopify exata.
- Landing page: remoção de IDs Merchant exatos quando o handle Shopify estava ausente/DRAFT/ARCHIVED; sem publicar Shopify e sem criar redirect.
- Imagem: reparo de imageLink/additionalImageLinks para IDs online com evidência Shopify exata.
- Missing attrs: tentativa controlada para atributos não críticos; a rota Content API criou overlays `source=api` indesejados em alguns IDs, então foi revertida/deletada para deixar o crawl/feed original ressurgir.
- GTIN: Kicks.dev consultado; nenhum patch aplicado porque não houve correspondência segura de tamanho sem conversão BR↔US. Mantido para uma onda dedicada.

## Resultado monitorado

Baseline residual antes:

- `price_updated`: 1089
- `strikethrough_price_updated`: 516
- `missing_item_attribute_for_product_type`: 44
- `landing_page_error`: 27 instâncias / 9 produtos únicos na triagem atual
- `landing_page_pending_crawl`: 5
- `image_link_broken`: 6
- `image_single_color`: 8
- `restricted_gtin`: 100
- `reserved_gtin`: 6

Após execução + reparos + rechecagem:

- `price_updated`: 915
- `strikethrough_price_updated`: 231
- `missing_item_attribute_for_product_type`: 34
- `landing_page_error`: 0
- `landing_page_pending_crawl`: 0
- `image_link_broken`: 3
- `image_single_color`: 8
- `restricted_gtin`: 100
- `reserved_gtin`: 6

Impacto líquido:

- Preço: -174 instâncias de `price_updated`; -285 de `strikethrough_price_updated`.
- Landing page: fechado no monitoramento atual (`landing_page_error` e `pending_crawl` zerados).
- Missing attrs: -10 instâncias vs baseline, depois de rollback da rota que gerou overlay.
- Imagem: `image_link_broken` caiu 6 → 3; `image_single_color` ainda depende de recrawl/política visual do Google.
- GTIN: sem alteração, por segurança.

## Writes/ações executadas

- 251 patches preço/salePrice via Merchant API v1.
- 9 deletes exatos de landing page stale.
- 3 patches de imagem online confirmados; 2 locais foram bloqueados (`local:` não suportado por ProductInputs online).
- 14 tentativas de missing attrs com erro de schema/feeds; revertidas.
- 15 overlays API introduzidos pela tentativa Content API foram deletados para restaurar o estado crawl/feed.

## Auditoria / rollback privado

- Executor principal: `reports/lk-gmc-2026-05-14-residual-approved-executor.json`
- Monitor atual: `reports/lk-gmc-2026-05-14-residual-triage-current.json`
- Rollback principal: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-residual-approved-executor-rollback-20260514T155630Z.json`
- Rollback API overlay delete: `/opt/data/hermes_bruno_ingest/local_sql/lk_gmc_rollback_snapshots/lk-gmc-2026-05-14-api-overlay-delete-repair-rollback-20260514T164433Z.json`

## Não executado

- Shopify write/publish/redirect.
- Tiny/POS/feed upload/fetchNow.
- Campanha, WhatsApp, Klaviyo, fornecedor, compra ou pagamento.
- GTIN sem match seguro no Kicks.dev.

## Próxima onda recomendada

1. Monitorar novamente em 1–2h porque `price_updated`, sale price e imagem podem lagar no Merchant Center.
2. Onda GTIN dedicada: cruzar Kicks.dev `unified/gtin` + SKU + tamanho com conversão BR↔US validada por marca/modelo antes de qualquer patch.
3. Missing attrs restantes: não usar Content API insert em itens `source=crawl`/multi-feed; usar rota específica por dataSource ou corrigir a fonte do feed/crawl.
