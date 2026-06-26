# Receipt — Template pedido realizado online LK

Data: 2026-06-13
Classificação: local-write / external-read-only
Solicitante: Lucas Cimino

## Decisão aprovada

Template `lk_online_pedido_realizado_v1` aprovado para submissão Meta, com:

- Canal: WhatsApp Business API para venda online/e-commerce
- Header: imagem do primeiro produto da compra
- Body com quebras de linha entre blocos
- Lista direta de produtos no formato `Título do produto - Variação`
- CTA: `Ver pedido`
- Próximo marco: pagamento aprovado

## Texto aprovado

```text
Olá, {{nome_cliente}}!

Recebemos seu pedido {{numero_pedido}} com sucesso.

Obrigado pela confiança em escolher a LK.

{{lista_produtos}}

Assim que o pagamento for aprovado, você receberá uma nova atualização por aqui.
```

## Ações executadas

- Registrado template aprovado no Brain.
- Criado draft de payload Meta com HEADER IMAGE + BODY + CTA.
- Consultado Chatwoot templates via API read-only.
- Confirmado que há templates WhatsApp aprovados existentes, inclusive `lk_pedido_criado`, `lk_pagamento_aprovado`, `lk_pedido_enviado`, `lk_pedido_entregue`.

## Bloqueio para submissão imediata

Não foi submetido um template novo porque o endpoint Chatwoot disponível observado aceita templates de BODY/BUTTONS, mas a referência local do builder não contempla HEADER IMAGE. Submeter sem imagem violaria a decisão do Lucas.

Para submissão correta, é necessário usar caminho que aceite `HEADER IMAGE`, com sample image upload handle Meta, ou ajustar/confirmar endpoint que suporte header image antes do POST.

## Segurança

- Secrets: valores não impressos.
- Cliente: nenhuma mensagem enviada.
- Shopify/Tiny/WhatsApp/Meta: nenhum disparo para cliente.
- Meta: nenhum template incompleto submetido.
