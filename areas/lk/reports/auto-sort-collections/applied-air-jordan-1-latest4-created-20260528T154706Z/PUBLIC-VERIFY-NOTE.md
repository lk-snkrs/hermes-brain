# Nota de verificação pública — Air Jordan 1 latest-created top 4

Data: 2026-05-28T15:50Z

## Resultado aplicado

A ordenação foi aplicada no Shopify Admin conforme o preview aprovado:

1. Tênis Jordan 11 Retro Low University Blue 2026 Azul — `9191695679710`
2. Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal — `9191686471902`
3. Tênis Nike Air Jordan 1 Low OG SP x Travis Scott Shy Pink Rosa — `9191446610142`
4. Tênis Nike Air Jordan 1 Low SE Repaired Denim Swoosh Azul — `9175662330078`

Admin readback:

- Admin top4 = alvo: `true`
- Admin top8 = alvo: `true`
- Admin full order = alvo: `true`

## Divergência pública encontrada

O produto `9191446610142` / `tenis-nike-air-jordan-1-low-og-sp-x-travis-scott-shy-pink-rosa` está em `status: draft`, `published_at: null` no Shopify Admin.

Consequência: ele aparece na ordenação do Admin, mas não aparece no `/collections/air-jordan-1/products.json` público nem no PDP público (`/products/...js` retorna 404). Portanto, a vitrine pública pula esse item e mostra como top visível:

1. Jordan 11 Retro Low University Blue 2026
2. Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
3. Nike Air Jordan 1 Low SE Repaired Denim Swoosh
4. Nike Air Jordan 1 Low OG Obsidian UNC

## Próxima decisão necessária

Para a regra ficar correta visualmente no storefront, há duas opções:

1. Publicar/ativar o produto Shy Pink — exige aprovação separada de produto/publicação.
2. Ajustar a regra operacional para `Top 4 = últimos 4 produtos criados e publicados/ativos na Online Store`, independente de vendas/visitas/estoque. Com essa regra, o quarto visível atualmente seria `9168759587038` — Tênis Nike Air Jordan 1 High Virgil Abloh Archive x Alaska Branco.

Nenhuma dessas duas ações foi executada nesta nota.
