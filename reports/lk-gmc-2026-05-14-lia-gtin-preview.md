# LK GMC local/LIA GTIN preview — 2026-05-14

Generated: `2026-05-14T18:01:01.752923+00:00`

## Summary
- local_lia_gtin_rows: `34`
- by_candidate_state: `{'candidate_same_style_sku': 33, 'candidate_title_search_fallback': 1}`
- candidate_writes_if_approved: `34`
- blocked_no_candidate: `0`

## Write route if approved
- Local/LIA rows are `source=api`, `channel=local`; Merchant API ProductInputs read returned 404 for sampled local rows.
- Recommended route is **not** ProductInputs v1. Use Content API full product-resource update/insert preserving the current local product and changing only `gtin`, with private rollback before every row.
- Pilot first; local inventory affects physical-store/local surfaces.

## Candidate examples
- `local:pt:BR:LIA_1203A655-100-7` → state `candidate_same_style_sku`; current `2100000381470`; recommended `197298534666`; style `1203A655-100`
- `local:pt:BR:LIA_43774078386380` → state `candidate_title_search_fallback`; current `2000020124746`; recommended `0194500868076`; style `43774078386380`
- `local:pt:BR:LIA_553558612-6` → state `candidate_same_style_sku`; current `2100000120253`; recommended `0195243825982`; style `553558-612`
- `local:pt:BR:LIA_553558612-7` → state `candidate_same_style_sku`; current `2100000062003`; recommended `0195243825982`; style `553558-612`
- `local:pt:BR:LIA_555088108-5` → state `candidate_same_style_sku`; current `2100000216932`; recommended `0195869260877`; style `555088-108`
- `local:pt:BR:LIA_AQ3692-004-3` → state `candidate_same_style_sku`; current `2409110001651`; recommended `1000005263508`; style `AQ3692-004`
- `local:pt:BR:LIA_AQ3692-004-5` → state `candidate_same_style_sku`; current `2409110001910`; recommended `1000005263508`; style `AQ3692-004`
- `local:pt:BR:LIA_CU9225100-4` → state `candidate_same_style_sku`; current `2100000084050`; recommended `0194274091199`; style `CU9225-100`
- `local:pt:BR:LIA_CZ0790-102-4` → state `candidate_same_style_sku`; current `3812919100071`; recommended `0197597025834`; style `CZ0790-102`
- `local:pt:BR:LIA_DD1503601-39` → state `candidate_same_style_sku`; current `2019990858933`; recommended `0196149208343`; style `DD1503-601`
- `local:pt:BR:LIA_DM7866200-6` → state `candidate_same_style_sku`; current `2460004274872`; recommended `0197599883388`; style `DM7866-200`
- `local:pt:BR:LIA_DM7866200-7` → state `candidate_same_style_sku`; current `2000281022133`; recommended `0197599883388`; style `DM7866-200`

## Não executado
- Merchant write
- Content API insert/update
- Shopify write
- Tiny write
- local inventory/POS changes
- feed fetch/upload
- campaign/message/send
