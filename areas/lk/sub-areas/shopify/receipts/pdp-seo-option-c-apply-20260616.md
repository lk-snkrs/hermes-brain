# Receipt — PDP SEO Option C Apply — 2026-06-16

## Aprovação

Lucas aprovou: `opçnao C por favor...` para o pacote `PDP SEO Estratégico`.

## Escopo executado

Foram atualizados apenas campos de SEO de produto no Shopify:

- `seo.title`
- `seo.description`

Não foram alterados:

- preço
- estoque
- disponibilidade
- variantes
- imagens
- tema
- coleção
- tags

## Produtos atualizados

1. `tenis-nike-mind-002-sail-bege`
2. `tenis-nike-mind-002-thunder-blue-azul`
3. `tenis-nike-mind-002-light-violet-ore-roxo`
4. `tenis-nike-mind-002-light-khaki-bege`
5. `slide-nike-mind-001-sail-bege`
6. `slide-nike-mind-001-geode-teal-verde`
7. `slide-nike-mind-001-light-bone-bege`
8. `slide-nike-mind-001-pearl-pink-rosa`
9. `tenis-nike-vomero-premium-black-volt-preto`
10. `tenis-new-balance-204l-mushroom-arid-stone-marrom`
11. `tenis-new-balance-204l-timberwolf-bege`
12. `new-balance-530-white-natural-indigo-1`
13. `yeezy-slide-glow-green`

## Artefatos

Approval packet:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/pdp-seo-strategic-products-20260616.md`

Pre-write snapshot / rollback source:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/pdp-seo-option-c-apply-20260616/prewrite-snapshot.json`

Apply results:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/pdp-seo-option-c-apply-20260616/apply-results.json`

Admin readback:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/pdp-seo-option-c-apply-20260616/admin-readback.json`

Live HTML readback:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/pdp-seo-option-c-apply-20260616/live-html-readback.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/pdp-seo-option-c-apply-20260616/live-html-focused-recheck.json`

## Verificação

### Shopify Admin readback

Status: OK

- 13/13 products updated
- 13/13 `seo.title` match target
- 13/13 `seo.description` match target
- userErrors: none

### Live HTML readback

Initial public readback:

- HTTP 200: 13/13
- Liquid errors: 0
- 9/13 immediately reflected the exact new title/meta

Focused retry showed cache propagation/intermittent stale HTML for some PDP routes:

- `slide-nike-mind-001-geode-teal-verde`: new SEO observed after retry
- `tenis-nike-vomero-premium-black-volt-preto`: new SEO observed after retry
- `tenis-new-balance-204l-mushroom-arid-stone-marrom`: new SEO observed after retry
- `tenis-new-balance-204l-timberwolf-bege`: Admin readback OK; public HTML alternated between new and old title/meta during cache propagation

Interpretation: Shopify Admin is authoritative and matches target. Public storefront SEO HTML may serve stale cached variants briefly after Product SEO field updates.

## Rollback

Rollback source:

- `prewrite-snapshot.json`

Rollback procedure:

1. For each product in snapshot, restore prior `seo.title` and `seo.description`.
2. Run Shopify Admin readback and compare against snapshot.
3. Re-check live HTML for key PDPs:
   - Mind 002 Sail
   - Mind 001 Sail
   - 204L Mushroom
   - New Balance 530

## Notes

No secrets printed. Shopify write was limited to Product SEO fields under current explicit approval.
