# LK Growth OS — GMC Review read-only — 2026-06-04

Gerado em: `2026-06-04T11:41:07.336724+00:00`  
Modo: `read-only / preview`  
Escopo: Google Merchant Center + Product Data Quality + divergências públicas Shopify ↔ GMC.  
Status de decisão: `decision-grade para triagem GMC`, porque Content API autenticado e amostras públicas Shopify foram consultadas. Execução/correção segue bloqueada sem aprovação explícita.

## Resumo executivo GMC

- Content API / Merchant Center autenticado respondeu com dados vivos: `21402` productstatuses e `21402` products.
- Cobertura de IDs: products sem status `0`; statuses sem product resource `0`.
- P0 preço/landing/atributo obrigatório: `com pendências` nesta leitura.
- Destinos: aprovações agregadas `38626`; reprovações agregadas `14707` por destino/status.
- Price auto-update: `price_updated` `234` produtos; `strikethrough_price_updated` `223` produtos. Continua sendo governança de preço/promos, não patch em lote.
- Product data quality: `missing_item_attribute_for_product_type` `712` produtos; preview de cor gerado com `393` high-confidence, `0` medium e `319` para revisão humana.

## Evidência principal

### Cobertura por destino

| Destino | Status | Produtos |
|---|---:|---:|
| Shopping | disapproved | 11835 |
| LocalSurfacesAcrossGoogle | approved | 10414 |
| SurfacesAcrossGoogle | approved | 9515 |
| Shopping | approved | 9351 |
| DisplayAds | approved | 9346 |
| SurfacesAcrossGoogle | disapproved | 1446 |
| DisplayAds | disapproved | 1399 |
| LocalSurfacesAcrossGoogle | disapproved | 27 |

### Issues por prioridade

Comparação: vs relatório anterior `2026-05-31`.

| Prioridade | Issue | Instâncias | Produtos | Δ produtos | Impacto |
|---|---|---:|---:|---:|---|
| P0 | `price_mismatch` | 0 | 0 | n/a | Preço feed ↔ landing divergente; pode reprovar Shopping/Surfaces. |
| P0 | `price_out_of_range` | 0 | 0 | n/a | Preço inválido/fora de faixa; risco P0 se final estiver 0.00. |
| P0/P1 | `landing_page_error` | 4219 | 1431 | +1416 | Landing indisponível; produto não servível até corrigir link/publicação/supressão. |
| P0/P1 | `item_missing_required_attribute` | 35 | 35 | +14 | Atributo obrigatório ausente; frequentemente preço/link em item com landing quebrada. |
| P1 | `price_updated` | 702 | 234 | -314 | Google corrigindo preço automaticamente; sinal de feed/origem stale. |
| P1 | `strikethrough_price_updated` | 669 | 223 | -131 | Google corrigindo preço riscado/sale; exige lógica promocional antes de patch. |
| P1 | `missing_item_attribute_for_product_type` | 1719 | 712 | -527 | Demotion por atributo ausente, principalmente cor/product type. |
| P2 | `utf8_encoding_error` | 18 | 6 | 0 | Caracteres/encoding inválidos no dado enviado. |
| P2 | `availability_updated` | 18 | 6 | +3 | Google corrigindo disponibilidade automaticamente; checar origem antes de write. |
| P2 | `condition_updated_from_detected` | 8 | 4 | 0 | Google inferiu condição; sinal de atributo ausente/incorreto. |
| P2 | `restricted_nfs_policy_violation` | 19 | 7 | -3 | Policy/restrição; revisar título/imagem/categoria. |
| P2 | `coupon_gtin` | 4 | 2 | 0 | GTIN associado a cupom/uso inválido; validar fonte oficial. |
| P2 | `image_single_color` | 4 | 2 | 0 | Imagem com área/cor única; qualidade visual no Shopping. |
| P2 | `image_too_small_for_high_resolution` | 1 | 1 | 0 | Imagem abaixo do ideal para alta resolução. |
| P2 | `sexual_interests_policy_violation` | 5 | 5 | -1 | Policy issue sensível; revisar título/imagem/categoria. |
| P2 | `restricted_gtin` | 30 | 15 | +1 | GTIN restrito/inválido; precisa validação oficial. |
| P2 | `reserved_gtin` | 2 | 1 | 0 | GTIN reservado/inválido; precisa validação oficial. |
| P2 | `image_link_internal_error` | 6 | 3 | -8 | Erro transitório de processamento de imagem; monitorar/rechecar. |
| P2 | `local_stores_lack_inventory` | 54 | 27 | -10 | Afeta LocalSurfaces; não é prioridade SEO/CRO geral. |
| P2 | `mhlsf_full_missing_valid_link_template` | 10441 | 10441 | +5 | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |
| P2 | `pause_expired` | 2 | 1 | 0 | Issue não mapeado no playbook; revisar amostra antes de qualquer ação. |

