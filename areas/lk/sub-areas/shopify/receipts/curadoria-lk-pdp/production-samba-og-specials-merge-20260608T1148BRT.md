# Receipt — Curadoria LK PDP Production Adidas Samba OG especiais merge (2026-06-08)

- values_printed: false
- aprovação: Lucas respondeu `aprovo` após approval packet `Curadoria LK PDP Production merge: Adidas Samba OG especiais`.
- interpretação segura: aprovação para merge Production via GitHub PR/production branch do batch Samba OG especiais.
- caminho executado: GitHub PR/production branch.
- write direto Shopify Asset API em Production: **não executado**.
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/38
- merge commit: `8d39bf31fc5894038fa0337029b2ff1e9a597cac`
- branch: `hermes/curadoria-samba-og-specials-production-20260608`
- base: `production`

## Mudança

- Criado split snippet no source Production:
  - `snippets/lk-variante-samba-og-specials-20260608.liquid`
- Inserida 1 render line no main:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
- Marker:
  - `top30-adidas-samba-og-specials-20260608`
- Escopo semântico:
  - Adidas Samba OG especiais / animal print / pony / seasonal.
  - Não mistura Samba regular, Wales Bonner, Samba Jane ou Sambae.

## Evidência GitHub/local

- PR state antes do merge: `MERGEABLE` / `CLEAN`.
- Status checks: sem checks configurados (`[]`).
- `git diff --check`: pass.
- Static source QA: pass.
- Source main SHA12: `1dd290044fd7`.
- Source split SHA12: `220b9679f22c`.
- Array counts: handles `10`, labels `10`, images `10`, titles `10`.

## Shopify Production readback

Após merge e sync:

- Main Production SHA12: `1dd290044fd7`.
- Split Production SHA12: `220b9679f22c`.
- Render line count: `1`.
- Static QA: `ok: true`, errors `[]`.
- Arrays alinhados:
  - handles `10`
  - labels `10`
  - images `10`
  - titles `10`
- Simulação: 5 cards; current product excluded.

## QA público Production

Amostra completa dos 10 handles com `view=default`, cache-buster e no-cache headers:

- `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-liberty-london-better-scarlet-branco`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-pony-hair-pack-night-indigo-clear-sky-azul-marinho`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-cow-print-bege`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-marron-sand-strata-pony-vinho`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-collegiate-green-leopard-marrom`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-wonder-white-black-pony-bege`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-adidas-samba-og-year-the-snake-2025-branco`
  - HTTP 200, marker presente, 5 cards, current ausente.

Nota QA: as primeiras coletas públicas oscilaram por cache/edge em alguns handles. Revalidação com `view=default`, cache-buster e no-cache headers retornou 10/10 marker presente.

## Rollback

Rollback preferencial:

1. Reverter o merge commit `8d39bf31fc5894038fa0337029b2ff1e9a597cac` via GitHub/production branch.
2. Aguardar sync Shopify.
3. Readback para confirmar ausência do marker/render line.

Rollback manual escopado:

1. Remover do main Production source a linha:
   - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
2. Remover/zerar:
   - `snippets/lk-variante-samba-og-specials-20260608.liquid`
3. Merge via GitHub/production branch e readback Shopify.

## Artefatos locais

- PR body: `/opt/data/tmp/curadoria_samba_og_prod_20260608_pr_body.md`
- Verificação final: `/opt/data/tmp/curadoria_samba_prod_20260608/verify_final.json`
- Verifier: `/opt/data/tmp/lk_curadoria_samba_prod_verify.py`
