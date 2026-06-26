# Curadoria LK PDP — Air Force 1 Low Special/Collabs — Production merge receipt

## Escopo
- Superfície: Shopify theme Production via GitHub branch `production`.
- Arquivo: `snippets/lk-variante-top30-visited-v2.liquid`.
- Grupo adicionado: `top30-nike-air-force-1-low-special`.
- Itens: Supreme Black, Supreme White, Ambush Black, Ambush Phantom, Ambush Game Royal, Tiffany 1837, Off-White Brooklyn.

## Aprovação
- Lucas aprovou o fluxo com comando no Telegram: `merge`.
- Guardrail mantido: nenhum write em produto, preço, estoque, checkout, collection, GMC, Klaviyo, ads ou Tiny.

## GitHub / Production
- PR: `#27` — `feat: add AF1 special Curadoria group`.
- Base: `production`.
- Head: `hermes/lk-af1-special-production-20260606`.
- Merge: squash merge concluído.
- Merge commit: `9d6b850515312540a37546b74bdbed6db8a5909f`.
- Branch temporária removida após merge.

## Verificação local pré-merge
- `git diff --check -- snippets/lk-variante-top30-visited-v2.liquid`: exit 0.
- Static parser:
  - SHA256 candidato: `dc30f0059f131a3b326698edc3094eb02db4a949bbac91a5b3b900571353b2a8`.
  - `marker_count`: 1.
  - Arrays Curadoria: 29 grupos em `lk_top30_markers`, `lk_top30_names`, `lk_top30_handles_groups`, `lk_top30_labels_groups`, `lk_top30_images_groups`.
  - Grupo AF1 Special: 7 handles, 7 labels, 7 images.

## Readback Production Shopify
- Tema Production: `155065417950`.
- Readback pós-merge via Admin API read-only:
  - SHA256: `dc30f0059f131a3b326698edc3094eb02db4a949bbac91a5b3b900571353b2a8`.
  - `marker_count`: 1.
  - Arrays Curadoria: 29 grupos alinhados.
  - `updated_at`: `2026-06-06T11:04:44-03:00`.
- Artefatos locais:
  - `/opt/data/tmp/lk_prod_af1_special_readback.json`
  - `/opt/data/tmp/lk-prod-after-af1-special.liquid`

## QA live público
Executado via CDP em PDPs públicas:

- `tenis-nike-air-force-1-low-x-supreme-black-preto`
  - Marker: `top30-nike-air-force-1-low-special`.
  - Cards renderizados: 5.
  - Labels: Supreme White, Ambush Black, Ambush Phantom, Ambush Game Royal, Tiffany 1837.
  - `fontWeight`: 300 em `span` e 300 em `::after`.

- `ambush-x-nike-air-force-1-low-black`
  - Marker: `top30-nike-air-force-1-low-special`.
  - Cards renderizados: 5.
  - Labels: Supreme Black, Supreme White, Ambush Phantom, Ambush Game Royal, Tiffany 1837.
  - `fontWeight`: 300 em `span` e 300 em `::after`.

- `tiffany-co-x-nike-air-force-1-low-1837`
  - Marker: `top30-nike-air-force-1-low-special`.
  - Cards renderizados: 5.
  - Labels: Supreme Black, Supreme White, Ambush Black, Ambush Phantom, Ambush Game Royal.
  - `fontWeight`: 300 em `span` e 300 em `::after`.

Resumo QA: `/opt/data/tmp/lk_af1_special_live_qa/summary.json` com `ok: true`.

## Risco
- Baixo: alteração restrita a um grupo de Curadoria no snippet de PDP.
- Não altera disponibilidade, preço, estoque, checkout ou cadastro de produto.

## Rollback
- GitHub: reverter o squash commit `9d6b850515312540a37546b74bdbed6db8a5909f` em `production`.
- Shopify/theme: restaurar snippet anterior se necessário. Backup local pré-AF1 no Git worktree: `/opt/data/tmp/lk-prod-git-before-af1-special.liquid`.

## Status
- Production merge concluído.
- Readback Production concluído.
- QA live público aprovado.
