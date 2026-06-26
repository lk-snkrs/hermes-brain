# LK OS Daily Sales Brief — 2026-05-15

Gerado em: `2026-05-16T18:46:20.628762+00:00`.
Janela: `2026-05-15T00:00:00-03:00` a `2026-05-15T23:59:59-03:00`.
Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_daily_sales_brief_20260515_184620Z.json`.

## 1. Resumo executivo

Ontem a LK vendeu **R$ 44.564,85** em **14 pedidos**. Fonte: `fact_shopify`.
Online/indefinido: **R$ 22.334,94 / 5 pedidos**. Loja física/POS detectado: **R$ 22.229,91 / 9 pedidos**.
GA4: **5845 sessões**, **5 transações GA4**, receita GA4 **R$ 15.914,97**. Fonte: `fact_ga4`, não receita oficial.
Conversão aproximada pedidos Shopify / sessões GA4: **0.24%**.
Tiny: **{'ruptura': 8, 'baixo_estoque_vs_venda_do_dia': 3, 'unknown': 4}** nos SKUs vendidos checados. Fonte: `fact_tiny_stock`.

## 2. Vendas Shopify

- Receita total: `R$ 44.564,85`
- Pedidos: `14`
- Ticket médio: `R$ 3.183,20`
- Linhas sem SKU: `2`
- Source/canal:
  - `web`: 5 pedidos, R$ 22.334,94
  - `pos`: 9 pedidos, R$ 22.229,91

## 3. Conversão e CRO

- `Paid Social`: 3393 sessões, 1 transações, conversão GA4 0.59%.
- `Cross-network`: 635 sessões, 0 transações, conversão GA4 0.79%.
- `Organic Search`: 470 sessões, 0 transações, conversão GA4 1.91%.
- `Direct`: 435 sessões, 2 transações, conversão GA4 2.53%.
- `Paid Shopping`: 400 sessões, 0 transações, conversão GA4 0.00%.
- `Organic Social`: 188 sessões, 0 transações, conversão GA4 3.72%.
- `Unassigned`: 111 sessões, 0 transações, conversão GA4 0.00%.
- `Paid Search`: 107 sessões, 1 transações, conversão GA4 2.80%.
- `Referral`: 57 sessões, 1 transações, conversão GA4 7.02%.
- `Organic Shopping`: 47 sessões, 0 transações, conversão GA4 2.13%.

## 4. Produtos/modelos/tamanhos vendidos

- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo**, SKU `1183C102 751-3`, tamanho `36`: 2 un., receita estimada de linhas R$ 4.799,98. Fonte: `fact_shopify`.
- **Tênis Nike Vomero Premium Black Volt Preto**, SKU `HQ2050-001-5`, tamanho `38`: 1 un., receita estimada de linhas R$ 4.499,99. Fonte: `fact_shopify`.
- **Chinelo Slide Nike Mind 001 Black Chrome Preto**, SKU `HQ4307-001-5`, tamanho `38`: 1 un., receita estimada de linhas R$ 3.999,99. Fonte: `fact_shopify`.
- **Chinelo Slide Nike Mind 001 Black Chrome Preto**, SKU `HQ4307-001-6`, tamanho `39`: 1 un., receita estimada de linhas R$ 3.999,99. Fonte: `fact_shopify`.
- **Tênis New Balance 204L Arid Timberwolf Bege**, SKU `U204LMMC-6`, tamanho `39`: 1 un., receita estimada de linhas R$ 2.799,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Bisque Frosted Glass Bege**, SKU `43774078387850`, tamanho `35`: 1 un., receita estimada de linhas R$ 2.699,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Sea Salt Moonbeam Branco**, SKU `U9060WHT-3`, tamanho `36`: 1 un., receita estimada de linhas R$ 2.599,99. Fonte: `fact_shopify`.
- **Tênis Nike Air Jordan 1 Low OG Olive Verde**, SKU `HQ6998-208`, tamanho `42`: 1 un., receita estimada de linhas R$ 2.499,99. Fonte: `fact_shopify`.
- **Tênis New Balance 9060 Rose Sugar Angora Rosa**, SKU `U9060LBC-2`, tamanho `34`: 1 un., receita estimada de linhas R$ 2.399,99. Fonte: `fact_shopify`.
- **Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom**, SKU `1183C102250-5`, tamanho `38`: 1 un., receita estimada de linhas R$ 2.399,99. Fonte: `fact_shopify`.
- **Onitsuka Tiger California 78 EX Black/Oatmel Preto**, SKU `1183A355.002-2`, tamanho `35`: 1 un., receita estimada de linhas R$ 2.299,99. Fonte: `fact_shopify`.
- **Moletom Represent Clo Storms in Heaven Black Preto**, SKU `Rep09-2`, tamanho `M/M`: 1 un., receita estimada de linhas R$ 1.899,99. Fonte: `fact_shopify`.
- **Tênis Air Jordan 1 Low SE "Legend Coffee" Marrom**, SKU `FJ3453-200-7`, tamanho `40`: 1 un., receita estimada de linhas R$ 1.789,90. Fonte: `fact_shopify`.
- **Tênis adidas Gazelle Indoor Collegiate Green Verde**, SKU `JI2062-2`, tamanho `35`: 1 un., receita estimada de linhas R$ 1.499,99. Fonte: `fact_shopify`.
- **Tênis Nike Cortez White Black Branco**, SKU `DM4044-105-4`, tamanho `35`: 1 un., receita estimada de linhas R$ 1.449,99. Fonte: `fact_shopify`.

## 5. Centro de Inteligência de Stock

- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo**, SKU `1183C102 751-3`, tamanho `36`: vendido 2 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis Nike Vomero Premium Black Volt Preto**, SKU `HQ2050-001-5`, tamanho `38`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Chinelo Slide Nike Mind 001 Black Chrome Preto**, SKU `HQ4307-001-5`, tamanho `38`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Chinelo Slide Nike Mind 001 Black Chrome Preto**, SKU `HQ4307-001-6`, tamanho `39`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Tênis New Balance 204L Arid Timberwolf Bege**, SKU `U204LMMC-6`, tamanho `39`: vendido 1 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_do_dia`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Bisque Frosted Glass Bege**, SKU `43774078387850`, tamanho `35`: vendido 1 un.; saldo Tiny `n/d`; risco `unknown`; match `exact_norm_sku`.
- **Tênis New Balance 9060 Sea Salt Moonbeam Branco**, SKU `U9060WHT-3`, tamanho `36`: vendido 1 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Tênis Nike Air Jordan 1 Low OG Olive Verde**, SKU `HQ6998-208`, tamanho `42`: vendido 1 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Tênis New Balance 9060 Rose Sugar Angora Rosa**, SKU `U9060LBC-2`, tamanho `34`: vendido 1 un.; saldo Tiny `n/d`; risco `unknown`; match `no_safe_candidate`.
- **Tênis Onitsuka Tiger Mexico 66 Beige Grass Green Marrom**, SKU `1183C102250-5`, tamanho `38`: vendido 1 un.; saldo Tiny `1.0`; risco `baixo_estoque_vs_venda_do_dia`; match `exact_norm_sku`.
- **Onitsuka Tiger California 78 EX Black/Oatmel Preto**, SKU `1183A355.002-2`, tamanho `35`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.
- **Moletom Represent Clo Storms in Heaven Black Preto**, SKU `Rep09-2`, tamanho `M/M`: vendido 1 un.; saldo Tiny `0.0`; risco `ruptura`; match `exact_norm_sku`.

