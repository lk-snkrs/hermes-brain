# Decisions and Guardrails — LK Stock Approval Packets Ledger

## Decisões

- Onda 11 separa o ledger de approval packets do hub operacional de compra/recompra para preservar histórico sem virar autorização automática.

## Guardrails

- Approval packet não é aprovação; Lucas/Júlio/fonte viva precisam estar explícitos e atuais.
- Fixtures/probes/testes nunca alimentam score ou recomendação operacional.
- Compra, fornecedor, Tiny, Shopify inventory, reserva ou promessa a cliente exigem aprovação escopada.
- Preço/tamanho/margem dependem de fonte viva e data/hora da consulta.
