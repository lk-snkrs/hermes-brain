# Receipt — Bloco B — schema Tokyo/Speedcat + ASICS SEO/meta + handoff NB740

Data: 2026-06-27
Owner: [LK] Growth
Aprovação: Lucas aprovou Bloco B no Telegram.
Writes externos executados: Shopify theme production + collection SEO/metafields/description ASICS.
values_printed=false

## 1. OAuth / processo

Lucas corrigiu o processo: não quer autorizar OAuth a cada write. Correção registrada no Brain AGENTS de LK Growth:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/AGENTS.md`

Nova regra: mapear escopos necessários do pacote aprovado e autenticar uma única vez com conjunto suficiente, sem pingar Lucas incrementalmente para cada subtarefa. O token/cache não foi impresso no relatório; `values_printed=false`.

## 2. Tokyo/Speedcat — FAQPage schema restaurado

Theme production: `lk-new-theme/production` (`155065417950`).

Executado:

- Backup de `sections/lk-collection.liquid`: `sections-lk-collection.before.liquid`.
- Backup de `snippets/lk-goc-schema-extra.liquid`: `snippets-lk-goc-schema-extra.before.liquid`.
- Patch production: render único `{%- render 'lk-goc-schema-extra' -%}` em `sections/lk-collection.liquid`.
- Admin readback: `render_count=1`, updatedAt `2026-06-27T16:57:16Z`.

QA público:

| URL | HTTP | FAQPage | Liquid error |
|---|---:|---:|---:|
| `/collections/adidas-tokyo` | 200 | 1 | false |
| `/collections/puma-speedcat` | 200 | 1 | false |

## 3. ASICS Gel NYC — SEO/meta/OG cleanup

Executado:

- `collectionUpdate` em `asics-gel-nyc` com SEO title/meta premium.
- `metafieldsSet` para `global.title_tag` e `global.description_tag`.
- `descriptionHtml` preenchido com copy premium curta para alimentar OG/descrição quando o theme usa `collection.description`.
- Patch em `layout/theme.liquid` com branch explícito para `collection.handle == 'asics-gel-nyc'` em title/meta/OG/Twitter.

Admin readback:

- SEO title: `ASICS Gel NYC Original | Curadoria LK`.
- SEO description: `ASICS Gel NYC original na curadoria LK: silhueta retrô running, amortecimento GEL e atendimento humano para escolher modelo e cor.`
- Metafields `global.title_tag` e `global.description_tag` criados.
- DescriptionHtml preenchido.
- Layout readback contém 4 ocorrências de `asics-gel-nyc` e literal `ASICS Gel NYC Original | Curadoria LK`.

QA público pós-write:

- Parte das requisições já retorna o head novo:
  - title `ASICS Gel NYC Original | Curadoria LK`;
  - meta/OG com copy premium;
  - sem `Envio imediato`.
- Parte das requisições ainda retorna head antigo:
  - title `ASICS Gel NYC: 1 modelos | LK Sneakers`;
  - meta genérica com parcelamento/frete;
  - OG global com `Envio imediato e troca grátis`.

Classificação: **source/Admin/theme corrigidos; storefront público em propagação/cache inconsistente**. Não apliquei novo write cego porque o readback de fonte está correto; próximo passo seguro é recheck de cache/edge antes de novo patch.

## 4. NB740 — handoff aberto

Handoff criado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/handoffs/lk-shopify-nb740-canonical-collection-20260627.md`

Escopo: LK Shopify validar/criar collection canônica `new-balance-740`, sem estoque/preço/produtos/ordenação/campanhas.

## Rollback

- Schema Tokyo/Speedcat: restaurar `sections-lk-collection.before.liquid` e/ou remover render único de `lk-goc-schema-extra`; manter snippet intacto se desejado.
- ASICS: restaurar `layout-theme.before-asics-meta-cleanup.liquid`, remover/restaurar metafields `global.title_tag`/`global.description_tag`, restaurar collection SEO/description a partir dos backups em `collections-before.json` e `asics-before-metafield-description-readback.stdout`.
- NB740: sem write executado por Growth; handoff apenas.

## Non-actions

Não alterado:
- preço;
- estoque/Tiny/inventory/grade/disponibilidade;
- produtos;
- ordenação;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp/e-mail;
- checkout.


## Incidente sanitizado — output verbose Shopify CLI

Após a execução, o processo background retornou telemetria do Shopify CLI em modo `--verbose` contendo variáveis sensíveis no campo `env_shopify_variables`. O valor não é repetido neste receipt.

Ação corretiva imediata:
- regra adicionada ao `AGENTS.md`: não usar `shopify store auth --verbose`; capturar OAuth URL com wrapper `BROWSER` simples;
- outputs futuros devem manter `values_printed=false`;
- recomendação: rotacionar/revalidar os secrets Shopify afetados no Doppler/Shopify Admin quando possível.
