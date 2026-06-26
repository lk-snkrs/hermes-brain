# LK GMC API/data sources investigation — resumo executivo — 2026-05-21

## Escopo

Investigação read-only das fontes/API conectadas ao Google Merchant Center da LK. Nenhum write, fetchNow, feed upload, Shopify write, campanha/envio ou impressão de segredo foi feito.

## Veredito

Há sim **duas fontes com nome `Content API`**, mas elas **não são equivalentes**:

- `10636492695` — `Content API`, `input=API`, fonte primária online BR/pt usada para Shopping Ads, Free Listings e Display Ads. Esta é a fonte que os scripts Merchant API/ProductInputs aprovados vinham usando.
- `10636384718` — `Content API`, `input=API`, também BR/pt, porém marcada pela API como `legacyLocal=true` e só com destino `FREE_LOCAL_LISTINGS` enabled. Pelo estado atual, isso parece ser a fonte legada/local, não a fonte principal de Shopping Ads.

Também existe:

- `10525577766` — `lksneakers.com.br`, `input=AUTOFEED`, fonte automática/crawl, com `FREE_LISTINGS` enabled e `SHOPPING_ADS` disabled.

A antiga fonte suplementar:

- `10646853947` — `LK Sneakers - Color Supplemental Feed` apareceu em relatório anterior, mas na verificação direta atual retorna `404 NOT_FOUND_DATA_SOURCE`. Portanto não deve ser tratada como fonte ativa hoje sem nova confirmação visual no painel.

## O que está errado/confuso

1. O painel mostra duas fontes chamadas `Content API`, com mesmo idioma/país/label (`pt`, `BR`, `BR`). Isso é confuso e perigoso para operação.
2. Uma delas (`10636384718`) é `legacyLocal=true`, então provavelmente não deve ser usada para correções online/Shopping Ads.
3. A fonte correta para ProductInputs online segue sendo `10636492695`, mas a existência da `AUTOFEED` e das melhorias automáticas do Google explica parte dos conflitos de preço.
4. As melhorias automáticas da conta estão ativas: `allowPriceUpdates=true`, `allowAvailabilityUpdates=true`, `allowConditionUpdates=true`. Isso bate com os avisos `price_updated` e `strikethrough_price_updated` vistos no GMC.

## Evidência técnica

- Merchant API dataSources v1 list: 3 fontes atuais retornadas.
- Content API legacy datafeeds: 0 datafeeds retornados.
- Content API products carregados: 19.652.
- Content API productstatuses carregados parcialmente: 14.236 antes de interrupção/limite de paginação.
- Top issues observados: `price_updated`, `strikethrough_price_updated`, `missing_item_attribute_for_product_type`.
- Merchant API v1beta está morto desde 2026-02-28; usar apenas v1.

## Recomendação

Não deletar/desativar nada agora pelo Telegram. Próximo passo seguro:

1. Abrir o painel Merchant Center → Data sources.
2. Confirmar visualmente os três IDs/nome/destinos:
   - `10636492695` deve ser a fonte online principal.
   - `10636384718` deve ser documentada/renomeada mentalmente como local/legacy, se o painel permitir distinguir.
   - `10525577766` é autofeed/crawl; avaliar se deve continuar só Free Listings.
3. Se for mexer em fonte, fazer pacote separado com screenshot, export/backup possível e rollback. Não recomendo apagar/desativar sem essa prova.
4. Para preço: antes de novo patch em massa, diagnosticar se o conflito vem de landing page/tema + Automatic Item Updates, não só do campo da API.

## Artefatos

- Relatório completo JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-api-data-sources-investigation-2026-05-21.json`
- Relatório completo MD: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-api-data-sources-investigation-2026-05-21.md`
- Resumo executivo: `/opt/data/hermes_bruno_ingest/hermes-brain/reports/lk-gmc-api-data-sources-investigation-2026-05-21-summary.md`

## Não executado

- Merchant/Content API writes
- Data source update/delete
- fetchNow/feed upload
- Shopify/Tiny writes
- Campanha/envio/contato
- Impressão de segredos
