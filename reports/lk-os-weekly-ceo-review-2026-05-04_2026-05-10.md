# LK OS Weekly CEO Review — 2026-05-04 a 2026-05-10

Gerado em: `2026-05-11T21:51:50.356893+00:00`.
Política de janela: `last_7_closed_days_brt`.
Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_weekly_ceo_review_20260504_20260510_215150Z.json`.

## 1. Resumo CEO

- Shopify: **R$ 312.261,74** em **97 pedidos**, ticket médio **R$ 3.219,19**. Fonte: `fact_shopify`.
- GA4: **29605 sessões**, **55 transações GA4**, receita GA4 **R$ 164.657,24**. Fonte: `fact_ga4`, não receita oficial.
- Conversão aproximada Shopify pedidos / GA4 sessões: **0.33%**.
- Tiny nos SKUs vendidos: **{'ruptura': 7, 'baixo_estoque_vs_venda_da_semana': 3, 'unknown': 4, 'ok_amostra': 1}**. Fonte: `fact_tiny_stock`.
- Meta Ads: gasto **R$ 9.374,43**, compras plataforma `62.0`, valor plataforma **R$ 140.697,30**, ROAS plataforma `15.01`. Fonte: `platform_signal`.
- Metricool/Google Ads: linhas `21`, status `200`. Fonte: `platform_signal`.

## 2. Vendas por dia

- `2026-05-04`: 10 pedidos, R$ 52.189,93.
- `2026-05-05`: 21 pedidos, R$ 50.819,97.
- `2026-05-06`: 10 pedidos, R$ 21.692,44.
- `2026-05-07`: 8 pedidos, R$ 31.199,91.
- `2026-05-08`: 15 pedidos, R$ 50.626,93.
- `2026-05-09`: 24 pedidos, R$ 70.922,64.
- `2026-05-10`: 9 pedidos, R$ 34.809,92.

## 3. Canais GA4

- `Paid Social`: 15390 sessões, 14 transações, conversão GA4 0.82%.
- `Cross-network`: 3719 sessões, 10 transações, conversão GA4 1.94%.
- `Organic Search`: 3225 sessões, 4 transações, conversão GA4 1.27%.
- `Direct`: 2072 sessões, 10 transações, conversão GA4 3.28%.
- `Paid Shopping`: 1608 sessões, 3 transações, conversão GA4 1.68%.
- `Organic Social`: 1363 sessões, 10 transações, conversão GA4 4.84%.
- `Paid Search`: 898 sessões, 1 transações, conversão GA4 4.01%.
- `Unassigned`: 686 sessões, 3 transações, conversão GA4 4.52%.
- `Organic Shopping`: 352 sessões, 0 transações, conversão GA4 2.27%.
- `Referral`: 233 sessões, 0 transações, conversão GA4 0.43%.

## 4. Produtos e estoque crítico

- **Tênis New Balance 9060 Rich Oak Marrom**, SKU `U9060CCC-4`, tamanho `37`: vendido 3 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis New Balance 530 Silver White Branco**, SKU `MR530EMA-5`, tamanho `38`: vendido 3 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_da_semana`; match `exact_norm_sku`.
- **MEDICOM TOY - Bearbrick Series 48 100% Toy Art Blind Box (Lacrado)**, SKU `MED-3410398-OS`, tamanho `sem tamanho informado`: vendido 3 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom**, SKU `HV8547-200-38`, tamanho `38`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa**, SKU `HV8547-601-37`, tamanho `37`: vendido 2 un.; saldo Tiny `2.0`; risco `baixo_estoque_vs_venda_da_semana`; match `exact_norm_sku`.
- **Tênis Nike Moon Shoe SP Jacquemus Off White**, SKU `HV8547-002-36`, tamanho `36`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Nike Mind 002 Light Smoke Grey Cinza**, SKU `HQ4308-003-5`, tamanho `36`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Sea Salt Moonbeam Branco**, SKU `U9060WHT-4`, tamanho `37`: vendido 2 un.; saldo Tiny `-1.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Angora Sea Salt Bege**, SKU `U9060ERB-3`, tamanho `36`: vendido 2 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_da_semana`; match `exact_norm_sku`.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo**, SKU `1183C102751-3`, tamanho `36`: vendido 2 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Polo Comme des Garçons PLAY Red Emblem White Branco**, SKU `CDGP2`, tamanho `G/L`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Camiseta Saint Studio Boxy Supima Breuer Preto**, SKU `SST-6502622-M`, tamanho `M/M`: vendido 2 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.

