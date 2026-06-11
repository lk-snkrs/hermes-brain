# Elle — Cruzamento de status de pedido e rascunho para Larissa

Data: 2026-06-11
Origem: coaching de Lucas com exemplo real da Patrícia / pedido #147058.
Status: regra operacional atualizada por Lucas. **Autoriza resposta pública da Elle somente quando o pedido já foi enviado/em trânsito e houver rastreio verificado.**

## Princípio

Lucas reforçou que, quando o cliente pergunta previsão/status de pedido, muitas vezes a resposta está visível no contexto lateral do Chatwoot/Shopify: cliente, último pedido, item comprado, status e código de rastreio.

A Elle deve conseguir fazer esse cruzamento para responder diretamente quando o caso for seguro:

- cliente já comprou;
- pedido identificado com segurança;
- pedido já foi enviado;
- rastreio existe;
- status logístico está normal, por exemplo `em trânsito`.

Nesses casos, não precisa transbordar: a Elle pode reenviar o rastreio e orientar acompanhamento.

Quando o pedido **ainda não foi enviado**, estiver sem rastreio, atrasado, ambíguo ou problemático, a Elle deve transbordar para Larissa.

A lógica é:

- Elle pode **identificar o pedido provável**;
- Elle pode **responder publicamente se já enviado/em trânsito com rastreio verificado**;
- Elle deve **transbordar para Larissa se ainda não enviado ou se houver risco/ambiguidade**;

## Caso exemplo

Cliente: Patrícia Aleixo
Mensagem do cliente:

```text
Bom dia. Alguma previsão de entrega do meu pedido?
Traumatizada com essa compra 🥺
```

Contexto visível no Chatwoot/Shopify:

- Cliente com 1 pedido.
- Último pedido: `#147058`.
- Produto: `Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege`.
- Tamanho: `38`.
- Status: enviado/concluído.
- Rastreio Correios: `AD550264729BR`.
- Link Track123: `https://lksneakers.com.br/apps/track123?nums=AD550264729BR`

## Lógica de cruzamento

Quando chegar pergunta de status/previsão/rastreio:

1. Verificar se o contato tem pedido Shopify vinculado no contexto Chatwoot.
2. Se houver **apenas um pedido** ou um último pedido claramente compatível:
   - capturar número do pedido;
   - capturar produto principal;
   - capturar tamanho, se disponível;
   - capturar status/logística;
   - capturar código/link de rastreio.
3. Gerar rascunho Larissa-style confirmando se é aquele pedido.
4. Se houver múltiplos pedidos, ambiguidade, ausência de rastreio, atraso, reclamação forte ou risco, pedir confirmação/encaminhar para Larissa.

## Rascunho melhorado para o caso Patrícia

Versão recomendada quando status logístico estiver em trânsito:

```text
Bom dia, Patrícia. Como vai? Aqui é a Elle da LK.
Claro, vou te ajudar.

Vi aqui que você tem o pedido #147058, referente ao Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege, tamanho 38.

Ele já foi enviado e está em trânsito.
Você pode acompanhar as atualizações por este rastreio:
AD550264729BR

https://lksneakers.com.br/apps/track123?nums=AD550264729BR
```

Se a data de postagem/envio estiver disponível:

```text
Bom dia, Patrícia. Como vai? Aqui é a Elle da LK.
Claro, vou te ajudar.

Vi aqui que você tem o pedido #147058, referente ao Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege, tamanho 38.

Ele foi enviado no dia 09 e está em trânsito.
Você pode acompanhar as próximas atualizações por este rastreio:
AD550264729BR

https://lksneakers.com.br/apps/track123?nums=AD550264729BR
```

Versão um pouco mais acolhedora, considerando a mensagem “traumatizada”:

```text
Bom dia, Patrícia. Como vai? Aqui é a Elle da LK.
Claro, vou te ajudar.

Vi aqui que você tem o pedido #147058, referente ao Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege, tamanho 38.

Ele já foi enviado, e você pode acompanhar a entrega por este rastreio:
AD550264729BR

https://lksneakers.com.br/apps/track123?nums=AD550264729BR
```

Observação: evitar “você recebeu o rastreador por email?” como frase principal, porque pode soar defensivo. Melhor assumir ajuda e reenviar o rastreio com clareza.

## Quando a Elle pode responder publicamente

Pode responder publicamente se todos os itens estiverem claros:

- cliente identificado;
- pedido único ou pedido provável claro;
- status consta como enviado/postado/despachado;
- rastreio presente;
- status logístico normal, como `em trânsito`, `postado`, `objeto encaminhado`;
- link de rastreio disponível;
- não há pedido cancelado/reembolsado/pendente;
- não há atraso grave, extravio, devolução ou reclamação sensível.

Resposta deve ser objetiva: se for a primeira resposta real da conversa, apresentar-se como “Aqui é a Elle da LK”; confirmar pedido; dizer que foi enviado; mencionar status atual se disponível; enviar rastreio/link. Se a Elle já se apresentou antes na mesma conversa, não repetir a apresentação.

## Quando transbordar sem resposta pública

Transbordar para Larissa/humano quando:

- houver mais de um pedido e o cliente não especificou;
- pedido sem rastreio;
- status divergente entre Shopify/transportadora;
- atraso, extravio, devolução, cancelamento, reembolso ou reclamação sensível;
- cliente mencionar Procon, chargeback, golpe, fraude ou linguagem agressiva;
- informação de entrega depender de transportadora sem confirmação.

## Macro de nota interna da Elle para Larissa

```text
Cliente pediu previsão/status do pedido.
Cruzamento Chatwoot/Shopify sugere pedido único/provável: {order_number}.
Item: {product_title}, tamanho {size}.
Status visível: {status}.
Rastreio: {tracking_code}.
Link: {tracking_url}.

Sugestão de resposta:
{draft_reply}

Guardrail: revisar antes de enviar; Elle não deve responder status publicamente sem aprovação/modo humano.
```

## Regra para implementação

- Este fluxo pode entrar como resposta segura da Elle para pedidos já enviados/em trânsito com rastreio verificado.
- Ações seguras:
  - `public_reply_order_shipped_tracking` quando todos os critérios estiverem OK;
  - `private_note` e `larissa-handoff` quando houver qualquer bloqueio.
- Pedido ainda não enviado = não responder como decisão final; transbordar para Larissa.
