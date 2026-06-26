# Receipt — Curadoria LK PDP baseline after PR #23

Data: 2026-06-05 / 2026-06-06 UTC

## Contexto

Após merge do PR #23 (`dev` GitHub rebaselined para `production`), Lucas pediu para seguir com LK Thumbnail PDP / Curadoria LK PDP.

## Verificações read-only executadas

### Shopify themes

- Production/Main: `155065417950` — `lk-new-theme/production` — role `main`
- DEV: `155065450718` — `lk-new-theme/dev` — role `unpublished`

### DEV vs Production — assets críticos

Todos os assets críticos comparados estão com SHA igual entre DEV e Production:

- `sections/lk-pdp.liquid`
  - SHA: `3698f5ec5745`
- `snippets/lk-variante-top30-visited.liquid`
  - SHA: `089cc730d730`
- `snippets/lk-variante-top30-visited-v2.liquid`
  - SHA: `493429e95ac5`
- `assets/lk-variante.css`
  - SHA: `703fdabbfa7c`
- `layout/theme.liquid`
  - SHA: `5d9db2d75ae3`

### Render target ativo

Em DEV e Production, `sections/lk-pdp.liquid` renderiza:

- `lk-variante-top30-visited-v2`

Isso confirma que a continuação da Curadoria LK PDP deve mirar o snippet `snippets/lk-variante-top30-visited-v2.liquid`.

### Estado Curadoria

- DEV e Production contêm `top30-yeezy-slide-regular` no snippet ativo `-v2`.
- DEV e Production contêm o grupo Air Jordan 1 Mid com `tenis-air-jordan-1-mid-glitter-swoosh-azul`.
- CSS contém hotfix de labels regulares:
  - `.lk-variante__label { font-weight: 400; }`
  - `.lk-variante__item.is-current .lk-variante__label { font-weight: 400; }`

## QA público read-only

URLs testadas com cachebuster:

- `tenis-air-jordan-1-mid-glitter-swoosh-azul`
- `yeezy-slide-glow-green`
- `yeezy-slide-azure`
- `new-balance-530-white-natural-indigo-1`

Resultado comum:

- HTTP 200
- Curadoria hint presente
- `data-lk-variante` count: 1
- card-like count: 5
- labels curtos renderizados

Notas:

- Requests com `preview_theme_id=155065450718` redirecionaram para canonical/live sem manter o preview parameter, então HTML público de preview é inconclusivo. Readback Admin API é a fonte para DEV.
- Screenshot mobile read-only gerado para Jordan Mid Glitter:
  - `/opt/data/tmp/lk_curadoria_screens/jordan_mid_glitter_mobile.png`

## Status

Baseline Shopify DEV está alinhado com Production para os assets críticos da Curadoria LK PDP.

Nenhum write Shopify foi executado nesta etapa.

## Próximo passo recomendado

Continuar com um pacote DEV ou correção Curadoria LK PDP mirando `snippets/lk-variante-top30-visited-v2.liquid`, com aprovação explícita antes de qualquer upload ao tema DEV.
