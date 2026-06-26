# Receipt — SEO PDP follow-up lote de 25

Data: 2026-06-19T16:09:23.658751+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-followup25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-followup25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_followup25_before_20260619T160725Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_followup25_after_readback_20260619T160725Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_followup25_public_qa_20260619T160725Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-nike-air-jordan-4-cave-stone-and-black-marrom`
2. `tenis-air-jordan-1-retro-high-og-black-toe-reimagined-vermelho`
3. `tenis-air-jordan-1-retro-low-og-zion-williamson-voodoo-alternate-azul`
4. `tenis-nike-air-jordan-1-retro-low-og-chicago-2025-vermelho`
5. `tenis-air-jordan-1-retro-low-fragment-design-x-travis-scott-couro-branco-preto-azul`
6. `tenis-air-jordan-4-retro-og-sp-undefeated-2025-verde`
7. `tenis-travis-scott-x-nike-air-jordan-1-retro-low-og-sp-olive-suede`
8. `tenis-air-jordan-1-low-archaeo-brown-nike-casual`
9. `tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho`
10. `tenis-air-jordan-1-low-og-mocha-marrom`
11. `tenis-air-jordan-1-high-og-shattered-backboard-laranja`
12. `tenis-air-jordan-1-low-se-gs-glitter-swoosh-branco-1`
13. `tenis-travis-scott-air-jordan-4-retro-cactus-jack-nubuck-azul-6`
14. `air-jordan-1-low-white-university-red`
15. `travis-scott-x-air-jordan-1-low-og-reverse-mocha`
16. `tenis-air-jordan-1-low-nike-sail-soft-pearl-sequins-couro-nobuck`
17. `air-jordan-1-low-medium-olive-verde`
18. `tenis-air-jordan-1-low-lunar-new-year-photon-dust-cinza`
19. `tenis-air-jordan-1-retro-high-og-year-of-the-snake-xuanwu-preto`
20. `tenis-air-jordan-1-retro-high-85-og-bred-2025-vermelho`
21. `tenis-nike-vomero-premium-black-sapphire-rose-preto`
22. `tenis-adidas-samba-lt-core-black-off-white-gum-preto`
23. `tenis-adidas-samba-og-pony-hair-pack-night-indigo-clear-sky-azul-marinho`
24. `tenis-adidas-samba-lt-cloud-white-core-black-black-sole-branco`
25. `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=25`
- `handles_all_rounds_match=22`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_followup25_before_20260619T160725Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.