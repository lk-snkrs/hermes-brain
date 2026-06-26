# LK Growth — Merchant/Product Data Ranking Review — 2026-06-18

Gerado em: `2026-06-18T11:36:09.404807+00:00`  
Modo: `read-only / preview`  
Writes executados: `0`  
values_printed=false

## Veredito executivo

- Leitura Merchant autenticada: `23744` products e `23744` productstatuses. Decision-grade para saúde GMC/product data; parcial para priorização comercial por SKU porque este run não cruzou GA4/Shopify revenue.
- Shopping aprovado/reprovado: `12181` / `11563` produtos. LocalSurfaces aprovado/reprovado: `986` / `10582`.
- Maior gargalo segue `missing_item_attribute_for_product_type`: `2530` produtos / `5314` instâncias; Δ produtos vs 2026-06-11: `-47`.
- Packet prioritário da semana: `mhlsf_full_missing_valid_link_template` em `11267` offers (`1000` linhas no CSV), típico de Local Inventory/LIA `link_template`/store_code — não é 404/preço/PDP.

## Evidência por issue

| Issue | Produtos | Instâncias | Δ produtos vs 11/06 | Impacto ranking/elegibilidade |
|---|---:|---:|---:|---|
| `missing_item_attribute_for_product_type` | 2530 | 5314 | -47 | Demotion/elegibilidade Shopping por atributo de produto incompleto, principalmente cor/tipo. |
| `local_stores_lack_inventory` | 10582 | 21164 | 9396 | Reprovação Local/LIA; não usar como SEO/CRO nem consultar estoque direto. |
| `mhlsf_full_missing_valid_link_template` | 11267 | 11267 | 10802 | Local offers sem link_template válido; bloqueia veiculação local/Shopping. |
| `strikethrough_price_updated` | 55 | 165 | 7 | Google corrigindo preço riscado; risco de governança promocional/overwrite. |
| `price_updated` | 20 | 60 | 1 | Google corrigindo preço final; checar origem antes de write. |
| `restricted_gtin` | 35 | 70 | 0 | Identificador restrito; não inferir GTIN. |
| `reserved_gtin` | 2 | 4 | 0 | Identificador reservado; não inferir GTIN. |
| `item_missing_required_attribute` | 6 | 12 | -26 | Atributo obrigatório ausente; pode bloquear destinos. |
| `landing_page_error` | 9 | 22 | -7 | Landing não servível; triagem por link/publicação/supressão. |
| `image_link_internal_error` | 0 | 0 | -2 | Imagem com erro de processamento; checar feed/imagem. |
| `image_too_small_for_high_resolution` | 1 | 1 | 0 | Qualidade de imagem abaixo do ideal para Shopping. |
| `image_single_color` | 4 | 10 | 0 | Imagem com risco de baixa qualidade visual. |
| `condition_updated_from_detected` | 4 | 8 | 0 | Google inferiu condição; atributo deve ser confirmado. |

## Produto/schema e consistência Shopify ↔ GMC

- Data source probe: `ok`; nomes/IDs expostos apenas como metadado não sensível: `lksneakers.com.br, Simprosys Local Feed (Merchant API), Simprosys Feed (Merchant API)`.
- Schema spot-check público `https://lksneakers.com.br/products/tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom`: HTTP `200`, JSON-LD `4`, Product `1`, Offer `10`, AggregateRating `1`, BreadcrumbList `1`, FAQPage `1`. Sem write; a checagem confirma Product/Offer básico, mas FAQ/schema não substitui correção GMC do `link_template`.
- Landing samples: `8` checadas por `.js`; ver JSON para status por offer. Disponibilidade pública foi tratada só como dado técnico; estoque operacional não foi consultado.

## Approval packet recomendado — Local Inventory link_template

- **Offers/SKUs afetados:** `11267` produtos/offers; amostra e CSV: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-link-template-packet-2026-06-18.csv`.
- **Issue/fonte:** Merchant itemLevelIssue `mhlsf_full_missing_valid_link_template`; mensagem exige valor válido em `link_template` para servir offer local/store code.
- **Impacto:** reduz elegibilidade Shopping/LocalSurfaces para ofertas `local`/`LIA_*`; corrige ranking/visibilidade local sem mexer em copy pública.
- **Ação proposta:** micro-piloto de 10–20 offers para descobrir/aplicar o menor surface correto: configuração Simprosys Local Feed/dataSource local ou ProductInput local-offer field se não for sobrescrito.
- **Risco de overwrite:** alto se aplicado fora do surface dono; Simprosys/API feed pode sobrescrever ProductInput no próximo sync.
- **Rollback/validação:** snapshot antes/depois por offer; reverter/remover `link_template` no mesmo surface; validar por readback Merchant/Content API e reprocessamento. Não usar `fetchNow` sem aprovação.
- **Aprovação necessária:** qualquer GMC/feed/ProductInput/dataSource/Simprosys write, fetch/reprocess ou Shopify write exige aprovação explícita atual de Lucas.

## Packet secundário — cor/atributo de produto

- `missing_item_attribute_for_product_type`: preview local em `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-missing-color-preview-2026-06-18.csv` com `1057` high-confidence, `1240` medium e `233` revisão humana.
- Aplicar só linhas aprovadas e de alto impacto comercial; não corrigir em massa sem priorização Shopify/GA4/GSC.

## Amostras

| Offer | Issue | Título | Link |
|---|---|---|---|
| `LIA_JI0324-6` | `mhlsf_full_missing_valid_link_template` | Tênis Adidas Gazelle Indoor Maroon Almost Yellow Marrom | https://lksneakers.com.br/products/tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom |
| `LIA_OXV-2785246-39` | `mhlsf_full_missing_valid_link_template` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown Blue Marrom | https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-blue-marrom |
| `LIA_SLCRCVOW-1` | `mhlsf_full_missing_valid_link_template` | Camiseta Slyce Racquet Club Off White | https://lksneakers.com.br/products/camiseta-slyce-racquet-club-off-white |
| `LIA_f99715` | `mhlsf_full_missing_valid_link_template` | Tênis Adidas Yeezy Boost 350 V2 Sesame Cinza | https://lksneakers.com.br/products/tenis-adidas-yeezy-boost-350-v2-sesame-cinza |
| `5706324928133224313` | `landing_page_error, landing_page_error, landing_page_error` | Tênis New Balance 204L x Atmos Cow Girl Brown Marrom - Tamanho 39 | https://lksneakers.com.br/products/tenis-new-balance-204l-x-atmos-cow-girl-brown-marrom |
| `16066821251494448304` | `landing_page_error, landing_page_error, item_missing_required_attribute, item_missing_required_attribute` | 39 | https://lksneakers.com.br/products/tenis-new-balance-204l-raincloud-ash-wood-cinza |
| `555088036` | `restricted_gtin, restricted_gtin` | Tênis Nike Air Jordan 1 High OG Starfish Laranja | https://lksneakers.com.br/products/air-jordan-1-high-og-starfish |
| `DD1503601-39` | `restricted_gtin, restricted_gtin` | Tênis Nike Dunk Low Pink Oxford Rosa | https://lksneakers.com.br/products/nike-dunk-low-pink-oxford |

## Limites e não-ações

- Não consultei Tiny/estoque e não usei disponibilidade como decisão comercial.
- Não executei Shopify, theme, GMC/feed, ProductInput, datafeed, `fetchNow`, preço, desconto, campanha, Klaviyo ou WhatsApp.
- DataForSEO/SERP não foi chamado nesta execução para evitar custo sem necessidade: o achado material veio de GMC autenticado.
