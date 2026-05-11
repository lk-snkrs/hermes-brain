# LK OS Daily Sales Brief — 2026-05-10

Gerado em: `2026-05-11T22:15:36.269438+00:00`.
Janela: `2026-05-10T00:00:00-03:00` a `2026-05-10T23:59:59-03:00`.
Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_daily_sales_brief_20260510_221536Z.json`.

## 1. Resumo executivo

Ontem a LK vendeu **R$ 34.809,92** em **9 pedidos**. Fonte: `fact_shopify`.
Online/indefinido: **R$ 34.809,92 / 9 pedidos**. Loja física/POS detectado: **R$ 0,00 / 0 pedidos**.
GA4: **4301 sessões**, **8 transações GA4**, receita GA4 **R$ 33.009,93**. Fonte: `fact_ga4`, não receita oficial.
Conversão aproximada pedidos Shopify / sessões GA4: **0.21%**.
Tiny: **{'ruptura': 5, 'ok_amostra': 1, 'baixo_estoque_vs_venda_do_dia': 3, 'unknown': 1}** nos SKUs vendidos checados. Fonte: `fact_tiny_stock`.

## 2. Vendas Shopify

- Receita total: `R$ 34.809,92`
- Pedidos: `9`
- Ticket médio: `R$ 3.867,77`
- Linhas sem SKU: `0`
- Source/canal:
  - `web`: 9 pedidos, R$ 34.809,92

## 3. Conversão e CRO

- `Paid Social`: 2315 sessões, 3 transações, conversão GA4 0.65%.
- `Cross-network`: 549 sessões, 2 transações, conversão GA4 1.46%.
- `Organic Search`: 458 sessões, 0 transações, conversão GA4 0.22%.
- `Paid Shopping`: 296 sessões, 1 transações, conversão GA4 2.70%.
- `Direct`: 264 sessões, 1 transações, conversão GA4 1.89%.
- `Organic Social`: 163 sessões, 1 transações, conversão GA4 4.29%.
- `Paid Search`: 109 sessões, 0 transações, conversão GA4 2.75%.
- `Unassigned`: 80 sessões, 0 transações, conversão GA4 8.75%.
- `Organic Shopping`: 54 sessões, 0 transações, conversão GA4 1.85%.
- `Referral`: 9 sessões, 0 transações, conversão GA4 0.00%.

## 4. Produtos/modelos/tamanhos vendidos

- **Polo Comme des Garçons PLAY Red Emblem White Branco**, SKU `CDGP2`, tamanho `G/L`: 2 un., receita estimada de linhas R$ 3.599,98. Fonte: `fact_shopify`.
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto**, SKU `HV8547-001-7`, tamanho `40`: 1 un., receita estimada de linhas R$ 6.999,99. Fonte: `fact_shopify`.
- **Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa**, SKU `HV8547-601-37`, tamanho `37`: 1 un., receita estimada de linhas R$ 5.999,99. Fonte: `fact_shopify`.
- **Tênis Nike Vomero Premium Barely Volt Verde**, SKU `HQ2050-300-6`, tamanho `39`: 1 un., receita estimada de linhas R$ 3.999,99. Fonte: `fact_shopify`.
- **Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza**, SKU `HQ4307-003-10`, tamanho `43`: 1 un., receita estimada de linhas R$ 3.199,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Triple White Branco**, SKU `U9060NRJ-38`, tamanho `38`: 1 un., receita estimada de linhas R$ 2.799,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Sea Salt Moonbeam Branco**, SKU `U9060WHT-4`, tamanho `37`: 1 un., receita estimada de linhas R$ 2.599,99. Fonte: `fact_shopify`.
- **Tênis Onitsuka Tiger Tsunahiki Slip-On White/Black Branco**, SKU `1183C529.101-8`, tamanho `41`: 1 un., receita estimada de linhas R$ 2.499,99. Fonte: `fact_shopify`.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo**, SKU `1183C102751-4`, tamanho `37`: 1 un., receita estimada de linhas R$ 2.399,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Cortado Marrom**, SKU `U9060496`, tamanho `37`: 1 un., receita estimada de linhas R$ 2.399,99. Fonte: `fact_shopify`.

## 5. Centro de Inteligência de Stock

- **Polo Comme des Garçons PLAY Red Emblem White Branco**, SKU `CDGP2`, tamanho `G/L`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto**, SKU `HV8547-001-7`, tamanho `40`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Nike Vomero Premium Barely Volt Verde**, SKU `HQ2050-300-6`, tamanho `39`: vendido 1 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_do_dia`; match `exact_norm_sku`.
- **Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza**, SKU `HQ4307-003-10`, tamanho `43`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Triple White Branco**, SKU `U9060NRJ-38`, tamanho `38`: vendido 1 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_do_dia`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Sea Salt Moonbeam Branco**, SKU `U9060WHT-4`, tamanho `37`: vendido 1 un.; saldo Tiny `-1.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Onitsuka Tiger Tsunahiki Slip-On White/Black Branco**, SKU `1183C529.101-8`, tamanho `41`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo**, SKU `1183C102751-4`, tamanho `37`: vendido 1 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Tênis New Balance 9060 Cortado Marrom**, SKU `U9060496`, tamanho `37`: vendido 1 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_do_dia`; match `exact_norm_sku`.

## 6. Pago, influencers e conteúdo

- Landing Shopify observada: `/?utm_medium=paid&utm_id=120236212896630224_v2_s04_e450_i20260507&utm_content=120237637573400224&utm_term=12023621289663` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/collections/nike-x-jacquemus-moon-shoe-sp?ad_id=120241352199470224&campaign_id=120241297336180224&fbclid=PAZXh0bgNhZW0B` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/tenis-new-balance-9060-angora-sea-salt-bege?currency=BRL&country=BR&variant=47583466193118&utm_source=google&u` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/?utm_id=97760_v0_s00_e0_tv3` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://instagram.com/` em 3 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://www.google.com/` em 3 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://l.instagram.com/` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://lksneakers.com.br/cart` em 1 pedido(s). Fonte: `fact_shopify`.

## 7. Recomendações e aprovações pendentes

- [P0] Preparar preview de reposição/sourcing para SKUs vendidos com saldo zero no Tiny. Motivo: 5 SKU(s) vendidos aparecem em ruptura no depósito oficial. Aprovação: Sim, antes de fornecedor/compra/Notion.. Fonte: `derived_reconciliation`.
- [P1] Revisar cobertura dos SKUs com saldo menor ou igual à venda do dia. Motivo: 3 SKU(s) com venda do dia encostando no saldo oficial. Aprovação: Sim, se virar compra, preço ou contato.. Fonte: `derived_reconciliation`.
- [P1] Resolver mapeamento Shopify SKU ↔ Tiny antes de campanha ou reposição automática. Motivo: 1 SKU(s) vendido(s) sem candidato Tiny seguro ou sem saldo legível. Aprovação: Sim, se exigir correção de cadastro.. Fonte: `derived_reconciliation`.

## 8. Limites da leitura

- Shopify é fonte oficial de pedidos/receita; GA4 é tráfego/canal/funil.
- Tiny foi checado apenas para SKUs vendidos no dia; não é auditoria completa de estoque por catálogo.
- Atribuição paga/influencer não foi promovida a fato sem ponte segura por UTM/referrer/cupom/ad_id.

## 9. O que este script não fez

- Não enviou WhatsApp, Klaviyo, e-mail, campanha ou mensagem externa.
- Não alterou Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.
- Não criou cron e não acionou fornecedor/compra.
