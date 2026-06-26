# Receipt — MK Provador Virtual script `?v=1`

- Data: 2026-06-15
- Perfil: LK Shopify
- Solicitação: acrescentar `?v=1` ao `src` do script MetaKosmos/mKFashion, preservando atributos `data-mk-*`.

## Escopo executado

- Shopify theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Asset: `layout/theme.liquid`
- Alteração exata:
  - de: `https://cdn.jsdelivr.net/npm/mk-sdk-git@latest/dist/mk-sdk.js`
  - para: `https://cdn.jsdelivr.net/npm/mk-sdk-git@latest/dist/mk-sdk.js?v=1`
- Atributos preservados:
  - `data-mk-project="698c806c1d3129430f15ddde"`
  - `data-mk-product="mk-fashion"`
  - `async`

## Evidência de readback Admin

- Antes: `new_url_count=0`, `old_url_exact=true`, SHA-12 inicial `b0c12d61f4e1`
- Depois: `new_url_count=1`, `old_url_remaining=0`, `project_attr_count=1`, `product_attr_count=1`, SHA-12 final `f27a89a10f53`
- `values_printed=false`

## Backup / rollback

- Backup local do asset antes do write:
  `/opt/data/profiles/lk-shopify/backups/theme-production/mk-provador-virtual-v1/20260615T105422Z__theme-155065417950__layout-theme.liquid`
- Rollback: re-subir esse backup para `layout/theme.liquid` do theme `155065417950`, se Lucas pedir.

## QA público

- PDP `https://www.lksneakers.com.br/products/new-balance-530-white-natural-indigo-1?mkcache=202606151054b`: HTTP 200, `new_url_count=1`, `old_url_exact_count=0`, `has_project=true`.
- Home cache-busted ainda retornou HTML antigo no primeiro monitor (`new_url_count=0`, `old_url_exact_count=1`), provável edge/cache de rota; Admin readback e PDP público já mostram o script novo.

## Não ações

- Não alterei projeto MK, produto MK, preço, estoque, checkout, app config, Klaviyo, GMC, campanhas ou conteúdo de produto.
- Não imprimi tokens/secrets.
