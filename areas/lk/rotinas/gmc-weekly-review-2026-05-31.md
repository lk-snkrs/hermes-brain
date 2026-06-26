# LK Growth OS — GMC Review read-only — 2026-05-31

Gerado em: `2026-05-31T16:37:05.241023+00:00`  
Modo: `read-only / preview`  
Escopo: Google Merchant Center + Product Data Quality + divergências públicas Shopify ↔ GMC.  
Status de decisão: `decision-grade para triagem GMC`, porque Content API autenticado e amostras públicas Shopify foram consultadas. Execução/correção segue bloqueada sem aprovação explícita.

## Resumo executivo GMC

- Content API / Merchant Center autenticado respondeu com dados vivos: `21338` productstatuses e `21338` products.
- Cobertura de IDs: products sem status `0`; statuses sem product resource `0`.
- P0 preço final continua limpo (`price_mismatch`/`price_out_of_range` = 0), mas há pendência crítica de servibilidade: `landing_page_error` em 15 produtos e `mhlsf_full_missing_valid_link_template` em 10.436 ofertas locais reprovadas em Shopping.
- Destinos: aprovações agregadas `42594`; reprovações agregadas `10505` por destino/status.
- Price auto-update: `price_updated` `548` produtos; `strikethrough_price_updated` `354` produtos. Continua sendo governança de preço/promos, não patch em lote.
- Product data quality: `missing_item_attribute_for_product_type` `1239` produtos; preview de cor gerado com `925` high-confidence, `0` medium e `314` para revisão humana.

## Evidência principal

### Cobertura por destino

| Destino | Status | Produtos |
|---|---:|---:|
| SurfacesAcrossGoogle | approved | 10871 |
| Shopping | approved | 10665 |
| DisplayAds | approved | 10659 |
| Shopping | disapproved | 10437 |
| LocalSurfacesAcrossGoogle | approved | 10399 |
| LocalSurfacesAcrossGoogle | disapproved | 37 |
| SurfacesAcrossGoogle | disapproved | 24 |
| DisplayAds | disapproved | 7 |
| SurfacesAcrossGoogle | pending | 7 |

### Issues por prioridade

Comparação: vs relatório anterior `2026-05-28`.

| Prioridade | Issue | Instâncias | Produtos | Δ produtos | Impacto |
|---|---|---:|---:|---:|---|
| P0 | `price_mismatch` | 0 | 0 | n/a | Preço feed ↔ landing divergente; pode reprovar Shopping/Surfaces. |
| P0 | `price_out_of_range` | 0 | 0 | n/a | Preço inválido/fora de faixa; risco P0 se final estiver 0.00. |
| P0/P1 | `landing_page_error` | 17 | 15 | n/a | Landing indisponível; produto não servível até corrigir link/publicação/supressão. |
| P0/P1 | `item_missing_required_attribute` | 21 | 21 | n/a | Atributo obrigatório ausente; frequentemente preço/link em item com landing quebrada. |
| P1 | `price_updated` | 1644 | 548 | +15 | Google corrigindo preço automaticamente; sinal de feed/origem stale. |
| P1 | `strikethrough_price_updated` | 1062 | 354 | +10 | Google corrigindo preço riscado/sale; exige lógica promocional antes de patch. |
| P1 | `missing_item_attribute_for_product_type` | 2772 | 1239 | +134 | Demotion por atributo ausente, principalmente cor/product type. |
| P2 | `utf8_encoding_error` | 18 | 6 | 0 | Caracteres/encoding inválidos no dado enviado. |
| P2 | `availability_updated` | 9 | 3 | +1 | Google corrigindo disponibilidade automaticamente; checar origem antes de write. |
| P2 | `condition_updated_from_detected` | 8 | 4 | 0 | Google inferiu condição; sinal de atributo ausente/incorreto. |
| P2 | `restricted_nfs_policy_violation` | 25 | 10 | +8 | Policy/restrição; revisar título/imagem/categoria. |
| P2 | `coupon_gtin` | 4 | 2 | 0 | GTIN associado a cupom/uso inválido; validar fonte oficial. |
| P2 | `image_single_color` | 4 | 2 | 0 | Imagem com área/cor única; qualidade visual no Shopping. |
| P2 | `image_too_small_for_high_resolution` | 1 | 1 | 0 | Imagem abaixo do ideal para alta resolução. |
| P2 | `sexual_interests_policy_violation` | 6 | 6 | +5 | Policy issue sensível; revisar título/imagem/categoria. |
| P2 | `restricted_gtin` | 28 | 14 | 0 | GTIN restrito/inválido; precisa validação oficial. |
| P2 | `reserved_gtin` | 2 | 1 | 0 | GTIN reservado/inválido; precisa validação oficial. |
| P2 | `image_link_internal_error` | 23 | 11 | n/a | Erro transitório de processamento de imagem; monitorar/rechecar. |
| P2 | `local_stores_lack_inventory` | 74 | 37 | +2 | Afeta LocalSurfaces; não é prioridade SEO/CRO geral. |
| P2 | `mhlsf_full_missing_valid_link_template` | 10436 | 10436 | n/a | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |
| P2 | `landing_page_pending_crawl` | 7 | 7 | n/a | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |
| P2 | `pause_expired` | 2 | 1 | 0 | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |
| P2 | `image_link_internal_error_fallback` | 1 | 1 | n/a | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |
| P2 | `vehicles_policy_violation` | 1 | 1 | 0 | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |

