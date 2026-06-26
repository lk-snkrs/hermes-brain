# LK Growth OS — GMC Review read-only — 2026-05-21

Gerado em: `2026-05-21 12:00 UTC`  
Modo: `read-only / preview`  
Escopo: Google Merchant Center + Product Data Quality + divergências públicas Shopify ↔ GMC.  
Status de decisão: `decision-grade para triagem GMC`, com ressalva de que qualquer correção continua exigindo approval packet e aprovação explícita.

## Resumo executivo GMC

- Content API / Merchant Center autenticado respondeu com dados vivos.
- Catálogo lido: `19.556` productstatuses e `19.556` products; não houve diferença de IDs entre `products.list` e `productstatuses.list` nesta leitura.
- Maior risco comercial continua em **preço/feed**:
  - `price_updated`: `1.437` instâncias / `479` produtos.
  - `strikethrough_price_updated`: `853` instâncias / `285` produtos.
  - `price_mismatch`: `6` instâncias / `2` produtos, com reprovação em Shopping/Display/Surfaces.
  - `price_out_of_range`: `6` instâncias / `2` produtos, preço enviado `0.00` em dois offers Adidas Gazelle x Bad Bunny.
- Data quality ainda relevante:
  - `missing_item_attribute_for_product_type`: `1.163` instâncias / `441` produtos, principalmente `color` com servability `demoted`.
  - `restricted_gtin`: `15` instâncias / `10` produtos.
  - `reserved_gtin`: `3` instâncias / `2` produtos.
- URLs/landing pages: `landing_page_error` em `17` produtos e `item_missing_required_attribute` em `16` produtos; amostra pública confirmou `.js` 404 em produtos de vestuário/rascunho/removidos.
- Local inventory: `local_stores_lack_inventory` em `15` produtos locais (`local:pt:BR:LIA_*`). Isto afeta LocalSurfaces, mas não deve ser misturado com SEO/CRO nem com estoque Shopify como fonte final.

## Evidência principal

### Cobertura por destino

| Destino | Status | Produtos |
|---|---:|---:|
| SurfacesAcrossGoogle | approved | 10.316 |
| Shopping | approved | 10.053 |
| DisplayAds | approved | 10.052 |
| LocalSurfacesAcrossGoogle | approved | 9.201 |
| SurfacesAcrossGoogle | disapproved | 22 |
| LocalSurfacesAcrossGoogle | disapproved | 15 |
| DisplayAds | disapproved | 3 |
| Shopping | disapproved | 2 |
| SurfacesAcrossGoogle | pending | 2 |

### Issues por prioridade

| Prioridade | Issue | Instâncias | Produtos | Impacto |
|---|---|---:|---:|---|
| P0 | `price_mismatch` | 6 | 2 | Reprovação por divergência de preço feed ↔ landing page. |
| P0 | `price_out_of_range` | 6 | 2 | Feed com `0.00`, inválido para Shopping. |
| P0/P1 | `landing_page_error` | 17 | 17 | Produto aponta para landing indisponível. |
| P0/P1 | `item_missing_required_attribute` | 16 | 16 | Campo obrigatório ausente, sobretudo preço em páginas 404. |
| P1 | `price_updated` | 1.437 | 479 | Google corrigindo automaticamente preço; risco de feed/source stale. |
| P1 | `strikethrough_price_updated` | 853 | 285 | Google corrigindo preço riscado/sale; exige lógica promocional antes de write. |
| P1 | `missing_item_attribute_for_product_type` | 1.163 | 441 | Demotion por atributo ausente, principalmente cor. |
| P2 | `restricted_gtin` | 15 | 10 | GTIN inválido/restrito; impacta confiança do catálogo. |
| P2 | `image_link_internal_error` | 5 | 3 | Imagem adicional não processada; pode reprocessar sozinha em até 3 dias. |

## Produtos/atributos prioritários

### P0 — preço inválido / mismatch

