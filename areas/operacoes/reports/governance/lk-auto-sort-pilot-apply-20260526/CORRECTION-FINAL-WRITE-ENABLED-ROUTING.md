# Correção final — próximo contexto deve ser LK Shopify/Growth write-enabled

Data: 2026-05-26
Origem: Telegram Lucas

## Correção solicitada

Lucas corrigiu a formulação operacional. O próximo turno/sessão não deve cair como Hermes Geral/read-only. Deve vir como LK Shopify/Growth write-enabled para executar o piloto já aprovado.

## Formulação correta

O próximo turno/sessão precisa vir como LK Shopify/Growth write-enabled, não como Hermes Geral/read-only.

Quando isso acontecer, executar direto:

- snapshot;
- Tiny para esgotados;
- esgotados no final;
- `collectionReorderProducts`;
- poll;
- readback;
- receipt;
- sem cron.

## Escopo aprovado preservado

Aplicar somente nas 10 coleções piloto:

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

## Limites preservados

Não executar fora do escopo:

- cron;
- produto;
- preço;
- estoque/disponibilidade;
- tema;
- SEO/tags;
- checkout;
- campanha;
- comunicação com cliente/time.

## Status deste registro

Documento local de correção/handoff. Nenhuma mutation Shopify foi enviada por este registro.
