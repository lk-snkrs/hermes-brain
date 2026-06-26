# Curadoria LK — Batch 4 aplicado no Dev

## Aprovação

Lucas aprovou no Telegram: `Pode aplicar` após o pacote recomendado para Batch 4.

## Escopo aprovado

Aplicar no Dev theme os grupos:

- Onitsuka Mexico 66 regular
- New Balance 9060
- Air Jordan 1 Mid regular
- Adidas Campus regular

Separar collabs/cápsulas quando fizer sentido.

## Tema

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`

## Assets alterados

- `snippets/lk-variante-top30-visited.liquid`

## Backups / rollback

Backups salvos neste diretório:

- `snippets__lk-variante-top30-visited.liquid.before`
- `sections__lk-pdp.liquid.before`
- `assets__lk-variante.css.before`
- `snippets__lk-variante-top30-visited.liquid.before-campus-semantic-fix`
- `snippets__lk-variante-top30-visited.liquid.before-campus-adult-clean-fix`

Rollback: re-upar `snippets__lk-variante-top30-visited.liquid.before` no Dev theme.

## Grupos / markers

- Onitsuka Mexico 66 regular — `top30-onitsuka-mexico66-regular`
- New Balance 9060 — `top30-new-balance-9060`
- Air Jordan 1 Mid regular — `top30-air-jordan-1-mid-regular`
- Adidas Campus regular — `top30-adidas-campus-regular`

## Correções semânticas durante QA

- Removido `pre-venda-tenis-korn-x-adidas-campus-2-0-carbon-cinza` do Campus regular porque é collab/cápsula.
- Substituído o bloco Campus por 6 Campus 00s adultos/regular, excluindo Korn, Bad Bunny e Kids.

## QA autoritativo por Asset API / readback

Arquivo: `qa_asset_synthetic_batch4_final.json`

Resultado:

- `all_pass`: true
- Markers presentes: 4/4
- Bad image schemes: 0
- Render sintético: 8 amostras com 5 itens e produto atual excluído
- CDN checks: 24/24 imagens OK
- Checagem semântica: pass para Onitsuka regular, NB 9060, AJ1 Mid regular e Campus regular

## QA preview público

Arquivo: `qa_public_preview_batch4.json`

Resultado: preview público não preservou `preview_theme_id=155065450718`; Shopify redirecionou/serviu live sem os markers. Isso é limitação já observada nos batches anteriores. Validação Dev autoritativa foi feita por readback de asset + simulação + CDN.

## Não-ações

Não foi alterado:

- Production
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