## 6. Pago, influencers e conteúdo

- Landing Shopify observada: `/products/onitsuka-tiger-california-78-ex-black-oatmel-preto?currency=BRL&country=BR&variant=46835232145630&utm_source=g` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/?gad_source=1&gad_campaignid=20840173127&gbraid=0AAAAAqcRqrxlgTzLKQbf_4u__9mrZZtWj&gclid=Cj0KCQjwiJvQBhCYARIsAMjts3JvOa` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/tenis-nike-mind-002-light-smoke-grey-cinza?utm_content=Facebook_UA&utm_source=facebook&variant=48191013290206&` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/cart/47675544731870:1,47839129075934:1` em 1 pedido(s). Fonte: `fact_shopify`.
- Landing Shopify observada: `/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo?utm_content=[influencer Lala noleto] —Simples&utm_source=face` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://www.google.com/` em 2 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `https://instagram.com/` em 1 pedido(s). Fonte: `fact_shopify`.
- Referrer Shopify observado: `http://instagram.com/` em 1 pedido(s). Fonte: `fact_shopify`.

## 7. Recomendações e aprovações pendentes

- [P0] Preparar preview de reposição/sourcing para SKUs vendidos com saldo zero no Tiny. Motivo: 6 SKU(s) vendidos aparecem em ruptura no depósito oficial. Aprovação: Sim, antes de fornecedor/compra/Notion.. Fonte: `derived_reconciliation`.
- [P1] Revisar cobertura dos SKUs com saldo menor ou igual à venda do dia. Motivo: 2 SKU(s) com venda do dia encostando no saldo oficial. Aprovação: Sim, se virar compra, preço ou contato.. Fonte: `derived_reconciliation`.
- [P1] Resolver mapeamento Shopify SKU ↔ Tiny antes de campanha ou reposição automática. Motivo: 4 SKU(s) vendido(s) sem candidato Tiny seguro ou sem saldo legível. Aprovação: Sim, se exigir correção de cadastro.. Fonte: `derived_reconciliation`.

## 8. Limites da leitura

- Shopify é fonte oficial de pedidos/receita; GA4 é tráfego/canal/funil.
- Tiny foi checado apenas para SKUs vendidos no dia; não é auditoria completa de estoque por catálogo.
- Atribuição paga/influencer não foi promovida a fato sem ponte segura por UTM/referrer/cupom/ad_id.

## 9. O que este script não fez

- Não enviou WhatsApp, Klaviyo, e-mail, campanha ou mensagem externa.
- Não alterou Shopify, Tiny, Supabase, Meta, Google, Metricool, Klaviyo, Notion, n8n, estoque, preço, produto, cliente ou banco de produção.
- Não criou cron e não acionou fornecedor/compra.
