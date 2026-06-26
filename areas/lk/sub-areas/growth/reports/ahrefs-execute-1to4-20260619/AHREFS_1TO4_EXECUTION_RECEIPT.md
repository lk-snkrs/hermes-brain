# LK Growth — Ahrefs 1 to 4 execution receipt — 2026-06-19

- Escopo aprovado por Lucas: “FAZER DO 1 AO 4”.
- Writes Shopify/theme executados com rollback; nenhum write em estoque/Tiny/GMC/GA4/GSC/ads/Klaviyo.
- values_printed=false; secrets não impressos.

## Execução

- Product SEO titles/descriptions atualizados: `172` produtos.
- Collection SEO titles/descriptions atualizadas: `4` collections.
- Alt text audit/patch: `4` produtos checados; imagens já tinham alt no Shopify, e validação pública mostrou missing_alt=0 nas páginas testadas.
- Página de links internos criada: `/pages/curadoria-lk-produtos`, com `194` links de produtos orphan/canonical.
- Footer production/dev recebeu link visível para “Curadoria de produtos”.

## Verificação pública

- `https://lksneakers.com.br/products/chinelo-havaianas-x-dolce-gabanna-blue-mediterraneo-azul`: status `200`, title_len `54`, desc_len `154`, missing_alt `0`, curadoria_link `True`
- `https://lksneakers.com.br/collections/roupas`: status `200`, title_len `22`, desc_len `108`, missing_alt `0`, curadoria_link `True`
- `https://lksneakers.com.br/collections/lululemon`: status `200`, title_len `44`, desc_len `138`, missing_alt `0`, curadoria_link `True`
- `https://lksneakers.com.br/pages/curadoria-lk-produtos`: status `200`, title_len `46`, desc_len `118`, missing_alt `0`, curadoria_link `True`, product_links `195`
- `https://lksneakers.com.br/`: status `200`, title_len `53`, desc_len `144`, missing_alt `0`, curadoria_link `False`

## Ahrefs / recrawl

- O snapshot Ahrefs disponível pela API ainda é o crawl antigo de 2026-06-18T19:46:19Z; por isso os contadores Ahrefs não podem cair até novo crawl.
- Foi feita validação pública/Shopify das mudanças. A queda em Ahrefs depende de recrawl externo.
- Durante recheck agressivo com HEAD/GET em massa, Shopify/CDN retornou 429; esse resultado não foi usado como prova de broken links reais.

## Rollback / evidência

- Rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619/shopify-rollback-before-1to4.json`
- Execution receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619/shopify-execution-receipt.json`
- Public verify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619/post-1to4-public-verify.json`
- Ahrefs live issue pulls: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619`

## Reminder OS

- Reminder OS loop needed: yes
- Reminder OS owner: lk-growth
- Reminder OS next action: após próximo crawl Ahrefs, comparar contadores de Page has links to broken page, title/meta warnings, missing alt, orphan e canonical no incoming; se persistirem, gerar lote 2 com URLs restantes reais.
- Reminder OS review trigger: novo email/crawl Ahrefs ou em 24h.
- Reminder OS evidence: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619/shopify-execution-receipt.json` + `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-execute-1to4-20260619/post-1to4-public-verify.json`
