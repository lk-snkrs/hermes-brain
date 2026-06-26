# Shopify product tag correction — Adidas Samba/Jane SALE incident (2026-05-15)

## Trigger

Lucas corrected a bulk tag request mid-flight: the intended scope was **not** all Adidas Samba products, but only **Adidas Samba Jane** should carry the `SALE` tag. This is a Shopify write, but Lucas's correction/approval was explicit and urgent.

## Safe pattern for future narrow tag corrections

1. Treat tag edits as Shopify writes: use this only when Lucas explicitly approves the narrow target in chat.
2. Stop/inspect any background task if one exists before continuing. If no process is visible locally, proceed by reconciling live Shopify state directly.
3. Pull secrets via Doppler token/API if `doppler` CLI is unavailable; never print secret values.
4. Query products read-only first with Admin GraphQL, using broad search (`adidas samba`) but filter locally with conservative predicates.
5. Build and save a JSON backup before writes containing product id, title, handle, tags, status, vendor/product type, and timestamp.
6. Define target predicate explicitly:
   - Jane target: title/handle contains `adidas`, `samba`, and `jane`.
   - Non-target correction: Adidas Samba matches that do not contain `jane` must not retain `SALE`.
7. Use Admin GraphQL `tagsAdd` only for target products missing canonical `SALE`.
8. Use Admin GraphQL `tagsRemove` for every `SALE`-case-insensitive tag on non-target products.
9. Re-query Shopify and verify both sides:
   - every target has a `SALE` tag;
   - no non-target has a `SALE` tag;
   - report violations as blockers.
10. Save a report JSON with counts, changed products, verification result, backup path, and violations.

## Doppler API fallback when CLI is missing

If `/opt/data/hermes_bruno_ingest/hermes_doppler.sh` fails because `doppler` CLI is not installed, use the local token file and Doppler API download endpoint inside a Python process:

```python
import urllib.request, urllib.parse, pathlib, base64, json

token = pathlib.Path('/opt/data/hermes_bruno_ingest/.secrets/doppler_token').read_text().strip()
qs = urllib.parse.urlencode({'project': 'lc-keys', 'config': 'prd', 'format': 'json'})
req = urllib.request.Request('https://api.doppler.com/v3/configs/config/secrets/download?' + qs)
req.add_header('Authorization', 'Basic ' + base64.b64encode((token + ':').encode()).decode())
with urllib.request.urlopen(req, timeout=30) as resp:
    secrets = json.loads(resp.read().decode())
```

Do not print `secrets` or token values.

## Example audit paths from the incident

- Backup: `/opt/data/hermes_bruno_ingest/lk-new-theme/backups/shopify-product-tags/20260515-171006-adidas-samba-sale-tag-backup.json`
- Report: `/opt/data/hermes_bruno_ingest/lk-new-theme/backups/shopify-product-tags/20260515-171006-adidas-samba-sale-tag-report.json`

## Pitfalls

- A search for `adidas samba` returns non-Samba products due Shopify search broadness; always apply local predicates to title/handle/vendor/type.
- `Sambae`, `Samba OG`, `Samba LT`, collaborations, and other Samba variants are **not** `Samba Jane` unless `jane` appears in the title/handle.
- Do not call the theme QA complete just because a tag correction finished; keep unrelated task status separate.