## Issues críticos e impacto comercial

### P0 — preço inválido / mismatch
- Sem amostra nessa leitura.

Interpretação: quando público `.js` mostra preço válido e GMC mostra preço divergente/0.00, o risco é feed/source defect com reprovação direta. Correção exige descobrir superfície ativa do dado antes de qualquer ProductInput/feed write.

### P0/P1 — landing page e atributo obrigatório ausente
- `online:pt:BR:FD0860001-5` — Tênis Jarritos x Nike SB Dunk Low Branco/Verde - Tamanho 43 — issues `landing_page_error`; GMC price `4999.99` sale ``; público `ok`, preço min `4999.99`, disponível `True`; relação `match`.
- `online:pt:BR:w5766r-1` — Calça Legging Alo Yoga 7/8 High-Waist Airlift — issues `landing_page_error`; GMC price `1599.99` sale ``; público `ok`, preço min `1599.99`, disponível `True`; relação `match`.
- `online:pt:BR:JR8772-4` — Tênis Adidas SL 72 RS Aurora Ivy Off White Verde - Tamanho 37 — issues `landing_page_error`; GMC price `1999.99` sale `1799.99`; público `ok`, preço min `1799.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1799.99`.
- `online:pt:BR:JI2714-5` — Tênis adidas Gazelle Indoor Dark Brown Glow Pink Court Green Marrom - Tamanho 38 — issues `landing_page_error`; GMC price `1699.99` sale ``; público `ok`, preço min `1699.99`, disponível `True`; relação `match`.
- `online:pt:BR:DH4401101-40` — Tênis Nike Dunk Low Blue Paisley Azul - Tamanho 34 — issues `landing_page_error`; GMC price `1999.99` sale `1599.99`; público `ok`, preço min `1599.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1599.99`.
- `online:pt:BR:DO9395400-10` — Tênis Nike SB Dunk Low LA Dodgers Azul - Tamanho 46 — issues `landing_page_error`; GMC price `3999.99` sale `3499.99`; público `ok`, preço min `3499.99`, disponível `True`; relação `diverges_content_3999.99_public_min_3499.99`.
- `online:pt:BR:HF6061-400-4` — Tênis Nike Sb Dunk Low x Futura Skateboard Bleached Aqua Azul - Tamanho 39 — issues `landing_page_error`; GMC price `5999.90` sale `2999.99`; público `ok`, preço min `2999.99`, disponível `True`; relação `diverges_content_5999.90_public_min_2999.99`.
- `online:pt:BR:IG6785-4` — Tênis adidas Gazelle Indoor Blue Semi Pink Velvet Azul - Tamanho 37 — issues `landing_page_error`; GMC price `1449.99` sale ``; público `ok`, preço min `1449.99`, disponível `True`; relação `match`.

Itens com `.js` 404 devem ser triados entre republish/corrigir link/suppress/delete/monitorar. Não apagar ou suprimir sem decisão comercial.

## Produtos/atributos prioritários

