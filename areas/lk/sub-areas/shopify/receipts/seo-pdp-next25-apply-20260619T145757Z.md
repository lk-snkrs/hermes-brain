# Receipt — SEO PDP próximo lote de 25

Data: 2026-06-19T14:59:50.262461+00:00
Escopo aprovado por Lucas: aplicar os 25 produtos do approval packet `seo-pdp-next25-approval-packet-20260619`, somente `seo.title` e `seo.description`.
Sistema: Shopify Admin GraphQL.
Campos alterados: somente `seo.title` e `seo.description` de Product.
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções, tema, checkout, canal, GMC, Klaviyo ou campanha.

## Arquivos

- Approval JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo-pdp-next25-approval-candidates-20260619.json`
- Snapshot antes: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_next25_before_20260619T145757Z.json`
- Readback depois: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_next25_after_readback_20260619T145757Z.json`
- QA público: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_next25_public_qa_20260619T145757Z.json`

## Execução

- `values_printed=false`
- `apply_count=25`
- `user_errors=[]`
- `all_match=True`

## Produtos alterados

1. `tenis-nike-x-skims-rift-mesh-light-bone-bege`
2. `camiseta-pace-buero-off-white`
3. `shorts-saint-studio-everywear-preto`
4. `shorts-saint-studio-everywear-caqui-bege`
5. `camiseta-saint-studio-boxy-supima-off-gola-vermelha-branco`
6. `camiseta-saint-studio-boxy-supima-mid-century-branco`
7. `camiseta-saint-studio-boxy-supima-its-all-good-preto`
8. `camiseta-saint-studio-boxy-supima-cool-branco`
9. `tenis-air-jordan-4-retro-og-nike-white-cement-couro`
10. `tenis-air-jordan-1-retro-high-og-unc-reimagined-nike-esportivo-couro`
11. `tenis-swarovski-x-air-jordan-1-retro-low-og-shadow-cinza`
12. `camiseta-nude-project-honor-tee-marshmallow-off-white`
13. `moletom-nude-project-side-eye-zip-up-black-preto`
14. `camiseta-nude-project-honor-tee-black-preto`
15. `camiseta-nude-project-kora-black-preto`
16. `camiseta-nude-project-berry-tee-white-branco`
17. `tenis-puma-speedcat-silk-chocotart-warm-white-marrom`
18. `define-jacket-nulu-rose-gold`
19. `wmns-air-jordan-1-mid-canyon-rust`
20. `tenis-air-jordan-1-low-neutral-grey-coconut-milk-cinza`
21. `tenis-new-balance-1906l-silver-shadow-grey-mesh-sintetico-slip-on`
22. `tenis-new-balance-1906l-rich-oak-suede-camurca-slip-on`
23. `tenis-travis-scott-x-jordan-jumpman-jack-tr-dark-mocha-nobuck-lona`
24. `tenis-jordan-jumpman-jack-tr-travis-scott-bright-cactus-couro-lona`
25. `tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo`

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
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-d1-audit-20260619/seo_pdp_next25_before_20260619T145757Z.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir Admin readback e QA público title/meta.