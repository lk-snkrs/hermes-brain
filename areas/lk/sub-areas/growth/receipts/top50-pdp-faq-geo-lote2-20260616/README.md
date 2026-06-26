# Receipt — Lote 2 Top 50 PDP FAQ/GEO

Data: 2026-06-16T17:53:35.133265+00:00

## Escopo aprovado/executado
- 10 PDPs do Lote 2 por receita 90d, excluindo Lote 1.
- Alteração aplicada: `descriptionHtml` dos produtos via Shopify Admin API.
- Não alterado: preço, estoque, variantes, theme, campanhas, Klaviyo, GMC, SEO title/meta.

## Resultado
- Shopify Admin readback: 10/10 com conteúdo novo e validação normalizada exata.
- HTML público: 10/10 com pelo menos 3 perguntas novas detectadas.
- Quality flags no bodyHtml aplicado: 0.
- Valores de secrets: não impressos (`values_printed=false`).

## Produtos atualizados
- `nike-moon-shoe-sp-jacquemus-alabaster-amarelo` — Admin OK: True; público FAQ hits: 4/4; chars: 1650
- `tenis-onitsuka-tiger-mexico-66-sd-beige-beet-juice-bege` — Admin OK: True; público FAQ hits: 4/4; chars: 1595
- `tenis-new-balance-9060-mushroom-arid-stone-camurca` — Admin OK: True; público FAQ hits: 4/4; chars: 1486
- `slide-nike-mind-001-black-chrome-preto` — Admin OK: True; público FAQ hits: 4/4; chars: 1450
- `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege` — Admin OK: True; público FAQ hits: 4/4; chars: 1635
- `tenis-new-balance-204l-sea-salt-linen-bege` — Admin OK: True; público FAQ hits: 4/4; chars: 1439
- `tenis-nike-moon-shoe-sp-jacquemus-pale-pink-rosa` — Admin OK: True; público FAQ hits: 4/4; chars: 1644
- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo` — Admin OK: True; público FAQ hits: 4/4; chars: 1587
- `tenis-new-balance-9060-rich-oak-marrom` — Admin OK: True; público FAQ hits: 4/4; chars: 1468
- `new-balance-9060-triple-white` — Admin OK: True; público FAQ hits: 4/4; chars: 1476

## Evidência local
- Backup before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/lote2-apply-20260616T175125Z/before-readback.json`
- Payload corrigido: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/lote2-apply-20260616T175125Z/lote2-proposed-payload.corrected.json`
- Apply results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/lote2-apply-20260616T175125Z/apply-results.json`
- Readback after: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/lote2-apply-20260616T175125Z/after-readback-corrected.json`
- Verificação pública: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/lote2-apply-20260616T175125Z/public-fetch-verification-corrected.json`

## Pendência separada detectada
- O HTML público tem FAQ global de PDP/theme com frase: “Produtos sob encomenda: 4 a 6 semanas”.
- Isso não veio do bodyHtml do Lote 2; apareceu em bloco global `pi-faq`.
- Recomendação: abrir pacote separado para remover linguagem operacional de disponibilidade/prazo do FAQ global do PDP, em dev/preview antes de production theme.

## Rollback
- Reverter `descriptionHtml` dos 10 produtos a partir do backup `before-readback.json`.
- Rollback pode ser feito por mutation `productUpdate` em cada `id` com `descriptionHtml` anterior.

## Review de impacto
- Reavaliar em ~7 dias: 2026-06-23
- Métricas: PDP sessions, add_to_cart, conversion rate, revenue, GSC impressions/clicks para queries produto/modelo, e indexação/trechos de FAQ.