# Receipt — Production AJ4 unavailable cleanup — Curadoria LK PDP

Data UTC: 2026-06-07T18:00:56.480108+00:00

## Escopo aprovado

Lucas respondeu `Aprovo` após a frase de aprovação Production para aplicar a limpeza AJ4 validada no DEV. Interpretação aplicada: **merge cirúrgico em Production/main**, sem outros writes.

## Tema / asset

- Production: `lk-new-theme/production` / `155065417950` / role `main`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- DEV referência read-only: `lk-new-theme/dev` / `155065450718` / role `unpublished`

## Mudança

- Marker: `top30-air-jordan-4-regular`
- Removido: `tenis-air-jordan-4-retro-military-blue-branco`
- Contagem do grupo: 16 → 15
- Label removida: `Military Blue`

## Evidência

- Production before SHA12: `c64dafba4777`
- Production target/readback SHA12: `811dbe5bdec7` / `811dbe5bdec7`
- Readback bate com target: `True`
- DEV permaneceu inalterado nesta etapa: `True`
- Static QA: target absent `True`; group counts `{'handles': 15, 'labels': 15, 'images': 15}`; arrays equal `True` / top arrays equal `True`; bad URL/placeholder counts `{'https:https://': 0, 'https://https://': 0, 'TenisMoldeLK': 0}`
- Observação: `substring_occurrences_total=1` por causa de handle distinto com sufixo `-copia`, não pelo handle removido.

## QA público imediato

Classificação: source/readback aprovado; HTML público pode sofrer edge/cache logo após write.

```json
[
  {
    "handle": "tenis-air-jordan-4-retro-metallic-gold-branco",
    "status": 200,
    "html_len": 622341,
    "has_marker": true,
    "has_curadoria": true,
    "removed_exact_card_href": false,
    "liquid_errors": 0,
    "anti_bot": false
  },
  {
    "handle": "tenis-nike-air-jordan-4-retro-black-cat-preto",
    "status": 200,
    "html_len": 613777,
    "has_marker": true,
    "has_curadoria": true,
    "removed_exact_card_href": false,
    "liquid_errors": 0,
    "anti_bot": false
  },
  {
    "handle": "air-jordan-4-frozen-moments",
    "status": 200,
    "html_len": 620847,
    "has_marker": true,
    "has_curadoria": true,
    "removed_exact_card_href": false,
    "liquid_errors": 0,
    "anti_bot": false
  },
  {
    "handle": "tenis-air-jordan-4-retro-military-blue-branco",
    "status": 200,
    "html_len": 617770,
    "has_marker": false,
    "has_curadoria": true,
    "removed_exact_card_href": true,
    "liquid_errors": 0,
    "anti_bot": false
  }
]
```

## Rollback

Restaurar backup Production:

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp/prod-aj4-unavailable-cleanup-20260607T180043Z/production-before.liquid`
- Theme: `155065417950`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`

## Não-ações

- Sem write em DEV nesta etapa de Production
- Sem produto, preço, estoque, Tiny, GMC, Klaviyo, Ads ou checkout
- Sem publish de tema
