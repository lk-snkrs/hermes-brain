# Correção Elle — troca com pedido identificado

Data: 2026-06-15 11:20 BRT
Canal: LK WhatsApp / Chatwoot
Conversa: #1931
Cliente: Luciane
Pedido informado: 147714
Contexto fornecido por Lucas: New Balance 9060 Cortado Marrom, tamanho 39

## Erro apontado por Lucas

1. Elle não deveria informar o horário da Larissa às 11:17, pois estava dentro do atendimento.
2. Em pedido de troca com pedido identificado, Elle deve mencionar o pedido/produto/tamanho atual e perguntar para qual tamanho a cliente quer trocar antes de transferir.

## Resposta correta esperada

"Luciane, recebi seu pedido de troca referente ao pedido 147714, do produto New Balance 9060 Cortado Marrom, tamanho 39. Para qual tamanho você gostaria de trocar? Me avise para eu transferir a conversa para a Larissa, ok?"

## Regra atualizada

- Para troca/devolução com número do pedido e contexto Shopify validado: confirmar pedido + produto/variante/tamanho atual, perguntar o tamanho desejado e só então encaminhar para Larissa.
- Não incluir horário da Larissa quando a conversa ocorrer dentro do horário de atendimento.
- Não prometer disponibilidade do tamanho desejado antes de validação por lk-stock/Larissa.

## Execução

- Sem envio ao cliente.
- Sem write externo em Chatwoot/Shopify/Tiny.
- Correção registrada localmente e regra adicionada à skill `customer-chat-operations`.
