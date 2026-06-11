# Checkout LK — Top benefit copy execução aprovada

Data UTC: 2026-06-10T19:44:25+00:00

## Aprovação

Lucas aprovou subir no checkout:

- Linha 1: `Parcele em até 10x sem juros`
- Linha 2 condicional:
  - subtotal >= R$499: `Frete grátis disponível após informar o CEP.`
  - subtotal < R$499: `Frete grátis acima de R$499.`

## Execução

- Arquivo alterado: `/opt/data/projects/lk-gift-bag-checkout-app/extensions/shipping-microcopy/src/Checkout.jsx`
- Hook usado: `useSubtotalAmount()`
- Threshold: `499`
- Build local: passou
- Deploy Shopify: passou
- App version liberada: `lk-gift-bag-checkout-17`
- Mensagem de deploy: `Update top checkout benefit copy with installments and conditional free shipping`

## QA real mobile — carrinho >= R$499

- Produto/carrinho: variante `48300570116318`, total observado `R$ 2.399,99`
- Report: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/shipping-microcopy-report.json`
- Screenshot topo: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/shipping-microcopy-0.png`
- `installmentCopyFound`: `True`
- `aboveThresholdCopyFound`: `True`
- `belowThresholdCopyFound`: `False`
- `oldLowerMicrocopyFound`: `False`

Positions:

```json
{
  "lkCheckout": 92,
  "installment": 104,
  "aboveThresholdShipping": 133,
  "belowThresholdShipping": -1,
  "contato": 178,
  "entrega": 273,
  "cep": 173,
  "pagarAgora": 5880,
  "google": 5892
}
```

Trecho:

```text
Pular para o conteúdo
Navegar até a loja virtual
Resumo do pedido
Preço total

R$ 2.399,99

LK Checkout
Parcele em até 10x sem juros
Frete grátis disponível após informar o CEP.
Contato
Fazer login
E‑mail ou número de celular
Enviar novidades e ofertas para mim por e-mail
Entrega
Escolher uma forma de entrega
Enviar
Retirada
Paí
```

## QA real mobile — carrinho < R$499

- Produto/carrinho: variante `48283857780958`, total observado no checkout `R$ 83,92`
- Report: `/opt/data/tmp/lk-checkout-qa/output-shipping-below499-20260610/shipping-microcopy-report.json`
- Screenshot topo: `/opt/data/tmp/lk-checkout-qa/output-shipping-below499-20260610/shipping-microcopy-0.png`
- `installmentCopyFound`: `True`
- `aboveThresholdCopyFound`: `False`
- `belowThresholdCopyFound`: `True`
- `oldLowerMicrocopyFound`: `False`

Positions:

```json
{
  "lkCheckout": 89,
  "installment": 101,
  "aboveThresholdShipping": -1,
  "belowThresholdShipping": 130,
  "contato": 159,
  "entrega": 254,
  "cep": 342,
  "pagarAgora": 5334,
  "google": 5346
}
```

Trecho:

```text
Pular para o conteúdo
Navegar até a loja virtual
Resumo do pedido
Preço total

R$ 83,92

LK Checkout
Parcele em até 10x sem juros
Frete grátis acima de R$499.
Contato
Fazer login
E‑mail ou número de celular
Enviar novidades e ofertas para mim por e-mail
Entrega
Escolher uma forma de entrega
Enviar
Retirada
País/Região
Brasil
Nom
```

## Rollback

Reverter `/extensions/shipping-microcopy/src/Checkout.jsx` para a copy anterior:

```text
Frete grátis acima de R$499
Calculado após informar o CEP.
```

e rodar novo `npm run build` + `npm run deploy -- --allow-updates` com QA real mobile. Alternativamente, remover o app block no Checkout Editor.

## Não-ações

- Nenhum pedido foi criado.
- Nenhum pagamento foi iniciado.
- Nenhum preço/estoque/produto foi alterado.
- Nenhum pixel/GA4/GTM/Klaviyo/Meta foi alterado.
