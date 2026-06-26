# Elle live report — 2026-06-14 15:24 BRT

Escopo: relatório read-only/sanitizado solicitado por Lucas sobre o que a Elle respondeu hoje, o que ficou fora do fluxo e o que não foi respondido.

Fonte: logs Elle `/opt/elle-chatwoot/logs/events.jsonl` e Chatwoot API read-only via Doppler. Secrets não impressos. Sem writes externos.

## Totais

- Conversas únicas com processamento da Elle: 10
- Eventos processed: 14
- Eventos ai_decision: 36
- Eventos ignorados/fora do fluxo: 126
- Travas por humano: 18

## Fora do fluxo

- event_filter: 119
- human_takeover_lock: 7
- eventos ignorados por tipo: conversation_updated=51, message_updated=33, message_created=31, sem_evento=7, conversation_status_changed=3, conversation_opened=1
- trava humana human_outgoing_message: 18

Interpretação: boa parte do “fora do fluxo” são eventos operacionais do Chatwoot (updates, status, outgoing/humano, duplicados/contexto), não perguntas reais que a Elle deveria responder. 7 foram bloqueados por trava humana.

## Conversas e temas sanitizados

- Conversa 123: stock_handoff; Chatwoot API não retornou mensagem pública legível na leitura; encaminhada/sem resposta final da Elle.
- Conversa 1360: pedido sem número informado; human_handoff; não respondido pela Elle, encaminhado.
- Conversa 1372: reclamação de pós-venda/reembolso e ameaça de medida; human_handoff; não respondido pela Elle, corretamente encaminhado.
- Conversa 1575: disponibilidade/tamanho New Balance 204L Mushroom; Elle respondeu que chamaria equipe para confirmar disponibilidade/tamanhos; cliente respondeu “ok”; depois human_handoff.
- Conversa 1694: saudação + pergunta se produto chegou no estoque + não recebeu; greeting/estoque/pós-venda; saída pública de saudação registrada sem marca elle_generated.
- Conversa 1888: cliente navegando em Onitsuka Mexico 66 e queria saber mais; saída pública respondeu originalidade, mas isso provavelmente está desalinhado com a correção de Lucas para coleção/produto.
- Conversa 1894: saudação + pergunta New Balance 9060/Moonbeam; Elle respondeu com handoff de disponibilidade/tamanhos e link de coleção; houve também saída de carrinho/ajuda.
- Conversa 1895: cliente em Track order status perguntou entrega; saída pública respondeu originalidade, desalinhado para pedido/rastreamento.
- Conversa 1896: cliente navegando em New Balance 530 queria saber mais; saída pública respondeu originalidade, possivelmente desalinhado.
- Conversa 1897: cliente em Air Jordan 1 queria saber mais e perguntou tamanho 36; Elle respondeu originalidade; pergunta de tamanho ficou em human_handoff/não respondida.

## Pontos de melhoria sugeridos

1. Ajustar categoria `institutional` para não responder originalidade quando a pergunta é “gostaria de saber mais” em página de produto/coleção.
2. Para página de produto: responder curto sobre o produto/coleção e perguntar como ajudar; se virar tamanho/disponibilidade, transferir para Larissa.
3. Para “Track order status”/pedido: não responder originalidade; pedir/validar número do pedido e encaminhar se não houver rastreio verificado.
4. Verificar marcação `content_attributes.elle_generated=true`, pois algumas saídas públicas parecem da Elle mas não vieram marcadas assim na API.

## Non-actions

- Nenhuma alteração em Chatwoot, Shopify, Tiny, WhatsApp ou código.
- Nenhum secret impresso.
- PII sanitizada no relatório.
