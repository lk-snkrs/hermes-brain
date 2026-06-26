# Pedido write-enabled recebido — bloqueado por preflight

Data: 2026-05-26
Origem: Telegram Lucas

## Destino

LK Growth / Shopify Collections

## Pedido limpo

Lucas enviou pedido explícito como LK Shopify/Growth write-enabled para executar agora o apply aprovado da auto-ordenação das coleções LK.

## Escopo solicitado e aprovado

- somente as 10 coleções piloto aprovadas;
- snapshot pré-write imediato;
- Tiny/SQLite como fonte primária para esgotados;
- produtos esgotados no final;
- executar `collectionReorderProducts`;
- poll dos jobs;
- readback por coleção;
- receipt final;
- sem cron;
- não mexer em produto, preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação.

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

## Evidências

- Lucas escreveu explicitamente: `LK Shopify/Growth write-enabled`.
- Lucas escreveu explicitamente: `Aprovação explícita atual: aprovado seguir`.
- O escopo está limitado e inclui rollback/readback.

## Bloqueio observado

Mesmo com o pedido write-enabled, o preflight deste turno continuou restringindo a sessão a leitura read-only, resolução local, rascunho interno e diagnóstico, bloqueando Shopify/Tiny write.

## Não ações

- Nenhuma mutation Shopify foi enviada.
- Nenhum `collectionReorderProducts` foi executado.
- Nenhum cron foi criado.
- Nenhuma alteração em Tiny, produto, preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação foi feita.

## Rollback planejado para execução real

Na execução write-enabled válida, gerar snapshot pré-write imediato e restaurar ordem anterior por `collectionReorderProducts`, com poll e readback.

## Decisão técnica necessária

Corrigir o Task Router/preflight para que pedidos explícitos de Lucas com `LK Shopify/Growth write-enabled` e escopo de Shopify collections aprovado não sejam classificados como read-only/bloqueados.
