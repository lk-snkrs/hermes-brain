# Receipt — Curadoria LK PDP Production Air Jordan 4 merge (2026-06-08)

- values_printed: false
- aprovação: Lucas respondeu `aprovo merge` após DEV AJ4 aplicado/validado e frase segura de merge Production via GitHub.
- caminho executado: GitHub PR/production branch.
- write direto Shopify Asset API em Production: **não executado**.
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/37
- merge commit: `782b4766572d33ddfb6e4cc938d60184e1784031`
- branch: `hermes/curadoria-aj4-production-20260608`
- base: `production`

## Mudança

- Criado split snippet no source Production:
  - `snippets/lk-variante-aj4-expansion-20260608.liquid`
- Inserida 1 render line no main:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `{%- render 'lk-variante-aj4-expansion-20260608', product: product -%}`
- Marker:
  - `top30-air-jordan-4-expansion-20260608`

## Evidência GitHub/local

- PR state antes do merge: `MERGEABLE` / `CLEAN`.
- Status checks: sem checks configurados (`[]`).
- `git diff --check`: pass.
- Static source QA: pass.
- Source main SHA12: `0c3e18df0bff`.
- Source split SHA12: `a88d68e3cb03`.
- Handle count: 9.

## Shopify Production readback

Após merge e sync:

- Main Production SHA12: `0c3e18df0bff`.
- Split Production SHA12: `a88d68e3cb03`.
- Render line count: `1`.
- Static QA: `ok: true`, errors `[]`.
- Simulação: 9 handles, 5 cards, current product excluded.

## QA público Production

Amostra pública pós-sync:

- `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `tenis-jordan-4-retro-toro-bravo-2026-vermelho-1`
  - HTTP 200, marker presente, 5 cards, current ausente.
- `air-jordan-4-seafoam`
  - HTTP 200, marker presente, 5 cards, current ausente.

## Rollback

Rollback preferencial:

1. Reverter o merge commit `782b4766572d33ddfb6e4cc938d60184e1784031` via GitHub/production branch.
2. Aguardar sync Shopify.
3. Readback para confirmar ausência do marker/render line.

Rollback manual escopado:

1. Remover do main Production source a linha:
   - `{%- render 'lk-variante-aj4-expansion-20260608', product: product -%}`
2. Remover/zerar:
   - `snippets/lk-variante-aj4-expansion-20260608.liquid`
3. Merge via GitHub/production branch e readback Shopify.

## Artefatos locais

- PR body: `/opt/data/tmp/curadoria_aj4_prod_20260608_pr_body.md`
- Verificação final: `/opt/data/tmp/curadoria_aj4_prod_20260608/verify_final.json`
- Verifier: `/opt/data/tmp/lk_curadoria_aj4_prod_verify.py`