1. `online:pt:BR:IF9737` — **Tênis adidas Gazelle x Bad Bunny Core White Bege**
   - Content/GMC price: `0.00`.
   - Público `.js`: `2199.99`, variant `45906859589854`, disponível.
   - Issues: `price_mismatch`, `price_out_of_range`.
2. `online:pt:BR:IF9735-9` — **Tênis adidas Gazelle x Bad Bunny Core White Bege**
   - Content/GMC price: `0.00`.
   - Público `.js`: `2199.99`, variant `45906859524318`, disponível.
   - Issues: `price_mismatch`, `price_out_of_range`.

### P1 — preço automático / strikethrough

A amostra confirma padrões distintos que não devem receber bulk patch sem triagem:

- `DV0426-012-2` — Content price `1899.99`, salePrice `1699.99`; público `.js` price `1999.90`, compare_at `1899.99`. Divergência complexa de preço promocional/compare-at.
- `U9060CCB-10` — Content price `2799.99`; público price `2799.99`, compare_at `2399.99`. Issue pode estar ligada ao preço riscado/compare-at, não ao preço final.
- `43774078387780` — Adidas Samba Jane Cream Black Gum: Content price `1999.99`, salePrice `1199.99`; público price `1199.99`, compare_at `1999.99`, variante pública `available=false`. Requer separar preço, disponibilidade e lógica promocional.
- `FN4193100-8` — Content price `2499.99`, salePrice `2199.90`; público price `2799.90`, compare_at `2499.99`. Divergência crítica de sale/compare-at.

### P1 — atributo `color` ausente

Amostras vivas com página pública OK e preço batendo, portanto bons candidatos para supplemental/ProductInput de atributo, depois de approval:

- `online:pt:BR:ONI-0995678-35` — Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown — issue `Missing color`; preço Content e público `2999.99`.
- `online:pt:BR:HQ4309-610-40` — Chinelo Slide Nike Mind 001 Pearl Pink — issue `Missing color`; preço `3199.99`.
- `online:pt:BR:1183A201-126-5` — Onitsuka Tiger Mexico 66 White Black — issue `Missing color`; preço `2399.99`.
- `online:pt:BR:11157608326226995514` — Pop Mart Disney Mickey Family Together Series Plush Keychain — issue de atributo por product_type; preço `549.99`.

### P1 — landing page / 404

Amostra pública confirmou `.js` 404:

- `online:pt:BR:1736512501686486863` — Camiseta Nude Project Hearts White Branco / title GMC `L/g` — missing price + 404.
- `online:pt:BR:11810372920072143991` — Calça Saint Studio Wide Alfaiataria Preto — missing price + landing 404.
- `online:pt:BR:3876299146406606317` — Calça Saint Studio Jeans Baggy Preta — missing price + landing 404.
- `online:pt:BR:6562590402534581177` — Calça Nude Project Illegal Jeans Ash Cinza — missing price + landing 404.
- `online:pt:BR:2258634078163248862` — Calça Chino Saint Studio Supima Preto — landing 404.

## Divergências Shopify ↔ GMC

Verificação pública via `https://lksneakers.com.br/products/{handle}.js` indica:

- Dois offers Adidas Gazelle x Bad Bunny têm preço GMC `0.00` enquanto a vitrine pública retorna `2199.99`; isto é P0 e likely feed/source defect.
- Vários `price_updated` não são simples “preço errado”: aparecem como divergência entre `price`, `salePrice` e `compare_at_price`. Não aplicar patch de preço final em lote sem separar venda/promocional/strikethrough.
- Alguns produtos com `landing_page_error` continuam apontando para páginas `.js` 404; esses devem virar pacote de suppress/delete/republicação, não correção de preço.
- `missing color` aparece em produtos com PDP pública OK; é fila mais segura para supplemental/ProductInput de atributo, mas ainda exige aprovação antes de write.

## Approval packets sugeridos — sem executar

### Packet A — P0 preço inválido Adidas Gazelle x Bad Bunny

