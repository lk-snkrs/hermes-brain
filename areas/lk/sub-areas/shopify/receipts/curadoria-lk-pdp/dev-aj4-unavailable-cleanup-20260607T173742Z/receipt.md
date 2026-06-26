# Receipt — DEV AJ4 unavailable cleanup — Curadoria LK PDP

Data UTC: 2026-06-07T17:37:48.681430+00:00

## Escopo aprovado

Lucas respondeu `Aprovo` logo após o approval packet pedir aprovação DEV para remover/substituir o AJ4 indisponível. Interpretação aplicada: **DEV-only**, remover o handle indisponível, sem Production.

## Tema / asset

- DEV: `lk-new-theme/dev` / `155065450718` / role `unpublished`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- Production read-only: `lk-new-theme/production` / `155065417950` / role `main`

## Mudança

- Marker: `top30-air-jordan-4-regular`
- Removido: `tenis-air-jordan-4-retro-military-blue-branco`
- Contagem do grupo: 16 → 15
- Label removida: `Military Blue`

## Evidência

- DEV before SHA12: `e5df3582f2e9`
- DEV target/readback SHA12: `aba2ed49b088` / `aba2ed49b088`
- Readback bate com target: `True`
- Production unchanged: `True`
- Static QA: target absent `True`; group counts `{'handles': 15, 'labels': 15, 'images': 15}`; arrays equal `True` / top arrays equal `True`; bad URL/placeholder counts `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- Observação: `substring_occurrences_total=1` por causa de handle distinto com sufixo `-copia`, não pelo handle removido.

## QA público/preview

- Preview theme id: `155065450718`
- Classificação: parcial/inconclusivo para preview público porque a URL final removeu `preview_theme_id`, mas o HTML amostrado retornou `200`, sem anti-bot, sem Liquid error e consistente com o source DEV.
- Amostras com marker AJ4 e Curadoria presentes, sem href exato para o handle removido como card: `tenis-air-jordan-4-retro-metallic-gold-branco`, `tenis-nike-air-jordan-4-retro-black-cat-preto`, `tenis-air-jordan-4-retro-og-nike-white-cement-couro`.
- PDP do handle removido também respondeu `200`, mas a evidência de href nele não é usada como prova de card porque pode ser self/current product URL.

## Rollback

Restaurar backup DEV:

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/dev-aj4-unavailable-cleanup-20260607T173742Z/dev-before.liquid`
- Theme: `155065450718`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`

## Não-ações

- Sem write em Production
- Sem publish de tema
- Sem produto, preço, estoque, Tiny, GMC, Klaviyo, Ads ou checkout
