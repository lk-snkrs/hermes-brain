# Final Receipt — GEO llms Onitsuka + Nike Mind — 2026-06-09

Criado em: 2026-06-09 17:35 UTC

## Aprovação / pedido

Lucas: “Vamos fazer?” sobre:

1. Alinhar Onitsuka broad collection no `llms.txt`/`llms-full.txt`.
2. Nike Mind 001 com bloco citável.

## O que foi feito

### 1) Onitsuka no `llms.txt` e `llms-full.txt`

Publicado em production theme:

- `templates/llms.txt.liquid`
- `templates/llms-full.txt.liquid`

Adicionado/garantido:

- `/collections/onitsuka-tiger-todos-os-modelos`
- linha de coleção “Onitsuka Tiger original — todos os modelos”
- bloco `AI Priority GEO source pages` com descrição citável do hub Onitsuka.

### 2) Nike Mind 001

Já estava publicado na collection production antes deste passo:

- URL: `/collections/nike-mind-001`
- bloco citável visível
- FAQ visível
- JSON-LD `FAQPage`

Neste passo, também garanti presença da collection Nike Mind nos arquivos AI:

- `/collections/nike-mind-001`
- bloco `AI Priority GEO source pages` com descrição citável.

## Readback público

`/llms.txt`:

- status: `200`
- Onitsuka broad: `True`
- Nike Mind collection: `True`
- AI Priority block: `True`

`/llms-full.txt`:

- status: `200`
- Onitsuka broad: `True`
- Nike Mind collection: `True`
- AI Priority block: `True`

`/agents.md`:

- Onitsuka broad: `True`
- Nike Mind collection: `True`

`/collections/nike-mind-001`:

- bloco Nike Mind production: `True`
- classe `lk-growth-nike-mind-geo`: `True`

## Observação técnica

O readback via Shopify Admin para `templates/llms.txt.liquid` retornou hash antigo imediatamente após PUT, comportamento já visto em receipt anterior de `llms.txt`; o readback público com cache buster confirmou a publicação correta. `llms-full.txt` confirmou tanto via Admin quanto público.

## Fora do escopo / não alterado

- Shopify product data: 0
- Preço: 0
- Estoque/disponibilidade: 0
- GMC/feed: 0
- Ads/Klaviyo/customer-facing outbound: 0
- Collection title/meta/metafields: 0
- Theme layout/PDP/checkout: 0 neste passo

## Rollback

Backups salvos no diretório:

- `templates__llms.txt.liquid.before.liquid`
- `templates__llms-full.txt.liquid.before.liquid`

Para rollback: restaurar os dois assets acima no production theme `155065417950`.
