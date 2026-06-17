# Receipt — SEO PDP apply segundo lote 10

Data: 2026-06-16  
Escopo aprovado: aplicar o segundo lote SEO PDP de 10 produtos.  
Sistema: Shopify Admin GraphQL.  
Campos alterados: somente `seo.title` e `seo.description` de Product.  
Sem alteração de preço, estoque, disponibilidade, descrição, tags, coleções ou tema.

## Evidência

Arquivos:
- Packet read-only: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next_candidates.json`
- Antes/Admin snapshot: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_before_20260616.json`
- Depois/Admin readback: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_after_readback_20260616.json`
- QA público inicial: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_public_qa_20260616.json`
- QA público focado em URLs stale: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_public_retry_stale_20260616.json`
- QA público multiround: `reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_public_multiround_qa_20260616.json`

Resumo da execução:
- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=true`

## Produtos alterados

1. `tenis-nike-air-jordan-1-high-fragment-design-x-union-la-varsity-red-branco`
2. `tenis-nike-air-jordan-1-low-se-repaired-denim-swoosh-azul`
3. `tenis-new-balance-1906l-black-suede-preto`
4. `tenis-new-balance-9060-lilac-white-kids-roxo`
5. `tenis-new-balance-9060-grey-day-kids-td-cinza`
6. `tenis-new-balance-gator-run-star-burst-bege`
7. `tenis-nike-shox-tl-pumice-night-maroon-cinza`
8. `tenis-onitsuka-tiger-mexico-66-fringe-black-black-preto`
9. `tenis-onitsuka-tiger-mexico-66-slip-on-white-tricolor`
10. `tenis-onitsuka-tiger-moage-co-birch-black-bege`

## Verificação Admin

Admin readback confirmou que todos os 10 produtos ficaram com os valores-alvo de `seo.title` e `seo.description`.

## QA público

Resultado inicial:
- `count=10`
- `admin_all_match=true`
- primeira checagem pública teve 7/10 matches por cache;
- repetição sem URL randômica teve 5/10 matches por cache;
- `liquid_error_count=0`.

QA focado nas URLs inicialmente stale confirmou match em 3/3 handles testados por 3 rodadas.

QA multiround final:
- `rounds_total=30`
- `handles_total=10`
- `admin_all_match=true`
- `handles_any_round_match=10`
- `handles_all_rounds_match=4`
- `liquid_error_count=0`

Classificação:
- Estado Admin/API: aplicado e correto.
- Estado público: todos os 10 já retornaram pelo menos uma amostra com title/meta novos; algumas rotas continuam alternando HTML antigo por cache/CDN.
- Sem evidência de erro Liquid ou falha de write.

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`reports/assets/seo-pdp-next-scan-20260616/seo_pdp_next10_before_20260616.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois, repetir:
- Admin readback por handle;
- QA público de title/meta;
- checagem de ausência de `Liquid error`.
