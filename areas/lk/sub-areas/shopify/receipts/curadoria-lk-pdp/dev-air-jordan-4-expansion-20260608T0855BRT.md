# Receipt — Curadoria LK PDP DEV Air Jordan 4 expansion (2026-06-08)

- values_printed: false
- gerado: 2026-06-08 08:55:35 BRT
- aprovação interpretada: Lucas respondeu `Aprov dev` após approval packet explícito para `Aprovo DEV Curadoria Air Jordan 4 expansion`; interpretado como aprovação atual para write somente no tema DEV/unpublished.
- target DEV: `lk-new-theme/dev` / theme `155065450718` / role `unpublished`
- Production verificado sem write: `lk-new-theme/production` / theme `155065417950` / role `main`
- main asset DEV: `snippets/lk-variante-top30-visited-v2.liquid`
- split asset DEV: `snippets/lk-variante-aj4-expansion-20260608.liquid`
- marker: `top30-air-jordan-4-expansion-20260608`

## Mudança executada

- Criado split snippet AJ4 no DEV.
- Inserida 1 render line no main Curadoria DEV:
  - `{%- render 'lk-variante-aj4-expansion-20260608', product: product -%}`
- Nenhum write em Production.
- Nenhum produto/preço/estoque/metafield/app/campanha alterado.

## Evidência

- Product `.js` preflight: 9/9 OK/available.
- Image HEAD preflight: 9/9 OK image.
- Main DEV SHA12: `97758147c9a9` → `cee33fcd8aa7`.
- Split DEV SHA12 readback: `6daeace1b9cc`.
- Render line count no main DEV: `1`.
- Static QA: `ok: true`; errors: `[]`.
- Simulação: 9 PDPs membros renderizam 5 alternativas, excluindo o produto atual.
- Production main unchanged: `true` (`d08dd7b15b83` → `d08dd7b15b83`).

## Preview público

- Amostra DEV com `preview_theme_id`: 3/3 HTTP 200, mas o Shopify removeu `preview_theme_id` do final URL.
- Marker AJ4 não apareceu no HTML público amostrado porque o request caiu no canonical/live, não no DEV.
- Classificação: preview público inconclusivo para DEV render; Admin Asset API readback + static QA são a source truth.

## Handles/labels

- `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco` — Nigel Brick
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho-1` — Toro Bravo
- `tenis-nike-sb-air-jordan-4-x-retro-sp-navy-branco` — SB Navy
- `tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho` — Valentine Sierra
- `tenis-travis-scott-air-jordan-4-retro-cactus-jack-nubuck-azul-6` — Travis Cactus Jack
- `tenis-air-jordan-4-retro-og-sp-undefeated-2025-verde` — Undefeated 2025
- `tenis-nike-air-jordan-4-retro-og-sp-brick-by-brick-camurca-firewood-orange` — Brick By Brick
- `tenis-air-jordan-4-retro-red-cement-branco` — Red Cement
- `air-jordan-4-seafoam` — Seafoam

## Rollback DEV

1. Restaurar `snippets/lk-variante-top30-visited-v2.liquid` removendo a render line AJ4. Backup local: `/opt/data/tmp/curadoria_aj4_dev_20260608/backup_dev_main.liquid`.
2. Remover/zerar `snippets/lk-variante-aj4-expansion-20260608.liquid`; ele não existia antes da execução.
3. Re-read Admin Asset API e confirmar ausência de `top30-air-jordan-4-expansion-20260608`/render line.

## Artefatos locais

- Script: `/opt/data/tmp/lk_curadoria_aj4_dev_apply.py`
- Preflight: `/opt/data/tmp/curadoria_aj4_dev_20260608/preflight.json`
- Resultado: `/opt/data/tmp/curadoria_aj4_dev_20260608/result.json`
- Readback main: `/opt/data/tmp/curadoria_aj4_dev_20260608/readback_dev_main.liquid`
- Readback split: `/opt/data/tmp/curadoria_aj4_dev_20260608/readback_dev_split.liquid`
