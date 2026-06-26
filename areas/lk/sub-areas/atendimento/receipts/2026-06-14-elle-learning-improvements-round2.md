# Receipt — Elle learning improvements round 2

Timestamp: 2026-06-14T23:13:03+00:00
Profile: lk-ops
Scope: LK Elle / Chatwoot production deterministic customer-reply improvements based on Lucas's supervised learning loop.

## Production actions
- VPS: `72.60.150.124`
- App path: `/opt/elle-chatwoot`
- Backup created before changes: `/root/elle-rollbacks/elle-learning-improvements-20260614-230412/`
- File edited: `/opt/elle-chatwoot/app.py`
- Deploy command: `docker compose up -d --no-deps --build --force-recreate elle-chatwoot`

## Implemented improvements
1. Guide/tabela de tamanhos or site page not opening:
   - deterministic `product_clear` reply;
   - acknowledges page/guide issue;
   - asks model + usual size for general guidance;
   - avoids inventing measures/stock.
2. Address/complement edit after purchase:
   - deterministic `human_handoff`;
   - transfers to Larissa;
   - asks for order number if available;
   - does not promise that change is still possible.
3. WhatsApp/channel complaint/no answer:
   - deterministic acknowledgement;
   - transfers to Larissa with atendimento hours;
   - no defensive copy.
4. Mixed catalog + physical-store question:
   - splits the answer;
   - gives safe site/catalog direction;
   - hands off store/retirada/pronta-entrega part to Larissa/lk-stock boundary.
5. Product URL + numeric size question:
   - deterministic product/checkout guidance;
   - prevents product URLs from being misclassified as home/site or originality.
6. Home/site detection tightened:
   - removed broad `lksneakers.com.br/` term from generic home detector;
   - root/home still handled, product URLs no longer treated as home by substring.
7. AI prompt guardrails updated for guide-size, address edit, channel complaint, and mixed catalog/store cases.

## Verification evidence
- `python3 -m py_compile app.py elle_observer_summary.py`: OK.
- Container rebuilt and recreated successfully.
- Synthetic deterministic tests inside live container with `AI_ENABLED=False`:
  - `guide_size`: `category=product_clear`, `handoff=false`.
  - `address`: `category=human_handoff`, `handoff=true`, `blocked=[address_edit_needs_larissa]`.
  - `channel`: `category=human_handoff`, `handoff=true`, `blocked=[channel_complaint_needs_larissa]`.
  - `mixed`: `category=stock_handoff`, `handoff=true`, includes safe site/catalog guidance + Larissa transfer.
  - `cart`: `category=product_clear`, `handoff=false`.
  - `home`: `category=product_clear`, `handoff=false`.
  - `product_page`: `category=product_clear`, `handoff=false`.
  - `product_size`: `category=product_clear`, `handoff=false`.
  - `order`: asks for order number, no originality copy.
  - `sensitive`: `category=human_handoff`, `handoff=true`.
- External health `https://elle.lkskrs.online/healthz`: `ok=true`, `dry_run=false`, `write_enabled=true`, `kill_switch=false`, `public_reply_enabled=true`, `ai_enabled=true`, `ai_provider=openrouter`, `observer_enabled=true`.

## Guardrails preserved
- No stock/pronta-entrega/physical-store availability promise added.
- No price, reservation, delivery deadline, refund decision, exchange decision, or compensation promise added.
- Handoff wording remains Larissa-facing to customer; internal assignee remains separate.
- No secrets printed or stored.

## Follow-up ideas for Lucas approval/observation
- Learn official safe answer for store hours and basic exchange policy if Lucas wants Elle to answer those without handoff.
- Add product-fit micro-guides only for models Lucas approves (e.g. New Balance 204L) and keep uncertain fits as questions/handoff.
- Add a stricter first-message vs later-message intro rule so Elle does not over-repeat the long IA intro in a continuing conversation.
- Add observer report bucket for `mixed_catalog_store` so reports show split answers instead of generic stock handoff.
- Add safe handling for image-only product identification: ask for model/link/readable screenshot, do not guess from photo.
