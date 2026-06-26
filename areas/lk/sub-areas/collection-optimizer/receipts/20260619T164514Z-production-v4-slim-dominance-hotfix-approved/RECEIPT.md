# Receipt — Production v4 slim dominance hotfix

- Data UTC: 20260619T164514Z
- Aprovação Lucas: "Aprovo merge"
- DEV validado: 155065450718 / lk-new-theme/dev / role `unpublished`
- Production: 155065417950 / lk-new-theme/production / role `main`
- Asset: `assets/lk-collection-v2.css`
- Ação: append_hotfix_block; merge do hotfix v4 slim dominance validado no DEV.
- Não alterado: preço, estoque, produtos, campanhas, feed/GMC, copy de collection.
- Rollback: restaurar `production.assets-lk-collection-v2.before.css` no asset production.
- values_printed=false

## Readback

```json
{
  "values_printed": false,
  "approval": "Lucas: Aprovo merge",
  "dev_theme": {
    "id": "155065450718",
    "name": "lk-new-theme/dev",
    "role": "unpublished"
  },
  "prod_theme": {
    "id": "155065417950",
    "name": "lk-new-theme/production",
    "role": "main"
  },
  "asset_key": "assets/lk-collection-v2.css",
  "action": "append_hotfix_block",
  "before_bytes": 26391,
  "candidate_bytes": 30799,
  "after_bytes": 30799,
  "before_sha256": "9baa8579929430bd406a406ea522353dd4920c224fcfb1c14dd0e877ded5a7d5",
  "candidate_sha256": "81e4d1a9fdb31d6495589388b15624df6e9dcdfe3ff280b14504058370fea72a",
  "after_sha256": "81e4d1a9fdb31d6495589388b15624df6e9dcdfe3ff280b14504058370fea72a",
  "readback_equals_candidate": true,
  "has_marker_after": true,
  "has_grid_none_after": true,
  "has_resumo_light_after": true,
  "receipt_dir": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/receipts/20260619T164514Z-production-v4-slim-dominance-hotfix-approved"
}
```
