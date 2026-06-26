# Receipt — SEO PDP quinto lote follow-up de 25

Data: 2026-06-19T19:07:45.692738+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-fifth25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-fifth25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fifth25_before_20260619T190548Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fifth25_after_readback_20260619T190548Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fifth25_public_qa_20260619T190548Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-onitsuka-tiger-mexico-66-kids-birch-rust-orange-bege`
2. `tenis-onitsuka-tiger-mexico-mid-runner-kids-white-directoire-blue-branco`
3. `tenis-adidas-gazelle-indoor-cream-white-preloved-teal-branco`
4. `tenis-adidas-sl-72-og-liberty-london-better-scarlet-rosa`
5. `tenis-adidas-samba-og-off-white-oat-violet-tone-branco`
6. `tenis-adidas-samba-og-cloud-white-rose-tone-branco`
7. `tenis-adidas-sambae-x-kseniaschnaiderc-black-multicolor-colorido`
8. `tenis-adidas-handball-spezial-clear-sky-white-warm-sandstone-azul`
9. `tenis-adidas-adistar-jellyfish-pharrell-williams-focus-olive-orange-branco`
10. `tenis-adidas-samba-x-wales-bonner-wonder-clay-royal-bege`
11. `tenis-adidas-samba-og-ivory-collegiate-green-branco`
12. `tenis-adidas-sambae-cloud-white-collegiate-green-branco`
13. `tenis-adidas-sl-72-og-clear-sky-sand-strata-cream-white-azul`
14. `livro-rizzoli-from-soul-to-sole-the-adidas-sneakers-of-jacques-chassaing`
15. `tenis-adidas-handball-spezial-sand-strata-clear-sky-bege`
16. `tenis-adidas-sl-72-og-sand-strata-preloved-brown-cream-white-bege`
17. `tenis-wmns-taekwondo-mei-ballet-adidas-couro-prata-metalico`
18. `tenis-adidas-wmns-taekwondo-mei-white-scarlet-gum-couro`
19. `tenis-new-balance-204l-silver-metallic-black-prateado`
20. `tenis-adidas-yeezy-slide-slate-marine-azul-escuro`
21. `nike-sb-dunk-low-pro-iso-dark-russet`
22. `nike-dunk-low-varsity-green`
23. `tenis-new-balance-204l-maroon-sea-salt-branco`
24. `tenis-nike-sb-dunk-low-supreme-94-white-metallic-silver-branco`
25. `tenis-levis-x-nike-air-max-95-og-black-anthracite-denim`

## QA

Admin readback:
- todos os 25 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=25`
- `handles_any_round_match=25`
- `handles_all_rounds_match=24`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_fifth25_before_20260619T190548Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.