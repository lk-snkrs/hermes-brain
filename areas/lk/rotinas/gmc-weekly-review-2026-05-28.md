# LK Growth OS — GMC Review read-only — 2026-05-28

Gerado em: `2026-05-28T12:11:04.478480+00:00`  
Modo: `read-only / preview`  
Escopo: Google Merchant Center + Product Data Quality + divergências públicas Shopify ↔ GMC.  
Status de decisão: `decision-grade para triagem GMC`, porque Content API autenticado e amostras públicas Shopify foram consultadas. Execução/correção segue bloqueada sem aprovação explícita.

## Resumo executivo GMC

- Content API / Merchant Center autenticado respondeu com dados vivos: `20443` productstatuses e `20462` products.
- Cobertura de IDs: products sem status `19`; statuses sem product resource `0`.
- P0 preço: `price_mismatch` agora `0` instâncias / `0` produtos; `price_out_of_range` `0` / `0`.
- Landing/atributo obrigatório: `landing_page_error` `0` produtos; `item_missing_required_attribute` `0` produtos.
- Preço automático continua grande: `price_updated` `533` produtos; `strikethrough_price_updated` `344` produtos. Não é seguro corrigir em lote sem separar preço final, salePrice e compare_at.
- Product data quality: `missing_item_attribute_for_product_type` `1105` produtos; GTIN restricted/reserved `15` produtos somados antes de deduplicar.

## Evidência principal

### Cobertura por destino

| Destino | Status | Produtos |
|---|---:|---:|
| SurfacesAcrossGoogle | approved | 10948 |
| Shopping | approved | 10718 |
| DisplayAds | approved | 10717 |
| LocalSurfacesAcrossGoogle | approved | 9459 |
| LocalSurfacesAcrossGoogle | disapproved | 35 |
| DisplayAds | disapproved | 1 |
| SurfacesAcrossGoogle | disapproved | 1 |

### Issues por prioridade

| Prioridade | Issue | Instâncias | Produtos | Δ produtos vs 21/05 | Impacto |
|---|---|---:|---:|---:|---|
| P0 | `price_mismatch` | 0 | 0 | -2 | Preço feed ↔ landing divergente; pode reprovar Shopping/Surfaces. |
| P0 | `price_out_of_range` | 0 | 0 | -2 | Preço inválido/fora de faixa; risco P0 se final estiver 0.00. |
| P0/P1 | `landing_page_error` | 0 | 0 | -17 | Landing indisponível; produto não servível até corrigir link/publicação/supressão. |
| P0/P1 | `item_missing_required_attribute` | 0 | 0 | -16 | Atributo obrigatório ausente; frequentemente preço em item com landing quebrada. |
| P1 | `price_updated` | 1599 | 533 | +54 | Google corrigindo preço automaticamente; sinal de feed/origem stale. |
| P1 | `strikethrough_price_updated` | 1032 | 344 | +59 | Google corrigindo preço riscado/sale; exige lógica promocional antes de patch. |
| P1 | `missing_item_attribute_for_product_type` | 2495 | 1105 | +664 | Demotion por atributo ausente, principalmente cor. |
| P2 | `utf8_encoding_error` | 18 | 6 | n/a | Caracteres/encoding inválidos no dado enviado; pode bloquear aprovação em destinos. |
| P2 | `availability_updated` | 6 | 2 | n/a | Google corrigindo disponibilidade automaticamente; exige checar origem de disponibilidade antes de write. |
| P2 | `condition_updated_from_detected` | 4 | 4 | n/a | Google inferiu condição; sinal de atributo ausente/incorreto em item local. |
| P2 | `restricted_nfs_policy_violation` | 4 | 2 | n/a | Policy/restrição de conteúdo; revisar título/imagem/categoria antes de qualquer ajuste. |
| P2 | `coupon_gtin` | 3 | 2 | n/a | GTIN associado a cupom/uso inválido; validar fonte oficial. |
| P2 | `image_single_color` | 2 | 2 | n/a | Imagem com área/cor única; risco de qualidade visual no Shopping. |
| P2 | `image_too_small_for_high_resolution` | 1 | 1 | n/a | Imagem abaixo do ideal para alta resolução; revisar mídia se comercialmente relevante. |
| P2 | `sexual_interests_policy_violation` | 1 | 1 | n/a | Policy issue sensível; revisar título/imagem/categoria antes de qualquer ação. |
| P2 | `restricted_gtin` | 23 | 14 | +4 | GTIN restrito/inválido; precisa validação oficial antes de alterar. |
| P2 | `reserved_gtin` | 2 | 1 | -1 | GTIN reservado/inválido; precisa validação oficial antes de alterar. |
| P2 | `image_link_internal_error` | 0 | 0 | n/a | Erro transitório de processamento de imagem; monitorar/rechecar. |
| P2 | `local_stores_lack_inventory` | 35 | 35 | n/a | Local inventory sem estoque local; afeta LocalSurfaces, não SEO/CRO geral. |

