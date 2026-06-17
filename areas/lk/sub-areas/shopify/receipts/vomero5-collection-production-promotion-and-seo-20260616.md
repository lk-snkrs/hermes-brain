# Receipt — Nike Vomero 5 Production promotion + SEO fields

Data: 2026-06-16  
Alvo: `/collections/nike-vomero-5`  
Tema DEV: `155065450718` (`lk-new-theme/dev`, unpublished)  
Tema Production: `155065417950` (`lk-new-theme/production`, main)  
Asset: `sections/lk-collection.liquid`  
Modo: execução aprovada por Lucas no Telegram.

## Escopo executado

1. Revisão técnica/textual do DEV antes da promoção.
2. Promoção para Production do mesmo asset/diff validado no DEV.
3. Aplicação dos SEO fields da coleção via Shopify Admin GraphQL:
   - `seo.title`
   - `seo.description`
4. Readback Admin/API e QA público.

## Evidência — promoção de tema

Arquivo: `reports/assets/vomero5-collection-improvement-20260616/prod_promotion_and_seo_readback_summary.json`

- `values_printed=false`
- DEV source hash: `a57e2818f3d9aedf7abc95d3ca34013131450c1321027b3d4e1f8b8b40a86352`
- Production antes: `364a46074ddcd930c1817288cc4a8d4864e8da99acb516184bd5d0b62c9019f3`
- Production depois: `a57e2818f3d9aedf7abc95d3ca34013131450c1321027b3d4e1f8b8b40a86352`
- `prod_matches_dev_source=true`
- Markers Production pós-write:
  - `schema=1`
  - `vomero5_class=9`
  - `handle_guard=4`

## Evidência — SEO fields Admin

Antes:
- Title: `Tênis Nike Vomero 5 | Curadoria Exclusiva | LK Sneakers`
- Description: `Compre Nike Vomero 5 na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.`

Depois/readback Admin:
- Title: `Nike Vomero 5 Original | LK Sneakers`
- Description: `Nike Vomero 5 original na LK Sneakers: modelos premium, curadoria especializada, loja física nos Jardins e atendimento humano.`

Validação:
- `seo_title_matches=true`
- `seo_description_matches=true`
- `collection_update_user_errors=[]`

## Evidência — QA estático / schema

A revisão DEV antes de publicar já havia confirmado:
- `pass=true`
- `schema_type=FAQPage`
- `schema_question_count=4`
- `visible_dt_count_for_schema_names=4`
- `schema_marker_count=1`
- `old_truncated_answer_count=0`
- `liquid_if_count=88`
- `liquid_endif_count=88`

## QA público Production

Arquivos:
- `reports/assets/vomero5-collection-improvement-20260616/prod_public_live_qa_summary.json`
- `reports/assets/vomero5-collection-improvement-20260616/prod_public_cache_convergence_qa.json`

Achado importante:
- API/Admin e Asset readback estão corretos.
- Public storefront começou a alternar entre HTML novo e HTML antigo por cache/CDN.
- Amostras novas retornaram:
  - title novo correto;
  - meta nova correta;
  - marker `lk-vomero5-faq-schema-20260616` presente;
  - guia novo presente;
  - FAQ truncado antigo ausente;
  - `FAQPage` detectado.
- Algumas amostras sem preview/cookie ainda retornaram o HTML antigo com FAQ truncado, sem Liquid error.
- Requests com `preview_theme_id=155065417950` retornaram o HTML novo corretamente, confirmando que o tema main/Production renderiza o novo estado quando o cache não serve a versão antiga.

Classificação:
- Estado Admin/API: aplicado e correto.
- Estado theme Production: aplicado e correto.
- Estado público sem preview: em propagação/cache intermitente.

## Screenshot

Mobile top screenshot salvo:
- `reports/assets/vomero5-collection-improvement-20260616/screenshots/vomero5-mobile-top.png`

## Rollback

Rollback de tema Production:
1. Restaurar `reports/assets/vomero5-collection-improvement-20260616/prod_lk_collection_before_promotion_20260616.liquid` para `sections/lk-collection.liquid` no tema Production `155065417950`.
2. Readback hash esperado antigo: `364a46074ddcd930c1817288cc4a8d4864e8da99acb516184bd5d0b62c9019f3`.

Rollback SEO fields:
1. Restaurar `reports/assets/vomero5-collection-improvement-20260616/collection_seo_before_promotion_20260616.json`:
   - Title: `Tênis Nike Vomero 5 | Curadoria Exclusiva | LK Sneakers`
   - Description: `Compre Nike Vomero 5 na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.`
2. Readback Admin GraphQL da coleção `gid://shopify/Collection/458592747742`.

## Próximo acompanhamento recomendado

Rodar nova checagem pública em 10–20 minutos para confirmar convergência do cache/CDN. Não há evidência de erro Liquid ou falha de write; o único ponto pendente é propagação pública estável.
