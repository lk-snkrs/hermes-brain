# Fila A1 — Ruptura de Best Sellers

Status: preview / manual read-only
Writes externos executados: 0
Fonte viva de estoque: Tiny / `LK | CONTROLE ESTOQUE` ou fonte viva equivalente declarada

## Pergunta

Quais best sellers estão acabando?

## Resumo executivo

- P0 encontrados:
- P1 encontrados:
- Itens bloqueados por SKU/Tiny:
- Decisão necessária de Lucas:

## Fila priorizada

### P0 — risco alto de venda perdida

- Produto/modelo:
- SKU/tamanho:
- Tiny código:
- Estoque Tiny loja física:
- Evidência de best seller/demanda:
- Risco:
- Recomendação: repor / transferir / comprar / sanear SKU / não agir
- Dono seguinte:
- Aprovação necessária:

### P1 — revisar/repor se viável

- Produto/modelo:
- SKU/tamanho:
- Tiny código:
- Estoque Tiny loja física:
- Evidência de best seller/demanda:
- Risco:
- Recomendação:
- Dono seguinte:
- Aprovação necessária:

### needs_sku_resolution — dado bloqueia decisão

- Produto/modelo:
- Shopify handle/variant:
- SKU informado:
- Lacuna Tiny:
- Motivo do bloqueio:
- Dono seguinte: `lk-shopify` / `lk-ops`

## Fontes consultadas

- Vendas Shopify 7/30/90:
- Histórico/família:
- Growth/Trends/campanha:
- Demanda humana loja/operação:
- Tiny estoque:

## Bloqueios

- Sem Tiny/fonte viva, não afirmar disponibilidade.
- Sem compra, fornecedor, cliente, Tiny/Shopify write, campanha ou WhatsApp sem aprovação escopada.
- Não enviar alerta de OK; só decisão acionável, P0, falha de fonte ou aprovação necessária.

## Frase de aprovação se houver ação

Aprovo [ação exata] para [produto/SKU/tamanho], com limite [quantidade/valor/escopo], usando [fonte], e quero receipt/readback após execução.
