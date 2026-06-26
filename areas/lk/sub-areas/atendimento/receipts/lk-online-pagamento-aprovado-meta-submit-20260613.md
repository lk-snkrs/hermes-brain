# Receipt — Submissão Meta template `lk_online_pagamento_aprovado_v1`

Data: 2026-06-13
Classificação: external-write autorizado por Lucas
Solicitante: Lucas Cimino

## Resultado

Template submetido à Meta para análise.

- Nome: `lk_online_pagamento_aprovado_v1`
- Template ID Meta: `1318612266466142`
- Status verificado: `PENDING`
- Categoria: `UTILITY`
- Idioma: `pt_BR`
- Componentes verificados: `HEADER IMAGE`, `BODY`, `BUTTONS`
- Chatwoot sync: HTTP 200
- Visível no Chatwoot após sync: sim

## Texto aprovado/submetido

```text
Olá, {{nome_cliente}}!

O pagamento do seu pedido {{numero_pedido}} foi aprovado com sucesso.

Nossa equipe vai acompanhar as próximas etapas e você receberá uma nova atualização por aqui quando houver novidade sobre o seu pedido.

Qualquer dúvida, ficamos à disposição.
```

## CTA

- Botão: `Ver pedido`
- URL button dinâmico com variável posicional de sufixo.

## Header / imagem

- Tipo: `IMAGE`
- Sample image carregada via Meta Resumable Upload API.
- Regra operacional aprovada para envio real: usar imagem do primeiro produto da compra; fallback institucional LK se não houver imagem pública válida.

## Observações técnicas

- Template submetido como `UTILITY` porque confirma pagamento aprovado de pedido existente.
- Sem agradecimento repetido e sem lista de produtos, conforme correção do Lucas.
- Mapeamento de envio real:
  - BODY `{{1}}` = nome_cliente
  - BODY `{{2}}` = numero_pedido
  - BUTTON URL `{{1}}` = sufixo/path do pedido
  - HEADER = imagem do primeiro produto

## Segurança

- values_printed=false
- Nenhum token/secret impresso.
- Nenhuma mensagem enviada para cliente.
- Nenhum fluxo de disparo ativado.
- Shopify/Tiny/estoque não alterados.
