# Rotina v0 — Loop de Controle de Estoque Loja Física

## Entrada

- vendas recentes por SKU/tamanho;
- estoque Tiny por SKU/tamanho/loja;
- sinais de demanda Growth/Trends/CRM;
- lacunas SKU Shopify↔Tiny.

## Passos

1. Resolver produto → variant → SKU → tamanho.
2. Consultar Tiny como estoque final.
3. Calcular score best-seller/pronta entrega.
4. Classificar P0/P1/P2/P3.
5. Para P0/P1, criar action packet com recomendação.
6. Handoff para dono: Ops/Tiny, Shopify, Growth, Trends ou Lucas.
7. Registrar receipt.

## Saída

Fila acionável com `writes externos: 0` até aprovação.
