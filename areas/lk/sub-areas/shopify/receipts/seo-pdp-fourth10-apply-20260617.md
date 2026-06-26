# Receipt — SEO PDP apply lote 4

Data: 2026-06-17  
Escopo aprovado: aplicar lote 4 SEO PDP de 10 produtos.  
Sistema: Shopify Admin GraphQL.  
Campos alterados: somente `seo.title` e `seo.description` de Product.  
Sem alteração de preço, estoque, disponibilidade, descrição de PDP, tags, coleções ou tema.

## Pré-checagem do dia

Antes do lote 4, foi feita revalidação do que foi publicado em 2026-06-16:

- 30 PDPs revalidados no Admin/API.
- `admin_all_title_match=true`.
- `admin_all_description_match=true`.
- Retry público lento confirmou `30/30` PDPs com title/meta novos em ao menos uma amostra.
- Nike Vomero 5 confirmou marker/FAQPage/title/meta em `3/3` tentativas lentas.
- `liquid_error_count=0`.

Arquivos:
- `reports/assets/seo-pdp-fourth-scan-20260617/revalidation_yesterday_20260617.json`
- `reports/assets/seo-pdp-fourth-scan-20260617/revalidation_public_slow_retry_20260617.json`

## Aplicação do lote 4

Arquivos:
- Packet revisado: `reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_candidates_reviewed.json`
- Snapshot antes: `reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_before_20260617.json`
- Readback depois: `reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_after_readback_20260617.json`
- QA público: `reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_public_qa_20260617.json`

Execução:
- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=true`

## Produtos alterados

1. `tenis-adidas-samba-og-crystal-linen-ivory-gum-branco`
2. `tenis-nike-kobe-11-protro-mamba-day-dourado`
3. `tenis-nike-shox-tl-black-cave-stone-preto`
4. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-brown-mauve-gum`
5. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-bold-gold-amarelo`
6. `tenis-adidas-stella-mccartney-x-adidas-wmns-sportswear-x-trainers-core-black-preto`
7. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-cloud-white-ivory-branco`
8. `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa`
9. `tenis-onitsuka-tiger-mexico-66-fringe-yellow-black-amarelo`
10. `tenis-onitsuka-tiger-mexico-66-sabot-black-black-preto`

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
`reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_before_20260617.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir:
- Admin readback por handle;
- QA público title/meta;
- checagem de ausência de `Liquid error`.
