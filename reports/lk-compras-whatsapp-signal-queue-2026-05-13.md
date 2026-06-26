# LK Compras — WhatsApp Signal Queue v1

Status: `read_only_sanitized_queue_ready`
Data: 2026-05-13T01:29:13.091188+00:00
Fonte: `platform_signal_wacli_local` (`lk-compras`).

## Resumo

- Mensagens escaneadas: 1000.
- Chats únicos na amostra: 15.
- Sinais classificados: 104.
- Store atual: chats=50; groups=34; messages=4873.

## Contagens por sinal

- `proximidade_sp_logistica`: 30
- `pedido_de_compra`: 28
- `produto_tamanho_estoque`: 23
- `resposta_fornecedor`: 17
- `negociacao_preco`: 17
- `fechamento_compra`: 15

## Regra de decisão aprendida

Compra LK não é apenas menor preço: escolher menor preço viável **ou** fonte mais perto de São Paulo quando a diferença não for grande.
Depois da compra humana, lançar no Notion.

## Não executado

- Nenhum WhatsApp enviado.
- Nenhum contato com fornecedor/grupo/cliente.
- Nenhuma compra/reserva/pagamento.
- Nenhum write em Notion.
- Nenhum write em Shopify/Tiny/Merchant/banco/Klaviyo/Meta/Google/n8n.
- Nenhum nome, telefone, JID ou texto literal publicado.

## Próximo seguro

Transformar esta fila em preview de ranking por produto/tamanho/preço/logística. Qualquer envio, compra ou lançamento Notion exige aprovação explícita atual.
