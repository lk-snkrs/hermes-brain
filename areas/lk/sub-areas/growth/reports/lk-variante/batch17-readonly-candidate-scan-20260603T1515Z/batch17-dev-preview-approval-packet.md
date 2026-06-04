# Batch 17 — Approval packet para Preview/Dev

- fonte live: `3918da96d152`
- scan read-only: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/batch17-readonly-candidate-scan-20260603T1515Z/batch17-readonly-candidate-scan.json`
- produtos públicos lidos: `1807`
- ação externa feita: `nenhuma`
- próximo write possível: somente upload em tema unpublished após aprovação explícita

## Proposta
### `top30-nike-dunk-low-regular` — append_new_group
- handles: `10`; product .js OK: `10/10`; imagens OK: `10/10`; malformed: `0`
- `tenis-nike-dunk-low-baroque-brown-marrom` — Baroque Brown
- `tenis-nike-dunk-low-denim-turquoise-azul` — Denim Turquoise
- `tenis-nike-dunk-low-viotech-rosa` — Viotech
- `tenis-nike-dunk-low-next-nature-aster-pink-rosa` — Next Nature Aster Pink
- `tenis-nike-dunk-flax-suede-marrom` — Flax Suede
- `tenis-nike-dunk-low-suede-panda-preto` — Suede Panda
- `tenis-nike-dunk-low-safari-oil-green-verde` — Safari Oil Green
- `tenis-nike-dunk-low-safari-phantom-bege` — Safari Phantom
- `tenis-nike-dunk-low-medium-olive-hemp-verde` — Medium Olive Hemp
- `tenis-nike-dunk-low-twist-university-blue-azul` — Twist University Blue

### `top30-air-jordan-4-regular` — expand_existing_group
- handles: `8`; product .js OK: `8/8`; imagens OK: `8/8`; malformed: `0`
- `tenis-nike-air-jordan-4-cave-stone-and-black-marrom` — Cave Stone and Black
- `tenis-air-jordan-4-retro-military-blue-branco-copia` — Oxidized Green
- `tenis-air-jordan-4-retro-forget-me-not-azul` — Forget Me Not
- `tenis-air-jordan-4-retro-seafoam-verde` — Seafoam
- `tenis-air-jordan-4-retro-orchid-rosa` — Orchid
- `tenis-air-jordan-4-retro-white-thunder-preto` — White Thunder
- `tenis-air-jordan-4-retro-shimmer-rosa` — Shimmer
- `tenis-air-jordan-4-retro-oxidized-branco` — Oxidized

## Bloqueados / deixados para depois
- air-jordan-1-low / air-jordan-1-low-og: deferred because previous semantic-hotfix blocker remains
- onitsuka-mexico-66 regular: deferred because first clean batch contained many Kids/Slip-On rows; needs adult-only curation
- new-balance-9060: deferred despite volume because Batch 14 already expanded it and known Arid Stone placeholder remains blocked
- adidas-samba-og: deferred because existing group has mixed capsule history; needs separate cleanup/curation rather than quick expansion
- asics-gel-1130: no-go for now due duplicate colorway handles and smaller commercial impact

## Rollback previsto
- Preview: restaurar backup do asset do tema `156623372510` antes do upload.
- Produção: não entra nesta etapa; se futuramente aprovado, backup live antes do merge e rollback pelo `live-before.liquid`.

## Decisão necessária
Aprovar ou não o upload do Batch 17 apenas no preview unpublished, com readback + QA estático + QA público do preview quando possível.