### P1 — missing color/product type
- `online:pt:BR:PERI049-1007` — Óculos de Sol Palm Angels PERI049-1007 Preto — issues `missing_item_attribute_for_product_type`; GMC price `1599.99` sale `1119.99`; público `ok`, preço min `1119.99`, disponível `True`; relação `diverges_content_1599.99_public_min_1119.99`.
- `online:pt:BR:6803695667030727884` — 37 — issues `missing_item_attribute_for_product_type`; GMC price `2799.99` sale ``; público `http_404`, preço min ``, disponível ``; relação `not_compared`.
- `online:pt:BR:U204L6A6-34` — Tênis New Balance 204L Reflection Bege — issues `missing_item_attribute_for_product_type`; GMC price `2799.99` sale ``; público `ok`, preço min `2799.99`, disponível `True`; relação `match`.
- `online:pt:BR:U204L2SZ-36` — Tênis New Balance 204L Sea Salt Linen Bege — issues `missing_item_attribute_for_product_type`; GMC price `2799.99` sale ``; público `ok`, preço min `2799.99`, disponível `True`; relação `match`.
- `online:pt:BR:11157608326226995514` — Pop Mart Disney Mickey Family Together Series Plush Keychain Single Blind Box Lacrada — issues `missing_item_attribute_for_product_type`; GMC price `549.99` sale ``; público `ok`, preço min `549.99`, disponível `True`; relação `match`.
- `online:pt:BR:IQ7604-104` — Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Sail Tropical Pink Rosa — issues `missing_item_attribute_for_product_type`; GMC price `9499.99` sale ``; público `ok`, preço min `9499.99`, disponível `True`; relação `match`.
- `online:pt:BR:2421339187503443526` — 34 — issues `missing_item_attribute_for_product_type`; GMC price `3499.00` sale ``; público `ok`, preço min `3499.00`, disponível `True`; relação `match`.
- `online:pt:BR:ALD-9318238-G` — Camiseta Aimé Leon Dore Pappoús Logo Pristine Off White — issues `missing_item_attribute_for_product_type`; GMC price `1299.99` sale ``; público `ok`, preço min `1299.99`, disponível `True`; relação `match`.

Preview de cor: `712` linhas totais; `393` high-confidence; `0` medium; `319` precisam curadoria humana. CSV: `reports/lk-gmc-missing-color-preview-2026-06-04.csv`.

### P1 — price_updated / strikethrough_price_updated
- `online:pt:BR:43774078387780` — Tênis Adidas Samba Jane Cream Black Gum Bege - Tamanho 36 — issues `price_updated`; GMC price `1999.99` sale `1199.99`; público `ok`, preço min `1199.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1199.99`.
- `online:pt:BR:DD1873102-4` — Tênis Nike Dunk Low Next Nature Black White Preto - Tamanho 37 — issues `price_updated, strikethrough_price_updated`; GMC price `1599.99` sale `1399.99`; público `ok`, preço min `1399.99`, disponível `True`; relação `diverges_content_1599.99_public_min_1399.99`.
- `online:pt:BR:FQ7056-100-3` — Tênis Nike Dunk Low Valentine's Day 2024 Rosa — issues `price_updated, strikethrough_price_updated`; GMC price `1699.99` sale `1499.99`; público `ok`, preço min `1499.99`, disponível `True`; relação `diverges_content_1699.99_public_min_1499.99`.
- `online:pt:BR:JR1402-4` — Tênis Adidas Samba Jane 'White Black' Branco — issues `price_updated`; GMC price `1999.99` sale `1199.99`; público `ok`, preço min `1199.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1199.99`.
- `online:pt:BR:dd1873-100-2` — Tênis Dunk Low Next Nature Pink Pale Coral Rosa — issues `price_updated, strikethrough_price_updated`; GMC price `1999.99` sale `1599.99`; público `ok`, preço min `1599.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1599.99`.
- `online:pt:BR:FQ9112100-3` — Tênis Nike Air Jordan 1 Low Se "Glitter Swoosh" Branco — issues `price_updated, strikethrough_price_updated`; GMC price `1999.99` sale `1699.99`; público `ok`, preço min `1699.99`, disponível `True`; relação `diverges_content_1999.99_public_min_1699.99`.
- `online:pt:BR:DH7577001-42` — Tênis Nike Dunk Low Fossil Rose Azul/Rosa — issues `price_updated, strikethrough_price_updated`; GMC price `1599.99` sale `1399.99`; público `ok`, preço min `1399.99`, disponível `True`; relação `diverges_content_1599.99_public_min_1399.99`.
- `online:pt:BR:DC0774502-9` — Tênis Nike Air Jordan 1 Low Sky J Purple Roxo — issues `strikethrough_price_updated`; GMC price `1999.99` sale `1999.90`; público `ok`, preço min `1999.90`, disponível `True`; relação `diverges_content_1999.99_public_min_1999.90`.

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
- `online:pt:BR:LAB05` — Pop Mart Labubu The Monsters Coca Cola Series Surprise Shake Vinyl Plush Figure Pingente — issues `availability_updated`; GMC price `1299.99` sale ``; público `ok`, preço min `1299.99`, disponível `True`; relação `match`.
- `online:pt:BR:FOG14-4` — Blusa Fear of God Essentials Sporty Nylon Half Zip Jet Black Preto — issues `availability_updated`; GMC price `2299.99` sale ``; público `ok`, preço min `2299.99`, disponível ``; relação `match`.
- `local:pt:BR:LIA_U9060PSD-5` — Tênis New Balance 9060 'Linen Burgundy' Bege — issues `image_single_color`; GMC price `2399.99` sale ``; público `ok`, preço min `2399.99`, disponível `True`; relação `match`.
- `online:pt:BR:CLC-0067294-XXL` — Moletom Cold Culture Down To Luck Blue Azul — issues `utf8_encoding_error`; GMC price `1499.99` sale ``; público `ok`, preço min `1499.99`, disponível `True`; relação `match`.
- `online:pt:BR:NUD-6884446-L` — Camiseta Nude Project Honor Tee Marshmallow Off White — issues `restricted_nfs_policy_violation, sexual_interests_policy_violation`; GMC price `999.99` sale ``; público `ok`, preço min `999.99`, disponível `True`; relação `match`.

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
- Problema: `712` produtos com demotion por atributo ausente.
- Ação proposta: revisar `reports/lk-gmc-missing-color-preview-2026-06-04.csv` e aplicar só linhas `high` aprovadas via supplemental/ProductInput.
- Risco: cor inferida errada prejudica relevância no Shopping; medium/ambíguos ficam bloqueados até curadoria.
- Rollback: remover/sobrescrever atributo no mesmo surface com snapshot anterior.
- Validação: itemLevelIssue deve cair após reprocessamento; monitorar D+7.
- Status: `preview_allowed_now`; write exige aprovação.

