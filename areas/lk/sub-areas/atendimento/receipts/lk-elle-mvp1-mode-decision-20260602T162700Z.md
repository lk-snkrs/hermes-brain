# Receipt — Elle MVP 1 mode decision

- Data UTC: 2026-06-02T16:27:00Z
- Sistema alvo: Chatwoot `https://chat.lkskrs.online`
- Conta: `LK Sneakers` / Account ID `1`
- Produto: Elle — Cérebro de Atendimento LK

## Decisão do Lucas

Lucas escolheu a opção C para o MVP 1:

> Nota privada + labels + transbordo automático para time humano.

## Interpretação

O MVP 1 deve operar em modo copiloto/assistivo, sem mensagem pública automática ao cliente, mas pode preparar organização interna:

1. Criar nota privada com sugestão/resumo/risco/fontes.
2. Aplicar labels operacionais conforme intenção.
3. Transbordar/atribuir para atendimento humano quando risco exigir.

## Guardrail crítico

A escolha C não autoriza resposta automática pública ao cliente.

Qualquer criação de webhook, agent, automação, envio de mensagem pública, criação de inbox WhatsApp, alteração externa ou write produtivo ainda requer plano e aprovação explícita de escopo.

## Escopo aprovado conceitualmente

- Cérebro em modo assistivo.
- Sem chatbot/site.
- WhatsApp Business API como canal alvo quando conectado.
- Shopify como contexto de atendimento/pedidos/clientes.
- Tiny como fonte oficial de estoque/disponibilidade.

## Próximos passos recomendados

1. Definir regras de labels e transbordo.
2. Definir formato da nota privada.
3. Definir filas/time/agente humano de destino.
4. Fazer plano técnico dry-run antes de configurar webhook/API.
5. Solicitar aprovação explícita para qualquer write produtivo no Chatwoot.
