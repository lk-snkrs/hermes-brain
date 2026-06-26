# Receipt — SEO PDP apply terceiro lote 10

Data: 2026-06-16  
Escopo aprovado: aplicar terceiro lote SEO PDP de 10 produtos, após refinamento manual.  
Sistema: Shopify Admin GraphQL.  
Campos alterados: somente `seo.title` e `seo.description` de Product.  
Sem alteração de preço, estoque, disponibilidade, descrição, tags, coleções ou tema.

## Refinamentos antes do write

- `tenis-nike-air-jordan-1-high-virgil-abloh-archive-x-alaska-branco`
  - de: `Jordan 1 High Virgil Abloh x Alaska Branco | LK Sneakers`
  - para: `Jordan 1 High Virgil Abloh Alaska Branco | LK Sneakers`
- `tenis-onitsuka-tiger-mexico-66-fringe-mocha-brown-dark-brown-marrom`
  - de: `Onitsuka Tiger Mexico 66 Marrom | LK Sneakers`
  - para: `Onitsuka Tiger Mexico 66 Fringe Marrom | LK Sneakers`

## Evidência

Arquivos:
- Packet final: `reports/assets/seo-pdp-third-scan-20260616/seo_pdp_third_candidates.json`
- Antes/Admin snapshot: `reports/assets/seo-pdp-third-scan-20260616/seo_pdp_third10_before_20260616.json`
- Depois/Admin readback: `reports/assets/seo-pdp-third-scan-20260616/seo_pdp_third10_after_readback_20260616.json`
- QA público multiround: `reports/assets/seo-pdp-third-scan-20260616/seo_pdp_third10_public_multiround_qa_20260616.json`

Execução:
- `values_printed=false`
- `apply_count=10`
- `user_errors=[]`
- `all_match=true`

## Produtos alterados

1. `tenis-nike-air-jordan-1-high-virgil-abloh-archive-x-alaska-branco`
2. `tenis-nike-air-jordan-1-retro-low-og-howard-university-vermelho`
3. `tenis-adidas-samba-jane-chalk-white-wonder-quartz-branco`
4. `tenis-jordan-11-retro-low-university-blue-2026-azul`
5. `tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal`
6. `tenis-new-balance-530-beige-angora-creme-1069960456`
7. `tenis-nike-air-max-90-x-patta-sp-sapphire-azul-branco`
8. `tenis-nike-sb-dunk-low-pro-muni-lightning-denim-turquoise-turquesa`
9. `tenis-nike-sb-zoom-air-paul-rodriguez-1-habanero-red-all-star-vermelho`
10. `tenis-onitsuka-tiger-mexico-66-fringe-mocha-brown-dark-brown-marrom`

## QA

Admin readback:
- todos os 10 produtos bateram exatamente com os valores-alvo.

QA público multiround:
- `rounds_total=30`
- `handles_total=10`
- `admin_all_match=true`
- `handles_any_round_match=10`
- `handles_all_rounds_match=6`
- `liquid_error_count=0`

Classificação:
- Write correto no Admin/API.
- Todos os 10 já renderizaram pelo menos uma amostra pública nova.
- Algumas rotas ainda alternam por cache/CDN, padrão já observado nos lotes anteriores.
- Sem evidência de erro Liquid.

## Rollback

Para desfazer, restaurar os valores anteriores a partir de:
`reports/assets/seo-pdp-third-scan-20260616/seo_pdp_third10_before_20260616.json`

Rollback deve alterar somente:
- `seo.title`
- `seo.description`

Depois repetir:
- Admin readback por handle;
- QA público title/meta;
- checagem de ausência de `Liquid error`.
