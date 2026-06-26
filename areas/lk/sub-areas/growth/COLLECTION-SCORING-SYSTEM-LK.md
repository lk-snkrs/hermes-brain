# LK Collection Scoring System — padrão canônico

Atualizado: 2026-06-18T17:38:08.008273+00:00

## Objetivo

Padronizar a ordenação comercial de coleções Shopify da LK com base em dados reais, evitando que uma coleção editorial vire filtro genérico ou que produtos muito visitados mas sem venda subam indevidamente.

## Regra canônica v1

- **70% vendas + 30% visitação PDP**.
- Janelas: **30 / 90 / 180 dias**.
- Blend de recência: **50% últimos 30d + 30% últimos 90d + 20% últimos 180d**.
- Gate comercial obrigatório: produto com **0 venda em 180 dias** nunca pode ficar acima de produto vendido apenas por tráfego.
- Para coleção editorial/campanha premium, usar `--exclude-zero-sales` quando Lucas pedir curadoria menor ou quando a coleção estiver ampla demais.
- A visitação é sinal auxiliar de demanda, não substitui venda.

## Script operacional

Script canônico local:

`/opt/data/profiles/lk-growth/scripts/lk_collection_scoring_system.py`

Execução dry-run/read-only:

```bash
/opt/data/scripts/hermes_doppler.py run --   python3 /opt/data/profiles/lk-growth/scripts/lk_collection_scoring_system.py   --collection <handle-ou-id-da-colecao>   --exclude-zero-sales
```

Saídas geradas:

- `summary.json`
- `ranking.json`
- `ranking.csv`
- `REPORT.md`

Diretório padrão:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/collection-scoring/<collection>-<timestamp>/`

## Segurança / aprovação

- O script é **read-only por padrão**.
- Write externo Shopify só é permitido com:
  - aprovação explícita atual de Lucas;
  - `--apply`;
  - `--approval-token LUCAS_APPROVED_SHOPIFY_COLLECTION_REORDER`;
  - rollback/readback/receipt.
- Não usar o `best-selling` nativo da Shopify quando a solicitação for “score LK”, “best sellers LK” ou “ordem por performance real”.
- Não consultar estoque/grade/disponibilidade neste sistema. Estoque é dono do `lk-stock`.

## Dados usados

- Shopify Admin API: coleção, produtos e pedidos/line items dos últimos 180 dias.
- GA4 Data API: `screenPageViews` por `pagePath` de PDP em 30/90/180 dias.
- Não usa Tiny, estoque, disponibilidade operacional, preço ou desconto como critério.

## Critérios de aceite

Uma execução decision-grade precisa registrar:

- coleção, handle, ID e sort order antes;
- total de produtos lidos;
- total de produtos ranqueados;
- quantidade de produtos com 0 venda 180d;
- top 20 proposto;
- fórmula usada;
- se houve ou não write externo;
- `values_printed=false` para secrets.

## Quando aplicar

Usar para:

- coleções editoriais/campanha;
- coleções de marca/modelo com muitos itens;
- páginas de entrada de tráfego pago/social;
- coleção “mais desejados”, “best sellers”, “presentes”, “neutros”, “tons”, “curadoria”.

Não usar isoladamente para:

- decisão de estoque/compra/reposição;
- preço/desconto;
- disponibilidade ao cliente;
- publicação de produto novo.

## Execução validada — 2026-06-18

Dry-run aplicado na coleção `tons-terrosos-sao-os-novos-neutros`:

- Produtos lidos: 150.
- Produtos ranqueados: 150.
- Produtos com 0 venda 180d: 0.
- Write externo: nenhum.
- Output: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/collection-scoring/tons-terrosos-sao-os-novos-neutros-20260618T173603Z/`.
- Top 5 proposto no dry-run:
  1. Tênis New Balance 204L Arid Timberwolf Bege
  2. Tênis New Balance 204L Mushroom Arid Stone Marrom
  3. Tênis Nike Moon Shoe SP Jacquemus Off White
  4. Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom
  5. Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege

## Relação com LKGOC

Este sistema cobre a camada de **ordenação comercial da coleção**. Ele não substitui o fluxo completo LK Growth Optimized Collection quando a demanda envolver SEO/GEO/CRO/layout/guia/descrição/schema. Para LKGOC, continuar usando o canônico `LKGOC-PADRAO-CANONICO.md` e a skill `lk-superpowers-collection-optimizer`.
