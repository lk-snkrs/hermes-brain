# Sambae collection — production publish/validation

UTC: 2026-06-03T12:26:33.823759+00:00

## Approval
Lucas pediu no Telegram: “Publique a colecao também no Production”.

## Coleção
- Título: `Adidas Sambae`
- Handle: `adidas-sambae`
- URL: `https://lksneakers.com.br/collections/adidas-sambae`
- Tipo: `smart`
- ID: `430079344862`

## Resultado
- Status: **publicada e visível em production**.
- Ação Shopify: `no write needed; collection already published`
- Observação: a coleção já estava publicada (`published_scope: global`), então não foi necessário alterar visibilidade.

## QA público refinado
- Status HTTP: `200`
- Title tag: `Adidas Sambae - LK Sneakers`
- H1 Adidas Sambae: `True`
- Canonical da coleção: `True`
- CollectionPage schema: `1`
- Produtos renderizados no HTML: `26` markers
- Frase real de página não encontrada: `0`
- Screenshot mobile: `sambae-collection-production-mobile.png`

## Produtos
- Produtos no Admin da coleção: `12`

## Rollback
- Snapshot antes salvo em `collection.before.json`.
- Como não houve mudança de visibilidade, rollback externo não é necessário.
