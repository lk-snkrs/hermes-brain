# Approval Packet — GMC LIA link_template repatch 181 — 2026-06-09

## Classificação

- Área: GMC / Product data quality / Local inventory LIA.
- Modo atual: read-only; nenhum write executado neste packet.
- Issue alvo: `mhlsf_full_missing_valid_link_template`.

## Evidência read-only

- Scan Merchant API `products_v1.products.list`: 23 páginas.
- Itens com issue atual: **181**.
- Data sources: {'accounts/5297679409/dataSources/10636384718': 181}.
- Itens sem link base: 0.
- Artefatos:
  - Scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-repatch-181-20260609/scan_missing_link_template.json`
  - CSV alvo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-repatch-181-20260609/link_template_targets_181.csv`
  - Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-repatch-181-20260609/summary.json`

## Correção proposta

Aplicar via Merchant API `productInputs.patch` somente nos 181 offerIds listados no CSV:

- `productAttributes.linkTemplate`
- `productAttributes.mobileLinkTemplate`
- `productAttributes.adsRedirect`

Valor proposto por item:

- `{link atual}?store_code={store_code}` quando o link não tiver querystring;
- `{link atual}&store_code={store_code}` quando já tiver querystring.

## Guardrails

- Não alterar Shopify.
- Não alterar preço, disponibilidade/estoque, título, GTIN, imagem, category/productType ou campanhas.
- Snapshot pré-write por item.
- Resultado incremental em JSONL.
- Readback imediato por processed product, sabendo que o status GMC pode lagar.
- Stop condition: falha sistêmica de auth/schema, ou >10% de erro não transitório.

## Impacto esperado

- Reduzir/remover a regressão atual de link template em LIA/local.
- Risco baixo porque corrige apenas template de URL local e usa link já existente como base.
- Risco operacional: regressão pode voltar se o feed/data source sobrescrever novamente; precisa revisão de causa/fonte depois.

## Rollback

- Reaplicar valores pré-snapshot para os três campos, por offerId, se necessário.
- Como fallback, remover o template aplicado nos mesmos offerIds via patch escopado, somente com nova aprovação.

## Aprovação necessária

Lucas, para executar, aprove exatamente este escopo:

> Aprovo LK Growth executar o packet `gmc-link-template-repatch-181-20260609`: patch somente dos 181 offerIds do CSV, apenas nos campos `linkTemplate`, `mobileLinkTemplate` e `adsRedirect`, com snapshot, readback e sem alterações em Shopify/preço/estoque/título/GTIN/imagem/campanhas.
