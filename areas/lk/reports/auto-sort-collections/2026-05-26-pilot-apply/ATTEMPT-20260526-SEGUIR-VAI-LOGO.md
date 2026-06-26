# Tentativa de execução — auto-ordenação piloto LK

Data: 2026-05-26
Pedido: "seguir vai logo"
Escopo solicitado: aplicar piloto nas 10 coleções aprovadas, Tiny como fonte primária para esgotados no final, snapshot imediato, readback, sem cron.

## Status

Não executado neste runtime.

## Motivo

O contexto operacional atual está restrito a pesquisa/síntese/documentação local e não permite write externo/produção. A ação `collectionReorderProducts` altera merchandising público de coleções Shopify e permanece bloqueada neste turno.

## Garantias mantidas

- Nenhum write Shopify enviado.
- Nenhum write Tiny enviado.
- Nenhum cron criado.
- Nenhuma alteração em preço, estoque, disponibilidade, tema, SEO, tags, checkout, campanha ou comunicação.

## Próximo executor necessário

Executar em contexto habilitado para Shopify write, mantendo exatamente:

1. Snapshot pré-write imediato das 10 coleções.
2. Tiny/SQLite como fonte primária para esgotados.
3. Produtos esgotados ao final.
4. `collectionReorderProducts` somente nas 10 coleções aprovadas.
5. Poll do job assíncrono.
6. Readback por coleção.
7. Receipt final.
8. Sem cron.
