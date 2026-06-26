# LK GMC — Residuals next packets read-only 2026-05-14

Status: `residual_packets_readonly_ready_no_write`

## Escopo

Fonte principal: `reports/lk-gmc-2026-05-14-p2a-post-status-monitor.json` + `reports/lk-merchant-center-feed-readonly-router-2026-05-11.json`.

Modo: leitura/análise local. Nenhum write em Merchant, Shopify, Tiny, feed, campanhas ou clientes.

## Estado pós-P2A

- `productstatuses` lidos: 23.279
- IDs P2A esperados: 9.826
- IDs P2A encontrados: 9.826
- IDs ausentes: 0
- Produtos P2A com algum issue/destino reprovado: 494
- Issue instances P2A: 1.735
- Destinos reprovados em IDs P2A: 39 instâncias
- Writes permitidos agora: 0

## Residuals por prioridade operacional

### Pacote A — Landing page errors / reprovação real

Status: `readonly_url_probe_next`

- Issue: `landing_page_error`
- Instâncias: 36
- Severidade: alta, porque é `servability=disapproved` nos samples.
- Destinos reprovados totais P2A: 39 instâncias, distribuídos em Shopping, DisplayAds e SurfacesAcrossGoogle.
- Ação segura agora: probe read-only das URLs dos IDs afetados para classificar 200/404/redirect/bloqueio/crawl.
- Não fazer ainda: editar link, produto, Shopify, feed ou Merchant.

Sample:
- `online:pt:BR:10002025469927148791` — Calça Nude Project Jeans Soft Velvet Azul Marinho — `Product page unavailable`.

### Pacote B — Missing attributes para product type

Status: `approval_packet_can_be_prepared_after_sampling`

- Issue: `missing_item_attribute_for_product_type`
- Instâncias: 136
- Atributos:
  - color: 128
  - age group: 4
  - gender: 4
- Severidade: média/alta: geralmente `servability=demoted`, não necessariamente reprovação.
- Ação segura agora: montar preview por produto com sugestão determinística:
  - cor a partir de título/token em português/inglês;
  - `ageGroup=adult` quando aplicável;
  - `gender=unisex` quando aplicável.
- Precisa aprovação antes de write Merchant.

Sample:
- `online:pt:BR:fv5029-100` — Tênis Nike Air Jordan 4 Retro OG Nike White Cement Couro Branco — faltando `color`.
- `online:pt:BR:dc0774-0211` — Tênis Nike Air Jordan 1 Low Black Brown Marrom — faltando `color`.

### Pacote C — Price / strikethrough price updated

Status: `monitor_first_then_price_v1_packet_if_needed`

- Issues:
  - `price_updated`: 987
  - `strikethrough_price_updated`: 468
- Severidade observada: `servability=unaffected` nos samples.
- Interpretação: Google já corrigiu automaticamente com base na landing page/loja.
- Ação segura agora: não fazer write imediato; separar amostra e confirmar se é divergência de preço Merchant vs Shopify/landing atual.
- Se persistente e relevante: usar Merchant API ProductInputs v1 `productAttributes.price`, nunca Content API v2.1, e somente com rollback/aprovação.

Sample:
- `online:pt:BR:BQ6472105-2` — Tênis Nike Air Jordan 1 Mid Wolf Grey Cinza — automatic price + strikethrough price update.

### Pacote D — GTIN restricted/reserved/coupon

Status: `manual_review_or_gtin_policy_packet_later`

- Issues:
  - `restricted_gtin`: 68
  - `reserved_gtin`: 4
  - `coupon_gtin`: 2
- Severidade observada: `servability=unaffected` nos samples.
- Ação segura agora: não mexer automaticamente; criar pacote específico para validar se GTIN deve ser removido/corrigido por evidência confiável.
- Risco: GTIN falso/errado pode prejudicar qualidade, mas inventar GTIN é pior.

### Pacote E — imagens

Status: `media_quality_review_later`

- Issues:
  - `image_single_color`: 6
  - `image_link_broken`: 6
  - `image_too_small_for_high_resolution`: 2
- Ação segura agora: revisar URLs de imagem e origem Shopify/feed em read-only; sem upload/troca de mídia.

### Pacote F — pause expired

Status: `manual_policy_later`

- Issue: `pause_expired`: 2
- Ação segura agora: revisar intenção comercial. Não remover pause automaticamente.

## Ordem recomendada

1. `GMC_A_URL_PROBE`: rodar probe read-only das 36 instâncias `landing_page_error`/IDs com destinos reprovados.
2. `GMC_B_COLOR_ATTR_PREVIEW`: montar preview de 128 cores + 4 age group + 4 gender, sem write.
3. `GMC_C_PRICE_MONITOR`: amostra de preço/strikethrough; confirmar se Google já mitigou e se vale pacote Merchant v1.
4. `GMC_D_GTIN_POLICY`: revisar GTIN inválido como pacote separado.
5. Imagem/pause depois.

## Não executado

- merchant_center_write
- product_patch
- product_delete
- feed_update
- shopify_write
- tiny_write
- campaign_or_customer_send
- marketplace_lookup adicional