## Issues críticos e impacto comercial

### P0 — preço inválido / mismatch
- Sem amostra nessa leitura.

Interpretação: quando público `.js` mostra preço válido e GMC mostra preço divergente/0.00, o risco é feed/source defect com reprovação direta. Correção exige descobrir superfície ativa do dado antes de qualquer ProductInput/feed write.

### P0/P1 — landing page e atributo obrigatório ausente
- `online:pt:BR:5706324928133224313` — Tênis New Balance 204L x Atmos Cow Girl Brown Marrom - Tamanho 39 — issues `landing_page_error`; GMC price `2799.99` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:11810372920072143991` — Calça Saint Studio Wide Alfaiataria Preto — issues `item_missing_required_attribute, landing_page_error`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:12726273505041435980` — Pop Mart Labubu The Monsters Big into Energy Series Vinyl Plush Pendant - Caixa Fechada (6 Blind Boxes) — issues `item_missing_required_attribute`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:3876299146406606317` — Calça Saint Studio Jeans Baggy Preta — issues `item_missing_required_attribute, landing_page_error`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:16066821251494448304` — 39 — issues `item_missing_required_attribute, landing_page_error`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:6562590402534581177` — Calça Nude Project Illegal Jeans Ash Cinza - LK — issues `item_missing_required_attribute, landing_page_error`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:2258634078163248862` — Calça Chino Saint Studio Supima Preto — issues `item_missing_required_attribute, landing_page_error`; GMC price `` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:12729936352569121203` — 35 — issues `landing_page_error`; GMC price `1999.99` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.

Itens com `.js` 404 devem ser triados entre republish/corrigir link/suppress/delete/monitorar. Não apagar ou suprimir sem decisão comercial.

### P1 — Local inventory / link template para Shopping
- Issue: `mhlsf_full_missing_valid_link_template` — `10.436` produtos, todos com `destination=Shopping`, `servability=disapproved`, atributo `link template`.
- Evidência do Merchant: `Missing valid value in [link_template] attribute`; detalhe: `A valid [link_template] value with store code is required for the offer to serve`.
- Amostras públicas checadas por `.js` indicam que a landing do produto pode estar OK, mas o problema é atributo de feed/local inventory, não página quebrada:
  - `local:pt:BR:LIA_JI0324-6` — Tênis Adidas Gazelle Indoor Maroon Almost Yellow Marrom — público `ok`, preço público `1999.99`, disponível `True`.
  - `local:pt:BR:LIA_OXV-2785246-39` — Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown Blue Marrom — público `ok`, preço público `10499.99`, disponível `True`.
  - `local:pt:BR:LIA_SLCRCVOW-1` — Camiseta Slyce Racquet Club Off White — público `ok`, preço público `269.00`, disponível `True`.
  - `local:pt:BR:LIA_f99715` — Tênis Adidas Yeezy Boost 350 V2 Sesame Cinza — público `ok`, preço público `3499.99`, disponível `True`.
- Interpretação: provável backlog sistêmico de ofertas `local:*`/local inventory feed sem `link_template` válido com store code. Não é correção de copy/PDP e não deve ser tratado como preço/estoque.

## Produtos/atributos prioritários

### P1 — missing color/product type
- `online:pt:BR:1201A789-020-41` — Tênis ASICS Gel-NYC Graphite Grey Black Preto — issues `missing_item_attribute_for_product_type`; GMC price `1999.99` sale ``; público `ok`, preço min `1999.99`, disponível `True`; relação `match`.
- `online:pt:BR:PERI049-1007` — Óculos de Sol Palm Angels PERI049-1007 Preto — issues `missing_item_attribute_for_product_type`; GMC price `1599.99` sale `1119.99`; público `ok`, preço min `1119.99`, disponível `True`; relação `diverges_content_1599.99_public_min_1119.99`.
- `online:pt:BR:DD0587-002-43` — Tênis Jordan 5 Retro Wolf Grey (2026) Cinza — issues `missing_item_attribute_for_product_type`; GMC price `3999.99` sale ``; público `ok`, preço min `3999.99`, disponível `True`; relação `match`.
- `online:pt:BR:1201A789-020-39` — Tênis ASICS Gel-NYC Graphite Grey Black Preto — issues `missing_item_attribute_for_product_type`; GMC price `1999.99` sale ``; público `ok`, preço min `1999.99`, disponível `True`; relação `match`.
- `online:pt:BR:IQ8055 100-35` — Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco — issues `missing_item_attribute_for_product_type`; GMC price `3999.99` sale ``; público `ok`, preço min `3999.99`, disponível `True`; relação `match`.
- `online:pt:BR:6803695667030727884` — 37 — issues `missing_item_attribute_for_product_type`; GMC price `2799.99` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:ALO-2441950-39` — Tênis Alo Yoga Alo Runner Pink Rosa — issues `missing_item_attribute_for_product_type`; GMC price `2399.99` sale ``; público `ok`, preço min `2399.99`, disponível `True`; relação `match`.
- `online:pt:BR:3MG10844970-40` — Tênis On Running x Kith ON K-Tech 2 Spirulina Barley Verde — issues `missing_item_attribute_for_product_type`; GMC price `8499.99` sale ``; público `ok`, preço min `8499.99`, disponível `True`; relação `match`.

