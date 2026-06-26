# Receipt — SEO PDP apply lote 10

Data: 2026-06-16  
Escopo aprovado: aplicar o lote SEO PDP de 10 produtos já preparado.  
Sistema: Shopify Admin GraphQL.  
Campos alterados: apenas `seo.title` e `seo.description` de Product.  
Sem alteração de preço, estoque, disponibilidade, descrição de produto, tags, coleções ou tema.

## Evidência

Arquivos:
- Antes/Admin snapshot: `reports/assets/seo-pdp-packet-20260616/seo_pdp_apply10_before_20260616.json`
- Depois/Admin readback: `reports/assets/seo-pdp-packet-20260616/seo_pdp_apply10_after_readback_20260616.json`
- QA público: `reports/assets/seo-pdp-packet-20260616/seo_pdp_apply10_public_qa_20260616.json`

Resumo da execução:
- `values_printed=false`
- Packet tinha `selected_total_in_packet=12`; escopo aplicado foi o lote aprovado de `10` primeiros produtos.
- `apply_count=10`
- `user_errors=[]`
- `all_match=true`

QA público:
- `count=10`
- `admin_all_match=true`
- `public_title_match_count=10`
- `public_description_match_count=10`
- `liquid_error_count=0`

## Produtos alterados

1. `tenis-nike-sb-air-jordan-4-x-retro-sp-navy-branco`
2. `tenis-nike-air-jordan-1-low-og-chinese-new-year-2026-cinza`
3. `tenis-nike-vomero-premium-alabaster-amarelo`
4. `tenis-nike-vomero-premium-realtree-camo-black-preto`
5. `tenis-new-balance-204l-reflection-bege`
6. `tenis-new-balance-204l-lone-star-grey-cinza`
7. `a-ma-maniere-x-air-jordan-1-sail-and-burgundy`
8. `tenis-air-jordan-1-retro-high-rare-air-sail-cinnabar-bege`
9. `tenis-air-jordan-1-low-multicolor-sashiko-colorido`
10. `tenis-onitsuka-tiger-mexico-66-sabot-natural-cream-bege-1070119339`

## Verificação

Admin readback confirmou que todos os 10 produtos ficaram com os valores-alvo de `seo.title` e `seo.description`.

QA público confirmou:
- os 10 PDPs renderizam title público igual ao alvo;
- os 10 PDPs renderizam meta description pública igual ao alvo;
- nenhum `Liquid error` foi detectado.

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`reports/assets/seo-pdp-packet-20260616/seo_pdp_apply10_before_20260616.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois, repetir:
- Admin readback por handle;
- QA público de title/meta;
- checagem de ausência de `Liquid error`.

## Observação

Dois itens adicionais existiam no packet original, mas ficaram fora deste apply porque Lucas aprovou o lote de 10:
- `tenis-new-balance-1906l-black-suede-preto`
- `tenis-new-balance-9060-lilac-white-kids-roxo`
