# Approval packet — Curadoria LK PDP DEV Adidas Samba OG especiais (2026-06-08)

- values_printed: false
- Status: **read-only packet; nenhum write Shopify/DEV/Production executado**.
- Pedido de Lucas: `seguir com os outros` após merge Production AJ4.
- Interpretação segura: continuar pós-Production em read-only, comparar candidatos restantes e preparar próximo pacote DEV controlado.

## Worker receipt

- demand_classification: LK Shopify / Curadoria PDP / next-batch preparation after Production merge.
- canonical_playbook: `curadoria-post-production-next-batch-controlled-dev-packet`.
- workers_selected: catalog/coverage scan, public preflight QA, packet writer.
- workers_skipped: visual/browser worker, because no DEV upload/preview approved yet; merge/publish worker, because only next-batch read-only is authorized.
- delegation_tool_used: no.
- reason_if_no_delegation: runtime não expõe `delegate_task`; subtarefas foram executadas localmente com scripts read-only e consolidadas pelo LK Shopify.
- owner_agent_final_decision: recomendar um lote DEV controlado de Samba OG especiais/materials, não Dunk/AJ1 broad.

## Maintenance baseline

Relatório quinzenal read-only gerado em 2026-06-08 11:19 BRT:

- Semáforo: verde 50 · amarelo 11 · vermelho 0 · cinza 0.
- Handles públicos checados: 260.
- Fonte: `origin/production` + storefront público `.js`.
- No write: nenhum Shopify/DEV/Production write executado.
- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260608T111912-0300.md`

## Production coverage source

- Source commit `origin/production`: `782b476`.
- Active snippet count parsed recursively from `sections/lk-pdp.liquid`: 9.
- Marker count: 55.
- Covered handle count detected: 744.

## Candidate scan summary

Top uncovered opportunities after NB9060 + AJ4 merge:

- Adidas Samba OG: sellable adult 52; covered 22; uncovered clean 30; public-valid sample 12.
- Nike Dunk Low: sellable adult 179; covered 55; uncovered clean 124; public-valid sample 12.
- Air Jordan 1 Low: sellable adult 111; covered 36; uncovered clean 75; public-valid sample 5.

## Recommendation

Próximo DEV recomendado: **Adidas Samba OG especiais / animal print / pony / seasonal**.

Motivo:

- Mais controlado semanticamente que `nike-dunk-low` e `air-jordan-1-low`, que têm universo grande, collabs muito misturados e maior risco de bloco broad demais.
- `adidas-samba-og` já tem grupo regular e Wales Bonner cobertos; este packet evita duplicar esses grupos e pega uma expansão coerente de materiais/prints especiais.
- 10 handles públicos válidos com imagens 200 `image/*`.
- Labels revisados manualmente para evitar duplicações/labels longos.

## Proposed DEV scope

- Criar split snippet DEV:
  - `snippets/lk-variante-samba-og-specials-20260608.liquid`
- Adicionar 1 render line no active snippet DEV:
  - `{%- render 'lk-variante-samba-og-specials-20260608', product: product -%}`
- Marker:
  - `top30-adidas-samba-og-specials-20260608`
- Max render: 5 cards.
- Excluir produto atual.
- Copy: `Curadoria LK` + `Outras variações`.
- Sem produto/preço/estoque/collection/app/checkout/ads/email/GMC/Tiny write.

## Proposed handles / labels / preflight

- `tenis-adidas-samba-og-pony-hair-wonder-beige-better-scarlet-branco` — Pony Beige Scarlet — HTML 200, JS 200, image 200 `image/jpeg`
- `tenis-adidas-samba-og-liberty-london-better-scarlet-branco` — Liberty London Scarlet — HTML 200, JS 200, image 200 `image/png`
- `tenis-adidas-samba-og-pony-hair-pack-night-indigo-clear-sky-azul-marinho` — Pony Indigo Sky — HTML 200, JS 200, image 200 `image/jpeg`
- `tenis-adidas-samba-og-silver-metallic-cracked-leather-prateado` — Silver Cracked — HTML 200, JS 200, image 200 `image/png`
- `tenis-adidas-samba-og-cow-print-bege` — Cow Print — HTML 200, JS 200, image 200 `image/png`
- `tenis-adidas-samba-og-marron-sand-strata-pony-vinho` — Sand Strata Pony — HTML 200, JS 200, image 200 `image/jpeg`
- `tenis-adidas-samba-og-collegiate-green-leopard-marrom` — Green Leopard — HTML 200, JS 200, image 200 `image/png`
- `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` — Red Leopard — HTML 200, JS 200, image 200 `image/jpeg`
- `tenis-adidas-samba-og-wonder-white-black-pony-bege` — Pony White Black — HTML 200, JS 200, image 200 `image/jpeg`
- `tenis-adidas-samba-og-year-the-snake-2025-branco` — Year Snake 2025 — HTML 200, JS 200, image 200 `image/jpeg`

## Static proposed snippet

- Local proposed snippet: `/opt/data/tmp/curadoria_samba_og_specials_dev_packet_20260608.liquid`
- SHA12: `490eaddd5316`
- Handles: 10.
- Labels: Pony Beige Scarlet, Liberty London Scarlet, Pony Indigo Sky, Silver Cracked, Cow Print, Sand Strata Pony, Green Leopard, Red Leopard, Pony White Black, Year Snake 2025.
- Static errors: none.

## Risks

- Semantic: medium-low. É Samba OG, mas focado em materiais/prints especiais; não mistura Samba Jane/Sambae/Wales Bonner.
- Coverage: existing regular Samba OG remains untouched; this is an additive split snippet.
- Public storefront: final visual QA só existe após DEV upload/preview aprovado.
- Labels: reviewed manually, but Lucas can prefer more commercial names.

## Rollback if DEV approved/applied

- Remove the single render line from the active DEV snippet.
- Delete/zero `snippets/lk-variante-samba-og-specials-20260608.liquid`.
- Readback DEV and verify marker absent.

## Approval needed

Para executar somente no DEV/unpublished theme, Lucas precisa aprovar exatamente:

`Aprovo DEV Curadoria Samba OG especiais`

Isso **não** aprova Production/merge. Production exigirá novo QA + aprovação específica depois.
