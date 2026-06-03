# Curadoria LK — Batch 5 Production merge

## Aprovação

Lucas aprovou no Telegram:

`Aprovo… você vai fazer o Merge na branch Production correto?`

Interpretação confirmada: promover Dev → Production e sincronizar/validar a branch `production` do repo, não aplicar patch solto.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados — Batch 5

- Gazelle Indoor active/new handles — `top30-adidas-gazelle-active-regular`
- Air Jordan 1 High regular — `top30-air-jordan-1-high-regular`
- Nike Shox TL regular — `top30-nike-shox-tl-regular`
- ASICS Gel-1130 regular — `top30-asics-gel-1130-regular`
- Yeezy Foam Runner regular — `top30-yeezy-foam-runner-regular`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 5 presentes: 5/5
- SHA readback prefix: `b7eda597c660`

## QA live Production

Arquivos:

- `qa-live-production.json`
- `qa-live-production-retry-gazelle-shox.json`
- `qa-live-production-final-shox-cache.json`

Resultado final: pass

- Gazelle: primeiro request oscilou por edge/cache; retry passou em 4 handles.
- Air Jordan 1 High: pass
- Nike Shox TL: primeiro request no handle `black-cave-stone` serviu cache antigo; retries passaram em outros handles e depois no próprio handle.
- ASICS Gel-1130: pass
- Yeezy Foam Runner: pass

Validações live:

- 1 seção por grupo
- 5 cards renderizados
- produto atual excluído
- imagens presentes
- zero `Liquid error` / `Liquid syntax error`

## GitHub / branch production

Arquivos:

- `github-production-merge-report.json`
- `github-production-merge-idempotent-report.json`

Resultado:

- Branch `production` já estava idêntica ao readback Production do Batch 5 no momento da sincronização.
- Não houve diff a commitar/PR porque `origin/production` == HEAD.
- HEAD / `origin/production`: `a319861be5b3fc76899123c7e68723d9a650eea2`
- Diff contra `origin/production`: vazio
- Markers Batch 5 presentes no repo: 5/5

Interpretação: merge/sync idempotente na branch `production` — branch já continha o source final.

## Rollback

Backup Production antes do upload:

- `production__snippets__lk-variante-top30-visited.liquid.before`

Rollback: re-upar esse arquivo para `snippets/lk-variante-top30-visited.liquid` no Production theme.

## Não-ações

Não foi alterado:

- Produtos
- Preço
- Estoque
- Checkout
- Apps
- GMC/feed
- Klaviyo
- Meta
- Tiny
- Campanhas/envios
