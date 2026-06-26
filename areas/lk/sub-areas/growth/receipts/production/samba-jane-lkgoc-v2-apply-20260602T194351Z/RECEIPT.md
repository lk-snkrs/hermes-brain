# Receipt — Adidas Samba Jane LKGOC v2

Timestamp: 2026-06-02T19:52:14.050475Z

## Applied
- Implemented Samba Jane collection top editorial block using LKGOC/204L contract.
- New snippet: `snippets/lk-samba-jane-lkgoc-v2.liquid`.
- Section render inserted once in `sections/lk-collection.liquid`, immediately before the New Balance 204L gold-source block.
- Legacy snippet `snippets/lk-samba-jane-coll-preview.liquid` now delegates to the v2 snippet to neutralize stale page-cache variants.

## Readback QA
- New render count in section: 1
- Old render count in section: 0
- Section bytes: 253801
- Under 256KB: True
- Snippet title count: 1
- Snippet v2 class count: 11

## Section Rendering QA
- `lk-collection-v2--adidas-samba-jane`: 4
- `Mary Jane terrace, leitura fashion.`: 1
- New LKGOC body text: 1
- Old body text: 0
- `Guia editorial LK`: 1
- Legacy `Perguntas Frequentes`: 0
- Old class `lk-samba-jane-coll-preview`: 0

## Public full-page cache note
Full page public HTML is still alternating stale cached variants. Current Shopify section render is correct; URL limpa may need cache propagation.

## Rollback
PUT sections__lk-collection.before.liquid and snippets__lk-samba-jane-lkgoc-v2.before.liquid back to their Shopify assets
