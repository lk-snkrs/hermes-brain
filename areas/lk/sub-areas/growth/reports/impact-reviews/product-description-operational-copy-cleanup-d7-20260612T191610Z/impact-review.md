# LK Growth Impact Review D+7 — Product Description Operational Copy Cleanup

Gerado em UTC: 2026-06-12T19:16:10Z

## Escopo

- Mudança analisada: limpeza customer-facing em `product.descriptionHtml/body_html`, `product.seo` e WhatsApp URL text, executada em 2026-06-05.
- Produtos/handles afetados reconstituídos do baseline/receipts: **679 handles únicos**.
- Operação desta revisão: **100% read-only**. Nenhum write em Shopify, GMC, GA4, GSC, theme, Klaviyo ou Ads.
- `values_printed=false`: nenhum secret/token foi impresso.

## Veredito

**Inconclusivo para SEO/orgânico em D+7; neutro-comercial com sinal Shopify positivo.**

A limpeza permaneceu aplicada e não apareceu regressão dos termos-alvo. O Shopify pós-7d dos produtos afetados subiu versus baseline 7d, mas GA4/GSC orgânico caiu em janelas comparáveis e GSC ainda sofre atraso de 2–3 dias. Não há evidência suficiente para atribuir melhora/piora orgânica à limpeza; também não há alerta material de queda comercial nos produtos afetados.

## Fatos verificados

### 1) QA de termos operacionais

- Produtos checados via Shopify Admin GraphQL query-only: **679 / 679**.
- Hits dos termos-alvo em `body_html`, `seo.title`, `seo.description`: **0**.
- Status: **PASS / sem regressão**.

Termos/padrões revalidados: `pronta entrega`, `produtos em estoque`, `Estoque próprio: envio`, `envio em 2 dias`, `Entrega SP`, `Envio SP`, WhatsApp `produto a pronta entrega`, e `roda/rodar/rodam` como copy residual.

### 2) Shopify — produtos afetados, pós 7d vs baseline 7d

| Métrica | Baseline 7d | Pós 7d | Delta | Delta % |
|---|---:|---:|---:|---:|
| Pedidos loja total | 85 | 98 | 13 | 15.3% |
| Receita loja total | 221700.21 | 247909.61 | 26209.4 | 11.8% |
| Pedidos com produto afetado | 24 | 32 | 8 | 33.3% |
| Unidades afetadas | 28 | 39 | 11 | 39.3% |
| Receita estimada linhas afetadas | 84554.72 | 105504.61 | 20949.89 | 24.8% |

Top 5 produtos afetados por receita pós-7d:

1. `tenis-nike-moon-shoe-sp-jacquemus-medium-brown` — 2 un. — R$ 11999.98
2. `tenis-nike-vomero-premium-alabaster-amarelo` — 2 un. — R$ 8999.98
3. `tenis-nike-moon-shoe-sp-jacquemus-off-noir-preto` — 1 un. — R$ 6999.99
4. `nike-moon-shoe-sp-jacquemus-alabaster-amarelo` — 1 un. — R$ 6999.99
5. `tenis-nike-moon-shoe-sp-jacquemus-off-white` — 1 un. — R$ 5999.99

### 3) GA4 — PDPs afetadas

- Janela comparável usada: baseline `2026-05-29` a `2026-06-04` vs pós `2026-06-06` a `2026-06-12`; rollout day excluído do baseline.
- Sessões: 15941 → 13317 (-16.5%).
- Usuários: 15208 → 12627 (-17.0%).
- Pageviews: 17183 → 14445 (-15.9%).

Limitação: o conector GA4 neste modo aceitou métricas de tráfego (`sessions`, `totalUsers`, `screenPageViews`) mas não retornou métricas de compra por `pagePath`; conversão comercial foi ancorada em Shopify read-only.

### 4) GSC — PDPs afetadas

- Janela comparável segura por atraso GSC: baseline `2026-05-31` a `2026-06-04` vs pós `2026-06-06` a `2026-06-10`.
- Cliques/dia: 48.8 → 37.2 (-23.8%).
- Impressões/dia: 8158.8 → 7861.4 (-3.6%).
- CTR: 0.6% → 0.47% (-0.13 p.p.).
- Posição ponderada: 5.84 → 6.07 (delta 0.23).

Limitação: GSC D+7 ainda não está completamente fechado; Search Analytics costuma ter atraso de 2–3 dias.

### 5) PageSpeed/CrUX — amostra PDP alto valor

- URL amostra: `https://lksneakers.com.br/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown`.
- PSI mobile Lighthouse: Performance 64, SEO 92, Accessibility 94, Best Practices 96.
- Lab LCP mobile: 6.1 s; CLS 0.002.
- CrUX URL-level da PDP: indisponível por volume; fallback origin-level mostrou LCP 1.38s, INP 95ms, CLS 0.0, todos `good`.

## Interpretação

- A limpeza de linguagem operacional foi preservada e reduziu risco de promessa customer-facing sem criar regressão textual.
- O sinal Shopify dos produtos afetados é positivo no pós-7d, mas não pode ser atribuído isoladamente à alteração de copy/SEO porque há mix de demanda, campanhas, social, sazonalidade e produto.
- GA4/GSC orgânico não confirmou melhora em D+7; a queda orgânica sugere acompanhar D+14 antes de qualquer nova alteração em massa.
- Não há evidência de que a remoção dos termos tenha prejudicado conversão comercial no curto prazo; também não há prova de ganho SEO.

## Recomendação

1. **Não executar novo write agora.** Aguardar D+14 com GSC completo e Shopify/GA4 por PDP.
2. Manter a regra editorial: não reintroduzir `pronta entrega`, `produtos em estoque`, `envio em 2 dias` ou promises similares em PDP/SEO/WhatsApp URL.
3. Se D+14 confirmar queda orgânica concentrada em poucos handles, preparar packet por PDP com proposta de copy demand-led/customer-safe — sem termos operacionais — e rollback por produto.

## Approval packet

- **Nenhum approval packet de correção foi gerado**, porque QA está PASS e não há regressão para corrigir.
- Qualquer novo ajuste de `product.descriptionHtml`, `product.seo`, theme, GMC/feed, Klaviyo ou campanha continua exigindo aprovação explícita atual de Lucas, com rollback e validação.

## Fontes/artefatos

- Diretório do relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact-reviews/product-description-operational-copy-cleanup-d7-20260612T191610Z`
- `shopify-qa-orders-ga4-gsc-summary.json`
- `ga4-affected-products-exact-7d-vs-baseline7d.json`
- `gsc-affected-products-comparable-5d.json`
- `pagespeed-mobile-sample-pdp.json`
- `tool-fallback-sample-pdp/impact-review.json`
