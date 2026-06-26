# Curadoria LK — Batch 6 Production merge

## Aprovação

Lucas respondeu `seguir` após o approval packet do Batch 6. Interpretado como aprovação atual para promover o Batch 6 validado do Dev para Production no escopo único do asset de curadoria.

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset

- `snippets/lk-variante-top30-visited.liquid`

## Grupos Batch 6 publicados

- Nike Air Force 1 Low regular — `top30-nike-air-force-1-low-regular`
- Adidas Handball Spezial regular — `top30-adidas-handball-spezial-regular`
- Adidas SL 72 regular — `top30-adidas-sl-72-regular`
- New Balance 1906L regular — `top30-new-balance-1906l-regular`
- New Balance 530 regular — `top30-new-balance-530-regular`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production mutated: false — já estava idêntico ao Dev source aprovado
- Readback Production bateu com Dev aprovado
- Markers Batch 6 presentes: 5/5
- SHA readback prefix: `f220da49cb1a`

## QA live Production

Arquivo: `qa-live-production-batch6.json`

Resultado final: pass

- 5/5 grupos renderizaram em URL live sem `preview_theme_id`
- 1 seção por grupo
- 5 cards por bloco
- Produto atual excluído
- Imagens presentes
- Zero `Liquid error`
- Zero `Liquid syntax error`

## GitHub / branch production

Arquivo: `github-repo-sync-report.json`

Resultado:

- `origin/production` já estava idêntico ao readback Production do Batch 6
- PR não criado porque não havia diff local
- HEAD / origin production: `c17603abe5aa`
- Diff contra `origin/production`: vazio
- Markers Batch 6 no repo: 5/5

## Rollback

Backup Production antes da promoção/readback:

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