## Issues críticos e impacto comercial

### P0 — preço inválido / mismatch
- Sem amostra nessa leitura.

Interpretação: quando público `.js` mostra preço válido e GMC mostra preço divergente/0.00, o risco é feed/source defect com reprovação direta. Ainda assim, correção exige descobrir superfície ativa do dado antes de qualquer ProductInput/feed write.

### P0/P1 — landing page e atributo obrigatório ausente
- Sem amostra nessa leitura.

Interpretação: itens com `.js` 404 devem ser triados entre republish/corrigir link/suppress/delete/monitorar. Não apagar ou suprimir sem decisão comercial.

## Produtos/atributos prioritários

### P1 — missing color/product type
- `online:pt:BR:1201A789-020-41` — Tênis ASICS Gel-NYC Graphite Grey Black Preto — issues `missing_item_attribute_for_product_type`; GMC price `1999.99` sale ``; público `ok`, preço min `1999.99`, disponível `True`; relação `match`.
- `online:pt:BR:PERI049-1007` — Óculos de Sol Palm Angels PERI049-1007 Preto — issues `missing_item_attribute_for_product_type`; GMC price `1599.99` sale `1119.99`; público `ok`, preço min `1119.99`, disponível `True`; relação `diverges_content_1599.99_public_min_1119.99`.
- `online:pt:BR:DD0587-002-43` — Tênis Jordan 5 Retro Wolf Grey (2026) Cinza — issues `missing_item_attribute_for_product_type`; GMC price `3999.99` sale ``; público `ok`, preço min `3999.99`, disponível `True`; relação `match`.
- `online:pt:BR:1201A789-020-39` — Tênis ASICS Gel-NYC Graphite Grey Black Preto — issues `missing_item_attribute_for_product_type`; GMC price `1999.99` sale ``; público `ok`, preço min `1999.99`, disponível `True`; relação `match`.
- `online:pt:BR:IQ8055 100-35` — Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco — issues `missing_item_attribute_for_product_type`; GMC price `3999.99` sale ``; público `ok`, preço min `3999.99`, disponível `True`; relação `match`.
- `online:pt:BR:ALO-2441950-39` — Tênis Alo Yoga Alo Runner Pink Rosa — issues `missing_item_attribute_for_product_type`; GMC price `2399.99` sale ``; público `ok`, preço min `2399.99`, disponível `True`; relação `match`.
- `online:pt:BR:3MG10844970-40` — Tênis On Running x Kith ON K-Tech 2 Spirulina Barley Verde — issues `missing_item_attribute_for_product_type`; GMC price `8499.99` sale ``; público `ok`, preço min `8499.99`, disponível `True`; relação `match`.
- `online:pt:BR:YZY-2566238-43` — Tênis Adidas Yeezy Boost 350 V2 Earth Marrom — issues `missing_item_attribute_for_product_type`; GMC price `5999.99` sale ``; público `ok`, preço min `5999.99`, disponível `True`; relação `match`.

