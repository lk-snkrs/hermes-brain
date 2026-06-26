# Revalidação Home Production — Opção C SWYM híbrido — 20260618T171940Z

- values_printed: false
- escopo: read-only; nenhum write Shopify/Git/tema executado.

## Home pública

Amostras: 6

- round 1: asset_ref=true, swym_ext_count=0
- round 2: asset_ref=false, swym_ext_count=4
- round 3: asset_ref=true, swym_ext_count=0
- round 4: asset_ref=true, swym_ext_count=0
- round 5: asset_ref=true, swym_ext_count=0
- round 6: asset_ref=true, swym_ext_count=0

Resultado:

- home_new_count: 5/6
- home_stable_last3: true
- topbar_wishlist presente em 6/6
- status HTTP: 200 em 6/6

Interpretação: Home convergiu nas últimas 3 amostras para o HTML novo, com `lk-swym-hybrid-v1.js` presente e sem `swym-ext-shopify` no HTML inicial.

## Topbar wishlist

Selector testado: `.lk-header__icon.lk-header__icon--wishlist`

Antes do clique:

- found: true
- href: `https://lksneakers.com.br/pages/my-wishlist`
- hybrid: true
- hasHybrid: true
- hasSwat: false
- errors: []

Depois do clique:

- url: `https://lksneakers.com.br/pages/my-wishlist`
- title: `Wishlist | LK Sneakers`
- hybrid: true
- hasHybrid: true
- hasSwat: true
- swymScriptCount: 1
- queue: 0
- errors: []

Resultado: topbar OK.

## Conclusão

A Opção C está ativa na Home nas últimas amostras e o botão do topbar navega corretamente para Wishlist, onde SWYM inicializa sem erro.
