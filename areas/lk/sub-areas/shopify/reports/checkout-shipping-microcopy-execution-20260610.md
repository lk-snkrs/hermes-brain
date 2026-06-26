# Checkout shipping microcopy — execução — 2026-06-10

## Escopo aprovado

Lucas pediu: `Adicionar microcopy curta de frete grátis na área de frete. -> FAZER`.

Escopo executado: adicionar copy curta de frete grátis ao checkout app controlado `lk-gift-bag-checkout`, sem alterar produto, preço, estoque, gateway, campanha, Klaviyo ou tema Shopify.

## Mudança

Arquivo principal alterado:

- `/opt/data/projects/lk-gift-bag-checkout-app/extensions/social-proof/src/Checkout.jsx`

Copy adicionada ao bloco ativo de confiança/social proof:

> Frete grátis acima de R$499 — calculado após o CEP.

Também foi criada uma tentativa de extensão dedicada:

- `/opt/data/projects/lk-gift-bag-checkout-app/extensions/shipping-microcopy/`
- target: `purchase.checkout.shipping-option-list.render-before`

QA mostrou que esse target dedicado foi deployado mas não renderizou automaticamente no checkout ativo. Por isso a copy foi aplicada no bloco ativo que já renderiza no checkout.

## Build/deploy

Build local passou:

- `npm run build -- --no-color`
- saída: `lk-gift-bag-checkout built!`

Deploy executado com aprovação escopada:

- comando: `npm run deploy -- --no-color --allow-updates --message "Add free shipping microcopy to active checkout trust block"`
- resultado: `New version released to users.`
- versão: `lk-gift-bag-checkout-12`

## QA real mobile

QA mobile automatizado:

- viewport: 390x844 iPhone-like
- produto/carrinho de teste: variant `48300570116318`
- nenhum pedido/pagamento foi criado
- relatório: `/opt/data/tmp/lk-checkout-qa/output-shipping-microcopy/shipping-microcopy-report.json`
- screenshots: `/opt/data/tmp/lk-checkout-qa/output-shipping-microcopy/`

Readback textual do checkout:

- `microcopyFound: true`
- texto encontrado: `Frete grátis acima de R$499 — calculado após o CEP.`

Observação de QA: no checkout automatizado, o bloco ainda aparece depois de `PAGAR AGORA` na ordem textual. Lucas informou que já moveu o Google/trust grid antes de pagamento; pode haver diferença de profile/editor/cache ou do checkout gerado no teste. A copy está no bloco ativo; a posição final depende da posição do app block no Checkout Editor.

## Risco

Baixo: alteração de copy/visual em extensão de checkout existente. Não muda lógica de pagamento, frete, preço, estoque ou pedido.

## Rollback

Rollback simples: remover a linha de microcopy de `extensions/social-proof/src/Checkout.jsx` e redeployar o app com nova versão. Se quiser remover também a extensão dedicada `shipping-microcopy`, isso é delete de extension/app component e deve ser aprovado separadamente com `--allow-deletes`.

## Não-ações

- Não fiz pedido.
- Não iniciei pagamento.
- Não mexi em frete real/tabela de frete.
- Não alterei preço, estoque, produto, tema ou campanhas.
