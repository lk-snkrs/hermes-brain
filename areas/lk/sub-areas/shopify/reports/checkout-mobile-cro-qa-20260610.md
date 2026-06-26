# Checkout mobile CRO QA — LK Sneakers — 2026-06-10

## Escopo

QA read-only do checkout mobile após ativação de trust grid / Google rating / birthday block.

- Produto de teste: `Moletom Aimé Leon Dore Overlay Logo Crewneck Sweatshirt Verde`
- Variant ID usado no cart permalink: `48300570116318`
- URL testada: checkout Shopify gerado por cart permalink, sem pedido e sem pagamento.
- Viewport: mobile 390x844, user-agent iPhone Safari.
- Não foram feitos writes em Shopify/Klaviyo/tema/campanhas; apenas navegação de checkout/carrinho de teste.

## Evidência runtime

Artefatos locais:

- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-report.json`
- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-top.png`
- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-scroll-1.png`
- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-scroll-2.png`
- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-scroll-3.png`
- `/opt/data/tmp/lk-checkout-qa/output/checkout-mobile-after-clicks.png`

Texto observado no checkout:

- `Data de nascimento (opcional)`
- `Use para receber benefícios de aniversário da LK.`
- `GOOGLE` / `4,9 • 411 avaliações`
- `AUTENTICIDADE Garantida`
- `PARCELE EM até 10x`
- `FRETE GRÁTIS acima de R$ 499`
- `TROCA GRÁTIS em 7 dias`
- `LOJA FÍSICA Jardins, SP`
- FAQ: autenticidade, entrega, troca/devolução

## Achados CRO

### P0 — bloco de confiança aparece tarde demais

Ordem DOM/texto observada:

1. Contato
2. Entrega
3. Frete pendente de endereço
4. Pagamento
5. Cartão / parcelas
6. Pix
7. Data de nascimento
8. Resumo do pedido
9. `PAGAR AGORA`
10. Google rating + trust grid + FAQ

Interpretação: a prova social aparece depois do botão de pagamento, ou seja, o cliente só vê os principais elementos de confiança no fim da página. Para conversão, o bloco deveria aparecer antes da decisão de pagamento, idealmente antes de `Pagamento` ou entre `Entrega` e `Pagamento`.

### P0 — parcelamento 11x/12x tem copy contraditória

Observado:

- `11 x R$ 226,99 (com 2% de desconto) - Total: R$ 2.496,91`
- `12 x R$ 204,58 (com 4% de desconto) - Total: R$ 2.454,93`

Interpretação: o total é maior que `R$ 2.399,99`, mas a copy diz `com desconto`. Isso pode quebrar confiança no pagamento. Deve ser corrigido para linguagem de juros/acréscimo ou removido.

### P1 — CTA genérico `Enviar` aparece em pontos sensíveis

Botões visíveis detectados incluem `Enviar` além de `PAGAR AGORA`. Interpretação: pode ser texto interno/submit do Shopify/app, mas em checkout mobile um CTA genérico perto de pagamento/finalização é menos claro que `Continuar`, `Calcular frete`, `Confirmar` etc. Precisa de verificação visual no editor/app.

### P1 — nascimento está tecnicamente OK, mas posicionado perto do pagamento

O campo aparece como `lk_birth_date`, placeholder `Data de nascimento (opcional)`, com calendário. Copy está boa. Risco: se visualmente ficar entre pagamento e resumo, pode parecer etapa extra no momento de pagar. Melhor se aparecer abaixo do contato/opt-in ou como benefício discreto, não dentro da área de pagamento.

### P1 — frete depende de endereço, mas confiança de frete aparece só no bloco inferior

O checkout informa `Insira o endereço de entrega para ver as formas de frete disponíveis`, mas o reforço `Frete grátis acima de R$499` só aparece no trust grid inferior. Para carrinhos acima de R$499, considerar microcopy perto de `Forma de frete`.

## Recomendações

1. Mover o trust/social proof block para antes de `Pagamento`.
2. Corrigir copy do parcelamento 11x/12x (`desconto` vs total maior).
3. Reposicionar birthday abaixo de contato/marketing opt-in, se o editor permitir.
4. Adicionar microcopy curto em `Forma de frete` para carrinho elegível: `Frete grátis acima de R$499 — calculado após o CEP.`
5. Fazer uma revisão visual manual no Checkout Editor para confirmar os CTAs `Enviar` e ajustar labels se forem app-controlled.

## Rollback / não-ações

- Nenhum write executado.
- Nenhum pagamento iniciado.
- Nenhum pedido criado.
- Nenhum cliente real usado.
- Qualquer ajuste de checkout app/editor/gateway exige aprovação explícita.
