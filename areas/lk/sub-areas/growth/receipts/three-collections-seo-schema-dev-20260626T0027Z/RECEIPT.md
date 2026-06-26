# Receipt — Adidas Taekwondo + Adidas Tokyo + Puma Speedcat

Data: 20260626T003626Z
Origem: `[LK] Growth`
Aprovação: Lucas respondeu `Fazer os 3` após recomendação de Adidas Taekwondo + Adidas Tokyo + Puma Speedcat.
values_printed=false

## Escopo executado

### 1) Adidas Taekwondo

Collection: `/collections/adidas-taekwondo`
Collection id: `440811880670`

Executado em produção:
- SEO title alterado para: `Adidas Taekwondo Original Feminino | Curadoria LK`
- Meta description alterada para: `Adidas Taekwondo original na curadoria LK: Taekwondo Mei, Ballet e Lace em silhueta baixa, estética sneakerina e atendimento humano para escolher.`

Preparado em DEV theme `155065450718`:
- guia/FAQ/schema visível restrito à collection Adidas Taekwondo no asset `snippets/lk-goc-guide-contract.liquid`.
- Production theme **não recebeu** guia Taekwondo.

### 2) Adidas Tokyo

Collection: `/collections/adidas-tokyo`
Collection id: `447368823006`

Executado em produção:
- FAQPage schema-only condicional via novo snippet `snippets/lk-goc-schema-extra.liquid` renderizado em `sections/lk-collection.liquid`.
- Sem alteração de SEO title/meta, description visual, handle, produtos, preço, estoque ou ordenação.

### 3) Puma Speedcat

Collection: `/collections/puma-speedcat`
Collection id: `438203777246`

Executado em produção:
- FAQPage schema-only condicional via novo snippet `snippets/lk-goc-schema-extra.liquid` renderizado em `sections/lk-collection.liquid`.
- Sem alteração de SEO title/meta, description visual, handle, produtos, preço, estoque ou ordenação.

## Artefatos principais

Workdir:
`areas/lk/sub-areas/growth/work/three-collection-dev-20260626/`

Backups:
- `adidas-taekwondo-admin-before.json`
- `adidas-tokyo-admin-before.json`
- `puma-speedcat-admin-before.json`
- `dev-snippet-before.liquid`
- `prod-section-before-schema-extra-render.liquid`
- `prod-section-before-remove-duplicate-schema-extra-render.liquid`
- `prod-section-before-schema-extra-render2.liquid`
- `prod-section-before-schema-extra-render2b.liquid`

Targets/readbacks:
- `dev-snippet-target-three.liquid`
- `dev-snippet-readback-three-final.liquid`
- `prod-snippet-lk-goc-schema-extra-target.liquid`
- `prod-section-readback-single-schema-extra-render-final.liquid`

## Observações técnicas

- Tentativa inicial de adicionar schema diretamente em `sections/lk-collection.liquid` excedeu limite Shopify de 256 KB e foi rejeitada por HTTP 422; nenhum write aplicado nessa tentativa.
- Solução aplicada: novo snippet pequeno `snippets/lk-goc-schema-extra.liquid` + render único em `sections/lk-collection.liquid`.
- Tentativa de schema via `descriptionHtml` em Tokyo/Speedcat não renderizou publicamente; foi revertida para os backups antes de concluir pela solução de snippet/theme.
- Corrigida duplicidade de render para manter `FAQPage count = 1` em Tokyo/Speedcat.

## QA público

Validação pública com query cache-bust/filter:

| Collection | HTTP | Title/meta | FAQPage | Schema alvo | Liquid error |
|---|---:|---|---:|---:|---:|
| Adidas Taekwondo | 200 | title novo presente | 0 | n/a | não |
| Adidas Tokyo | 200 | preservado | 1 | presente | não |
| Puma Speedcat | 200 | preservado | 1 | presente | não |
| ASICS Gel-1130 controle | 200 | preservado | 1 | sem vazamento | não |

QA DEV Taekwondo:
- Preview `?preview_theme_id=155065450718` renderizou guia LK + FAQ visível.

## Non-actions confirmadas

Não alterado:
- preço;
- estoque/Tiny/inventory;
- produtos;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout.

Tokyo/Speedcat:
- sem alteração de SEO title/meta;
- sem alteração visual final de description.

Taekwondo:
- sem alteração de description visual;
- sem guia/schema em production nesta etapa.

## Próximo passo

- D+7/D+14: medir GSC/SEMrush para Adidas Taekwondo, Adidas Tokyo e Puma Speedcat.
- Se Taekwondo responder bem ou se quisermos fechar o gap de schema, publicar o guia/FAQ/schema de DEV em produção com aprovação específica.
