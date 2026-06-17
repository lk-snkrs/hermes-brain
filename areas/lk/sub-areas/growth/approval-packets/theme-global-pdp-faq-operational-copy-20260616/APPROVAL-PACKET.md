# Approval Packet — Correção FAQ global PDP

Gerado: 2026-06-16T18:33:16.944814+00:00

## Contexto
Após aplicar o Lote 2, o Shopify Admin e `/products/handle.js` ficaram OK, mas o HTML público ainda contém texto operacional em um FAQ global do tema PDP.

## Evidência
- Asset encontrado: `sections/lk-pdp.liquid`
- Tema: `lk-new-theme/production` / role `main`
- Texto atual: `Produtos sob encomenda: 4 a 6 semanas.`
- Busca read-only: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/top50-product-faq-geo-20260616/theme-global-pdp-faq-20260616/global-pdp-faq-theme-search.json`

## Mudança proposta
Trocar somente a resposta do FAQ global `Qual o prazo de entrega?` em `sections/lk-pdp.liquid`.

De:
`Itens confirmados são preparados com agilidade. O prazo varia conforme sua região. Produtos sob encomenda: 4 a 6 semanas.`

Para:
`Itens confirmados são preparados com cuidado e o prazo varia conforme a região e a confirmação do pedido. Se houver qualquer dúvida antes da compra, a equipe LK orienta pelo chat.`

## Impacto
- Remove promessa operacional pública incompatível com guardrails LK.
- Mantém confiança e atendimento humano.
- Afeta todos os PDPs que usam o FAQ global.

## Risco
- Baixo, mas é alteração de theme production e customer-facing.
- Precisa backup do asset antes, write controlado, readback e fetch público pós-apply.

## Rollback
Restaurar o conteúdo anterior do asset `sections/lk-pdp.liquid` a partir do backup salvo antes do write.

## Aprovação necessária
Para aplicar, usar aprovação explícita:
`Aprovo corrigir o FAQ global do PDP em theme production, com backup e rollback.`