# LK GMC — Governance next decision

Gerado em: `2026-05-15T20:19:30Z`
Status: `read_only_governance_decision_complete`

## Veredito

Não liberar bulk retry nem patch amplo de preço no GMC agora.

A governança correta é separar três trilhas:

1. **Preço regular price-only**: pode virar micro-piloto aprovável, mas só com pacote exato de IDs, snapshot/rollback e verificação pós-delay.
2. **Strikethrough / salePrice / compare-at**: permanece bloqueado; precisa análise promocional separada para não mexer em preço riscado errado.
3. **Landing/crawl/DRAFT/404**: não é problema de preço; pode virar pacote exato de suppress/delete para DRAFT/404, ou monitor para os casos public 200.

## Checklist executado

### Shopify / Google & YouTube

Fonte: `reports/lk-gmc-2026-05-14-google-youtube-channel-readonly-diagnostic.md`

- Google & YouTube publication encontrada: `79416787166`.
- Catálogo Shopify Google ativo.
- Amostra: `6/6` SKUs publicados no Google & YouTube.
- `5/6` tinham preço stale no Merchant apesar de publicados no canal.

Conclusão: publicação Shopify/Google & YouTube não parece ser o bloqueio primário; o problema é sync/output/source ownership do Merchant.

### Merchant / preço

Fonte: `reports/lk-gmc-2026-05-14-price-source-diagnostic.md`

- Produtos diagnosticados: `152`.
- `108` classificados como `merchant_stale_vs_shopify_and_public`.
- `44` já batem com Shopify Admin.

Conclusão: parte relevante do preço no Merchant está stale contra Shopify Admin e contra `/products/{handle}.js`; não é erro simples no preço Shopify.

### Merchant / source ownership

Fonte: `reports/lk-gmc-2026-05-14-price-source-ownership-drilldown.md`

- Account settings API: HTTP `200`.
- Automatic Improvements retornado pela API: `returned`.
- Fresh final output vs Shopify target na amostra: `12/12` stale.
- Productstatus confirma `price_updated` na amostra.
- ProductInputs GET retornou 404 para as fontes testadas, então a leitura direta do input não provou ownership por ProductInput.

Conclusão: não dá para assumir que um patch amplo ProductInputs vai resolver de forma estável. Se for testar, precisa micro-piloto exato e pós-verificação.

### Residual deduplicado

Fonte: `areas/lk/rotinas/gmc-residual-dedup-preview-2026-05-15.md`

- `310` produtos online com `price_updated`/`strikethrough_price_updated`.
- `42` candidatos price-only contra preço atual Shopify.
- `268` casos promocionais/compare-at/strikethrough em revisão.
- `22` landing errors: `20` DRAFT/404, `2` public OK/monitor.

## Decisão operacional

### Liberado sem nova aprovação

- Monitor read-only.
- Preview/deduplicação.
- Pacote de aprovação com IDs exatos.
- Snapshot/rollback local.
- Verificação read-only pós-evento.

### Não liberado sem aprovação explícita

- ProductInputs PATCH.
- Content API upsert/delete.
- Supplemental/feed upload ou fetchNow.
- Alteração de automatic item updates.
- Shopify price/source/channel write.
- Suppress/delete de produtos Merchant.
- Qualquer bulk retry.

## Próximo pacote aprovável recomendado

### Pacote A — price-only micro-pilot

Escopo: `42` candidatos price-only, sem salePrice/strikethrough/compare-at.

Contrato antes de aplicar:

- IDs exatos no pacote.
- Campo exato: `productAttributes.price`.
- Sem `salePrice`.
- Sem `strikethrough_price_updated`.
- Snapshot/rollback privado antes.
- Aplicar poucos primeiro se quiser reduzir risco: `10` IDs iniciais.
- Verificação depois por Product API/statuses com delay.

Status: `needs_explicit_approval`.

### Pacote B — DRAFT/404 suppress/delete

Escopo: `20` produtos com Shopify DRAFT e public 404/.js 404.

Contrato antes de aplicar:

- IDs exatos.
- Snapshot de rollback.
- Confirmar que não são produtos que a LK quer republicar.
- Os 2 public OK ficam fora.

Status: `needs_explicit_approval`.

### Pacote C — strikethrough/sale/compare-at

Escopo: `268` casos.

Contrato:

- Não aplicar agora.
- Exige análise promocional separada por Shopify Admin + public .js + Merchant final output.

Status: `blocked_pending_promo_logic`.

## O que não foi feito

- Merchant write
- ProductInputs PATCH
- Content API write/delete
- Shopify write
- Tiny write
- feed fetch/upload/fetchNow
- automatic item updates settings change
- campaign/send/contact
- bulk retry
