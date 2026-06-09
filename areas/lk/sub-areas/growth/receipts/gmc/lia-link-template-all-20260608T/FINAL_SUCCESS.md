# FINAL SUCCESS — LIA link_template all remaining

Data: `2026-06-08T11:33:53.302131+00:00`

## Resultado

- Escopo aprovado: Lucas respondeu “Seguir com os outros…” após o piloto de 5 itens Nike Mind.
- GMC alterado: `true`.
- Shopify alterado: `false`.
- Problema atacado: `mhlsf_full_missing_valid_link_template` em produtos Local/LIA.
- Itens com issue no scan inicial: `10987`.
- Patch responses OK registradas: `10987` unique offerIds.
- Falhas finais de patch: `0`.
- Scan final Merchant API: `0` itens restantes com `mhlsf_full_missing_valid_link_template`.
- Páginas Merchant API varridas no scan final: `23`.

## Método

- Surface: Merchant API `products_v1`.
- Mutation: `accounts.productInputs.patch` no `dataSource` original de cada item.
- Campos aplicados:
  - `productAttributes.linkTemplate`
  - `productAttributes.mobileLinkTemplate`
  - `productAttributes.adsRedirect`
- Valor aplicado: `link` atual do produto + `store_code={store_code}`.
- Preservação: não alterei preço, estoque, título, descrição, Shopify, tema ou campanhas.

## Verificação

- Antes: `10987` itens com `mhlsf_full_missing_valid_link_template`.
- Depois: `0` itens com `mhlsf_full_missing_valid_link_template`.
- Um item residual (`LIA_43774078390130`) precisou de re-patch/readback individual por lag/timeout; readback individual confirmou `linkTemplate` e aprovação em `LOCAL_INVENTORY_ADS`/`FREE_LOCAL_LISTINGS`.

## Artefatos

- `before_scan_missing_link_template.json`
- `patch_results.jsonl`
- `patch_summary_parallel.json`
- `after_scan_missing_link_template.json`
- `after_scan_2_missing_link_template.json`
- `final_scan_missing_link_template.json`
- scripts de execução no mesmo diretório

## Rollback

- Snapshot base: `before_scan_missing_link_template.json`.
- Rollback seguro: aplicar `productInputs.patch` no mesmo `dataSource` removendo/limpando `linkTemplate`, `mobileLinkTemplate` e `adsRedirect` para os offerIds afetados.
- Não executei rollback porque o scan final confirmou zero itens restantes com o erro.

## Revisão de impacto

- Rechecar Merchant Diagnostics em 24–72h e novamente em ~7 dias.
- Monitorar se Simprosys/feed reprocessa e sobrescreve esses campos.