Preview de cor: `1239` linhas totais; `925` high-confidence; `0` medium; `314` precisam curadoria humana. CSV: `reports/lk-gmc-missing-color-preview-2026-05-31.csv`.

### P1 — price_updated / strikethrough_price_updated
- `online:pt:BR:DV0426-012-2` — Tênis Nike Air Jordan 1 Low SE 'Light Steel Grey' Cinza - Tamanho 36 — issues `price_updated, strikethrough_price_updated`; GMC price `1899.99` sale `1699.99`; público `ok`, preço min `1699.99`, disponível `True`; relação `diverges_content_1899.99_public_min_1699.99`.
- `online:pt:BR:FQ8138-103-3` — Tênis Nike Air Jordan 4 Retro Oxidized Branco - Tamanho 36 — issues `price_updated, strikethrough_price_updated`; GMC price `2499.99` sale `2299.99`; público `ok`, preço min `2299.99`, disponível `True`; relação `diverges_content_2499.99_public_min_2299.99`.
- `online:pt:BR:43774078387780` — Tênis Adidas Samba Jane Cream Black Gum Bege - Tamanho 36 — issues `price_updated`; GMC price `1999.99` sale `1199.99`; público `ok`, preço min `1199.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1199.99`.
- `online:pt:BR:DC6991200-42` — Tênis Nike Air Jordan 1 Low SE Mocha Marrom — issues `price_updated`; GMC price `2499.99` sale ``; público `ok`, preço min `2499.99`, disponível `True`; relação `match`.
- `online:pt:BR:FN4193100-8` — Tênis Crenshaw Skate Club x Nike SB Dunk Low Multicolor — issues `price_updated, strikethrough_price_updated`; GMC price `2499.99` sale `2199.90`; público `ok`, preço min `2199.90`, disponível `True`; relação `diverges_content_2499.99_public_min_2199.90`.
- `online:pt:BR:DV0426-012-9` — Tênis Nike Air Jordan 1 Low SE 'Light Steel Grey' Cinza - Tamanho 40.5 — issues `price_updated, strikethrough_price_updated`; GMC price `1899.99` sale `1699.99`; público `ok`, preço min `1699.99`, disponível `True`; relação `diverges_content_1899.99_public_min_1699.99`.
- `online:pt:BR:CZ5127001-1` — Tênis Medicom Toy x Nike SB Dunk Be@rbrick Preto — issues `price_updated, strikethrough_price_updated`; GMC price `2099.99` sale `1749.90`; público `ok`, preço min `1749.90`, disponível `True`; relação `diverges_content_2099.99_public_min_1749.90`.
- `online:pt:BR:HQ6998-212` — Tênis Nike Air Jordan 1 Low OG Olive Verde — issues `price_updated`; GMC price `2499.99` sale ``; público `ok`, preço min `2499.99`, disponível `True`; relação `match`.

