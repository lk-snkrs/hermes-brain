# Addendum — GMC landing_page_error + invalid_color — 2026-06-25

Gerado em: `2026-06-25T11:38:11.425672+00:00`  
Modo: `read-only / preview`; writes `0`; values_printed=false.

## Achado material novo vs 18/06

- `landing_page_error`: `161` produtos / `483` instâncias; Δ vs 18/06: `+152` produtos no relatório principal.
- Bounded public `.js` check: `80` URLs checadas; status: `{'ok': 58, 'http_404': 2, 'http_429': 20}`.
- `invalid_color`: `146` produtos / `292` instâncias; issue novo no snapshot atual.

## Packet prioritário recomendado — landing_page_error

- CSV: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-landing-page-error-packet-2026-06-25.csv`.
- Ação proposta: triagem de 20–50 offers em micro-lote, separando `Shopify 404/despublicado`, `link do feed antigo`, `cache/reprocessamento`, `produto que deve ser suprimido` e `falso positivo`.
- Impacto: reprovação em Shopping/DisplayAds/SurfacesAcrossGoogle; mais bloqueante que os 17 casos de missing attribute.
- Risco de overwrite: médio/alto se a correção for feita no ProductInput enquanto Simprosys/API continuar enviando link antigo.
- Rollback/validação: snapshot do Product resource/source antes, correção no menor surface dono, readback do Product link e productstatuses após reprocessamento; sem delete/suppress/fetchNow sem aprovação.

## Packet secundário — invalid_color

- CSV: `areas/lk/sub-areas/growth/reports/gmc/lk-gmc-invalid-color-packet-2026-06-25.csv`.
- Ação proposta: agrupar por produto/handle e corrigir color apenas quando houver cor canônica inequívoca; se o erro vier de source local/Simprosys, corrigir no source dono.
- Impacto: qualidade de matching e elegibilidade Shopping; menor urgência que landing errors.

## Amostra landing_page_error

| Offer | Título | public .js | Link |
|---|---|---|---|
| `JI2714-5` | Tênis adidas Gazelle Indoor Dark Brown Glow Pink Court Green Marrom | `ok` | https://lksneakers.com.br/products/tenis-adidas-gazelle-indoor-dark-brown-glow-pink-court-green-marrom |
| `w4535r-1` | Blusa Alo Yoga Sherpa Edge Bomber Ivory Bege | `ok` | https://lksneakers.com.br/products/blusa-alo-yoga-sherpa-edge-bomber-ivory-bege |
| `43774078386356-24` | Meia Alo Yoga Unisex Half-Crew Throwback | `ok` | https://lksneakers.com.br/products/meia-alo-yoga-unisex-half-crew-throwback |
| `DD1873102-4` | Tênis Nike Dunk Low Next Nature Black White Preto | `ok` | https://lksneakers.com.br/products/nike-dunk-low-next-nature-black-white |
| `43774078390070` | Tênis Nike Air Jordan 1 Retro Low Fragment Design x Travis Scott Couro Branco Preto Azul | `ok` | https://lksneakers.com.br/products/tenis-air-jordan-1-retro-low-fragment-design-x-travis-scott-couro-branco-preto-azul |
| `BQ6817600-2` | Tênis Nike SB Dunk Low Pro Chicago Vermelho | `ok` | https://lksneakers.com.br/products/nike-sb-dunk-low-pro-chicago |
| `5706324928133224313` | Tênis New Balance 204L x Atmos Cow Girl Brown Marrom - Tamanho 39 | `http_404` | https://lksneakers.com.br/products/tenis-new-balance-204l-x-atmos-cow-girl-brown-marrom |
| `FV5029006-2` | Tênis Nike Air Jordan 4 "Bred Reimagined" Preto | `ok` | https://lksneakers.com.br/products/tenis-air-jordan-4-bred-reimagined-preto |
