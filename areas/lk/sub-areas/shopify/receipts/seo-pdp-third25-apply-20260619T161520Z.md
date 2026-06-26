# Receipt — SEO PDP terceiro lote follow-up de 25

Data: 2026-06-19T16:17:14.777047+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-third25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-third25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_third25_before_20260619T161520Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_third25_after_readback_20260619T161520Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_third25_public_qa_20260619T161520Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-adidas-samba-og-liberty-london-better-scarlet-branco`
2. `tenis-adidas-samba-cardboard-marrom`
3. `tenis-air-jordan-4-retro-metallic-gold-branco`
4. `new-balance-9060-black-cement-black-cat-preto`
5. `tenis-new-balance-2002r-protection-pack-rain-cloud-suede-mesh`
6. `tenis-new-balance-2002r-protection-pack-phantom-cinza-camurca-mesh`
7. `air-jordan-1-low-gs-light-arctic-pink`
8. `air-jordan-1-low-voodoo-flax-and-oil-green`
9. `air-jordan-1-low-royal-toe`
10. `tenis-air-jordan-1-low-og-metallic-silver-cinza`
11. `air-jordan-1-low-crater-grey-university-blue`
12. `air-jordan-1-retro-low-og-atmosphere-grey`
13. `air-jordan-1-high-university-blue-unc`
14. `air-jordan-1-low-gs-fierce-pink`
15. `air-jordan-1-mid-smoke-grey`
16. `air-jordan-1-elevate-low-black-white`
17. `tenis-air-jordan-1-low-og-oxidized-white-green-branco`
18. `air-jordan-1-elevate-low-se-silver-toe`
19. `air-jordan-1-low-og-ex-black-and-smoke-grey`
20. `air-jordan-1-mid-se-craft-inside-out-black`
21. `air-jordan-1-low-multi-color-royal-toe`
22. `air-jordan-1-high-chicago-lost-and-found`
23. `tenis-air-jordan-1-low-se-gs-gold-toe-preto`
24. `nike-sb-x-air-jordan-4-retro-pine-green`
25. `tenis-air-jordan-1-low-se-paw-print-pink-foam-rosa`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=25`
- `handles_all_rounds_match=25`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_third25_before_20260619T161520Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.