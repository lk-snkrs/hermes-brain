# Curadoria LK — Batch 6 Production merge

## Aprovação

Lucas aprovou no Telegram: `Aprovo`

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset promovido

- `snippets/lk-variante-top30-visited.liquid`

## Grupos publicados

- Nike Air Force 1 Low regular — `top30-nike-air-force-1-low-regular`
- Adidas Handball Spezial regular — `top30-adidas-handball-spezial-regular`
- Adidas SL 72 regular — `top30-adidas-sl-72-regular`
- New Balance 1906L regular — `top30-new-balance-1906l-regular`
- New Balance 530 regular — `top30-new-balance-530-regular`

## Shopify API readback

Arquivo: `shopify-promotion-report.json`

Resultado:

- Production foi alterado: true
- Readback Production bateu com Dev aprovado
- Markers Batch 6 presentes: 5/5
- SHA readback prefix: `f220da49cb1a`

## QA live Production

Arquivos:

- `qa-live-production-batch6.json` — primeira tentativa com handles de amostra incorretos retornou 404
- `qa-live-production-batch6-final.json` — reteste com handles reais extraídos do readback Production

Resultado final:

- Nike Air Force 1 Low regular: pass
- Adidas Handball Spezial regular: pass
- Adidas SL 72 regular: pass
- New Balance 1906L regular: pass
- New Balance 530 regular: pass
- Resultado final: pass
- Sem Liquid error nos grupos validados
- 5 itens por bloco
- Produto atual excluído
- Imagens presentes

## GitHub / repo sync

Arquivo: `github-sync-report.json`

Resultado:

- `origin/production` já estava idêntico ao source/readback Production do Batch 6.
- PR não criado porque não havia diff a commitar.
- HEAD / origin production: `c17603abe5aa...`
- Diff contra `origin/production`: vazio
- Markers Batch 6 presentes no repo: 5/5

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
