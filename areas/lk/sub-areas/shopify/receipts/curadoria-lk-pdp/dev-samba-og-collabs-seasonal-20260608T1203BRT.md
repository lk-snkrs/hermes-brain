# Receipt — Curadoria LK PDP DEV Adidas Samba OG collabs/seasonal II (2026-06-08)

- values_printed: false
- aprovação: Lucas respondeu `aprovo` após approval packet `Curadoria LK PDP DEV Adidas Samba OG collabs/seasonal II`.
- interpretação segura: aprovação somente para DEV/unpublished theme do packet imediato; **não aprova Production/merge**.
- write executado: Shopify DEV/unpublished theme only.
- Production: read-only/unchanged.
- Sem produto/preço/estoque/collection/app/checkout/ads/email/GMC/Tiny/Klaviyo write.

## Tema

- DEV theme: `155065450718` / `lk-new-theme/dev` / role `unpublished`.
- Production theme: `155065417950` / `lk-new-theme/production` / role `main`.

## Mudança DEV

- Split snippet criado/atualizado:
  - `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`
- Active main DEV atualizado com 1 render line:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `{%- render 'lk-variante-samba-og-collabs-seasonal-20260608', product: product -%}`
- Marker:
  - `top30-adidas-samba-og-collabs-seasonal-20260608`
- Escopo semântico:
  - Adidas Samba OG collabs/seasonal continuação.
  - Separado de regular, Wales Bonner, Samba Jane, Sambae e do batch `top30-adidas-samba-og-specials-20260608` já publicado.

## Handles / labels

- `tenis-adidas-samba-og-x-lionel-messi-triunfo-estelar-pack-branco` — Messi Triunfo
- `tenis-adidas-samba-og-x-dingyun-zhang-white-vapour-branco` — Dingyun White Vapour
- `tenis-adidas-samba-og-x-sporty-rich-usa-branco` — Sporty & Rich USA
- `tenis-adidas-samba-og-dia-de-muertos-pack-black-preto` — Día de Muertos Black
- `tenis-adidas-samba-og-dia-de-muertos-pack-off-white-branco` — Día de Muertos Off White
- `tenis-adidas-samba-og-x-naked-consortium-off-white-crystal-white-branco` — Naked Crystal White
- `tenis-adidas-samba-og-linen-green-metallic-verde` — Linen Green Metallic
- `tenis-adidas-samba-og-semi-blue-burst-azul` — Semi Blue Burst
- `tenis-adidas-samba-og-off-white-cyber-metallic-branco` — Cyber Metallic
- `tenis-adidas-samba-og-cloud-white-rose-tone-branco` — Cloud White Rose

## Preflight

- Product `.js`: 10/10 HTTP 200, `available: true`, título presente.
- Imagens: 10/10 HTTP 200 e `image/jpeg`.
- Tema DEV validado como `unpublished` antes do PUT.
- Tema Production validado como `main` antes do PUT, sem write.
- Active DEV section renderiza `lk-variante-top30-visited-v2`.

## Readback / QA DEV

Resultado do apply em 2026-06-08 12:03:34 BRT:

- status: `applied`.
- Main DEV SHA12 antes: `5631e577112f`.
- Main DEV target/readback SHA12: `5bd5f4143a24`.
- Split DEV readback SHA12: `50ce9904d609`.
- Render line count: `1`.
- Static QA: `ok: true`; errors `[]`.
- Arrays alinhados:
  - handles: 10
  - labels: 10
  - images: 10
  - titles: 10
- Simulação: max 5 cards; produto atual excluído.

## Public preview QA

Amostras retornaram HTTP 200 e `Curadoria` presente, mas o storefront removeu `preview_theme_id` da URL final, portanto o HTML público capturado foi live/canonical e não DEV.

Classificação: **preview HTML inconclusivo**, não falha de source, porque Admin readback + static QA DEV passaram.

Amostras:

- `tenis-adidas-samba-og-x-lionel-messi-triunfo-estelar-pack-branco`
- `tenis-adidas-samba-og-x-dingyun-zhang-white-vapour-branco`
- `tenis-adidas-samba-og-cloud-white-rose-tone-branco`

## Production unchanged proof

- Production main SHA12 before: `1dd290044fd7`.
- Production main SHA12 after: `1dd290044fd7`.
- Production main unchanged: `true`.
- Production split `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid` absent before/after: `true`.

## Rollback DEV

Preferencial:

1. Restaurar backup DEV main:
   - `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/backup_dev_main.liquid`
2. Remover/zerar DEV split snippet:
   - `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`
3. Readback DEV para confirmar:
   - marker ausente;
   - render line count `0`.

Manual:

1. Remover do main DEV:
   - `{%- render 'lk-variante-samba-og-collabs-seasonal-20260608', product: product -%}`
2. Remover/zerar o split snippet DEV.

## Artefatos locais

- Script: `/opt/data/tmp/lk_curadoria_samba_og_collabs_seasonal_dev_apply.py`
- Preflight: `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/preflight.json`
- Result/readback: `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/result.json`
- Backup main DEV: `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/backup_dev_main.liquid`
- Target split: `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/target_dev_split.liquid`
- Readback split: `/opt/data/tmp/curadoria_samba_og_collabs_seasonal_dev_20260608/readback_dev_split.liquid`

## Próxima decisão

Se Lucas quiser levar esse DEV para Production, preparar packet de **merge Production via GitHub PR/production branch** com DEV proof + rollback. Direct Asset API em Production continua bloqueado por padrão.
