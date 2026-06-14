# Receipt — New Balance 2002R collection created

Status: CREATED / PUBLIC COLLECTION BASIC LIVE / DEV LKGOC PREPARED
Data UTC: 20260613T102800Z
Owner: [LK] Otimização de Coleções

## Approval
Lucas: "Aprovo criar" in current Telegram turn.

## Shopify writes executed
- Created collection: `New Balance 2002R`
- Handle: `new-balance-2002r`
- Collection ID: `gid://shopify/Collection/1128114815198`
- SEO title: `New Balance 2002R original | Curadoria LK Sneakers`
- SEO description: `New Balance 2002R original na curadoria LK: modelos selecionados, autenticidade, atendimento humano e guia para escolher cor, forma e estilo.`
- Rule set: `TITLE CONTAINS 2002R`
- Published to Online Store publication.
- Deleted blocking URL redirect: `/collections/new-balance-2002r` → `/collections/new-balance-todos-os-modelos`.

## Readback
- Collection handle resolves publicly: `https://lksneakers.com.br/collections/new-balance-2002r`
- Public page title/description readback OK.
- Products count readback: 2 products.
- Products visible in readback:
  - Tênis New Balance 2002R Protection Pack Phantom Cinza Camurça Mesh Preto
  - Tênis New Balance 2002R Protection Pack Rain Cloud Suede Mesh Cinza

## DEV LKGOC prep
Theme validated before write:
- `lk-new-theme/dev`
- Theme ID: `155065450718`
- role: `UNPUBLISHED`

Assets touched in DEV only:
- `snippets/lk-goc-collection.liquid`
- `sections/lk-collection.liquid`

Readback assets saved in this work folder.

## Important caveat
Public storefront currently renders through production/main theme and shows the basic collection experience. Full LKGOC visual hero/guide is prepared in DEV asset readback but not promoted to production. Public unauthenticated preview could not be relied on for visual QA because Shopify returned the main theme unless preview cookies are active.

## Guardrails
- No stock/grade validation performed. Any availability decision must go through `lk-stock`.
- No Production theme code was edited.
- Production LKGOC merge remains blocked until visual QA + Lucas approval.

## Rollback
If rollback is needed:
1. Unpublish collection from Online Store.
2. Recreate redirect `/collections/new-balance-2002r` → `/collections/new-balance-todos-os-modelos` if Lucas wants old behavior restored.
3. Delete or archive collection after confirmation.
4. Restore DEV assets from `before` snapshots in this folder if needed.