- Problema: dois offers com `price=0.00`, gerando `price_mismatch` e `price_out_of_range`.
- Evidência: Content/GMC `0.00`; público `.js` `2199.99`; status `in stock` no GMC e variante pública disponível.
- Offers: `online:pt:BR:IF9737`, `online:pt:BR:IF9735-9`.
- Ação proposta: preparar snapshot/readback e corrigir apenas o campo de preço do feed/ProductInput correspondente para `2199.99 BRL`, confirmando antes a origem real do feed/dataSource.
- Risco: se a origem ativa for Shopify Google & YouTube ou outro feed primário, ProductInput patch pode não persistir; se houver promoção/compare-at oculta, pode sobrescrever lógica comercial.
- Rollback: snapshot dos Product resources/ProductInput antes do patch; rollback para valor anterior ou remoção do override.
- Validação: readback Content API + Merchant API; aguardar reprocessamento de status; checar issue clearance depois.
- Status: `needs_explicit_approval`.

### Packet B — P1 missing color por product_type

- Problema: `441` produtos demoted por atributo `color` ausente.
- Evidência: amostras Onitsuka/Nike/Pop Mart com página pública OK e preço batendo.
- Ação proposta: gerar CSV/preview com offerId, título, cor derivada do título/handle, confiança e campo `color`; aplicar via supplemental feed/ProductInput apenas nos high-confidence.
- Risco: cor inferida errada reduz qualidade do catálogo; deve haver amostra e revisão antes de write.
- Rollback: remover/sobrescrever o atributo no supplemental/ProductInput com snapshot anterior.
- Validação: Merchant productstatuses sem `missing_item_attribute_for_product_type` após reprocessamento.
- Status: `preview_allowed_now`; write exige aprovação.

### Packet C — landing/DRAFT/404 cleanup

- Problema: `17` landing errors e `16` missing required price ligados em parte a PDP `.js` 404.
- Evidência: amostra de vestuário retornou 404 público.
- Ação proposta: classificar cada offer entre `republicar Shopify`, `corrigir link`, `suppress/delete Merchant`, ou `monitor se voltou 200`.
- Risco: deletar/suprimir item que deveria voltar à venda; precisa confirmação comercial.
- Rollback: snapshot do product resource/feed row e lista de IDs; se suprimir/delete, reintroduzir via fonte original.
- Validação: products.list/productstatuses e público `.js`.
- Status: `needs_explicit_approval` para suppress/delete; triagem read-only liberada.

### Packet D — preço automático / strikethrough governance

- Problema: `479` produtos com `price_updated` e `285` com `strikethrough_price_updated`.
- Evidência: amostra mostra múltiplos padrões de preço final/sale/compare-at.
- Ação proposta: não fazer bulk retry. Separar em: preço final divergente, salePrice divergente, compare_at/strikethrough divergente, e false-positive/lag.
- Risco: patch amplo pode mexer em promoção errada e piorar Shopping.
- Rollback: snapshot por offerId; micro-piloto de no máximo 10 IDs após aprovação.
- Validação: readback + productstatuses após delay.
- Status: `blocked_pending_promo_logic`.

## Próximos passos seguros

1. Gerar preview CSV do Packet A com os 2 offers Adidas, Product resource atual, público `.js`, dataSource provável e rollback shape — sem patch.
2. Gerar preview deduplicado de `missing color` com confiança de cor inferida e separar `high-confidence` vs `needs human review`.
3. Rechecar os 17 `landing_page_error` com público HTML + `.js` + Shopify Admin read-only para separar DRAFT/404 de handle trocado.
4. Manter `strikethrough_price_updated` bloqueado até haver lógica promocional explícita.
5. Se Lucas aprovar um pacote, aplicar só o escopo aprovado, com snapshot, readback e revisão de impacto em ~7 dias.

## O que não foi feito

- Nenhum Content API write.
- Nenhum ProductInput PATCH.
- Nenhum supplemental feed write/upload/fetchNow.
- Nenhum Shopify write.
- Nenhum preço/estoque/desconto alterado.
- Nenhum reprocess/fetch que altere estado.
- Nenhuma campanha, envio externo ou contato com cliente/fornecedor.
