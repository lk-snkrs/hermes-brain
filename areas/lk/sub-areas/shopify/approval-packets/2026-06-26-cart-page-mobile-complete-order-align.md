# Approval packet — /cart mobile “Complete seu pedido” alinhado + botão Adicionar preto

Data: 2026-06-26
Owner: LK Shopify
Superfície: Shopify theme / `sections/lk-cart.liquid`
Escopo: `/cart` mobile, bloco `Complete seu pedido` / `.cart-upsell`

## Pedido do Lucas

> “No móbile, o complete seu pedido, deve estar tudo alinhado… E o adicionar deve ter s fonte preta”

Screenshot recebido mostra cards em grid 2 colunas com alturas/textos variando, fazendo preço/botão `ADICIONAR` ficarem desalinhados entre cards. O texto do botão também aparece azul/claro; deve ficar preto.

## Evidência read-only

Fonte atual lida do GitHub `production` em:

`/opt/data/profiles/lk-shopify/workdirs/cart-page-mobile-complete-order-align-20260626/prod_sections__lk-cart.liquid`

Arquivo alvo preparado localmente:

`/opt/data/profiles/lk-shopify/workdirs/cart-page-mobile-complete-order-align-20260626/target_sections__lk-cart.liquid`

Seletores encontrados:

- `.cart-upsell__grid`
- `.cart-upsell__card`
- `.cart-upsell__card-info`
- `.cart-upsell__card-name`
- `.cart-upsell__card-price`
- `.cart-upsell__card-btn`
- `@media (max-width: 749px)`

## Interpretação

O desalinhamento vem de títulos com quantidade de linhas diferente dentro do grid 2 colunas no mobile. Como os cards não estão em flex column, preço e botão sobem/descem conforme o texto de cada card.

A cor do `ADICIONAR` não está explicitamente fixada em preto no botão base, então pode herdar/ficar azul conforme o browser/theme.

## Patch local proposto

Arquivo único: `sections/lk-cart.liquid`

Mudança CSS-only:

1. Transformar cards do upsell em `display:flex; flex-direction:column`.
2. Fazer `.cart-upsell__card-info` ocupar o restante do card com `flex: 1`.
3. Usar `align-items: stretch` no grid.
4. Empurrar preço/botão para uma linha visualmente consistente com `margin: auto 0 10px` no preço.
5. No mobile, estabilizar altura de marca/nome/preço:
   - brand `min-height: 10px`
   - nome `min-height: 55px`
   - preço `min-height: 24px`
6. Reduzir levemente o topo do bloco no mobile:
   - `.cart-upsell { padding-top: 28px; }`
7. Fixar fonte do botão:
   - `.cart-upsell__card-btn { color: var(--black); }`

## Fora de escopo

- Não muda ranking/cross-sell X→Y.
- Não muda produtos, estoque, preço, checkout, GA4, Tiny, GMC, Klaviyo ou campanhas.
- Não toca cart drawer snippet.
- Não altera lógica JS de add-to-cart.

## QA planejado

Depois de aprovação:

1. Upload em DEV/unpublished theme apenas do `sections/lk-cart.liquid`.
2. Readback do asset DEV por SHA/substrings.
3. QA visual mobile `/cart` com viewport similar ao print:
   - grid 2 colunas;
   - títulos/preços/botões alinhados por linha;
   - `ADICIONAR` com texto preto;
   - botão ainda clicável;
   - desktop sem regressão visual grave.
4. Se DEV OK e Lucas tiver aprovado Production no mesmo escopo, abrir PR GitHub para `production`, merge, readback Shopify Production e QA público.

## Risco

Baixo. CSS-only, escopo em `.cart-upsell` do `/cart`. Risco principal: nomes com 4+ linhas ainda quebrarem a altura fixa no mobile. Mitigação: `price/button` com flex mantém alinhamento relativo e QA visual valida.

## Rollback

Plano B apenas se precisar — não é recomendação de reverter.

Restaurar `sections/lk-cart.liquid` a partir do snapshot:

`/opt/data/profiles/lk-shopify/workdirs/cart-page-mobile-complete-order-align-20260626/prod_sections__lk-cart.liquid`

## Aprovação necessária

Para executar DEV + Production no escopo acima, frase sugerida:

**Aprovo DEV e merge Production mobile Complete seu pedido alinhado + Adicionar preto**

Reminder OS loop needed: yes
Reminder OS owner: LK Shopify
Reminder OS next action: aguardar aprovação explícita; aplicar em DEV, QA, e só então merge Production se aprovado no mesmo escopo.
Reminder OS review trigger: resposta do Lucas aprovando DEV/Production ou pedindo ajuste visual diferente.
Reminder OS evidence: este approval packet + workdir local com snapshot/target.
