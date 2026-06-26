# Klaviyo Tracking Diagnostic — 2026-06-08

Generated: `2026-06-08T19:27:49.949367+00:00`

KLAVIYO_API_KEY present: `True`
Metrics endpoint status: `200`

Modo: read-only / nenhum flow, campaign, list, segment ou send alterado

## Target metrics encontrados
- Active on Site: `True`
- Viewed Product: `True`
- Added to Cart: `True`
- Started Checkout: `True`
- Placed Order: `True`
- Clicked Email: `True`
- Opened Email: `True`

## Aggregates 28 dias
- Active on Site: status `200`, count approx `2822.0`
- Placed Order: status `200`, count approx `348.0`
- Added to Cart: status `200`, count approx `651.0`
- Clicked Email: status `200`, count approx `1033.0`
- Started Checkout: status `200`, count approx `422.0`
- Opened Email: status `200`, count approx `59490.0`
- Viewed Product: status `200`, count approx `6183.0`

## Diagnóstico inicial
- A API Klaviyo está acessível em read-only e lista métricas.
- Métricas de email existem na conta.

## Próximos passos

- Se ecommerce events estão ausentes ou zerados, checar snippet onsite/Shopify integration e mapping de eventos.
- Não corrigir tracking em produção sem approval, porque pode afetar customer-facing/CRM data.