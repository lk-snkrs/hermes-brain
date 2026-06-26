# Elle official send persistence + delivery audit — 2026-06-16

Scope: Lucas asked to persist the official Chatwoot public-send hotpatch and confirm whether abandoned-cart and order-created messages were successfully sent from 2026-06-15 00:00 BRT through 2026-06-16 07:38 BRT.

## Persistence action

- Live container: `elle-chatwoot`.
- Compose metadata still points to `/opt/elle-chatwoot/docker-compose.yml` and working dir `/opt/elle-chatwoot`, but that source path is not visible in this profile filesystem.
- Verified live `/app/app.py` contains `send_official_chatwoot_public_reply`, `content_attributes.elle_generated=true`, and `official_channel=chatwoot_messages_api`.
- Verified pre-existing image `elle-chatwoot-elle-chatwoot` did not contain the helper, confirming the prior state was a live-container hotpatch.
- Created rollback tag for old image: `elle-chatwoot-elle-chatwoot:rollback-pre-official-send-20260616-1039`.
- Committed patched live container to immutable image: `elle-chatwoot-elle-chatwoot:official-send-persisted-20260616-1039`.
- Retagged local compose-referenced image `elle-chatwoot-elle-chatwoot:latest` to the committed patched image so a normal recreate without rebuild keeps the patch.
- Verification: persisted image `/app/app.py` SHA/content matches live patched app; `python -m py_compile` passed; live `/healthz` returned `ok=true`, `dry_run=false`, `public_reply_enabled=true`, `kill_switch=false`, `catalog_cache_present=true`.

Remaining caveat: source/compose reconciliation is not fully solved because `/opt/elle-chatwoot` is not visible here. A future `docker compose up --build` from a host where that source exists could still rebuild from older source if not patched there.

Rollback: retag `elle-chatwoot-elle-chatwoot:rollback-pre-official-send-20260616-1039` back to `elle-chatwoot-elle-chatwoot:latest` and recreate `elle-chatwoot` if needed.

## Delivery audit: 2026-06-15 00:00 BRT → 2026-06-16 07:38 BRT

Read-only source: Chatwoot Postgres `messages`, account 1, outgoing public WABA template rows. Status mapping used: `0=sent/accepted`, `1=delivered`, `2=read`, `3=failed`.

### Abandoned cart

Templates:
- `lk_checkout_abandonado_24h_v2`: 6 public sends, 4 delivered, 2 read, 0 failed.
- `lk_checkout_abandonado_30min_v2`: 5 public sends, 1 sent/accepted, 3 delivered, 1 read, 0 failed.

Conclusion:
- 11 public abandoned-cart sends total.
- 10 have confirmed delivery/read.
- 1 remains sent/accepted without final delivery/read callback at audit time.
- 0 failed.
- Today after 00:00 BRT: 1 abandoned-cart public send, delivered.

### Order-created / pedido feito

Templates:
- Original image/button template `lk_online_pedido_realizado_v1`: 32 failed, 0 successful; dominant error bucket observed: Meta `132012`, header format mismatch (`expected IMAGE, received UNKNOWN`).
- Fallback no-button template `lk_pedido_criado`: 14 public sends, 6 delivered, 7 read, 1 failed.

Conclusion:
- If counting the fallback now used for `pedido feito`: yes, 13 were successfully delivered/read from yesterday to audit time, with 1 failed.
- If counting the original `lk_online_pedido_realizado_v1`: no, it is still not healthy and failed in the audited window.
- Today after 00:00 BRT: no `pedido feito` public template sends observed.

No customer sends, retries, template changes, WhatsApp/Meta writes, Shopify/Tiny writes, or container restart were performed during this audit.

Sanitization: no phone, e-mail, customer name, order URL, token, or secret values stored here.
