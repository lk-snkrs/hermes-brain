# Receipt — LK Sort Manual Regra B v2 em coleções manuais

Data: 2026-05-30T17:05:57.115915+00:00

## Regra aplicada
- Slots 1–2: best sellers elegíveis.
- Slots 3–4: produtos novos dos últimos 90 dias.
- Slots 5–6: próximos best sellers elegíveis.
- Slots 7–8: próximos produtos novos dos últimos 90 dias.
- Posição 9+: ranking best seller/comercial da coleção.
- Depois: Zona 3; por último: Zona 4/OOS.
- Expurgo: cancelado/refunded/void/pending/authorized/fraude.
- Regra dura: esgotado nunca entra em BEST SELLER/top slots.

## Resumo
- Coleções selecionadas: 4
- Movimentos totais: 2607
- Admin full ok: 4/4
- Público top12 ok: 4/4

## Coleções
- Todos os Produtos (`ultimos-lancamentos-2`): moves=1666; admin_full_ok=True; public_top12_ok=True
  - 1. Tênis New Balance 204L Mushroom Arid Stone Marrom — slots_1_2_best_seller
  - 2. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — slots_1_2_best_seller
  - 3. Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho — slots_3_4_new_90d
  - 4. Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege — slots_3_4_new_90d
- Tênis e Sneakers Originais (`sneakers`): moves=189; admin_full_ok=True; public_top12_ok=True
  - 1. Tênis New Balance 204L Mushroom Arid Stone Marrom — slots_1_2_best_seller
  - 2. Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — slots_1_2_best_seller
  - 3. Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho — slots_3_4_new_90d
  - 4. Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege — slots_3_4_new_90d
- Nike (`nike-todos-os-modelos`): moves=557; admin_full_ok=True; public_top12_ok=True
  - 1. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — slots_1_2_best_seller
  - 2. Tênis Nike Moon Shoe SP Jacquemus Off White — slots_1_2_best_seller
  - 3. Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho — slots_3_4_new_90d
  - 4. Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege — slots_3_4_new_90d
- Air Jordan 1 (`air-jordan-1`): moves=195; admin_full_ok=True; public_top12_ok=True
  - 1. Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul — slots_1_2_best_seller
  - 2. Tênis Nike Air Jordan 1 Low Og Sp x Travis Scott Medium Olive Verde — slots_1_2_best_seller
  - 3. Tênis Nike Air Jordan 1 Retro Low OG Howard University Vermelho — slots_3_4_new_90d
  - 4. Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Shy Pink Bege — slots_3_4_new_90d

## Rollback
- Snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260530T170141Z/rollback-snapshot-pre-write.json`
- Receipt JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/auto-sort-collections/all-manual-ruleB-net-sales-ga4-20260530T170141Z/receipt-final.json`

## Não ações
- Nenhum cron ativado.
- Nenhum produto/preço/estoque/tema/tag/SEO/GMC/campanha/checkout/cliente alterado.
