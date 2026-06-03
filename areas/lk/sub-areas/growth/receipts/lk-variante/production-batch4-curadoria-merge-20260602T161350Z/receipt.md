# Curadoria LK — Batch 4 Production merge

## Aprovação

Lucas aprovou no Telegram: `agora faca o merge no production..`

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados

- Onitsuka Mexico 66 regular — `top30-onitsuka-mexico66-regular`
- New Balance 9060 — `top30-new-balance-9060`
- Air Jordan 1 Mid regular — `top30-air-jordan-1-mid-regular`
- Adidas Campus regular — `top30-adidas-campus-regular`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 4 presentes: 4/4
- SHA readback prefix: `019f22e835fa`

## QA live Production

Arquivos:

- `qa-live-production.json`
- `qa-aj1-mid-investigation.json`
- `qa-live-production-final.json`

Resultado final:

- Onitsuka Mexico 66: pass
- New Balance 9060: pass
- Adidas Campus: pass
- Air Jordan 1 Mid: primeira amostra oscilou por edge/cache; retry em 6 handles passou
- Resultado final após retry/cache: pass
- Sem Liquid error nos grupos validados
- 5 itens por bloco
- Produto atual excluído

## GitHub / repo sync

Arquivo: `github-merge-idempotent-report.json`

Resultado:

- `origin/production` já estava idêntico ao source/readback Production do Batch 4.
- PR não criado porque GitHub retornou `422: No commits between production and hermes/curadoria-lk-batch4-production-20260602`.
- HEAD / origin production: `abae4f70ce2c9b0514a94321e87d21339d44acb5`
- Diff contra `origin/production`: vazio
- Markers Batch 4 presentes no repo: 4/4

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
