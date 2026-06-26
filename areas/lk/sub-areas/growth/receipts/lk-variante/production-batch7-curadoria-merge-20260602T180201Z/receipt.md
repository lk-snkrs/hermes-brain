# Curadoria LK — Batch 7 Production merge

## Aprovação

Lucas aprovou via botão inline: `Aprovar subir Batch 7 para Production`.

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados

- Adidas Samba OG regular — `top30-adidas-samba-og-regular`
- Nike Dunk Low regular — `top30-nike-dunk-low-regular`
- Adidas Tokyo regular — `top30-adidas-tokyo-regular`
- Puma Speedcat regular — `top30-puma-speedcat-regular`
- Air Jordan 4 regular — `top30-nike-air-jordan-4-regular`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 7 presentes: 5/5
- SHA readback prefix: `91c5bed42a99`

## QA live Production

Arquivo: `qa-live-production-batch7.json`

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

- `origin/production` já estava idêntico ao readback Production do Batch 7.
- PR não criado porque não havia diff após sincronizar o readback sobre `origin/production`.
- HEAD / origin production: `7e87d1b6b54c`
- Diff contra `origin/production`: vazio
- Markers Batch 7 presentes no repo: 5/5

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
