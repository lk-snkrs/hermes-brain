# Decisão — copy canônica WhatsApp checkout abandonado LK

Data: 2026-05-20
Área: LK CRM / WhatsApp / Crisp / n8n
Status: decisão corrigida por Lucas; T2/T3 aprovados por Lucas; templates T2/T3 enviados para aprovação Meta em 2026-05-20.

## Contexto

Lucas corrigiu que a primeira mensagem usada em proposta posterior estava errada. A versão genérica abaixo **não** deve ser tratada como a primeira mensagem escolhida:

```text
Olá {{1}}, aqui é a LK Sneakers. Nosso atendimento está à disposição para te ajudar com {{2}} e finalizar com segurança.
```

## Primeira mensagem canônica

```text
Oi {{1}}, aqui é da LK. Vi que você estava olhando {{2}} e deixamos seu checkout salvo por aqui.

Na LK, todos os produtos têm garantia de originalidade. Se quiser, nosso atendimento pode te ajudar com a numeração e finalizar tudo com segurança.
```

Botão:

```text
Finalizar compra
```

## Diretriz para sequência 24h/72h

- As mensagens seguintes devem ser continuação natural desta primeira mensagem.
- T2/24h sem desconto por padrão.
- T3/72h pode incluir cupom personalizado de 10%, gerado especialmente para a cliente, desde que o fluxo de cupom seja aprovado e seguro.
- Não usar urgência falsa.
- Não falar de estoque, pronta entrega, encomenda ou prazo no template fixo.
- Garantia de originalidade deve aparecer como afirmação positiva da LK, não como dúvida do cliente.
- Todos os touchpoints WhatsApp de checkout abandonado devem manter imagem do produto no topo/header quando o template/canal suportar `HEADER IMAGE`.
- Evitar repetir em T2 a frase/conceito `finalizar com segurança`, porque T1 já usa esse território. Em T2, trocar por ajuda com numeração, detalhes do produto, checkout salvo ou atendimento humano.

## T2/24h — aprovado por Lucas

```text
Oi {{1}}, tudo bem?

Passando só para saber se ficou alguma dúvida sobre {{2}}. Se quiser, nosso atendimento pode te ajudar com numeração, detalhes do produto ou retomar seu checkout salvo.
```

Botão:

```text
Finalizar compra
```

Imagem:

```text
Header com imagem do produto
```

## T3/72h — aprovado por Lucas

Direção corrigida por Lucas:

- Não falar “retomar {{2}}” / “retomar o produto”.
- O objetivo é **finalizar a compra**.
- Usar formulação direta: “criamos um cupom de 10% para você finalizar sua compra”.
- Cupom personalizado em `{{2}}` no template T3 (template sem variável de produto; variáveis Meta devem ser sequenciais).
- Header com imagem do produto.

Rascunho ajustado com direção preferida por Lucas:

```text
Oi {{1}}, passando para deixar uma condição especial para você finalizar sua compra.

Criamos um cupom de 10% de desconto especialmente para você usar no checkout: {{2}}

Ele é válido por 24 horas e depois expira.
```

Botão:

```text
Finalizar compra
```

Imagem:

```text
Header com imagem do produto
```

## Guardrail operacional

Antes de criar/editar template Meta/Crisp, patchar n8n ou ativar fluxo customer-facing, exigir aprovação explícita atual de Lucas.

## Envio para aprovação Meta

Data UTC: 2026-05-20T17:15:05Z
WABA: `1478026007140488`
Categoria: `MARKETING`
Idioma: `pt_BR`

Templates submetidos:

- `lk_checkout_abandonado_24h_v1`
  - Meta ID: `1524179605779294`
  - Status inicial: `PENDING`
- `lk_checkout_abandonado_72h_cupom10_v1`
  - Meta ID: `914082654982551`
  - Status inicial: `PENDING`

Receipt:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/crm/receipts/meta-template-submit-checkout-24h-72h-2026-05-20.json
```

Não foi ativado n8n, não foi enviado WhatsApp e não foi criado cupom Shopify neste passo.
