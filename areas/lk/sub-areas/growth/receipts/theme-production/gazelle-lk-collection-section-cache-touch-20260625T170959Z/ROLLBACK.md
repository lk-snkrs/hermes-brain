# Rollback — Gazelle canonical section cache-touch — 2026-06-25

Scope executed:
- Theme: `lk-new-theme/production` / MAIN
- Theme ID: `155065417950`
- Asset: `sections/lk-collection.liquid`

Action was intended as cache-touch only: re-write identical content.

To rollback, restore:
- `sections__lk-collection.before.liquid`

to the same asset key. Since readback confirmed identical content, rollback should be a no-op unless future edits happen.

No SEO title/meta, collection description, products, price, stock, ordering, GMC, campaigns, Klaviyo or checkout were changed.
