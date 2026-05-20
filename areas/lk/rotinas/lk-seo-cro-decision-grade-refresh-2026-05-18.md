# LK SEO/CRO — Bloco 2 Decision-grade Refresh

Data: 2026-05-18
Status: executado, read-only, sem writes externos.

## Objetivo

Fechar o principal gap do Bloco 1 do roteador comercial: o spine local de vendas Shopify terminava em 2026-04-16. Este bloco adiciona um refresh Shopify live read-only por pedido/linha de item e resolve membership exato de produto/coleção para as principais URLs antes de gerar approval packets.

## Artefatos

- Script: `scripts/lk_seo_cro_decision_grade_refresh_20260518.py`
- JSON: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.json`
- Markdown: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.md`
- CSV: `reports/lk-seo-cro-decision-grade-refresh-2026-05-18.csv`
- Base: `reports/lk-seo-cro-commercial-opportunity-router-2026-05-18.json`

## Fontes lidas

- Shopify Admin REST `GET /orders.json`, somente leitura.
- Shopify Admin GraphQL `query productByHandle` e `query collectionByHandle`, somente leitura.
- Relatório do Bloco 1 com GA4, GSC, GMC/contexto e Tiny parcial.

## Resultado

- Pedidos Shopify lidos desde `2026-04-17T00:00:00-03:00`: 397.
- Pedidos pagos/considerados: 340.
- Janela efetiva: `2026-04-17T01:28:58-03:00` até `2026-05-18T09:13:36-03:00`.
- Lookups Shopify produto/collection: 19/19 OK.
- URLs refinadas: 20.
- Prioridades após refresh: 13 P1, 6 P2, 1 P3, 0 data-gap.
- Writes externos: 0.

## Top validado após refresh

1. Onitsuka Tiger todos os modelos — P1, score 100.
   - Vendas recentes live: 98 un.; R$ 244.099,02.
   - Vendas combinadas: 740 un.; R$ 1.768.732,64.
   - Membership: `exact_collection_membership_first_120`.

2. New Balance 204L — P1, score 100.
   - Vendas recentes live: 29 un.; R$ 81.199,71.
   - Vendas combinadas: 366 un.; R$ 938.571,38.
   - Membership: `exact_collection_membership_first_120`.

3. Air Jordan Travis Scott — P1, score 100.
   - Vendas recentes live: 2 un.; R$ 14.498,99.
   - Vendas combinadas: 35 un.; R$ 154.448,68.
   - Membership: `exact_collection_membership_first_120`.

4. Lululemon — P1, score 100.
   - Vendas recentes live: 5 un.; R$ 7.199,95.
   - Vendas combinadas: 46 un.; R$ 56.649,54.
   - Membership: `exact_collection_membership_first_120`.

5. Adidas Samba Jane — P1, score 100.
   - Vendas recentes live: 5 un.; R$ 9.198,96.
   - Vendas combinadas: 154 un.; R$ 319.347,51.
   - Membership: `exact_collection_membership_first_120`.

6. Onitsuka Tiger Kill Bill PDP — P1, score 100.
   - Vendas recentes live: 20 un.; R$ 47.999,80.
   - Vendas combinadas: 107 un.; R$ 256.798,93.
   - Membership: `exact_product_handle`.

## Decisão operacional

O Bloco 2 confirma que a fila do Bloco 1 não era um falso positivo de HTML: as páginas P1 têm demanda comercial real e recente, com Shopify live e membership exato.

A fila agora está pronta para gerar **approval packets** aplicáveis, mas somente como preview:

- SEO title/meta por produto/collection;
- CRO visível em dev theme quando aplicável;
- sourcing/estoque somente depois de Tiny/margem por SKU;
- nenhuma alteração sem payload + alvo + rollback + aprovação explícita do Lucas.

## Gaps restantes

- Tiny estoque completo ainda parcial/rate-limited; não foi chamado ao vivo neste bloco para evitar pressão de API.
- Margem/custo por SKU ainda não está confiável para score final.
- Collections foram lidas até os primeiros 120 produtos por segurança; se uma collection maior precisar de auditoria completa, adicionar paginação controlada.

## Guardrails

Não foi executado:

- Shopify mutation;
- alteração de tema/conteúdo;
- Tiny API/write;
- Merchant/feed write;
- GA4/GSC write;
- campanha/envio externo;
- WhatsApp/e-mail;
- contato com fornecedor;
- alteração de preço ou estoque;
- criação de cron.
