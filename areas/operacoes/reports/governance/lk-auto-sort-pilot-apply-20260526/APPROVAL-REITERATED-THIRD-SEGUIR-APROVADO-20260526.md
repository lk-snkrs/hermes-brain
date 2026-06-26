# Aprovação reiterada novamente — seguir aprovado

Data: 2026-05-26
Origem: Telegram Lucas

## Pedido limpo

Lucas reiterou novamente: "aprovado seguir" para execução do piloto de auto-ordenação das coleções LK com Shopify write.

## Interpretação

A autorização de negócio está inequívoca e atual. O bloqueio remanescente é de runtime/roteamento, que continua classificando o turno como documentação local/read-only.

## Escopo aprovado para o próximo contexto write-enabled

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

## Não ações deste registro

- Nenhuma mutation Shopify enviada.
- Nenhum cron criado.
- Nenhuma alteração em Tiny, produto, preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação.

## Próxima execução correta

Em sessão/turno write-enabled de LK Shopify/Growth, executar imediatamente o apply com snapshot, Tiny, mutation, poll, readback e receipt, sem pedir nova aprovação para este mesmo escopo.
