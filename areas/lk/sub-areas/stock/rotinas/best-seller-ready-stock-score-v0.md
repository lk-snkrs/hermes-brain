# Score v0 — Best Seller / Pronta Entrega

## Campos mínimos

- produto;
- handle Shopify;
- variant/SKU/tamanho;
- Tiny código;
- estoque loja física/pronta entrega;
- vendas 7/30/90 dias;
- sinais de demanda;
- confiança de mapeamento;
- recomendação;
- dono seguinte.

## Fórmula inicial

- Vendas recentes: 30
- Margem/valor: 20
- Demanda externa: 15
- Risco de ruptura: 15
- Histórico/família: 10
- Confiança de dados: 10

## Regra de bloqueio

Se SKU/Tiny mapping < confiança alta, o item vira `needs_sku_resolution` antes de compra/reposição.
