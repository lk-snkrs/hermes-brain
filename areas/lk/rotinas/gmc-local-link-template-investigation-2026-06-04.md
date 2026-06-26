# LK GMC — Packet E local link_template investigation — 2026-06-04

Gerado em: `2026-06-04T11:44:28.392533+00:00`
Modo: `read-only / preview`; nenhum write, upload, fetchNow ou reprocessamento executado.

## Resultado executivo

- Problema investigado: `mhlsf_full_missing_valid_link_template` em ofertas locais.
- Afetados nesta leitura: `10441` produtos/ofertas.
- Canais afetados: `{'local': 10441}`.
- Source dos produtos afetados: `{'api': 10441}`.
- Prefixo offerId: `{'LIA_': 10441}`.
- `link_template`/`mobile_link_template` no product resource: `{'missing': 10441}`.
- Sinal de `store_code` no template atual: `{'no_store_code_signal': 10441}`.

## Evidência do issue

- `10441`× — A valid [link_template] value with store code is required for the offer to serve

- Destinos do issue: `{'Shopping': 10441}`.
- Atributo citado pelo Merchant: `{'link template': 10441}`.

## Fonte / data source provável

- LIA settings: sem recursos retornados ou sem permissão de leitura.
- Datafeeds Content API: nenhum feed primário/local evidente retornado.
- Merchant API DataSources listados:
  - `accounts/5297679409/dataSources/10525577766` — lksneakers.com.br; input `AUTOFEED`; flags `primaryProductDataSource`.
  - `accounts/5297679409/dataSources/10636384718` — Simprosys Local Feed (Merchant API); input `API`; flags `primaryProductDataSource`.
  - `accounts/5297679409/dataSources/10636492695` — Simprosys Feed (Merchant API); input `API`; flags `primaryProductDataSource`.

Interpretação: os afetados são `local:*`, majoritariamente `LIA_`, `source=api`, compatível com integração Shopify POS/local inventory em vez de feed CSV primário. A correção deve ocorrer na superfície que gera/atualiza ofertas locais, não em copy/PDP nem em feed online.

## Amostras

| product_id | source | link_template atual | link | público | detalhe |
|---|---|---|---|---|---|
| `local:pt:BR:LIA_001010841` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139041502&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_001010842` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139074270&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_001010843` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139107038&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_001010844` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139139806&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_001010845` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139172574&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_001010846` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ls75-branco?variant=47543139205342&country=BR | `ok` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_002010759` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143792862&country=BR | `n/a` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_002010760` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143825630&country=BR | `n/a` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_002010761` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143858398&country=BR | `n/a` | A valid [link_template] value with store code is required for the offer to serve |
| `local:pt:BR:LIA_002010762` | `api` | `MISSING` | https://lksneakers.com.br/products/tenis-autry-medalist-low-ll15-branco?variant=47543143891166&country=BR | `n/a` | A valid [link_template] value with store code is required for the offer to serve |

CSV preview dos primeiros 200 afetados: `reports/lk-gmc-local-link-template-preview-2026-06-04.csv`.

## Preview de correção — sem executar

- Hipótese técnica: incluir um `link_template` válido que aceite/store-code explicitamente, preservando o link de PDP atual e adicionando contrato de loja.
- Padrão candidato para revisão técnica: `{current_product_link}{separator}store_code={store_code}`.
- Exemplo materializado por linha no CSV: `https://lksneakers.com.br/products/<handle>?store_code={store_code}` quando não há querystring, ou `...&store_code={store_code}` quando o link já tem `?variant=...&country=BR` (ou equivalente exigido pela integração/Google).
- Antes de escrever, confirmar o nome exato do placeholder/param aceito por Merchant/LIA e se a URL final por loja resolve corretamente.
- Superfície candidata: integração Shopify POS/local inventory / recurso local `source=api` que cria `local:*`; evitar patch no feed online e evitar resolver via PDP copy.

## Approval packet proposto

- **Pedido de aprovação futuro (não executar agora):** micro-piloto em 5–20 ofertas locais aprovadas nominalmente, alterando apenas `link_template` no surface dono, após snapshot.
- **Escopo bloqueado sem nova aprovação:** bulk nos 10.436, fetchNow/reprocess, upload/feed, Shopify/POS config, ProductInput/Product write, campanhas.
- **Rollback:** snapshot do product resource/config/data source antes do piloto; reverter o template anterior no mesmo surface; manter lista de offerIds afetados.
- **Validação:** readback do product resource + productstatuses; aguardar processamento; sucesso = queda/remoção de `mhlsf_full_missing_valid_link_template` e Shopping passar de disapproved para pending/approved nas ofertas piloto; revisar D+7 antes de escala.
- **Risco:** alteração sistêmica no local inventory pode afetar milhares de ofertas e elegibilidade de Shopping/LocalSurfaces; se placeholder/URL estiver errado, pode criar reprovação em massa de landing/local.

## O que não foi feito

- Nenhum Content API/Merchant API write.
- Nenhum `fetchNow`, upload, reprocess ou alteração de data source/feed.
- Nenhum Shopify/Tiny/POS write, preço, estoque, campanha ou contato externo.

