# Receipt — mKFashion remove custom style DEV sync

- timestamp_utc: 2026-06-15T18:14:56Z
- classification: external-write
- owner_profile: lk-shopify
- user_approval: Lucas confirmou alinhar DEV após Production com "Sim exato".

## Scope

Sincronizar no theme DEV o mesmo estado já mergeado em Production para a remoção da camada LK de estilo do botão do Provador MK.

## Shopify target

- theme_id: 155065450718
- theme_name: lk-new-theme/dev
- theme_role: unpublished
- asset: layout/theme.liquid

## Write performed

- Uploaded only `layout/theme.liquid` to DEV theme.
- Source file: `/opt/data/worktrees/lk-new-theme-remove-mk-custom-20260615/layout/theme.liquid`
- backup_path: `/opt/data/backups/theme-dev/mk-remove-custom-style-20260615/1781547265__theme-155065450718__layout-theme.liquid`

## Verification

DEV Asset API readback:

- before_sha: eae1ba24717ab72a7b5bb712d30494b142a489ee2ef2b2fc8280462d66b643b1
- local_target_sha: e3716fd11aa813a10d60fc366067a3793e5f9db7ae01f72b26635d26d0944200
- dev_readback_sha: e3716fd11aa813a10d60fc366067a3793e5f9db7ae01f72b26635d26d0944200
- sha_matches_local_target: true
- sdk_present_v1: true
- anchor_present: true
- style_background_opacity_absent: true
- open_shadow_patch_absent: true
- tune_button_absent: true
- targeted_mk_width_override_absent: true
- values_printed: false

DEV preview HTML QA:

- preview_theme_id: 155065450718
- tested_path: /products/new-balance-530-white-natural-indigo-1
- home_status: 200
- pdp_status: 200
- cookie_count: 6
- sdk_present_v1: true
- anchor_present: true
- opacity_marker_absent: true
- open_shadow_patch_absent: true
- tune_button_absent: true
- values_printed: false

## Production state already completed

- PR: https://github.com/lk-snkrs/lk-new-theme/pull/77
- merge_commit: 4fc40a4ceb782038c014ad5fcf599ae11e68adbf
- Production theme_id: 155065417950
- Production asset_sha/readback: e3716fd11aa813a10d60fc366067a3793e5f9db7ae01f72b26635d26d0944200

## Non-actions

- No product, price, stock, collection, checkout, discount, Klaviyo, GMC, Meta, WhatsApp or email write.
- No Production theme direct Asset API write in this DEV sync step.
- No secrets printed; values_printed=false.

## Rollback

- DEV rollback: re-upload backup file from `backup_path` to theme `155065450718`, asset `layout/theme.liquid`.
- Production rollback: revert PR #77 / merge commit `4fc40a4ceb782038c014ad5fcf599ae11e68adbf`.
