# Approval packet — Piloto V2 auto-ordenação coleções LK

Modo preparado: aprovação de piloto; sem Shopify write executado; sem cron criado.

## Regra adicional Lucas

- Produtos esgotados devem ir sempre para o final da coleção.
- Implementação futura deve usar Tiny/stock truth quando possível; se usar apenas sinal Shopify, rotular como sinal e não como estoque final.

## Coleções piloto para aprovação

1. Nude Project — https://www.lksneakers.com.br/collections/nude-project
   - Produtos: 90; novos 90d: 7; top 8: 4 best-sellers + 4 novidades; movimentos: 79.
2. Jacquemus — https://www.lksneakers.com.br/collections/jacquemus
   - Produtos: 35; novos 90d: 4; top 8: 4 best-sellers + 2 novidades + performance; movimentos: 17.
3. Saint Studio — https://www.lksneakers.com.br/collections/saint-studio
   - Produtos: 82; novos 90d: 17; top 8: 4 best-sellers + 4 novidades; movimentos: 82.
4. Calça | Apparels — https://www.lksneakers.com.br/collections/calca-streetwear
   - Produtos: 70; novos 90d: 5; top 8: 4 best-sellers + 4 novidades; movimentos: 68.
5. Pace — https://www.lksneakers.com.br/collections/pace
   - Produtos: 75; novos 90d: 7; top 8: 4 best-sellers + 4 novidades; movimentos: 75.
6. Aimé Leon Dore — https://www.lksneakers.com.br/collections/aime-leon-dore
   - Produtos: 89; novos 90d: 11; top 8: 4 best-sellers + 4 novidades; movimentos: 89.
7. Nike Mind — https://www.lksneakers.com.br/collections/nike-mind-001
   - Produtos: 18; novos 90d: 11; top 8: 4 best-sellers + 4 novidades; movimentos: 12.
8. Onitsuka Tiger Mexico 66 — https://www.lksneakers.com.br/collections/onitsuka-tiger-mexico-66
   - Produtos: 101; novos 90d: 7; top 8: 4 best-sellers + 4 novidades; movimentos: 98.
9. Onitsuka Tiger Mexico 66 Sabot — https://www.lksneakers.com.br/collections/onitsuka-tiger-mexico-66-sabot
   - Produtos: 13; novos 90d: 4; top 8: 4 best-sellers + 4 novidades; movimentos: 10.
10. Shorts — https://www.lksneakers.com.br/collections/shorts
    - Produtos: 28; novos 90d: 4; top 8: 4 best-sellers + 4 novidades; movimentos: 24.

## Bloqueios

- Aplicação real via `collectionReorderProducts` ainda exige aprovação explícita após Lucas revisar os links/lista.
- Cron domingo 04h permanece fora de escopo.

## Rollback

- Usar `rollback-snapshot-v2-guardrails.json` e restaurar `current_order_product_ids` por coleção, com readback.
