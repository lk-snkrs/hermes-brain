# Receipt — LK Chatwoot WhatsApp API initial config

- Data UTC: 2026-06-02T15:03:17Z
- Sistema: Chatwoot self-hosted `https://chat.lkskrs.online`
- Conta: LK Sneakers
- Account ID: 1
- Versão verificada anteriormente: Chatwoot 4.14.1

## Decisão de Lucas

Lucas informou que não haverá configuração de chatbot/widget no site no momento. O foco operacional passa a ser WhatsApp Business API.

## Ações executadas via API

Com autorização explícita de Lucas (`pode seguir`):

- Criadas labels operacionais:
  - `pedido`
  - `estoque`
  - `troca`
  - `devolucao`
  - `prazo`
  - `reclamacao`
  - `vip`
  - `financeiro`
  - `humano`
  - `whatsapp-api`
- Criado time/fila:
  - `atendimento whatsapp`
  - auto-assign desativado (`allow_auto_assign=false`)

## Verificação

- Labels verificadas via API: OK.
- Times verificados via API: `suporte`, `atendimento whatsapp`.
- Inboxes verificados via API: nenhum inbox existente ainda.

## Não executado

- Não foi criado inbox Website.
- Não foi configurado chatbot/Captain/IA.
- Não foi configurado Shopify.
- Não foi criado inbox WhatsApp ainda porque faltam credenciais Meta/WhatsApp Cloud API:
  - número em formato E.164;
  - WhatsApp Phone Number ID;
  - WhatsApp Business Account ID;
  - Meta/WhatsApp Cloud API access token.

## Guardrails

- WhatsApp externo/produtivo continua sensível: não ativar automação ou resposta cliente sem escopo/aprovação.
- Atendimento humano primeiro; IA/Elle apenas futuro observe-only/rascunho se aprovado.
- Para estoque/disponibilidade, Tiny permanece fonte de verdade.
