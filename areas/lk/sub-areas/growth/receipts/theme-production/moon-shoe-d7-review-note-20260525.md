# D+7 Impact Review — Moon Shoe Collection Publish

- Data do publish: 2026-05-25
- Revisão sugerida: 2026-06-01
- URL: https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp
- Mudança publicada: bloco editorial Moon Shoe em produção, guia editorial após produtos, FAQ único, alinhamento mobile Guia/FAQ em 22px.
- Recibos:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/moon-shoe-publish-20260525-134350/receipt.json`
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/moon-shoe-after-grid-guide-20260525-134708/receipt.json`

## Checklist D+7

- Verificar URL pública com cache-busting.
- Confirmar ordem: Hero > Produtos > Guia editorial > Perguntas Frequentes.
- Confirmar ausência de termos públicos proibidos: estoque, encomenda, pronta entrega.
- Se houver dados autenticados disponíveis: comparar sessões, cliques GSC, CTR, posição, add-to-cart/checkout e receita da coleção.
- Se dados autenticados faltarem, marcar análise como não decision-grade.
- Recomendar manter, ajustar ou reverter.

## Rollback

- Reverter `sections/lk-collection.liquid` usando os arquivos `production.before.liquid` dos receipts acima, começando pelo receipt mais recente se necessário.
