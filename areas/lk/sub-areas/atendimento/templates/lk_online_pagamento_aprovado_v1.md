# Template WhatsApp — LK Online Pagamento Aprovado v1

Status: submetido à Meta; aguardando análise (`PENDING`)
Canal: WhatsApp Business API
Categoria: UTILITY
Idioma: pt_BR
Nome interno: lk_online_pagamento_aprovado_v1
Template ID Meta: 1318612266466142

## Header / imagem

Tipo: IMAGE
Regra de envio: usar a imagem do primeiro produto da compra.
Fallback: imagem institucional LK aprovada, caso o primeiro produto não tenha imagem pública válida.

## Body aprovado

```text
Olá, {{nome_cliente}}!

O pagamento do seu pedido {{numero_pedido}} foi aprovado com sucesso.

Nossa equipe vai acompanhar as próximas etapas e você receberá uma nova atualização por aqui quando houver novidade sobre o seu pedido.

Qualquer dúvida, ficamos à disposição.
```

## CTA

Tipo: URL
Texto do botão: Ver pedido
URL dinâmica: {{url_pedido}}

## Variáveis funcionais

- nome_cliente
- numero_pedido
- url_pedido
- primeiro_produto_imagem_url

## Restrições

- Não repetir agradecimento da primeira mensagem.
- Não repetir lista de produtos da primeira mensagem.
- Não prometer separação.
- Não prometer pronta entrega.
- Não prometer envio em breve.
- Não prometer prazo.
- Não assumir que é sneaker; pode ser roupa/acessório/outro produto.

## Observação operacional

Mensagem de utility/transacional: confirmação de pagamento aprovado de um pedido existente. Não incluir cupom, oferta, cross-sell ou linguagem promocional.
