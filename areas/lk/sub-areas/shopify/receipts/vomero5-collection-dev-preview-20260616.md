# Receipt — Nike Vomero 5 collection DEV preview

Data: 2026-06-16  
Alvo: `/collections/nike-vomero-5`  
Tema DEV: `155065450718` (`lk-new-theme/dev`, unpublished)  
Tema Production: `155065417950` (`lk-new-theme/production`, main)  
Asset: `sections/lk-collection.liquid`

## Escopo aprovado/executado

Foi preparado e subido somente no tema DEV um preview da melhoria GEO/source page para a coleção Nike Vomero 5.

Mudança no DEV:
- Intro acima da grade com copy curta e comercial.
- Bloco pós-grade `Guia LK` com conteúdo citável sobre Nike Vomero 5.
- FAQ visível com 4 perguntas.
- `FAQPage` JSON-LD espelhando as perguntas visíveis.
- Correção do FAQ truncado antigo, removendo a resposta cortada `recomendação g`.

## Evidência de readback

Arquivo de evidência: `reports/assets/vomero5-collection-improvement-20260616/dev_upload_readback_summary.json`

- `values_printed=false`
- DEV antes: `fa713172cbb71df2e8bcffd416ab0976808cdc13a1efa6e37451c359cecc1ace`
- DEV depois: `a57e2818f3d9aedf7abc95d3ca34013131450c1321027b3d4e1f8b8b40a86352`
- Target local: `a57e2818f3d9aedf7abc95d3ca34013131450c1321027b3d4e1f8b8b40a86352`
- `dev_matches_target=true`
- Production antes: `364a46074ddcd930c1817288cc4a8d4864e8da99acb516184bd5d0b62c9019f3`
- Production depois: `364a46074ddcd930c1817288cc4a8d4864e8da99acb516184bd5d0b62c9019f3`
- `prod_unchanged=true`
- Marker schema DEV: `1`
- Marker classe Vomero 5 DEV: `9`

## QA estático DEV

Arquivo de evidência: `reports/assets/vomero5-collection-improvement-20260616/dev_static_qa_summary.json`

- `pass=true`
- `schema_type=FAQPage`
- `schema_question_count=4`
- `visible_dt_count_for_schema_names=4`
- `schema_marker_count=1`
- `guide_headline_count=1`
- `old_truncated_answer_count=0`
- `liquid_if_count=88`
- `liquid_endif_count=88`

Perguntas do schema/FAQ:
1. O Nike Vomero 5 é original na LK Sneakers?
2. O Nike Vomero 5 é confortável para o dia a dia?
3. Como escolher o tamanho do Nike Vomero 5?
4. Qual cor de Nike Vomero 5 combina melhor com uso diário?

## QA público de preview DEV

Arquivo de evidência: `reports/assets/vomero5-collection-improvement-20260616/dev_public_preview_probe.json`

Preview público com cookie/preview:
- HTTP `200`
- `Liquid error=false`
- Marker schema presente: `true`
- Guia presente: `true`
- FAQ truncado antigo: `false`
- JSON-LD detectado: `Organization/ShoeStore/ClothingStore`, `FAQPage`, `BreadcrumbList`, `CollectionPage`
- `faqpage_count=1`

Controle Production/live:
- Production permaneceu inalterado por hash de Asset API.
- Fetch público live sem preview ainda não contém o novo marker e ainda reflete o conteúdo antigo/truncado, como esperado porque Production não foi promovido.

## Bloqueio

Ainda não foram aplicados os SEO fields globais da coleção (`seo.title` / `seo.description`) porque isso é write de coleção Shopify separado do tema DEV e exige aprovação explícita escopada.

## Rollback DEV

Rollback seguro:
1. Repor no DEV o snapshot `reports/assets/vomero5-collection-improvement-20260616/dev_lk_collection_before_20260616.liquid`.
2. Readback do asset `sections/lk-collection.liquid` no tema `155065450718`.
3. Confirmar ausência dos markers `lk-vomero5-faq-schema-20260616` e `coll-rich-content--vomero5`.
4. Confirmar Production hash inalterado.

## Próxima decisão

Para promover ao storefront, é necessária aprovação explícita para:
- promover o mesmo diff aprovado do DEV para Production; e/ou
- aplicar também os SEO fields da coleção (`seo.title` / `seo.description`) via Shopify Admin.
