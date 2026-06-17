# Receipt — Lote 2 Top 50 PDP FAQ/GEO/CRO

Executado em: 2026-06-16T18:30:42.447992+00:00

## Status
- Aprovação recebida de Lucas: sim, no turno atual.
- Shopify production PDP body/SEO: aplicado nos 10 produtos finais.
- Theme production: não alterado.
- GMC/feed/campanhas/Klaviyo: não alterados.
- Valores de secrets: não impressos (`values_printed=false`).

## Produtos aplicados
- `nike-moon-shoe-sp-jacquemus-alabaster-amarelo`
- `tenis-new-balance-9060-mushroom-arid-stone-camurca`
- `tenis-new-balance-9060-rich-oak-marrom`
- `new-balance-9060-triple-white`
- `slide-nike-mind-001-black-chrome-preto`
- `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-brown-bege`
- `tenis-new-balance-204l-sea-salt-linen-bege`
- `tenis-onitsuka-tiger-mexico-66-brich-peacoat-bege`
- `tenis-onitsuka-tiger-mexico-66-sd-beige-beet-juice-bege`
- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo`

## Evidência
- Apply results: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/apply-results.json`
- Backup before: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/backup-before.json`
- Readback after: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/readback-after.json`
- Readback QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/readback-qa.json`
- Public fetch QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/public-fetch-qa.json`
- Rollback script preparado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/apply-lote2-20260616T182807Z/rollback_lote2_from_backup.py`

## QA
- Shopify Admin readback: OK — body, SEO title e SEO description batem com os drafts; termos operacionais proibidos nos campos editados: 0.
- `/products/handle.js`: confirmado atualizado por amostragem; descrição nova presente e sem termos proibidos.
- HTML público: SEO/meta já reflete parte dos updates; porém o HTML ainda contém um FAQ global do PDP com: `Produtos sob encomenda: 4 a 6 semanas.`

## Ressalva importante
O termo operacional remanescente não vem dos campos de descrição/SEO aplicados agora. Ele aparece em um bloco global de FAQ do tema PDP (`Qual o prazo de entrega?`) e afeta os 10 PDPs. Remover isso exige alteração de theme production ou seção global, que não estava incluída na aprovação deste item.

## Rollback
Rollback preparado com backup anterior. Execução de rollback só deve ocorrer se Lucas aprovar explicitamente ou se houver falha crítica de conversão/render.

## Próxima recomendação
Criar approval separado para corrigir o FAQ global do PDP, trocando o texto operacional por algo premium e seguro: `O prazo varia conforme região e confirmação do pedido. A equipe LK orienta pelo chat quando houver qualquer dúvida antes da compra.`

## Impact review
Revisar em aproximadamente 7 dias: GSC queries/PDPs, GA4 PDP→cart, conversão por produto, Search Console CTR e presença de FAQ/AI snippets.