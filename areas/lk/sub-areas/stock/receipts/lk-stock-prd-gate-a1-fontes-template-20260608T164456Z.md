# Receipt — PRD lk-stock: Gate A1 fontes e template

Data UTC: 2026-06-08T16:44:56Z

## Decisão/continuação

Lucas mandou seguir após escolher o caso A1:

**Ruptura: “quais best sellers estão acabando?”**

Foi detalhada a ordem de fontes e criado o template canônico de saída.

## Arquivos atualizados

- `areas/lk/sub-areas/stock/PRD.md`
- `areas/lk/sub-areas/stock/templates/ruptura-best-sellers-a1.md`

## Fonte dos candidatos — funil A1

Fase 1 — formar candidatos de demanda:

1. vendas Shopify 7/30/90;
2. histórico/família forte;
3. sinais Growth/Trends/campanha;
4. demanda humana da loja/operação.

Fase 2 — validar risco real:

5. Tiny / `LK | CONTROLE ESTOQUE` como fonte final para estoque por SKU/tamanho/loja física.

Regra registrada: Shopify/Growth/Trends/humano criam candidatos; Tiny confirma ou bloqueia a decisão de estoque.

## Output canônico criado

Template:

- `areas/lk/sub-areas/stock/templates/ruptura-best-sellers-a1.md`

Ele cobre:

- resumo executivo;
- P0/P1;
- `needs_sku_resolution`;
- fontes consultadas;
- bloqueios;
- frase de aprovação caso haja ação.

## Guardrails preservados

- Writes externos executados: `0`.
- Sem cron/gateway/bot.
- Sem compra/fornecedor/cliente/Tiny/Shopify/campanha sem aprovação escopada.
