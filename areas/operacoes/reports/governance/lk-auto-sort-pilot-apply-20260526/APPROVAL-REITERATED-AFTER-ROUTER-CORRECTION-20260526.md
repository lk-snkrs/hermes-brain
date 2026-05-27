# Aprovação reiterada após correção de roteamento — Shopify write piloto LK

Data: 2026-05-26
Origem: Telegram Lucas

## Pedido limpo

Lucas respondeu "aprovado seguir" após a identificação de que o bloqueio atual é erro de roteamento/classificação, não falta de aprovação de negócio.

## Interpretação operacional

A aprovação para Shopify write está reiterada. O próximo contexto write-enabled deve executar o piloto sem pedir nova autorização, respeitando exatamente o escopo aprovado.

## Escopo aprovado

- Aplicar somente nas 10 coleções piloto aprovadas.
- Usar Tiny/SQLite como fonte primária para produtos esgotados.
- Mover produtos esgotados para o final.
- Gerar snapshot pré-write imediato.
- Executar `collectionReorderProducts`.
- Pollar jobs assíncronos.
- Fazer readback por coleção.
- Gerar receipt final.
- Não criar cron.

## Coleções piloto

1. Nude Project
2. Jacquemus
3. Saint Studio
4. Calça | Apparels
5. Pace
6. Aimé Leon Dore
7. Nike Mind
8. Onitsuka Tiger Mexico 66
9. Onitsuka Tiger Mexico 66 Sabot
10. Shorts

## Status deste runtime

A execução real continua pendente de contexto habilitado para Shopify write. Este arquivo é documentação/handoff local.

## Não ações

- Nenhuma mutation Shopify foi enviada por este registro.
- Nenhum cron foi criado.
- Nenhuma alteração foi feita em Tiny, produto, preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação.

## Rollback obrigatório na execução

Usar snapshot pré-write imediato e restaurar a ordem anterior via `collectionReorderProducts`, com poll e readback.
