# Receipt — Production v4 slim dominance inline fallback

- Data UTC: 20260619T164734Z
- Aprovação Lucas: "Aprovo merge"
- Theme: 155065417950 / lk-new-theme/production / role `main`
- Asset: `layout/theme.liquid`
- Ação: inserir style fallback v4 slim dominance antes de `</body>` para vencer CSS inline antigo/cacheado.
- Rollback: restaurar `layout-theme.before.liquid`.
- values_printed=false

## Readback

```json
{
  "values_printed": false,
  "approval": "Lucas: Aprovo merge",
  "theme": {
    "id": "155065417950",
    "name": "lk-new-theme/production",
    "role": "main"
  },
  "asset_key": "layout/theme.liquid",
  "before_bytes": 101199,
  "after_bytes": 105207,
  "before_sha256": "812457341aef2527a0870927687b0ee3397e3f90bb805d1095bdc3db85c70962",
  "after_sha256": "90cbe81b4561e1141e547fda7439e68bbc98e4ab083bd07ece36d8b6c1a9764f",
  "has_style_id_after": true,
  "readback_equals_candidate": true,
  "receipt_dir": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260619T164734Z-production-v4-slim-dominance-inline-fallback-approved"
}
```
