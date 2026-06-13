# Klaviyo Tracking QA — metric duplicates / 2026-06-12

Generated: `2026-06-12T12:06:47Z`

Modo: read-only. Nenhum flow, campaign, list, segment, profile, send, Shopify, GMC ou Ads alterado. `values_printed=false`.

Período consultado: `2026-06-05T12:06:26+00:00` a `2026-06-12T12:06:26+00:00` UTC.

## Achado principal

- Os zeros anteriores não significam ausência real de evento onsite/order. A conta tem métricas duplicadas com o mesmo nome; o script antigo pegava a primeira métrica por nome e, para alguns eventos, caiu em métricas API novas/zeradas.

- Métricas canônicas/ativas mostram eventos ecommerce no período: `Placed Order` Shopify e `Added to Cart` Shopify têm volume; `Active on Site` API antigo também tem volume.

- Ainda existe anomalia de instrumentação/mapeamento: há métricas API duplicadas zeradas criadas em 2025/2026 para `Placed Order`, `Added to Cart` e `Active on Site`. Isso pode confundir relatórios e automações se filtrarem só por nome.

## Métricas encontradas — 7 dias

- Active on Site / API / created `2026-03-16T17:42:42+00:00`: count `0` / unique `0`
- Active on Site / API / created `2024-08-16T01:20:33+00:00`: count `723` / unique `566`
- Placed Order / API / created `2025-06-12T20:17:57+00:00`: count `0` / unique `0`
- Added to Cart / API / created `2025-06-12T15:49:30+00:00`: count `0` / unique `0`
- Clicked Email / Klaviyo / created `2024-08-16T01:20:33+00:00`: count `435` / unique `316`
- Placed Order / Shopify / created `2024-08-16T01:20:33+00:00`: count `100` / unique `95`
- Started Checkout / API / created `2025-06-12T15:26:44+00:00`: count `53` / unique `4`
- Opened Email / Klaviyo / created `2024-08-16T01:20:34+00:00`: count `22763` / unique `14184`
- Added to Cart / Shopify / created `2024-10-14T23:05:14+00:00`: count `216` / unique `123`
- Received Email / Klaviyo / created `2024-08-16T01:20:34+00:00`: count `29010` / unique `23635`

## Leitura operacional

- Email engagement está OK: received/opened/clicked têm volume consistente.

- Ecommerce Klaviyo não está zerado quando a métrica correta é usada: `Placed Order` Shopify = 100 eventos / 95 únicos; `Added to Cart` Shopify = 216 / 123.

- `Started Checkout` aparece como API com 53 eventos / 4 únicos; deve ser validado contra Shopify/GA4 antes de usar como verdade de funil.

- Para decisão comercial, Klaviyo segue como sinal auxiliar; causalidade e receita devem ser reconciliadas com Shopify/GA4.

## Correção local aplicada

- Script local `/opt/data/profiles/lk-growth/scripts/lk_klaviyo_readonly_analytics.py` ajustado para não deduplicar métricas só por nome e para expor integração/criação no output.

- Backup local: `/opt/data/profiles/lk-growth/scripts/lk_klaviyo_readonly_analytics.py.bak_20260612_metric_duplicates`.

- Verificação: `py_compile` OK e rerun read-only retornou 10 métricas-alvo.

## Próximo passo recomendado

- Usar nos relatórios apenas a métrica por integração correta: Email = Klaviyo; Placed Order/Added to Cart = Shopify; Active on Site/Viewed Product = API legado com volume.

- Se quiser limpar a causa raiz, preparar approval separado para revisar integração/mapeamento Klaviyo/Shopify; não fiz nenhum ajuste externo.

