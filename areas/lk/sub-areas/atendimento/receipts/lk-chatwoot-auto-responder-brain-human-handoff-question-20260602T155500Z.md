# Receipt — Pergunta sobre Chatwoot API, auto-responder com cérebro e transbordo humano

- Data UTC: 2026-06-02T15:55:00Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Conta: `LK Sneakers` / ID `1`

## Pergunta do Lucas

Lucas perguntou se Hermes consegue acessar conversas via API para responder mensagens automaticamente usando um cérebro criado para atendimento, com transbordo humano.

## Interpretação operacional

Sim, tecnicamente é possível com Chatwoot self-hosted usando:

- Webhooks de eventos de conversa/mensagem recebida;
- API do Chatwoot para ler conversas, contatos, mensagens, labels e times;
- Um serviço/agent interno para consultar Brain/Tiny/Shopify/contexto e decidir resposta;
- API do Chatwoot para enviar mensagem pública quando autorizado;
- Labels/status/assignments para transbordo humano.

## Guardrails necessários

- Não ativar envio automático ao cliente sem aprovação explícita e testes controlados.
- Começar em modo assistivo/draft: gerar sugestão interna/nota privada, não resposta pública.
- Tiny segue fonte oficial de estoque/disponibilidade; Shopify só contexto.
- Reclamação, negociação, prazo sensível, reserva, desconto, troca/devolução complexa e disponibilidade ambígua devem ir para humano.
- WhatsApp fora da janela 24h exige template aprovado Meta.
- Toda automação deve ter kill switch, logs, rastreabilidade, rate limits e fallback humano.

## Próximo caminho recomendado

1. Modo leitura/draft-only.
2. Brain de atendimento com políticas, macros e base de conhecimento.
3. Classificador de intenção/risco.
4. Resposta automática apenas para FAQs seguras após validação.
5. Transbordo humano por label/time/assignment.

## Nenhuma ação externa executada

Nenhum webhook, bot, automação, mensagem, inbox ou integração produtiva foi criado/alterado neste momento.
