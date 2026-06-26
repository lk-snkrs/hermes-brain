# P0 Execution Receipt — Approval A

Data UTC: 2026-06-18T21:21:23Z

## Executado

- Menu production atualizado via Shopify GraphQL `menuUpdate`.
- Item: `Sneakers > Adidas > Adidas Samba`.
- De: `/collections/samba-duplicata-backup-20260616` / `gid://shopify/Collection/424590213342`.
- Para: `/collections/adidas-samba` / `gid://shopify/Collection/468244332766`.
- Dev theme `lk-new-theme/dev` (`155065450718`) patchado no asset `snippets/judgeme_widgets.liquid`.
- Production theme não foi alterado.
- Redirect não foi criado.
- values_printed=false.

## Readback

- GraphQL menu readback: OK, item aponta para `/collections/adidas-samba`.
- Dev asset readback: OK, contém `lk_picture_src`.
- URL nova `/collections/adidas-samba`: HTTP 200.
- URL antiga `/collections/samba-duplicata-backup-20260616`: HTTP 404.
- Home HTML público ainda continha 1 ocorrência do slug antigo no momento do readback, provável cache/propagação ou render residual; assets main não contêm o slug antigo e GraphQL menus não contêm o slug antigo.

## Pendência recomendada

- Se precisar fechar o 404 imediatamente enquanto cache propaga, criar redirect `/collections/samba-duplicata-backup-20260616` → `/collections/adidas-samba` mediante aprovação explícita adicional.

## Rollback

- Menu: reverter item `gid://shopify/MenuItem/618084499678` para `/collections/samba-duplicata-backup-20260616` e resource `gid://shopify/Collection/424590213342`.
- Dev theme: restaurar arquivo salvo em `execution-approval-A-$(date -u +%Y%m%dT%H%M%SZ)/dev-judgeme-before.liquid` ou hash anterior registrado.
