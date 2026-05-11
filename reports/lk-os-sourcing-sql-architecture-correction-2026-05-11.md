# LK OS — correção de arquitetura SQL vs sourcing externo — 2026-05-11

## Correção Lucas

O SQL local da LK deve guardar principalmente a operação própria da LK:

- pessoas/clientes;
- pedidos e histórico de compra;
- RFM/recompra/filas de aprovação;
- produtos, catálogo, variantes, SKU e tamanho;
- estoque Tiny e snapshots internos necessários;
- aprovações, bloqueios e histórico de ações.

Não deve ser desenhado como um warehouse permanente de preços voláteis de StockX/GOAT/Droper.

## Interpretação correta

GOAT, Droper, StockX e KicksDev entram como automação **on-demand**, não como full sync permanente.

Usar quando:

- a LK vai comprar/repor um tênis;
- há ruptura ou sinal interno de demanda;
- Lucas quer subir um produto novo e precisa foto/histórico/referência;
- é necessário comparar fonte viável antes de comprar.

Não usar para:

- manter preço externo variando todo dia dentro do SQL local;
- tratar StockX/GOAT/Droper como fonte de verdade da LK;
- fazer monitoramento amplo sem sinal interno.

## Regra mantida

Quando consultar StockX/GOAT, normalizar tamanho US Men/US Women para LK/BR/EU antes de comparar com produto/tamanho da LK.

## Impacto

O scaffold criado anteriormente deve ser tratado como rascunho/legado de sourcing, não como requisito de arquitetura. A próxima evolução correta é completar o SQL local com pessoas/clientes/produtos e criar um módulo separado de cotação on-demand para compra/reposição/subida de produto.
