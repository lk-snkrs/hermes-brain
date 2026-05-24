# LK OS — WhatsApp Hermes Agent Number Pending

Status: `pending_connect_tomorrow`
Data registrada: 2026-05-12 BRT / 2026-05-13 UTC
Escopo: LK OS / wacli/OpenClaw / WhatsApp agent account

## Número planejado

- Account slug planejado no wacli: `hermes`
- Apelido operacional: `Hermes`
- Número: `+55 11 98555-5245`
- Digits para phone pairing: `5511985555245`

## Papel pretendido

O número `Hermes` será o agente de interação com grupos de WhatsApp e suporte da LK, separado das contas:

- `pessoal` — Lucas pessoal.
- `lk-compras` — WhatsApp Business compras/sourcing.
- `hermes` — agente Hermes para grupos/suporte/reportes/perguntas operacionais.

## Exemplos de uso desejado

1. Enviar report diário de vendas para grupos autorizados.
2. Responder perguntas operacionais em WhatsApp, por exemplo:
   - Pergunta do Júlio: “quem ofereceu o tênis 9060wht mais barato?”
   - Resposta esperada: buscar na fila/sinais do `lk-compras`, comparar fornecedores/preços/proximidade SP quando aplicável e responder com a melhor evidência disponível.
3. Apoiar suporte com respostas baseadas em fontes internas, sem inventar dado.

## Fontes necessárias para respostas

- `lk-compras` wacli local: sinais de pedidos/respostas/preço/logística.
- Shopify/Tiny quando envolver produto/SKU/tamanho/estoque.
- Notion quando envolver compra lançada, se integração estiver autorizada.
- Reports LK OS quando envolver vendas diárias.

## Guardrails

- Conectar/autenticar o número é permitido quando Lucas estiver pronto para inserir código/QR.
- Entrar em grupos, responder mensagens, enviar report diário ou operar suporte é ação externa e exige escopo/guardrails aprovados.
- A conta `hermes` não deve enviar mensagem automática antes de aprovação explícita de Lucas para destino, gatilho, texto/formato e fallback de erro.
- Respostas devem citar fonte/classe de evidência quando possível: `lk-compras`, Shopify, Tiny, Notion, report diário.
- Se a evidência não estiver clara, responder “não sei ainda / preciso verificar”, não inventar.
- PII e conversas brutas não devem ser expostas fora do contexto autorizado.

## Próximo passo planejado

Amanhã: criar/autenticar a conta wacli nomeada `hermes` com phone pairing:

```bash
/opt/data/bin/wacli accounts add hermes --phone 5511985555245 --events --idle-exit 5m
```

Se a conta já existir ou o pairing expirar:

```bash
/opt/data/bin/wacli --account hermes auth --phone 5511985555245 --events --idle-exit 5m
```

Depois verificar:

```bash
/opt/data/bin/wacli --account hermes auth status --json
/opt/data/bin/wacli accounts list --json
```

## Não executar ainda

- enviar WhatsApp;
- responder Júlio/grupo/suporte;
- adicionar cron de report diário;
- entrar/alterar grupo;
- criar automação de suporte;
- write em Notion, Shopify, Tiny, banco ou qualquer sistema externo.
