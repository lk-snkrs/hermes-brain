# Receipt — PDP SEO-only cleanup — sob encomenda + SEO drift

Data: 20260625T192149Z
Origem: `[LK] Growth`
Classificação: Shopify production write aprovado por Lucas no turno atual
values_printed=false

## Aprovação Lucas

> Aprovo preparar em dev/readback e, se o diff estiver restrito, aplicar em produção a limpeza dos 9 PDPs SEO-only do review D+7, limitada a remover/normalizar sob encomenda público e corrigir drift de SEO title/description conforme receipt/intenção aprovada, sem alterar preço, estoque, variantes, disponibilidade, imagens, tags, collections, GMC, Klaviyo, campanhas, checkout ou tema, com backup, rollback e readback público por PDP.

## Fonte

- D+7 report: `areas/lk/sub-areas/growth/reports/impact-reviews/pdp-cro-seo-d7-20260625T190553Z/REPORT.md`
- Approval packet: `areas/lk/sub-areas/growth/approval-packets/pdp-seo-only-cleanup-sob-encomenda-20260625/APPROVAL-PACKET.md`
- Workdir: `areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/production-apply/`

## O que foi feito

- Backup Admin antes do write: `backup-before.json`.
- Preflight/dry-run gerou diff restrito.
- Aplicado em produção nos 9 PDPs SEO-only:
  - body_html: substituição da frase pública `Itens sob encomenda seguem prazo estimado de 4 a 6 semanas.` por `O atendimento humano da LK confirma os detalhes de entrega quando necessário.`
  - SEO metafields `global.title_tag` / `global.description_tag`: corrigidos apenas nos handles com drift vs receipt/intenção de 2026-06-18.

## Escopo preservado

Não alterado:
- preço;
- estoque;
- variantes;
- disponibilidade/inventory;
- imagens;
- tags;
- collections;
- GMC;
- Klaviyo;
- campanhas;
- checkout;
- tema.

Estoque/Tiny/inventory não consultado.

## Resultado técnico

- Produtos planejados: 9
- Produtos aplicados: 9
- Body updates: 9
- Metafield updates: 7
- Admin readback pós-write: 9/9 sem `sob encomenda` em `descriptionHtml`.
- SEO drift corrigido: todos os metafields alvo passaram a bater com valores esperados.

## Readback público por PDP

Observação: o Admin já está limpo em 9/9. O público apresentou cache/propagação parcial em alguns handles nos primeiros retries; onde o HTML público ainda mostra a frase antiga, o body Admin já está limpo e o status é tratado como cache/propagação, não falha de write.

| Handle | Público antes tinha `sob encomenda` | Admin depois tem `sob encomenda` | Público depois imediato tinha `sob encomenda` | HTTP | Title público imediato |
|---|---:|---:|---:|---:|---|
| `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` | True | False | True | 200 | Tênis Nike Vomero Premium SP Black Mini | LK Sneakers |
| `tenis-nike-vomero-premium-white-lapis-total-orange-off-white` | True | False | True | 200 | Tênis Nike Vomero Premium White Lapis Total | LK Sneakers |
| `tenis-nike-vomero-premium-particle-rose-burgundy-rosa` | True | False | True | 200 | Nike Vomero Premium Particle Rose Burgundy | LK Sneakers |
| `tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja` | True | False | True | 200 | Tênis Nike Vomero Premium x Melitta | LK Sneakers |
| `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom` | True | False | True | 200 | Onitsuka Tiger x Versace Sakura Leather Loafers Brown W… | LK Sneakers |
| `tenis-nike-vomero-premium-volt-tint-sapphire-verde` | True | False | False | 200 | Nike Vomero Premium Volt Tint Sapphire Verde | LK Sneakers |
| `tenis-new-balance-gator-run-timberwolf-bege` | True | False | True | 200 | New Balance Gator Run Timberwolf Bege | LK Sneakers |
| `tenis-nike-x-tom-sachs-mars-yard-3-0-bege` | True | False | True | 200 | Nike x Tom Sachs Mars Yard 3.0 Bege | LK Sneakers |
| `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green` | True | False | True | 200 | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura | LK Sneakers |

## Artefatos

- Backup: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/production-apply/backup-before.json`
- Plano/diff: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/production-apply/plan.json`
- Aplicação + verify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/production-apply/applied.json`
- Script: `areas/lk/sub-areas/growth/work/pdp-seo-only-cleanup-20260625/apply_pdp_seo_only_cleanup.py`

## Rollback

Usar `backup-before.json` para restaurar por produto:
- `body_html` original;
- metafields `global.title_tag` e `global.description_tag` originais.

Rollback não precisa tocar preço, estoque, variantes, imagens, tags, collections, GMC, Klaviyo, campanhas, checkout ou tema porque essas superfícies não foram alteradas.

## Próximos passos

- Revalidar público em nova janela caso o cache continue mostrando frase antiga em alguns handles.
- D+14: manter impact review; não fazer rollback de CRO com D+7 inconclusivo.
