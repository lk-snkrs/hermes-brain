# Elle Brain v2 shadow report

Generated UTC: 2026-06-26T18:39:31.717519+00:00
Mode: local/shadow only; no customer writes; values_printed=false

## Summary

- Events tail read: 10000
- Processed rows evaluated: 157
- Category diffs vs legacy: 57
- Handoff diffs vs legacy: 44
- External writes: 0
- Mode: live_openrouter
- Live OpenRouter classify-only used: 100
- Live OpenRouter non-valid/error: 1

## V2 categories

- product_clear: 59
- human_handoff: 45
- stock_handoff: 24
- greeting: 20
- coupon: 5
- institutional: 4

## V2 policy actions

- allow: 78
- handoff: 64
- rewrite: 8
- clarify: 7

## V2 parse status

- valid_json: 99
- not_consulted: 57
- invalid_json_or_empty: 1

## V2 providers

- openrouter: 100
- None: 57

## Response diagnostics (sanitized)

### finish_reason
- stop: 96
- length: 4

### content_len_bucket
- 101-500: 79
- 501+: 19
- 0: 1
- 21-100: 1

### parse_failure
- none: 99
- json_parse_none: 1

### error_class
- : 100

### attempt
- 1: 99
- 2: 1


## Policy IDs

- P-BROWSE-001: 28
- P-STOCK-001: 22
- P-POSTSALE-001: 21
- P-HUMAN-001: 18
- P-PHOTO-001: 6
- P-COUPON-001: 4
- P-AUTH-001: 4
- P-DELIVERY-001: 3
- P-FIT-001: 3
- P-UNKNOWN-PRODUCT-001: 1

## Sample (sanitized IDs only)

- conv=2230 msg=51577 legacy=product_clear/False v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=2230 msg=51580 legacy=product_clear/False v2=coupon/False action=rewrite ids=P-COUPON-001
- conv=2230 msg=51583 legacy=human_handoff/True v2=product_clear/False action=clarify ids=P-PHOTO-001
- conv=2233 msg=51606 legacy=product_clear/False v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=2233 msg=51611 legacy=product_clear/False v2=stock_handoff/True action=allow ids=
- conv=2233 msg=51614 legacy=greeting/False v2=greeting/False action=allow ids=
- conv=1469 msg=28457 legacy=human_handoff/True v2=human_handoff/True action=handoff ids=P-POSTSALE-001
- conv=2234 msg=51628 legacy=human_handoff/True v2=product_clear/False action=allow ids=
- conv=2236 msg=51642 legacy=greeting/False v2=greeting/False action=allow ids=
- conv=2236 msg=51643 legacy=product_clear/False v2=product_clear/False action=allow ids=
- conv=2236 msg=51652 legacy=product_clear/False v2=product_clear/False action=allow ids=
- conv=2236 msg=51654 legacy=human_handoff/True v2=greeting/False action=allow ids=
- conv=1639 msg=31634 legacy=stock_handoff/True v2=product_clear/False action=allow ids=P-BROWSE-001
- conv=2239 msg=51683 legacy=product_clear/False v2=stock_handoff/True action=handoff ids=P-STOCK-001
- conv=2239 msg=51688 legacy=product_clear/False v2=product_clear/False action=allow ids=