Atributo `color` continua sendo a fila mais limpa para supplemental/ProductInput, mas só nos casos high-confidence e com revisão humana para nomes ambíguos.

### P1 — price_updated / strikethrough_price_updated
- `online:pt:BR:DV0426-012-2` — Tênis Nike Air Jordan 1 Low SE 'Light Steel Grey' Cinza - Tamanho 36 — issues `price_updated, strikethrough_price_updated`; GMC price `1899.99` sale `1699.99`; público `ok`, preço min `1699.99`, disponível `True`; relação `diverges_content_1899.99_public_min_1699.99`.
- `online:pt:BR:FQ8138-103-3` — Tênis Nike Air Jordan 4 Retro Oxidized Branco - Tamanho 36 — issues `price_updated, strikethrough_price_updated`; GMC price `2499.99` sale `2299.99`; público `ok`, preço min `2299.99`, disponível `True`; relação `diverges_content_2499.99_public_min_2299.99`.
- `online:pt:BR:43774078387780` — Tênis Adidas Samba Jane Cream Black Gum Bege - Tamanho 36 — issues `price_updated`; GMC price `1999.99` sale `1199.99`; público `ok`, preço min `1199.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1199.99`.
- `online:pt:BR:DC6991200-42` — Tênis Nike Air Jordan 1 Low SE Mocha Marrom — issues `price_updated`; GMC price `2499.99` sale ``; público `ok`, preço min `2499.99`, disponível `True`; relação `match`.
- `online:pt:BR:FN4193100-8` — Tênis Crenshaw Skate Club x Nike SB Dunk Low Multicolor — issues `price_updated, strikethrough_price_updated`; GMC price `2499.99` sale `2199.90`; público `ok`, preço min `2199.90`, disponível `True`; relação `diverges_content_2499.99_public_min_2199.90`.
- `online:pt:BR:DV0426-012-9` — Tênis Nike Air Jordan 1 Low SE 'Light Steel Grey' Cinza - Tamanho 40.5 — issues `price_updated, strikethrough_price_updated`; GMC price `1899.99` sale `1699.99`; público `ok`, preço min `1699.99`, disponível `True`; relação `diverges_content_1899.99_public_min_1699.99`.
- `online:pt:BR:CZ5127001-1` — Tênis Medicom Toy x Nike SB Dunk Be@rbrick Preto — issues `price_updated, strikethrough_price_updated`; GMC price `2099.99` sale `1749.90`; público `ok`, preço min `1749.90`, disponível `True`; relação `diverges_content_2099.99_public_min_1749.90`.
- `online:pt:BR:HQ6998-212` — Tênis Nike Air Jordan 1 Low OG Olive Verde — issues `price_updated`; GMC price `2499.99` sale ``; público `ok`, preço min `2499.99`, disponível `True`; relação `match`.

Amostras mostram que parte das divergências envolve `salePrice`/preço riscado/compare-at. Bulk patch de preço final permanece bloqueado.

### P2 — GTIN restricted/reserved
- `local:pt:BR:LIA_553558612-6` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público `None`; relação `n/a`.
- `online:pt:BR:553558612-6` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público `None`; relação `n/a`.
- `local:pt:BR:LIA_553558612-7` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público `None`; relação `n/a`.
- `online:pt:BR:cz0790-101-6` — Tênis Nike Air Jordan 1 Retro Low OG 'Atmosphere Grey' Roxo — issues `restricted_gtin`; GMC price `2499.90` sale ``; público `None`; relação `n/a`.
- `online:pt:BR:CZ0790-102-4` — Tênis Nike Air Jordan 1 Low Og Mocha Marrom — issues `reserved_gtin`; GMC price `2499.99` sale ``; público `None`; relação `n/a`.
- `local:pt:BR:LIA_IE0875-5` — Tênis adidas Samba Og Off White Oat Violet Tone Branco — issues `restricted_gtin`; GMC price `1999.99` sale ``; público `None`; relação `n/a`.
- `local:pt:BR:LIA_555088108-5` — Tênis Nike Air Jordan 1 High Stage Haze Cinza — issues `restricted_gtin`; GMC price `2999.99` sale `2449.99`; público `None`; relação `n/a`.
- `online:pt:BR:IE0875-5` — Tênis adidas Samba Og Off White Oat Violet Tone Branco — issues `restricted_gtin`; GMC price `1999.99` sale ``; público `None`; relação `n/a`.

