# LKGOC — Local CLI Setup

Atualizado UTC: 2026-06-03T19:41:23.824032+00:00

## Instalado/validado
- Node: `/usr/local/bin/node` — `v22.12.0`
- npm: `/usr/local/bin/npm` — `10.9.0`
- Doppler CLI: `/usr/bin/doppler` — `v3.76.0`
- Shopify CLI: `/usr/local/bin/shopify` — `4.1.0`
- Chromium: `/usr/bin/chromium`
- Playwright local: `/opt/data/profiles/lk-collection-optimizer/tools/lkgoc-qa` — `1.60.0`

## Histórico/rollback
Antes do update:
- Node: `/usr/bin/node` — `v20.19.2`
- npm: `/usr/bin/npm` — `9.2.0`
- Shopify CLI: `3.84.0`

Node 22 foi instalado via `n`, ficando em `/usr/local/bin/node`, que tem precedência no PATH.
O Node antigo do sistema permanece em `/usr/bin/node` como referência/rollback operacional.

## Motivo
`@shopify/cli@4.1.0` exige Node `>=22.12.0`. O host estava em Node `v20.19.2`.

## Playwright
Instalado localmente no profile/projeto LKGOC, não global.

- Diretório: `/opt/data/profiles/lk-collection-optimizer/tools/lkgoc-qa`
- Browser download pulado.
- Usar Chromium do sistema: `/usr/bin/chromium`

## Receipts
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/local-cli-install-20260603T192726Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/local-cli-shopify-downgrade-20260603T192844Z`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/local-node-update-20260603T193008Z`

## Guardrail
Essas ferramentas podem apoiar leitura, preview, QA e DEV-first. Writes externos/Production continuam exigindo approval explícito do Lucas.

## Shopify CLI auth
- Login validado para `lk@lksneakers.com.br` em 2026-06-03.
- Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/local-cli-login-20260603T194224Z`
