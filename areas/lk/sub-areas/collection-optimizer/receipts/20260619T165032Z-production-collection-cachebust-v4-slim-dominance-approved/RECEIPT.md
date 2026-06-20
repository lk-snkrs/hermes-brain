# Receipt — Production collection cache-bust v4 slim dominance

- Data UTC: 20260619T165032Z
- Aprovação Lucas: "Aprovo merge"
- Ação: comentário HTML invisível nas descrições de 4 collections para invalidar cache de página.
- Texto visível: não alterado.
- Production theme/cache: suporte ao hotfix v4 slim dominance já aplicado.
- Rollback: restaurar `collections-before.json` ou remover marker `<!-- lk-goc-prod-cachebust-v4-slim-dominance-20260619T165032Z; visible_text_unchanged=true -->`.
- values_printed=false

## Results

```json
[
  {
    "handle": "adidas-handball-spezial",
    "status": "updated",
    "id": "gid://shopify/Collection/445699653854",
    "errors": [],
    "before_bytes": 9395,
    "after_bytes": 9490,
    "visible_text_unchanged": true
  },
  {
    "handle": "new-balance-1906l",
    "status": "updated",
    "id": "gid://shopify/Collection/456441135326",
    "errors": [],
    "before_bytes": 9276,
    "after_bytes": 9371,
    "visible_text_unchanged": true
  },
  {
    "handle": "alo-yoga-1",
    "status": "updated",
    "id": "gid://shopify/Collection/444271722718",
    "errors": [],
    "before_bytes": 9130,
    "after_bytes": 9225,
    "visible_text_unchanged": true
  },
  {
    "handle": "air-jordan-1-low",
    "status": "updated",
    "id": "gid://shopify/Collection/1126715654366",
    "errors": [],
    "before_bytes": 9331,
    "after_bytes": 9426,
    "visible_text_unchanged": true
  }
]
```