GTIN não deve ser inferido automaticamente. Próximo passo seguro é fila de validação com fonte oficial/fornecedor antes de qualquer alteração.

### P1/P2 — encoding, disponibilidade e policy/image quality
- `local:pt:BR:LIA_IG6192-3` — Tênis adidas Handball Spezial Preloved Green Verde — issues `condition_updated_from_detected`; GMC price `1749.90` sale ``; público `ok`, preço min `1749.90`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_IG6192-2` — Tênis adidas Handball Spezial Preloved Green Verde — issues `condition_updated_from_detected`; GMC price `1749.90` sale ``; público `ok`, preço min `1749.90`, disponível `True`; relação `match`.
- `online:pt:BR:20054-4` — Camisa Aphase Check - Light Yellow Bege — issues `availability_updated`; GMC price `369.99` sale `99.99`; público `ok`, preço min `99.99`, disponível `False`; relação `diverges_content_369.99_public_min_99.99`.
- `online:pt:BR:3128383465433270909` — Top Skims Cotton Rib Marble Branco — issues `restricted_nfs_policy_violation`; GMC price `599.99` sale ``; público `ok`, preço min `599.99`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_U9060PSD-5` — Tênis New Balance 9060 'Linen Burgundy' Bege — issues `image_single_color`; GMC price `2399.99` sale ``; público `ok`, preço min `2399.99`, disponível `True`; relação `match`.
- `online:pt:BR:CLC-0067294-XXL` — Moletom Cold Culture Down To Luck Blue Azul — issues `utf8_encoding_error`; GMC price `1499.99` sale ``; público `ok`, preço min `1499.99`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_IG6192-4` — Tênis adidas Handball Spezial Preloved Green Verde — issues `condition_updated_from_detected`; GMC price `1749.90` sale ``; público `ok`, preço min `1749.90`, disponível `True`; relação `match`.
- `online:pt:BR:43774078388550` — Camiseta Skims Cotton Jersey Kyanite Azul — issues `restricted_nfs_policy_violation, sexual_interests_policy_violation`; GMC price `699.99` sale ``; público `ok`, preço min `699.99`, disponível `True`; relação `match`.

Esses issues são menores em volume, mas podem bloquear destinos específicos. A triagem precisa separar erro de dado textual/encoding, disponibilidade inferida pelo Google, policy issue e qualidade de imagem.

## Divergências Shopify ↔ GMC

- Verificação feita por GET público em `products/{handle}.js` a partir dos links GMC, sem Shopify Admin write.
- Divergências de preço foram classificadas como evidência para approval packet, não autorização de correção.
- Itens com público `.js` 404 foram tratados como landing/product lifecycle triage, não como simples problema de preço.
- Disponibilidade pública foi usada apenas como sinal; Tiny/estoque não entrou na priorização SEO/GMC desta rotina.

## Approval packets sugeridos — sem executar

### Packet A — P0 preço inválido/divergente

- Problema atual: `0` produtos com `price_mismatch` e `0` com `price_out_of_range`.
- Status desta semana: backlog crítico P0 limpo na leitura autenticada; manter monitoramento, sem correção proposta agora.
- Ação proposta se reaparecer: preparar micro-piloto por offerId com snapshot Product/ProductInput e origem de feed/dataSource; corrigir apenas os offers aprovados.
- Risco: ProductInput pode não persistir se fonte primária/Google app sobrescrever; preço promocional pode exigir salePrice/compare-at, não preço final.
- Rollback: snapshot do Product resource/ProductInput antes do patch; rollback por offerId.
- Validação: readback Content/Merchant API + aguardar status reprocessado; sem `fetchNow` sem aprovação.
- Status: `no_action_now`; se reaparecer, `needs_explicit_approval`.

### Packet B — Missing color/product-type attributes

- Problema: `1105` produtos com demotion por atributo ausente.
- Ação proposta: gerar/atualizar preview CSV com `offerId`, título, cor sugerida, confiança e evidência; aplicar só high-confidence aprovados via supplemental/ProductInput.
- Risco: cor inferida errada prejudica catálogo; revisão humana necessária em medium/ambíguos.
- Rollback: remover/sobrescrever atributo no mesmo surface com snapshot anterior.
- Validação: itemLevelIssue some após reprocessamento; monitorar D+7.
- Status: `preview_allowed_now`; write exige aprovação.

### Packet C — Landing page / 404 cleanup

- Problema: `0` produtos com landing error e `0` com atributo obrigatório ausente.
- Ação proposta: classificar cada offer como `republicar Shopify`, `corrigir link`, `suppress/delete Merchant`, ou `monitorar` se voltou 200.
- Risco: suprimir item que deveria voltar à venda; precisa confirmação comercial.
- Rollback: snapshot do resource/feed row; reintrodução pela fonte original se suprimido por engano.
- Status: `needs_explicit_approval` para qualquer suppress/delete/republicação/write.

### Packet D — Price auto-update governance

- Problema: `533` produtos com `price_updated` e `344` com `strikethrough_price_updated`.
- Ação proposta: separar em preço final divergente, salePrice divergente, compare_at/strikethrough e lag/false-positive; só depois propor micro-piloto de até 10 IDs.
- Risco: bulk patch pode quebrar promoção correta.
- Status: `blocked_pending_promo_logic`.

## Escopo 18 tópicos — cobertura desta rotina

- GMC: coberto com dados autenticados.
- Catálogo/product data quality: coberto em atributos, preço, landing, GTIN e imagens.
- Schema/Product e Shopify SEO/CRO: observado apenas quando impacta PDP/feed; não foi auditoria completa de schema/CRO.
- GA4, GSC, PageSpeed/CrUX, reviews, paid/influencer, concorrência/SERP, local SEO, Klaviyo/CRM e QA de eventos: fora do escopo desta rotina GMC semanal; usar nas rotinas específicas quando a decisão depender de demanda/conversão.
- Impact review/experimentation: qualquer packet aprovado deve ter readback e revisão em aproximadamente 7 dias.

## Próximos passos seguros

1. Usar o preview `reports/lk-gmc-missing-color-preview-2026-05-28.csv` para revisar as `795` linhas high-confidence de cor; manter as `310` linhas sem cor segura para curadoria humana.
2. Não há P0 de preço/landing para corrigir nesta semana; manter monitoramento e só abrir micro-piloto se `price_mismatch`, `price_out_of_range` ou `landing_page_error` reaparecerem.
3. Separar `price_updated`/`strikethrough_price_updated` em preço final, salePrice, compare_at/strikethrough e lag/false-positive antes de qualquer proposta de patch.
4. Triar os poucos casos de encoding/policy/imagem por produto, sem ajuste automático.
5. Se Lucas aprovar um packet, executar apenas o escopo aprovado com snapshot/readback e D+7.

## O que não foi feito

- Nenhum Content API write, ProductInput PATCH, supplemental feed write/upload, `fetchNow` ou reprocess que altere estado.
- Nenhum Shopify write, preço, estoque, desconto, theme, campanha ou envio externo.
- Nenhum contato com cliente/fornecedor.

Artefatos: `reports/lk-gmc-weekly-review-2026-05-28.json`, `reports/lk-gmc-weekly-review-2026-05-28.md`, `areas/lk/rotinas/gmc-weekly-review-2026-05-28.md`, `reports/lk-gmc-missing-color-preview-2026-05-28.csv`, `reports/lk-gmc-missing-color-preview-2026-05-28.md`.
