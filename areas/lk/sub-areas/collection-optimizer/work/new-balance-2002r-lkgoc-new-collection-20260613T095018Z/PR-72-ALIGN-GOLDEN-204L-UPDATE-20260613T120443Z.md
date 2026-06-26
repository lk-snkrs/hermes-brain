# PR 72 update — Align 2002R with 204L golden contract

Data UTC: 20260613T120443Z
PR: https://github.com/lk-snkrs/lk-new-theme/pull/72

## User feedback
"Ele não está no padrão desejado pelo LKGOC"

## Action taken
Updated the existing PR branch without Shopify writes.

## New commit
`2314a87 Align 2002R hero with 204L golden contract`

## Fix details
- Rebuilt `snippets/lk-goc-new-balance-2002r-hero-204l-clone.liquid` from the literal 204L golden block in `sections/lk-collection.liquid`.
- Removed extra custom 2002R height/position CSS that was inherited from the 530 clone path.
- Restored the 204L JS/read-more/modal contract shape.
- Fixed accidental 530 copy contamination in the 2002R hero text.
- Kept only 2002R adaptations: handle, class `lk-goc-coll-preview--2002r`, copy, alt labels and images.

## Verification
- PR remains open and mergeable.
- Branch pushed to GitHub.
- No Shopify Admin API write performed.
