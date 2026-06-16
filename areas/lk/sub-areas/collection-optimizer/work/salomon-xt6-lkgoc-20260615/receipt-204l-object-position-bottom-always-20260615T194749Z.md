# Receipt — 204L object-position bottom always

Data UTC: 20260615T194749Z

## Pedido Lucas
"Mude por favor sempre para bottom" para a regra 204L de imagem/card grande.

## Execução
Aplicado em Production e DEV:
- `sections/lk-collection.liquid`
- Regra `.lk-204l-card--large img` alterada de `object-position:center 24%` para `object-position:center bottom`.
- Regra responsiva antiga `object-position:center 48%` também alterada para `object-position:center bottom`.
- Hotfix CSS público com `center 24%!important`/`center 48%!important` também ficou zerado após atualização.

## Validação pública
URL:
https://lksneakers.com.br/collections/salomon-xt-6?view=salomon-xt6-bottomfix

HTML público:
- `object-position:center 24%`: 0
- `object-position:center 48%`: 0
- `object-position:center bottom`: presente

Chromium computed style:
- card grande: `50% 100%`
- segunda imagem Hypebeast: `50% 100%`

## Rollback
Rollback salvo com prefixo:
- `rollback-204l-large-card-bottom-always-*`
- `rollback-bottom-always-*`