Amostras costumam envolver `salePrice`/preço riscado/compare-at. Bulk patch de preço final permanece bloqueado.

### P2 — GTIN restricted/reserved
- `local:pt:BR:LIA_553558612-6` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público ``, preço min ``, disponível ``; relação `n/a`.
- `online:pt:BR:553558612-6` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público ``, preço min ``, disponível ``; relação `n/a`.
- `local:pt:BR:LIA_553558612-7` — Tênis Nike Air Jordan 1 Low Bred Toe Vermelho — issues `restricted_gtin`; GMC price `1899.99` sale `1799.99`; público ``, preço min ``, disponível ``; relação `n/a`.
- `online:pt:BR:cz0790-101-6` — Tênis Nike Air Jordan 1 Retro Low OG 'Atmosphere Grey' Roxo — issues `restricted_gtin`; GMC price `2499.90` sale ``; público ``, preço min ``, disponível ``; relação `n/a`.
- `online:pt:BR:CZ0790-102-4` — Tênis Nike Air Jordan 1 Low Og Mocha Marrom — issues `reserved_gtin`; GMC price `2499.99` sale ``; público ``, preço min ``, disponível ``; relação `n/a`.
- `local:pt:BR:LIA_IE0875-5` — Tênis adidas Samba Og Off White Oat Violet Tone Branco — issues `restricted_gtin`; GMC price `1999.99` sale ``; público ``, preço min ``, disponível ``; relação `n/a`.
- `local:pt:BR:LIA_555088108-5` — Tênis Nike Air Jordan 1 High Stage Haze Cinza — issues `restricted_gtin`; GMC price `2999.99` sale `2449.99`; público ``, preço min ``, disponível ``; relação `n/a`.
- `online:pt:BR:IE0875-5` — Tênis adidas Samba Og Off White Oat Violet Tone Branco — issues `restricted_gtin`; GMC price `1999.99` sale ``; público ``, preço min ``, disponível ``; relação `n/a`.

