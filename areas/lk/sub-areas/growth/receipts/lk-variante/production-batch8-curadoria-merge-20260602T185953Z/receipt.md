# Curadoria LK — Batch 8 Production merge

## Aprovação

Lucas aprovou no Telegram: `Aprovado subir Batch 8 para Production`.

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados

- New Balance 204L regular — `top30-new-balance-204l-regular`
- Onitsuka Mexico 66 Sabot regular — `top30-onitsuka-mexico-66-sabot-regular`
- Adidas Taekwondo Mei Ballet regular — `top30-adidas-taekwondo-regular`
- Nike Cortez regular — `top30-nike-cortez-regular`
- Alo Airlift line — `top30-alo-airlift-line`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 8 presentes: 5/5
- SHA readback prefix: `d6b35f73b048`

## QA live Production

Arquivo: `qa-live-production-batch8.json`

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

- `origin/production` já estava idêntico ao readback Production do Batch 8.
- PR não criado porque não havia diff após sincronizar o readback sobre `origin/production`.
- HEAD / origin production: `2bdbaa3a112b`
- Diff contra `origin/production`: vazio
- Markers Batch 8 presentes no repo: 5/5

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
