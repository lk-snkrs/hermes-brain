# Elle / Chatwoot AgentBot — pesquisa e rollout seguro

Data: 2026-06-11
Origem: pergunta de Lucas no Telegram sobre usar a opção A: AgentBot read-only em inbox de teste.
Fontes consultadas:
- Chatwoot AgentBot docs: https://www.chatwoot.com/docs/product/others/agent-bots
- Chatwoot Webhooks docs: https://www.chatwoot.com/hc/user-guide/articles/1677693021-how-to-use-webhooks

## Conclusão

Sim: para validar a integração nativa do Chatwoot AgentBot, a maneira correta/segura é começar com **AgentBot em inbox de teste**, em modo read-only/observe-only do lado da Elle.

Não é recomendado conectar AgentBot read-only diretamente no inbox real como primeiro passo, porque a própria documentação do Chatwoot diz que, quando um AgentBot é conectado a um inbox, novas conversas são automaticamente atribuídas ao status `pending`. Isso pode alterar a fila operacional e o handoff da Larissa.

## Evidências da documentação

A documentação oficial do Chatwoot AgentBot afirma:

- AgentBot conecta agentes externos/IA diretamente a um inbox do Chatwoot.
- Depois de conectado a um inbox, novas conversas são automaticamente atribuídas ao status `pending`.
- Chatwoot envia eventos como `widget_triggered`, `message_created` e `message_updated` para a URL do bot.
- O bot pode responder usando a API de mensagens.
- Para handoff humano, o bot muda o status da conversa para `open`.
- Agentes podem devolver uma conversa ao bot mudando status para `pending`.

A documentação de webhooks confirma:

- Webhooks enviam eventos como `message_created`, `message_updated`, `conversation_created`, `conversation_updated` etc.
- Assinatura HMAC usa headers `X-Chatwoot-Signature`, `X-Chatwoot-Timestamp`, `X-Chatwoot-Delivery`.
- A verificação deve usar raw body, comparação constant-time e janela anti-replay.

## Rollout recomendado

### Fase A — AgentBot em inbox de teste

Objetivo: validar comportamento nativo sem risco na fila real.

Configuração esperada da Elle:

```text
ELLE_DRY_RUN=true
CHATWOOT_WRITE_ENABLED=false
ELLE_PUBLIC_REPLY_ENABLED=false
ELLE_AGENTBOT_MODE=observe_only
```

Ações permitidas:

- receber eventos;
- validar assinatura;
- logar payload sanitizado;
- classificar intenção;
- simular decisão/resposta;
- não escrever no Chatwoot;
- não mudar status;
- não responder cliente.

Testes mínimos:

- nova conversa fica `pending` quando bot está conectado;
- evento `message_created` chega no endpoint da Elle;
- mensagens `outgoing`/privadas são ignoradas;
- assinatura HMAC é validada com raw body;
- falha da Elle não afeta inbox real;
- kill switch bloqueia processamento;
- casos de LK: pedido enviado, pedido não enviado, estoque/pronta entrega, print concorrente, foto solta, reclamação.

### Fase B — produção observe-only por webhook genérico

Se o objetivo for observar produção real sem alterar fila, usar webhook genérico `message_created` é mais seguro do que AgentBot real, porque não força status `pending`.

### Fase C — AgentBot no inbox real

Só depois de validar A e/ou B. Ao ativar no inbox real, precisa ter fallback/handoff explícito:

- resposta pública somente em categorias liberadas;
- casos ambíguos/problemas mudam para `open` para humano;
- stock/pronta entrega segue para Larissa/lk-stock;
- pedido não enviado/problemático segue para Larissa.

## Decisão operacional

Para testar AgentBot nativo: **fazer A**.
Para observar produção sem impacto: **usar webhook genérico observe-only**.
Para atender clientes com Elle: só após rollout controlado e aprovação explícita.
