# Receipt — Curadoria LK PDP DEV Adidas Samba OG especiais (2026-06-08)

- values_printed: false
- aprovação: Lucas respondeu `aprovo dev` após approval packet `Curadoria LK PDP DEV Adidas Samba OG especiais`.
- interpretação segura: aprovação somente para DEV/unpublished theme do packet imediato; **não aprova Production/merge**.
- write executado: Shopify DEV/unpublished theme only.
- Production: read-only/unchanged.
- Sem produto/preço/estoque/collection/app/checkout/ads/email/GMC/Tiny write.

## Tema

- DEV theme: `155065450718` / `lk-new-theme/dev` / role `unpublished`.
- Production theme: `155065417950` / `lk-new-theme/production` / role `main`.

## Mudança DEV

- Split snippet criado/atualizado:
  - `snippets/lk-variante-samba-og-specials-20260608.liquid`
- Active main DEV atualizado com 1 render line:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
- Marker:
  - `top30-adidas-samba-og-specials-20260608`
- Escopo semântico:
  - Adidas Samba OG especiais / animal print / pony / seasonal.
  - Não mistura Samba regular, Wales Bonner, Samba Jane ou Sambae.

## Handles / labels

- `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco` — Pony Beige Scarlet
- `tenis-adidas-samba-og-liberty-london-better-scarlet-branco` — Liberty London Scarlet
- `tenis-adidas-samba-og-pony-hair-pack-night-indigo-clear-sky-azul-marinho` — Pony Indigo Sky
- `tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado` — Silver Cracked
- `tenis-adidas-samba-og-cow-print-bege` — Cow Print
- `tenis-adidas-samba-og-marron-sand-strata-pony-vinho` — Sand Strata Pony
- `tenis-adidas-samba-og-collegiate-green-leopard-marrom` — Green Leopard
- `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` — Red Leopard
- `tenis-adidas-samba-og-wonder-white-black-pony-bege` — Pony White Black
- `tenis-adidas-samba-og-year-the-snake-2025-branco` — Year Snake 2025

## Preflight

- Product `.js`: 10/10 HTTP 200 e disponíveis.
- Imagens: 10/10 HTTP 200 e `image/*`.
- Tema DEV validado como `unpublished` antes do PUT.
- Tema Production validado como `main` antes do PUT, sem write.
- Active DEV section renderiza `lk-variante-top30-visited-v2`.

## Readback / QA DEV

Resultado do apply em 2026-06-08 11:33:44 BRT:

- status: `applied`.
- Main DEV SHA12 antes: `cee33fcd8aa7`.
- Main DEV target/readback SHA12: `5631e577112f`.
- Split DEV readback SHA12: `57e7cfe630ef`.
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

- `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco`
- `tenis-adidas-samba-og-liberty-london-better-scarlet-branco`
- `tenis-adidas-samba-og-year-the-snake-2025-branco`

## Production unchanged proof

- Production main SHA12 before: `0c3e18df0bff`.
- Production main SHA12 after: `0c3e18df0bff`.
- Production main unchanged: `true`.
- Production split `snippets/lk-variante-samba-og-specials-20260608.liquid` absent before/after: `true`.

## Rollback DEV

Preferencial:

1. Restaurar backup DEV main:
   - `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/backup_dev_main.liquid`
2. Remover/zerar DEV split snippet:
   - `snippets/lk-variante-samba-og-specials-20260608.liquid`
3. Readback DEV para confirmar:
   - marker ausente;
   - render line count `0`.

Manual:

1. Remover do main DEV:
   - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
2. Remover/zerar o split snippet DEV.

## Artefatos locais

- Script: `/opt/data/tmp/lk_curadoria_samba_og_specials_dev_apply.py`
- Preflight: `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/preflight.json`
- Result/readback: `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/result.json`
- Backup main DEV: `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/backup_dev_main.liquid`
- Target split: `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/target_dev_split.liquid`
- Readback split: `/opt/data/tmp/curadoria_samba_og_specials_dev_20260608/readback_dev_split.liquid`

## Próxima decisão

Se Lucas quiser levar esse DEV para Production, preparar packet de **merge Production via GitHub PR/production branch** com DEV proof + rollback. Direct Asset API em Production continua bloqueado por padrão.
