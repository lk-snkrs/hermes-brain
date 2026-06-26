# Receipt — SEO PDP apply lote 5

Data: 2026-06-17  
Escopo aprovado: aplicar lote 5 SEO PDP de 10 produtos.  
Sistema: Shopify Admin GraphQL.  
Campos alterados: somente `seo.title` e `seo.description` de Product.  
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções ou tema.

## Preparação

Arquivos:
- Packet revisado: `reports/assets/seo-pdp-fifth-scan-20260617/seo_pdp_fifth10_candidates_reviewed.json`
- Approval packet: `approval-packets/seo-pdp-fifth10-approval-packet-20260617.md`

Evidência do scan:
- `scanned_active_products=800`
- `excluded_already_applied_handles=40`
- `remaining_candidates_with_objective_seo_issue=502`
- `selected_count=10`

## Aplicação

Arquivos:
- Snapshot antes: `reports/assets/seo-pdp-fifth-scan-20260617/seo_pdp_fifth10_before_20260617.json`
- Readback depois: `reports/assets/seo-pdp-fifth-scan-20260617/seo_pdp_fifth10_after_readback_20260617.json`
- QA público: `reports/assets/seo-pdp-fifth-scan-20260617/seo_pdp_fifth10_public_qa_20260617.json`

Execução:
- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=true`

## Produtos alterados

1. `tenis-nike-air-force-1-low-protro-kobe-bryant-siempre-hermanos-marrom`
2. `tenis-new-balance-1906l-silver-metallic-black-prata`
3. `tenis-adidas-tokyo-mj-core-black-cream-white-gold-metallic-preto`
4. `tenis-adidas-taekwondo-mei-ballet-cream-white-branco`
5. `tenis-onitsuka-tiger-mexico-66-sabot-pure-silver-cream-cinza`
6. `tenis-onitsuka-tiger-mexico-66-sabot-dark-brown-marrom`
7. `tenis-asics-gel-1130-white-black-silver-prata`
8. `tenis-nike-air-jordan-1-retro-high-og-sp-union-la-chicago-shadow`
9. `tenis-air-jordan-1-low-archaeo-brown-nike-casual-couro-1069539760`
10. `tenis-air-jordan-1-mid-gs-rookie-season-branco-vermelho`

## QA

Admin readback:
- todos os 10 produtos bateram exatamente com os valores-alvo.

QA público:
- `handles_total=10`
- `handles_any_round_match=10`
- `handles_still_not_public_match=[]`
- `liquid_error_count=0`
- `http_429_count=0`

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`reports/assets/seo-pdp-fifth-scan-20260617/seo_pdp_fifth10_before_20260617.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir:
- Admin readback por handle;
- QA público title/meta;
- checagem de ausência de `Liquid error`.
