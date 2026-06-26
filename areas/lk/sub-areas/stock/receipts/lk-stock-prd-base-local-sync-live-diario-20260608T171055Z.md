# Receipt — PRD lk-stock: base local com sync live e diário

Data UTC: 2026-06-08T17:10:55Z

## Pedido de Lucas

Adicionar ao PRD e aos gates do agente `[LK] Estoque Loja Física` uma **base local** com:

- sync live via webhook;
- sync diário via cron.

## Alterações feitas

Arquivo PRD atualizado:

- `areas/lk/sub-areas/stock/PRD.md`

Skill operacional atualizada:

- `lk-stock` — seção “Modo de trabalho gradual”.

## O que entrou no PRD

### Base local operacional com sync vivo

A base local foi definida como **cache operacional/índice de decisão**, não como fonte final de disponibilidade.

Ela será alimentada por:

1. **Webhook live** — eventos Shopify/Tiny/fonte autorizada atualizam venda, produto/variante, estoque ou demanda.
2. **Cron diário** — reconcilia contra fontes vivas, corrige eventos perdidos, recalcula score e registra evidência.

### Freshness obrigatória

Toda resposta material deve declarar freshness:

- `live`;
- `cron diário`;
- `stale`;
- `fonte viva consultada agora`.

### Gate novo

Foi criado o **Gate B — Base local read-only + sync live/diário**.

Com isso, a sequência gradual agora é:

1. Gate A — Manual read-only.
2. Gate B — Base local read-only + sync live/diário.
3. Gate C — Rotina read-only silent-OK.
4. Gate D — Bot/perfil dedicado Telegram.
5. Gate E — Sistema completo operacional.

## Guardrails preservados

- Documentar no PRD não ativa webhook nem cron.
- Webhook/cron produtivos exigem aprovação escopada.
- Tiny / `LK | CONTROLE ESTOQUE` continua fonte final para disponibilidade.
- Base local pode acelerar candidatos e score, mas não pode prometer estoque sozinha.
- Writes externos executados: `0`.
