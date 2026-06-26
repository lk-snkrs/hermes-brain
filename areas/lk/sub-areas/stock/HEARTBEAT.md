# HEARTBEAT — [LK] Estoque Loja Física

Status v0.1: preparado, não ativado.

## Cadência futura recomendada

- Diário manhã: gerar fila local/read-only de P0/P1 se houver dados disponíveis.
- Semanal: revisar top best sellers, rupturas e itens que deveriam estar na loja física.
- Evento futuro: venda/cancelamento Shopify pode ser gatilho, mas estoque final vem do Tiny.

## Telegram

Silent-OK. Só alertar Lucas quando:

- P0 com risco claro de venda perdida;
- decisão de compra/transferência necessária;
- dado crítico ausente impede decisão;
- integração/cron/fonte falhou.

Nenhum cron está aprovado/ativo nesta v0.1.
