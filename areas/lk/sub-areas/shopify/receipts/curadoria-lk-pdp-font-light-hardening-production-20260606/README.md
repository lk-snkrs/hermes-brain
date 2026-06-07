# Receipt — Curadoria LK PDP font-light hardening Production — 2026-06-06

## Status
Merge para Production concluído via GitHub PR. Shopify Production sincronizou e QA visual live passou.

## Escopo aprovado
- Asset: `assets/lk-variante.css`
- Tema Production: `155065417950`
- Alteração: hardening de tipografia light (`font-weight:300`) para título e labels do bloco `Outras variações`.
- Sem alteração em produtos, preços, estoque, checkout, coleções, apps ou snippet de grupos.

## GitHub
- PR: `#32`
- URL: `https://github.com/lk-snkrs/lk-new-theme/pull/32`
- Branch: `hermes/font-light-hardening-production-20260606T162318Z`
- Head SHA: `31d09208281e3f5e213778f6a87ec5729703c37c`
- Merge SHA: `71581a1517dcd9bd61387dc5d042057ef0cc3390`
- Merge method: squash
- Branch remota: deletada com sucesso

## Diff
- `assets/lk-variante.css | 3 ++-`
- `1 file changed, 2 insertions(+), 1 deletion(-)`
- `git diff --check`: passed

## Readback Production
Antes do merge:
- `title_base_500_count`: `0`
- `title_base_300_count`: `1`
- `current_label_base_500_count`: `1`
- `current_label_base_300_count`: `0`
- `canonical_hardening_count`: `0`
- SHA: `7f014399ad96fd55ec33229bea1758c9c5f4db66c066e65a87511046adb6914a`

Depois do merge / Shopify poll 2:
- `title_base_500_count`: `0`
- `title_base_300_count`: `1`
- `current_label_base_500_count`: `0`
- `current_label_base_300_count`: `1`
- `canonical_hardening_count`: `1`
- SHA: `69417ddf74a039c529ce0e3b225f4a5ee12234778f6ba16b1a40d6a2317a07b7`

## CSS público live
- `https://lksneakers.com.br/cdn/shop/t/91/assets/lk-variante.css?v=146918974967942648421780763023`

## QA visual Production via CDP

### New Balance 530
- PDP: `new-balance-530-white-natural-indigo-1`
- Marker: `top30-nb-530`
- Título: `Outras variações`
- `titleWeight`: `300`
- `labelWeights`: `300, 300, 300, 300, 300`
- Labels: `Turtledove`, `Silver Cream`, `Silver White`, `Steel Grey`, `Silver Blue`
- Challenge anti-bot: `false`

### Adidas Superstar special
- PDP: `tenis-adidas-superstar-x-clot-chinese-new-year-preto`
- Marker: `top30-adidas-superstar-special`
- Título: `Outras variações`
- `titleWeight`: `300`
- `labelWeights`: `300, 300`
- Labels: `Korn 30th`, `Wales Bonner`
- Challenge anti-bot: `false`

## Backup
Backup pré-merge Production:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-font-light-hardening-production-20260606/20260606T162318Z-production-theme-155065417950-assets__lk-variante.before.css`

## Receipt JSON
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-font-light-hardening-production-20260606/20260606T162318Z-production-merge-receipt.json`

## Risco
Baixo. CSS localizado na Curadoria LK PDP; destaque visual do item atual permanece por borda/cor, não por negrito.

## Rollback
Preferencial: reverter PR `#32` no GitHub.
Alternativo: restaurar o backup acima no asset `assets/lk-variante.css` do tema Production.