## 5. Mídia e atribuição, ainda como sinal

- Meta/Metricool entram como `platform_signal`: úteis para diagnóstico de gasto, alcance e campanha, mas não substituem Shopify como venda real.
- Landing Shopify observada: `/?utm_id=97760_v0_s00_e0_tv3` em 6 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/` em 3 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/collections/roupas?utm_medium=paid&utm_id=120242040260570224_v2_s09_e7608&utm_content=120242040260560224&utm_term=12024` em 2 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/tenis-nike-air-max-1-87-stranger-things-steve-harrington-branco?utm_id=97760_v0_s00_e0_tv3&fbclid=PAT01DUARkqW` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo?variant=47598961393886` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/collections/onitsuka-tiger-mexico-66?utm_source=facebook&utm_medium=cpc&utm_campaign=[PD] [FUNDO] RMKT (antiga Campanha` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/collections/nike-x-jacquemus-moon-shoe-sp?ad_id=120241352220370224&campaign_id=120241297336180224&fbclid=PAZXh0bgNhZW0B` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/?utm_medium=paid&utm_id=120236212896630224_v2_s10_e7644&utm_content=120237637573420224&utm_term=120236212896630224&utm_` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/calca-pace-pf-sweatpants-preto?srsltid=AfmBOopXo5oiIL55vBo3bA5GvDMcHJ6IELO-sB0JRXjkSxoY0izvL1ZW` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/oculos-de-sol-balenciaga-bb0041s-014-azul?currency=BRL&country=BR&variant=46163270795486&utm_source=google&utm` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://www.google.com/` em 19 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://instagram.com/` em 17 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://l.instagram.com/` em 6 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://lksneakers.com.br/cart` em 2 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `http://instagram.com/` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://lksneakers.com.br/?utm_id=97760_v0_s00_e0_tv3` em 1 pedido(s). Fonte: `fact_shopify`.

## 6. Prioridades e aprovações

- [P0] Preparar fila de sourcing/reposição para SKUs vendidos na semana com saldo zero no Tiny. Motivo: 7 SKU(s) vendidos aparecem em ruptura no depósito oficial. Aprovação: Sim, antes de compra/fornecedor/Notion.. Fonte: `derived_reconciliation`.
- [P1] Revisar cobertura dos SKUs com venda semanal encostando no saldo oficial. Motivo: 3 SKU(s) têm saldo menor ou igual à venda da semana. Aprovação: Sim, se virar compra, preço ou contato.. Fonte: `derived_reconciliation`.
- [P1] Priorizar saneamento SKU Shopify ↔ Tiny antes de escalar mídia dos produtos vendidos. Motivo: 4 SKU(s) vendidos sem candidato Tiny seguro ou sem saldo legível. Aprovação: Sim, se exigir write em cadastro.. Fonte: `derived_reconciliation`.
- [P2] Usar Meta como sinal de mídia e reconciliar campanhas com landing/referrer/cupom antes de falar em ROAS real. Motivo: Gasto Meta sinalizado equivale a 3.0% da receita Shopify semanal, sem prova SKU por campanha ainda. Aprovação: Não para análise; sim para campanha.. Fonte: `derived_reconciliation`.

## 7. O que este script não fez

- `telegram_send`
- `cron`
- `external_send`
- `campaign`
- `shopify_write`
- `tiny_write`
- `stock_or_price_change`
- `customer_contact`
- `supplier_contact`
- `production_db_write`

## 8. Limitações

- Semana read-only de 7 dias fechados, sem margem/CMV ainda.
- CRM/RFM e SEO entram como próximos módulos de profundidade, não foram recalculados neste script.
- Nenhum ROAS operacional foi declarado sem reconciliação por pedido/SKU/campanha.
