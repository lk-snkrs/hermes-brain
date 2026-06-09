# Receipt — PRD lk-stock: Gate A1 ruptura de best sellers

Data UTC: 2026-06-08T15:47:08Z

## Decisão capturada

Lucas escolheu o primeiro caso real de aceite do Gate A manual read-only:

**Ruptura: “quais best sellers estão acabando?”**

## Alteração documental

Arquivo atualizado:

- `areas/lk/sub-areas/stock/PRD.md`

Seção adicionada:

- `12 / Gate A / Caso real de aceite A1 — Ruptura de best sellers`

## Contrato do caso A1

O agente deve, sob demanda:

1. listar candidatos best sellers;
2. resolver produto → variante → SKU → tamanho → código Tiny quando possível;
3. consultar Tiny/fonte viva para estoque atual;
4. classificar P0/P1/P2/needs_sku_resolution;
5. entregar fila curta e acionável;
6. gerar packet quando houver ação que exija aprovação;
7. manter writes externos executados em `0`.

## Guardrails preservados

- Sem Tiny/fonte viva, não afirma disponibilidade.
- Sem cron/gateway/bot nesta etapa.
- Sem compra, fornecedor, cliente, Tiny/Shopify write ou campanha sem aprovação escopada.
