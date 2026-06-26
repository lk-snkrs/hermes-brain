# Rotina v0 — Loop de Controle de Estoque Loja Física

## Entrada

- vendas recentes por SKU/tamanho;
- estoque Tiny por SKU/tamanho/loja;
- sinais de demanda Growth/Trends/CRM;
- lacunas SKU Shopify↔Tiny.

## Passos

1. Resolver produto → variant → SKU → tamanho.
2. Separar fonte operacional de fonte técnica/teste; aplicar `rotinas/anti-fixture-operational-scoring.md` antes de qualquer soma.
3. Consultar Tiny como estoque final.
4. Calcular score best-seller/pronta entrega.
5. Classificar P0/P1/P2/P3.
6. Para P0/P1, criar action packet com recomendação.
7. Handoff para dono: Ops/Tiny, Shopify, Growth, Trends ou Lucas.
8. Registrar receipt.

## Bloqueio anti-fixture

`shopify_fixture`, `tiny_fixture`, `manual_fixture`, `GATEB-PROBE-*` e qualquer fonte marcada como fixture/probe/teste não entram em vendas, demanda, snapshot Tiny, score, P0/P1 ou recomendação operacional. Se só houver fonte de teste, a saída é bloquear a decisão e consultar fonte viva.

## Saída

Fila acionável com `writes externos: 0` até aprovação.
