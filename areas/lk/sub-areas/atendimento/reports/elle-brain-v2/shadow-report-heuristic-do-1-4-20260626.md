# Elle Brain v2 shadow report

Generated UTC: 2026-06-26T16:08:05.439200+00:00
Mode: local/shadow only; no customer writes; values_printed=false

## Summary

- Events tail read: 2000
- Processed rows evaluated: 36
- Category diffs vs legacy: 19
- Handoff diffs vs legacy: 14
- External writes: 0
- Mode: heuristic
- Live OpenRouter classify-only used: 0
- Live OpenRouter non-valid/error: 0

## V2 categories

- product_clear: 20
- human_handoff: 9
- stock_handoff: 3
- greeting: 3
- institutional: 1

## V2 policy actions

- allow: 17
- handoff: 12
- clarify: 6
- rewrite: 1

## V2 parse status

- not_consulted: 36

## V2 providers

- None: 36

## Policy IDs

- P-BROWSE-001: 9
- P-POSTSALE-001: 5
- P-PHOTO-001: 5
- P-HUMAN-001: 4
- P-STOCK-001: 3
- P-UNKNOWN-PRODUCT-001: 1
- P-FIT-001: 1
- P-AUTH-001: 1

## Sample (sanitized IDs only)

- conv=2328 msg=55902 legacy=human_handoff/True v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=2329 msg=55934 legacy=stock_handoff/True v2=stock_handoff/True action=handoff ids=P-STOCK-001
- conv=2315 msg=55894 legacy=human_handoff/True v2=human_handoff/True action=handoff ids=P-POSTSALE-001
- conv=2315 msg=55968 legacy=human_handoff/True v2=human_handoff/True action=handoff ids=P-HUMAN-001
- conv=2315 msg=55968 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2315 msg=55968 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2315 msg=56000 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2315 msg=56000 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2331 msg=56088 legacy=human_handoff/True v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=2332 msg=56108 legacy=human_handoff/True v2=human_handoff/True action=handoff ids=P-POSTSALE-001
- conv=1440 msg=56239 legacy=product_clear/False v2=product_clear/False action=clarify ids=P-UNKNOWN-PRODUCT-001
- conv=2335 msg=56262 legacy=human_handoff/True v2=human_handoff/True action=handoff ids=P-HUMAN-001
- conv=2315 msg=56409 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2341 msg=56509 legacy=human_handoff/True v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=1175 msg=56520 legacy=human_handoff/True v2=stock_handoff/True action=handoff ids=P-STOCK-001
