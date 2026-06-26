# Checkout — Frete grátis no topo — QA final

Data UTC: 2026-06-10T19:27:32Z

## Status

Confirmado no checkout real mobile após ajuste manual no Checkout Editor/profile.

## Evidência

- Report JSON: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/shipping-microcopy-report.json`
- Screenshot: `/opt/data/tmp/lk-checkout-qa/output-shipping-top-20260610/shipping-microcopy-6.png`
- URL QA: `https://lksneakers.com.br/checkouts/cn/hWNDBlcEoC7Kwwvd2LUhRTsY/pt-br?_r=AQABUsXvpS4OcSSzh3slvJ-D1IJD_sRAasEdqKqDhDlL&cart_link_id=2WM5pr4t`
- `microcopyFound`: `True`
- `oldLowerMicrocopyFound`: `False`

## Posições no texto do checkout

```json
{
  "lkCheckout": 92,
  "contato": 163,
  "entrega": 258,
  "freeShipping": 104,
  "cep": 158,
  "pagarAgora": 5865,
  "google": 5877
}
```

## Trecho inicial observado

```text
Pular para o conteúdo
Navegar até a loja virtual
Resumo do pedido
Preço total

R$ 2.399,99

LK Checkout
Frete grátis acima de R$499
Calculado após informar o CEP.
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
Nome
Sobrenome
CEP
Endereço
Apartamento, bloco etc. (opcional)
Cidade
Estado
Acre
Alagoas
```

## Interpretação

A microcopy `Frete grátis acima de R$499` e `Calculado após informar o CEP.` aparece no topo do checkout, logo após `LK Checkout` e antes de `Contato`/`Entrega`. A copy antiga embaixo não reapareceu.

## Rollback

Remover o app block `Frete grátis LK` / `lk-checkout-shipping-microcopy` no Checkout Editor e salvar o profile publicado.
