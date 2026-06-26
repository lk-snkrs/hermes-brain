# FINAL SUCCESS — Nike Mind LIA link_template 5

Data: `2026-06-08T09:28:02.865373+00:00`

## Resultado

- Escopo: 5 itens Local/LIA Nike Mind no Google Merchant.
- Aprovação do turno: Lucas respondeu “Seguir” ao gargalo remanescente de `link_template`.
- GMC alterado: `true`.
- Shopify alterado: `false`.
- Método que funcionou: Merchant API `productInputs.patch` no data source original dos itens.
- Método que não bastou: Content API `products.insert` aceitou a chamada, mas ignorou `linkTemplate` no readback.
- Campos aplicados: `productAttributes.linkTemplate`, `productAttributes.mobileLinkTemplate`, `productAttributes.adsRedirect`.
- Formato aplicado: URL do PDP/variant atual + `&store_code={store_code}`.
- Confirmados por patch response: `5/5`.
- Confirmados por processed product readback: `5/5`.
- Issue `mhlsf_full_missing_valid_link_template` restante no readback imediato: `0`.
- Status imediato: `LOCAL_INVENTORY_ADS` aprovado em BR e `FREE_LOCAL_LISTINGS` aprovado em BR nos 5 itens.

## Readback final

- `LIA_HQ4307-600-3` → linkTemplate `https://lksneakers.com.br/products/slide-nike-mind-001-solar-red-vermelho?variant=47839692488926&country=BR&store_code={store_code}` | issues: `0` | LOCAL_INVENTORY_ADS: approved=BR disapproved=; FREE_LOCAL_LISTINGS: approved=BR disapproved=
- `LIA_HQ4307-600-4` → linkTemplate `https://lksneakers.com.br/products/slide-nike-mind-001-solar-red-vermelho?variant=47839692521694&country=BR&store_code={store_code}` | issues: `0` | LOCAL_INVENTORY_ADS: approved=BR disapproved=; FREE_LOCAL_LISTINGS: approved=BR disapproved=
- `LIA_HQ4307-003-7` → linkTemplate `https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza?variant=47839129534686&country=BR&store_code={store_code}` | issues: `0` | LOCAL_INVENTORY_ADS: approved=BR disapproved=; FREE_LOCAL_LISTINGS: approved=BR disapproved=
- `LIA_HQ4307-002-5` → linkTemplate `https://lksneakers.com.br/products/slide-nike-mind-001-light-bone-bege?variant=47839128682718&country=BR&store_code={store_code}` | issues: `0` | LOCAL_INVENTORY_ADS: approved=BR disapproved=; FREE_LOCAL_LISTINGS: approved=BR disapproved=
- `LIA_HQ4307-003-5` → linkTemplate `https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza?variant=47839129469150&country=BR&store_code={store_code}` | issues: `0` | LOCAL_INVENTORY_ADS: approved=BR disapproved=; FREE_LOCAL_LISTINGS: approved=BR disapproved=

## Rollback

- Snapshot antes: `merchantapi_before_products.json` e `before_snapshot.json`.
- Para rollback, aplicar `productInputs.patch` no mesmo `dataSource` removendo/limpando `linkTemplate`, `mobileLinkTemplate` e `adsRedirect`, usando o snapshot anterior como referência.
- Não executar rollback automático agora, porque o readback final aprovou os 5 itens.

## Evidências

- `merchantapi_patch_results.json`
- `merchantapi_after_readback.json`
- `merchantapi_before_products.json`
- `insert_results.json` / `after_readback.json` documentam a tentativa via Content API e por que foi descartada.

## Revisão de impacto

- Rechecar Merchant Diagnostics/status em 24–72h e novamente em ~7 dias para confirmar que o feed/Simprosys não sobrescreveu os campos e que LIA segue aprovado.
