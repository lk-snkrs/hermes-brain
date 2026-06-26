# Receipt — Submissão Meta template `lk_online_pedido_realizado_v1`

Data: 2026-06-13
Classificação: external-write autorizado por Lucas
Solicitante: Lucas Cimino

## Resultado

Template submetido à Meta para análise.

- Nome: `lk_online_pedido_realizado_v1`
- Template ID Meta: `1027566083104214`
- Status verificado: `PENDING`
- Categoria: `UTILITY`
- Idioma: `pt_BR`
- Componentes verificados: `HEADER IMAGE`, `BODY`, `BUTTONS`
- Chatwoot sync: HTTP 200
- Visível no Chatwoot após sync: sim

## Texto aprovado/submetido

```text
Olá, {{nome_cliente}}!

Recebemos seu pedido {{numero_pedido}} com sucesso.

Obrigado pela confiança em escolher a LK.

{{lista_produtos}}

Assim que o pagamento for aprovado, você receberá uma nova atualização por aqui.
```

## CTA

- Botão: `Ver pedido`
- URL button dinâmico submetido com variável posicional de sufixo.

## Header / imagem

- Tipo: `IMAGE`
- Sample image carregada via Meta Resumable Upload API.
- Regra operacional aprovada para envio real: usar imagem do primeiro produto da compra; fallback institucional LK se não houver imagem pública válida.

## Observações técnicas

- O endpoint Chatwoot de builder local não contemplava `HEADER IMAGE`; por isso a criação foi feita diretamente pela Meta Graph API.
- Primeira tentativa com variáveis nomeadas no URL button foi rejeitada pela Meta com erro de URI inválida.
- Submissão final usou `parameter_format=positional` internamente, preservando o texto aprovado pelo Lucas.
- Mapeamento de envio real:
  - BODY `{{1}}` = nome_cliente
  - BODY `{{2}}` = numero_pedido
  - BODY `{{3}}` = lista_produtos
  - BUTTON URL `{{1}}` = sufixo/path do pedido
  - HEADER = imagem do primeiro produto

## Segurança

- values_printed=false
- Nenhum token/secret impresso.
- Nenhuma mensagem enviada para cliente.
- Nenhum fluxo de disparo ativado.
- Shopify/Tiny/estoque não alterados.
