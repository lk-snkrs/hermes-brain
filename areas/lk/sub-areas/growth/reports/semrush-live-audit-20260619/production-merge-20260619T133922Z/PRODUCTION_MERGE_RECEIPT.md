# LK Growth — Production merge receipt — SEMrush anchor text patch

- Data UTC: `2026-06-19T13:39Z`
- Aprovação: Lucas pediu `Ok fazer merge` após dev patch.
- Escopo: merge para production theme apenas do patch de `links sem anchor text` no category grid.
- Writes externos: Shopify production theme asset = 1; estoque consultado=false; values_printed=false.

## Executado

- Production theme: `lk-new-theme/production` / ID `155065417950`.
- Dev source: `lk-new-theme/dev` / ID `155065450718`.
- Asset: `sections/lk-category-grid.liquid`.
- Patch aplicado:
  - adiciona CSS `.catcard__sr` screen-reader-only;
  - troca anchors vazios dos category cards por `<span class="catcard__sr">Ver coleção ...</span>`.

## Readback

- PUT Shopify: `200`.
- Admin readback depois de propagação: `catcard__sr=True`, empty anchor pattern removido.
- SHA antes: `094ec658490fad7d0e51c7944485f7176f1c09fe0ba764a93ad6afee6dd51ea1`.
- SHA depois: `c077852cf219243b0b770631f8aaf738e3ca587678c15210c67a9de933dc16fa`.

## Verificação pública

- Public cache inicialmente serviu versão antiga por alguns polls.
- Último poll: `{'i': 3, 'status': 200, 'sr': True, 'empty': 0}`.
- Resultado: produção já servindo `catcard__sr=True` e `empty=0`.

## Rollback

- Backup do asset antes do merge: `rollback-before-production-asset.json`.
- Rollback: PUT do `before_value` de volta em `sections/lk-category-grid.liquid` no theme `155065417950`.

## Próximo recheck

- No próximo SEMrush crawl, esperar queda/remoção do notice `Links with no anchor text` para a home/category grid.
