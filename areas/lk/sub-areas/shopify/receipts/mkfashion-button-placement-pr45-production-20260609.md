# Receipt — mKFashion PDP button placement fix

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`
PR: https://github.com/lk-snkrs/lk-new-theme/pull/45
Base: `production`
Merge commit: `46693d5 fix: align mKFashion PDP button placement (#45)`

## Pedido

Lucas identificou no print que o botão/ícone do Provador Virtual estava errado e pediu para colocar um botão acima da Trust Bar.

## Execução

Foi criado e mergeado PR escopado para `production`:

- move/configura o auto-mount do SDK mKFashion para ancorar em `.pi-actions .shopify-payment-button`;
- posição: `afterend`, ou seja, depois do `Compre já` e antes da Trust Bar;
- aplica estilo CTA full-width LK;
- remove via shadow root aberto o ícone padrão de 24px que estava errado;
- mantém SDK zero-touch já promovida.

## Arquivos alterados

- `layout/theme.liquid`
- `projetos/lk-new-theme/layout/theme.liquid`
- `projetos/lk-new-theme/dev-theme/layout/theme.liquid`

## Verificações

### Git/origin production

- `origin/production` atualizado para `46693d5`.
- Static verification passou:
  - SDK nova presente exatamente 1 vez em cada layout esperado;
  - `window.__MK.anchor` presente;
  - selector `.pi-actions .shopify-payment-button` configurado para mobile/tablet/desktop;
  - tuner `mk-tryon-button-host` presente;
  - selector de remoção do ícone padrão presente;
  - sem `unpkg.com/mkfashion-sdk`;
  - sem `mkfashion-tryon`.

### Shopify Admin readback

Theme main:

- id: `155065417950`
- name: `lk-new-theme/production`
- role: `main`

Readback de `layout/theme.liquid`:

- `new_sdk_count`: 1
- `anchor_config_count`: 1
- `payment_anchor_count`: 3
- `host_tuner_count`: 1
- `icon_removal_selector`: true
- old refs:
  - `unpkg`: false
  - `mkfashion_tryon`: false

### Storefront headless DOM QA

PDP testada:

- `https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1`

Resultado:

- `hostExists`: true
- `buttonExists`: true
- `iconExists`: false
- `buttonText`: `Provar Virtualmente`
- `hostPreviousClass`: `shopify-payment-button`
- `hostTop`: 928.109375
- `hostBottom`: 978.109375
- `trustTop`: 1002.109375
- `paymentBottom`: 920.109375
- `buttonWidth`: 389
- `buttonMaxWidth`: `100%`
- `buttonBorderRadius`: `0px`
- `newScriptCount`: 1
- `oldUnpkg`: false
- `orderOk`: true
- `afterPaymentOk`: true

Final:

```text
PASS headless_dom_verification
```

## Rollback

Rollback seguro via PR revertendo:

- `46693d5`

Evitar hotfix direto em Shopify Production salvo emergência aprovada.

## Guardrails

- Não houve Shopify Asset API write manual nesta correção.
- Não houve alteração de produto, estoque, preço, checkout, apps, campanhas ou Klaviyo.
- Secrets usados via Doppler sem impressão de valores.
