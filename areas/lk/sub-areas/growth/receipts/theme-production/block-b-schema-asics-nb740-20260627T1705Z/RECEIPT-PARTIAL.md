# Receipt parcial — Bloco B — schema Tokyo/Speedcat + ASICS + NB740

Data: 2026-06-27
Owner: [LK] Growth
Aprovação: Lucas aprovou Bloco B no Telegram.
values_printed=false

## Executado com sucesso

### 1. Tokyo/Speedcat FAQPage schema restaurado

- Backup de `sections/lk-collection.liquid` salvo em `sections-lk-collection.before.liquid`.
- Backup de `snippets/lk-goc-schema-extra.liquid` salvo em `snippets-lk-goc-schema-extra.before.liquid`.
- Patch aplicado em production theme `lk-new-theme/production` (`155065417950`): render único de `lk-goc-schema-extra` em `sections/lk-collection.liquid`.
- Readback Admin: `render_count=1`; updatedAt `2026-06-27T16:57:16Z`.

QA público após patch:

| URL | HTTP | FAQPage | Liquid error |
|---|---:|---:|---:|
| `/collections/adidas-tokyo?_qa=bblockb1705` | 200 | 1 | false |
| `/collections/puma-speedcat?_qa=bblockb1705` | 200 | 1 | false |

### 2. Handoff NB740 aberto

Arquivo:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/handoffs/lk-shopify-nb740-canonical-collection-20260627.md`

Escopo: LK Shopify validar/criar collection canônica `new-balance-740`, sem estoque/preço/produtos/ordenação/campanhas.

## Bloqueado parcialmente

### ASICS Gel NYC SEO/meta cleanup

Tentativa de `collectionUpdate` via Shopify CLI oficial com `--allow-mutations` falhou por escopo ausente:

- Required access: `write_products`.
- Não foi alterada a collection ASICS.

QA público ainda mostra:

- meta description fallback com `Parcele em 10x, frete grátis acima de R$ 500`.
- `og:description` global com `Envio imediato e troca grátis`.

## Próximo desbloqueio

Foi iniciado OAuth oficial Shopify CLI adicionando `write_products`, apenas para concluir o cleanup ASICS aprovado.

Após callback, executar somente:
- backup/readback collection ASICS;
- `collectionUpdate` SEO title/meta;
- QA público head/meta/OG.

## Non-actions

Não alterado: preço, estoque/Tiny/inventory/grade, produtos, ordenação, GMC/feed, campanhas, Klaviyo, WhatsApp/e-mail ou checkout.