GTIN não deve ser inferido automaticamente. Próximo passo seguro é fila de validação com fonte oficial/fornecedor antes de qualquer alteração.

### P1/P2 — encoding, disponibilidade e policy/image quality
- `online:pt:BR:NUD-6884446-S` — Camiseta Nude Project Honor Tee Marshmallow Off White — issues `restricted_nfs_policy_violation, sexual_interests_policy_violation`; GMC price `999.99` sale ``; público `ok`, preço min `999.99`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_IG6192-3` — Tênis adidas Handball Spezial Preloved Green Verde — issues `condition_updated_from_detected`; GMC price `1749.90` sale ``; público `ok`, preço min `1749.90`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_IG6192-2` — Tênis adidas Handball Spezial Preloved Green Verde — issues `condition_updated_from_detected`; GMC price `1749.90` sale ``; público `ok`, preço min `1749.90`, disponível `True`; relação `match`.
- `online:pt:BR:NUD-6884446-XS` — Camiseta Nude Project Honor Tee Marshmallow Off White — issues `restricted_nfs_policy_violation, sexual_interests_policy_violation`; GMC price `999.99` sale ``; público `ok`, preço min `999.99`, disponível `True`; relação `match`.
- `online:pt:BR:FOG14-4` — Blusa Fear of God Essentials Sporty Nylon Half Zip Jet Black Preto — issues `availability_updated`; GMC price `2299.99` sale ``; público `ok`, preço min `2299.99`, disponível ``; relação `match`.
- `online:pt:BR:3128383465433270909` — Top Skims Cotton Rib Marble Branco — issues `restricted_nfs_policy_violation`; GMC price `599.99` sale ``; público `ok`, preço min `599.99`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_U9060PSD-5` — Tênis New Balance 9060 'Linen Burgundy' Bege — issues `image_single_color`; GMC price `2399.99` sale ``; público `ok`, preço min `2399.99`, disponível `True`; relação `match`.
- `local:pt:BR:LIA_NUD-6884446-L` — Camiseta Nude Project Honor Tee Marshmallow Off White — issues `restricted_nfs_policy_violation`; GMC price `999.99` sale ``; público `ok`, preço min `999.99`, disponível `True`; relação `match`.

Triar por produto e destino; não ajustar automaticamente policy/image/encoding sem fonte e aprovação.

## Divergências Shopify ↔ GMC

- Verificação feita por GET público em `products/{handle}.js` a partir dos links GMC, sem Shopify Admin write.
- Divergências de preço foram classificadas como evidência para approval packet, não autorização de correção.
- Disponibilidade pública foi usada apenas como sinal; Tiny/estoque não entrou como critério de priorização SEO/GMC.

## Approval packets sugeridos — sem executar

### Packet A — P0 preço inválido/divergente
- Problema atual: `0` produtos com `price_mismatch` e `0` com `price_out_of_range`.
- Ação proposta se reaparecer: micro-piloto por offerId com snapshot Product/ProductInput e origem de feed/dataSource; corrigir apenas offers aprovados.
- Risco: ProductInput pode ser sobrescrito; preço promocional pode exigir salePrice/compare-at, não preço final.
- Rollback: snapshot do Product resource/ProductInput antes do patch; rollback por offerId.
- Validação: readback Content/Merchant API + status após reprocessamento; sem `fetchNow` sem aprovação.
- Status: `no_action_now`.

### Packet B — Missing color/product-type attributes
- Problema: `1239` produtos com demotion por atributo ausente.
- Ação proposta: revisar `reports/lk-gmc-missing-color-preview-2026-05-31.csv` e aplicar só linhas `high` aprovadas via supplemental/ProductInput.
- Risco: cor inferida errada prejudica relevância no Shopping; medium/ambíguos ficam bloqueados até curadoria.
- Rollback: remover/sobrescrever atributo no mesmo surface com snapshot anterior.
- Validação: itemLevelIssue deve cair após reprocessamento; monitorar D+7.
- Status: `preview_allowed_now`; write exige aprovação.

### Packet C — Landing page / 404 cleanup
- Problema: `15` produtos com landing error e `21` com atributo obrigatório ausente.
- Ação proposta: classificar cada offer como `republicar Shopify`, `corrigir link`, `suppress/delete Merchant`, ou `monitorar`.
- Risco: suprimir item que deveria voltar à venda; precisa confirmação comercial.
- Rollback: snapshot do resource/feed row; reintrodução pela fonte original se suprimido por engano.
- Status: `needs_explicit_approval` para qualquer suppress/delete/republicação/write.

### Packet D — Price auto-update governance
- Problema: `548` produtos com `price_updated` e `354` com `strikethrough_price_updated`.
- Ação proposta: separar preço final, salePrice, compare_at/strikethrough e lag/false-positive; só depois propor micro-piloto.
- Risco: bulk patch pode quebrar promoção correta.
- Status: `blocked_pending_promo_logic`.

### Packet E — Link template / ofertas locais reprovadas em Shopping
- Problema: `10.436` ofertas `local:*` com `mhlsf_full_missing_valid_link_template`, `servability=disapproved` em Shopping.
- Evidência: Merchant pede valor válido em `[link_template]` com store code; amostras públicas de PDP estão OK, então o gargalo parece feed/local inventory, não storefront 404.
- Ação proposta: investigar, em read-only, qual data source alimenta as ofertas locais e preparar preview de correção de `link_template`/estrutura local inventory; não alterar datafeed, fetch/reprocess ou ProductInput sem aprovação.
- Risco: mexer em local inventory/feed template pode afetar milhares de ofertas e Shopping/LocalSurfaces; precisa snapshot da data source e rollback antes de qualquer write.
- Rollback: backup integral da configuração/feed row/supplemental surface antes da mudança; reversão no mesmo surface.
- Validação: re-read Content/Merchant productstatuses depois do processamento; D+7 para queda do issue e aprovação por destino.
- Status: `needs_investigation_preview`; write exige aprovação explícita.

## Escopo 18 tópicos — cobertura desta rotina

- GMC: coberto com dados autenticados.
- Catálogo/product data quality: coberto em atributos, preço, landing, GTIN, policy e imagens.
- Schema/Product e Shopify SEO/CRO: observado apenas quando impacta PDP/feed; não foi auditoria completa de schema/CRO.
- GA4, GSC, PageSpeed/CrUX, reviews, paid/influencer, concorrência/SERP, local SEO, Klaviyo/CRM e QA de eventos: fora do escopo desta rotina GMC semanal; usar rotinas específicas quando a decisão depender de demanda/conversão.
- Impact review/experimentation: qualquer packet aprovado deve ter readback e revisão em aproximadamente 7 dias.

## Próximos passos seguros

1. Prioridade segura desta semana: preparar investigação read-only do `link_template` das ofertas locais (`local:*`) antes de qualquer proposta de feed write.
2. Revisar o preview `reports/lk-gmc-missing-color-preview-2026-05-31.csv`; aprovar somente linhas high-confidence se fizer sentido comercial.
3. Triar os 15 produtos com `landing_page_error`/404 e 21 com atributo obrigatório ausente em uma fila de lifecycle/link, sem suppress/delete automático.
4. Separar `price_updated`/`strikethrough_price_updated` por lógica de promoção antes de qualquer proposta de write.
5. Triar encoding/policy/imagem por produto, com fonte oficial e validação de destino.
6. Se Lucas aprovar um packet, executar apenas o escopo aprovado com snapshot/readback e D+7.

## O que não foi feito

- Nenhum Content API write, ProductInput PATCH, supplemental feed write/upload, `fetchNow` ou reprocess que altere estado.
- Nenhum Shopify write, preço, estoque, desconto, theme, campanha ou envio externo.
- Nenhum contato com cliente/fornecedor.
