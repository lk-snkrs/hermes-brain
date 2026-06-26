# Curadoria LK — Batch 9 Production merge

## Aprovação

Lucas aprovou via botão inline: `Aprovado subir Batch 9 para Production`.

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados

- Adidas Samba Jane regular — `top30-adidas-samba-jane-regular`
- Yeezy 350 regular — `top30-yeezy-350-regular`
- Alo Accolade line — `top30-alo-accolade-line`
- Alo Airbrush line — `top30-alo-airbrush-line`
- Alo Serenity Coverup line — `top30-alo-serenity-coverup-line`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 9 presentes: 5/5
- SHA readback prefix: `0b530160154a`

## QA live Production

Arquivo: `qa-live-production-batch9.json`

Resultado: pass

- 5/5 grupos renderizaram em URL live sem `preview_theme_id`
- 1 seção por grupo
- 5 cards por bloco
- Produto atual excluído
- Imagens presentes
- Zero `Liquid error`
- Zero `Liquid syntax error`

## GitHub / repo sync

Arquivo: `github-sync-report.json`

Resultado:

- `origin/production` já estava idêntico ao readback Production do Batch 9.
- PR não criado porque não havia diff após sincronizar o readback sobre `origin/production`.
- HEAD / origin production: `d59916421656`
- Diff contra `origin/production`: vazio
- Markers Batch 9 presentes no repo: 5/5

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
