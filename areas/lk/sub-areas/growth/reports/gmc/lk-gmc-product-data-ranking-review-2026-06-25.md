# LK Growth — Merchant/Product Data Ranking Review — 2026-06-25

Gerado em: `2026-06-25T11:34:17.942917+00:00`  
Modo: `read-only / preview`  
values_printed=false  
Writes executados: `0`

## Veredito executivo

- Leitura GMC autenticada: `21805` products e `21805` productstatuses. Decision-grade para saúde Merchant/product data; parcial para priorização comercial SKU por SKU porque GA4/Shopify revenue não foi cruzado nesta rotina.
- Destinos agregados: `33048` aprovações e `501` reprovações por destination/status.
- Gargalo material novo: `landing_page_error` com `161` produtos / `483` instâncias (`+152` produtos vs 18/06); prioridade desta quinta é micro-triagem de links Merchant/Shopping, não HTML público.
- Schema spot-check em `https://lksneakers.com.br/products/tenis-nike-x-skims-rift-mesh-light-bone-bege`: status `http_200`, Product `True`, Offer `11`, AggregateRating `1`, Breadcrumb `1`.

## Evidência por issue

| Issue | Produtos | Instâncias | Δ produtos vs 18/06 | Impacto |
|---|---:|---:|---:|---|
| `mhlsf_full_missing_valid_link_template` | 0 | 0 | -11267 | Local offers sem link_template válido; bloqueia/derruba elegibilidade local/Shopping em massa. |
| `missing_item_attribute_for_product_type` | 17 | 34 | -2513 | Atributo de produto ausente; reduz qualidade/elegibilidade no Shopping e pode afetar matching orgânico/merchant. |
| `local_stores_lack_inventory` | 18 | 18 | -10564 | Local/LIA sem inventário por loja; não usar como decisão de estoque, mas afeta LocalSurfaces. |
| `strikethrough_price_updated` | 37 | 111 | -18 | Google corrigiu preço riscado; sinal de governança promocional/source overwrite. |
| `price_updated` | 16 | 48 | -4 | Google corrigiu preço final; sinal de feed/source stale. |
| `landing_page_error` | 161 | 483 | +152 | Landing não servível; bloqueia ofertas até correção/supressão/republicação validada. |
| `item_missing_required_attribute` | 0 | 0 | -6 | Atributo obrigatório ausente; pode bloquear destinos. |
| `restricted_gtin` | 32 | 64 | -3 | GTIN restrito/inválido; pode limitar rich/shopping matching. Não inferir GTIN. |
| `reserved_gtin` | 2 | 4 | 0 | GTIN reservado/inválido; exige validação oficial. |
| `image_too_small_for_high_resolution` | 1 | 1 | 0 | Imagem abaixo do ideal para Shopping. |
| `image_single_color` | 4 | 8 | 0 | Imagem com risco de baixa qualidade visual. |
| `condition_updated_from_detected` | 0 | 0 | -4 | Google inferiu condição; confirmar atributo no source correto. |
| `image_link_internal_error` | 0 | 0 | 0 | Erro de processamento de imagem; monitorar/rechecar. |

## Packet prioritário recomendado — landing_page_error

- **Issue/evidência/fonte:** `landing_page_error` subiu para `161` produtos / `483` instâncias (`+152` produtos vs 18/06). CSV preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-landing-page-error-packet-2026-06-25.csv`.
- **Public check limitado:** 80 URLs `.js` checadas; status `ok=58`, `http_404=2`, `http_429=20`. Como muitas URLs públicas ainda respondem OK, o problema parece misturar feed/source/reprocessamento/cache e alguns 404 reais — não é correção cega de PDP.
- **Impacto:** reprovação em Shopping, DisplayAds e SurfacesAcrossGoogle; bloqueia visibilidade Merchant/Shopping mais do que os 17 casos de missing attribute.
- **Ação proposta:** aprovar micro-triagem de 20–50 offers para classificar `Shopify 404/despublicado`, `link de feed antigo`, `cache/reprocessamento`, `produto a suprimir` ou `falso positivo`, corrigindo somente no menor surface dono.
- **Risco de overwrite:** médio/alto se ProductInput for corrigido enquanto Simprosys/API continuar enviando link antigo.
- **Rollback/validação:** snapshot do Product resource/source antes, readback do Product link e productstatuses depois; sem delete/suppress/`fetchNow` sem aprovação separada.

## Packets secundários — invalid_color e atributos/cor

- `invalid_color`: `146` produtos / `292` instâncias; CSV preview: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-invalid-color-packet-2026-06-25.csv`. Corrigir por agrupamento de produto/handle e só quando a cor canônica for inequívoca.
- `missing_item_attribute_for_product_type`: `17` linhas no preview `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-missing-color-preview-2026-06-25.csv`; high-confidence `12`, medium `0`, revisão humana `5`.
- Ação segura: aplicar só linhas high-confidence aprovadas e comercialmente relevantes via menor surface reversível; ambíguas ficam bloqueadas até curadoria.

## Consistência Shopify ↔ GMC e schema

- Public `.js` spot-check executado apenas como evidência técnica; disponibilidade pública não foi usada como decisão de estoque e Tiny/stock não foi consultado.
- Schema Product/Offer/AggregateRating/Breadcrumb existe no spot-check, então a prioridade de ranking/elegibilidade desta rodada é GMC product-data/local feed, não schema estrutural.
- Data sources lidos em modo read-only; surface provável continua Simprosys Local Feed / Merchant API local inventory.

## Cobertura 18 tópicos nesta rotina

- Cobertos: GMC, catálogo/product data quality, schema spot-check, Shopify public read-only técnico, impact/experimentation via packet+rollback.
- Parciais/não aplicáveis nesta quinta: GA4, GSC, Shopify CRO, GEO/AI Search, PageSpeed/CrUX, reviews, paid/influencer, concorrência/SERP, Google Business/local, Klaviyo/CRM, QA de eventos. Não escondi a limitação: esta rotina é decision-grade para GMC/product data, não para revenue priority completa.

## Approval necessário

- Qualquer GMC/feed/ProductInput/dataSource/Simprosys write, `fetchNow`, Shopify write, preço/desconto/estoque, theme, Ads, Klaviyo, WhatsApp ou envio externo exige aprovação explícita atual.
- Frase segura para o packet principal: `aprovado GMC landing_page_error micro-triagem 20-50 offers com snapshot readback e rollback`.

## O que não foi feito

- Não executei writes externos; não consultei estoque; não alterei Shopify/GMC/feed/campanhas; não imprimi secrets/tokens.
