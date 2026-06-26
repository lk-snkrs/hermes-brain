# Curadoria LK — Batch 6 Production merge

## Aprovação

Lucas aprovou no Telegram com `seguir`, após o approval packet do Batch 6 para Production.

## Interpretação operacional

Promoção Dev→Production do asset aprovado no Dev, preservando a linhagem do tema.

## Production theme

- Theme: `lk-new-theme/production`
- Theme ID: `155065417950`
- Role: `main`

## Asset

- `snippets/lk-variante-top30-visited.liquid`

## Resultado Shopify

Arquivo: `shopify-promotion-report.json`

- Production mutation needed: false
- Motivo: Production já continha o mesmo source do Dev aprovado / readback idempotente
- Readback Production: match
- SHA readback prefix: `f220da49cb1a`

## Grupos Batch 6 em Production

1. Nike Air Force 1 Low regular
   - `top30-nike-air-force-1-low-regular`
2. Adidas Handball Spezial regular
   - `top30-adidas-handball-spezial-regular`
3. Adidas SL 72 regular
   - `top30-adidas-sl-72-regular`
4. New Balance 1906L regular
   - `top30-new-balance-1906l-regular`
5. New Balance 530 regular
   - `top30-new-balance-530-regular`

Markers Production: 5/5, uma ocorrência cada.

## QA live Production

Arquivo: `qa-live-production-batch6.json`

Resultado: pass

Validação por grupo com handles extraídos do readback Production:

- HTTP 200
- marker presente
- 1 seção LK Variante
- 5 cards
- imagens presentes
- produto atual excluído
- zero `Liquid error`
- zero `Liquid syntax error`

## GitHub / repo production

Arquivo: `github-repo-sync-report.json`

Resultado: idempotente sem diff local.

- Repo: `lk-snkrs/lk-new-theme`
- `HEAD`: `c17603abe5aade222881ab5df062992e092de21e`
- `origin/production`: `c17603abe5aade222881ab5df062992e092de21e`
- Diff contra `origin/production`: vazio
- Markers Batch 6 no repo: 5/5

## Rollback

Backup Production antes da verificação/upload:

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
