# Aprovação capturada — Shopify write piloto auto-ordenação LK

Data: 2026-05-26
Origem: Telegram Lucas

## Pedido limpo

Lucas autorizou explicitamente Shopify write para avançar com o piloto de auto-ordenação das coleções LK.

Escopo aprovado já documentado:

- aplicar somente nas 10 coleções piloto aprovadas;
- usar Tiny/SQLite como fonte primária para produtos esgotados;
- mover esgotados para o final;
- gerar snapshot imediato antes de qualquer write;
- executar `collectionReorderProducts`;
- pollar o job assíncrono;
- readback por coleção;
- gerar receipt final;
- não criar cron.

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

## Status deste turno

A aprovação foi capturada, mas a execução de write externo continua bloqueada pelo contexto atual, que permite apenas pesquisa, síntese e documentação local.

## Não ações deste turno

- Não foi enviado `collectionReorderProducts`.
- Não foi alterada nenhuma coleção Shopify.
- Não foi alterado Tiny.
- Não foi criado cron.
- Não houve mudança em produto, preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação.

## Próxima execução correta

Em contexto habilitado para produção/Shopify write, executar imediatamente o apply seguindo esta sequência:

1. Reconsultar as 10 coleções no Shopify.
2. Gerar snapshot pré-write imediato.
3. Reconsultar Tiny/SQLite para classificar esgotados.
4. Recomputar a ordem com esgotados no bucket final.
5. Rodar `collectionReorderProducts` somente nas 10 coleções.
6. Pollar cada job até finalizar.
7. Fazer readback e comparar ordem esperada vs ordem aplicada.
8. Gerar receipt final.

## Rollback

Usar o snapshot pré-write imediato e restaurar a ordem anterior via `collectionReorderProducts`, com poll e readback.