### Packet C — Landing page / 404 cleanup
- Problema: `1431` produtos com landing error e `35` com atributo obrigatório ausente.
- Ação proposta: classificar cada offer como `republicar Shopify`, `corrigir link`, `suppress/delete Merchant`, ou `monitorar`.
- Risco: suprimir item que deveria voltar à venda; precisa confirmação comercial.
- Rollback: snapshot do resource/feed row; reintrodução pela fonte original se suprimido por engano.
- Status: `needs_explicit_approval` para qualquer suppress/delete/republicação/write.

### Packet D — Price auto-update governance
- Problema: `234` produtos com `price_updated` e `223` com `strikethrough_price_updated`.
- Ação proposta: separar preço final, salePrice, compare_at/strikethrough e lag/false-positive; só depois propor micro-piloto.
- Risco: bulk patch pode quebrar promoção correta.
- Status: `blocked_pending_promo_logic`.

## Escopo 18 tópicos — cobertura desta rotina

- GMC: coberto com dados autenticados.
- Catálogo/product data quality: coberto em atributos, preço, landing, GTIN, policy e imagens.
- Schema/Product e Shopify SEO/CRO: observado apenas quando impacta PDP/feed; não foi auditoria completa de schema/CRO.
- GA4, GSC, PageSpeed/CrUX, reviews, paid/influencer, concorrência/SERP, local SEO, Klaviyo/CRM e QA de eventos: fora do escopo desta rotina GMC semanal; usar rotinas específicas quando a decisão depender de demanda/conversão.
- Impact review/experimentation: qualquer packet aprovado deve ter readback e revisão em aproximadamente 7 dias.

## Próximos passos seguros

1. Revisar o preview `reports/lk-gmc-missing-color-preview-2026-06-04.csv`; aprovar somente linhas high-confidence se fizer sentido comercial.
2. Manter P0 preço/landing em monitoramento; se reaparecer, montar micro-piloto por offerId, nunca bulk patch.
3. Separar `price_updated`/`strikethrough_price_updated` por lógica de promoção antes de qualquer proposta de write.
4. Triar encoding/policy/imagem por produto, com fonte oficial e validação de destino.
5. Se Lucas aprovar um packet, executar apenas o escopo aprovado com snapshot/readback e D+7.

## O que não foi feito

- Nenhum Content API write, ProductInput PATCH, supplemental feed write/upload, `fetchNow` ou reprocess que altere estado.
- Nenhum Shopify write, preço, estoque, desconto, theme, campanha ou envio externo.
- Nenhum contato com cliente/fornecedor.
