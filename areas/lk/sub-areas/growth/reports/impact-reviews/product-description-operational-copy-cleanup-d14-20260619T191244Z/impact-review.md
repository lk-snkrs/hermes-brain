# LK Growth — Impact Review D+14 limpeza de termos operacionais — 2026-06-19

- Read-only: true; values_printed=false.
- Handles reconstituídos: 679 únicos.
- Janela completa disponível usada para Shopify/GSC: 2026-06-06 a 2026-06-18; Shopify até horário do cron também salvo. GA4 D+14 ficou bloqueado por permissão 403 da propriedade.

## QA
- Status: regression_or_incomplete; checados: 679/679; missing_nodes: 0; hits: 172.
- Regressão encontrada: {'envio_imediato': 172} em {'seo_description': 172}; padrão principal `envio imediato` em `product.seo.description`.

## Shopify
- Pós D+14 completo disponível: 54 pedidos afetados, 64 unidades, R$ 170836.76.
- Comparação baseline14: {"affected_orders": {"current": 54, "baseline": 62, "delta": -8.0, "delta_pct": -12.9}, "affected_units": {"current": 64, "baseline": 72, "delta": -8.0, "delta_pct": -11.1}, "affected_line_item_revenue_estimate": {"current": 170836.76, "baseline": 219404.28, "delta": -48567.52, "delta_pct": -22.1}, "orders": {"current": 156, "baseline": 168, "delta": -12.0, "delta_pct": -7.1}, "non_cancelled_revenue_total_price": {"current": 419997.45, "baseline": 466653.33, "delta": -46655.88, "delta_pct": -10.0}}
- Top receita: tenis-nike-moon-shoe-sp-jacquemus-off-white, tenis-nike-moon-shoe-sp-jacquemus-medium-brown, tenis-nike-vomero-premium-alabaster-amarelo, tenis-new-balance-204l-mushroom-arid-stone-marrom, tenis-new-balance-9060-rich-oak-marrom.

## GA4/GSC
- GA4: bloqueado por permissão 403; relatório não é 100% decision-grade em GA4 até regularizar acesso.
- GSC completo 2026-06-06..2026-06-18: 436 cliques / 113602 impressões em 1235 páginas afetadas.
- Top perda GSC: short-alo-yoga-match-point, tenis-nike-travis-scott-x-jordan-jumpman-jack-tr-university-red, tenis-adidas-samba-disney-101-dalmatians-penny-branco, tenis-travis-scott-x-nike-air-jordan-1-retro-low-og-sp-olive-suede, tenis-nike-vomero-premium-white-bright-crimson-branco.

## Obrigatórios salvos
- Top 20 receita Shopify: `shopify-orders-d14-readonly.json` → `post_14d_complete_available.affected_product_revenue_top20`.
- Top 20 perda cliques GSC: `gsc-affected-comparison-d14.json` → `top20_click_loss_vs_baseline28_prorated`.
- Top 20 queda CTR: `gsc-affected-comparison-d14.json` → `top20_ctr_drop_vs_baseline28`.
- Produtos venda subindo/tráfego caindo: `impact-review-summary.json` → `products_sales_up_traffic_down`.
- Approval packet: `approval-packet-if-needed.md`.

## Veredito
NÃO executar correção automática: há regressão QA em SEO description; precisa approval packet. Comercialmente, Shopify D+14 completo disponível caiu vs baseline14, mas D+7 tinha subido; GSC não mostra concentração material suficiente para culpar a limpeza isoladamente sem GA4.

## Erros/limitações
["ga4:<HttpError 403 when requesting https://analyticsdata.googleapis.com/v1beta/properties/253411115:runReport?alt=json returned \"User does not have sufficient permissions for this property. To learn more about Property ID, see https://developers.google.com/analytics/devguides/reporting/data/v1/property-id.\". Details: \"User does not have sufficient permissions for this property. To learn more about Property ID, see https://developers.google.com/analytics/devguides/reporting/data/v1/property-id.\">", "pagespeed:HTTPSConnectionPool(host='www.googleapis.com', port=443): Read timed out. (read timeout=90)", "shopify_qa:regression_or_incomplete"]
