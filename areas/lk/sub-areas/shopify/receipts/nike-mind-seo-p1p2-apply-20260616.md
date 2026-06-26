# Receipt — Nike Mind SEO P1+P2 Apply — 2026-06-16

## Aprovação

Lucas aprovou: `aprovar aplicar P1 + P2 Nike Mind.`

## Escopo executado

Atualizados apenas campos SEO de produto Shopify para os PDPs Nike Mind classificados como P1/P2:

- `seo.title`
- `seo.description`
- SEO metafields globais legados quando necessário (`global.title_tag`, `global.description_tag`) para um PDP com HTML público persistente

Não foram alterados:

- preço
- estoque
- disponibilidade
- variantes
- imagens
- tema
- coleções
- tags
- produto title/copy

## Produtos atualizados

Total: 10 PDPs

P1:

1. `tenis-nike-mind-002-grey-football-grey-cinza`
2. `tenis-nike-mind-002-sail-bege`
3. `slide-nike-mind-001-blackened-blue-azul`
4. `slide-nike-mind-001-mineral-slate-verde`
5. `slide-nike-mind-001-team-red-vermelho`
6. `slide-nike-mind-001-white-speed-red-branco`

P2:

1. `tenis-nike-mind-002-black-hyper-crimson-preto`
2. `tenis-nike-mind-002-light-smoke-grey-cinza`
3. `slide-nike-mind-001-light-smoke-grey-cinza`
4. `slide-nike-mind-001-solar-red-vermelho`

## Artefatos

Approval packet:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/approval-packets/nike-mind-seo-audit-20260616.md`

Snapshot/rollback:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/prewrite-snapshot.json`

Apply results:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/apply-results.json`

Admin readback:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/admin-readback.json`

Live HTML readback:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/live-html-readback.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/live-html-focused-recheck.json`

Extra sync for persistent public stale case:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/nike-mind-seo-p1p2-apply-20260616/light-smoke-grey-metafield-sync.json`

## Verificação Admin

Status: OK

- 10/10 products updated
- 10/10 `seo.title` matches target
- 10/10 `seo.description` matches target
- userErrors: none

## Verificação HTML público

Initial live HTML:

- 10/10 HTTP 200
- 0 Liquid errors
- 7/10 reflected target immediately

Focused recheck:

- `tenis-nike-mind-002-sail-bege`: target reflected in 4/4 focused probes
- `slide-nike-mind-001-blackened-blue-azul`: target reflected in 3/4 focused probes; 1 stale cached response
- `slide-nike-mind-001-light-smoke-grey-cinza`: Admin + global SEO metafields correct, but public HTML still served old title/meta in 8/8 probes after extra metafield sync

## Persistent note — Light Smoke Grey

Product:

- `slide-nike-mind-001-light-smoke-grey-cinza`

Admin/source of truth:

- `seo.title`: `Slide Nike Mind 001 Light Smoke Grey | LK Sneakers`
- `seo.description`: `Nike Mind 001 Light Smoke Grey original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.`
- `global.title_tag`: matches target
- `global.description_tag`: matches target

Public HTML still serves:

- title: `Slide Nike Mind 001 Light Smoke Grey Cinza | LK Sneakers`
- meta: `Slide Nike Mind 001 Light Smoke Grey Cinza original. a partir de R$ 3200 em 10x sem juros. Curadoria LK · Frete grátis +R$500 · LK Sneakers`

Interpretation: source of truth is corrected; public route/cache remains stale for this PDP. Do not keep rewriting identical SEO fields. If it persists later, prepare a separate scoped packet to investigate theme/app SEO rendering or request Shopify/cache escalation.

## Rollback

Rollback source:

- `prewrite-snapshot.json`

Rollback steps:

1. Restore prior `seo.title` and `seo.description` for all 10 products.
2. Restore legacy global SEO metafields if needed.
3. Run Admin readback.
4. Run live HTML spot QA.

## Security

No secrets printed. Shopify write was limited to SEO fields under explicit approval.
