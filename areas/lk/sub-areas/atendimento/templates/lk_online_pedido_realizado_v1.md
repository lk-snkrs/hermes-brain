# Template WhatsApp — LK Online Pedido Realizado v1

Status: submetido à Meta; aguardando análise (`PENDING`)
Canal: WhatsApp Business API
Categoria: UTILITY
Idioma: pt_BR
Nome interno: lk_online_pedido_realizado_v1
Template ID Meta: 1027566083104214

## Header / imagem

Tipo: IMAGE
Regra de envio: usar a imagem do primeiro produto da compra.
Fallback: imagem institucional LK aprovada, caso o primeiro produto não tenha imagem pública válida.

## Body aprovado

```text
Olá, {{nome_cliente}}!

Recebemos seu pedido {{numero_pedido}} com sucesso.

Obrigado pela confiança em escolher a LK.

{{lista_produtos}}

Assim que o pagamento for aprovado, você receberá uma nova atualização por aqui.
```

## CTA

Tipo: URL
Texto do botão: Ver pedido
URL dinâmica: {{url_pedido}}

## Variáveis funcionais

- nome_cliente
- numero_pedido
- lista_produtos
- url_pedido
- primeiro_produto_imagem_url

## Regra da lista de produtos

Uma linha por produto, no formato:

```text
{{titulo_produto}} - {{variacao}}
```

Exemplo:

```text
New Balance 204L Mushroom - 38
```

Se quantidade > 1:

```text
2x New Balance 204L Mushroom - 38
```

## Restrições

- Não prometer separação.
- Não prometer pronta entrega.
- Não prometer prazo.
- Não assumir que é sneaker; pode ser roupa/acessório/outro produto.
- Próximo marco explícito: pagamento aprovado.

## Observação operacional

Submissão realizada diretamente pela Meta Graph API porque o endpoint Chatwoot disponível não aceitava HEADER IMAGE no builder local.

Resultado verificado:

- Template ID Meta: `1027566083104214`
- Status: `PENDING`
- Componentes: `HEADER IMAGE`, `BODY`, `BUTTONS`
- Chatwoot sync: HTTP 200
- Visível no Chatwoot: sim

A versão submetida usa variáveis posicionais internamente porque a Meta rejeitou variável nomeada no URL button como URI inválida. O texto final exibido ao cliente permanece o aprovado.