# Approval Packet — GMC link_template regressão ampla Local/LIA 11.410 — 2026-06-09

## Contexto

Após o patch aprovado dos 181 itens, o post-scan Merchant API mostrou uma regressão ampla no data source local/LIA:

- Issue: `mhlsf_full_missing_valid_link_template`
- Itens atuais: **11410**
- Data source: `accounts/5297679409/dataSources/10636384718`
- Itens sem link base: `0`

Interpretação: não parece consequência do patch de 181; o issue apareceu/foi reavaliado em massa no data source local. O write anterior ficou restrito aos 181 aprovados.

## Correção proposta

Aplicar via Merchant API `productInputs.patch` aos 11410 offerIds do CSV:

- `productAttributes.linkTemplate`
- `productAttributes.mobileLinkTemplate`
- `productAttributes.adsRedirect`

Valor por item:

- `{link atual}?store_code={store_code}` quando link não tiver querystring;
- `{link atual}&store_code={store_code}` quando já tiver querystring.

## Risco

- Esforço técnico baixo, mas volume alto.
- Risco principal: se o data source local continuar sobrescrevendo/omitindo template, o problema pode voltar.
- Recomendado executar em ondas, não tudo cego: onda 1 de 1.000, readback, depois escala se OK.

## Guardrails

- Não alterar Shopify.
- Não alterar preço, estoque/disponibilidade, título, GTIN, imagem, category/productType ou campanhas.
- Snapshot pré-write por item.
- JSONL incremental.
- Readback por amostra + full target quando viável.
- Stop condition: >5% falha não transitória, auth/schema error, ou comportamento de readback inesperado.

## Artefatos

- Source scan: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/link-template-repatch-181-20260609T/post_scan/scan_missing_link_template.json`
- CSV targets: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-regression-local-lia-11410-20260609/link_template_regression_targets_11410.csv`
- Summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-link-template-regression-local-lia-11410-20260609/summary.json`

## Aprovação sugerida

> Aprovo LK Growth executar a onda 1 do packet `gmc-link-template-regression-local-lia-11410-20260609`: patch de até 1.000 offerIds do CSV, apenas nos campos `linkTemplate`, `mobileLinkTemplate` e `adsRedirect`, com snapshot, readback e sem alterações em Shopify/preço/estoque/título/GTIN/imagem/campanhas. Se a onda 1 fechar sem falha sistêmica e com readback adequado, preparar próximo approval antes de escalar.
