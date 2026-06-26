# Approval packet — LK Stock OS — variant promotion after full live match

- Run ID: `20260618T175635Z`
- Input DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260618T175250Z.db`
- Output DB: `areas/lk/sub-areas/stock/data/lk_stock_os_current_variant_promotion_20260618T175635Z.db`
- Promoted exact variant rows: `0`
- Current local rows after promotion: `12591`
- Guardrails: Tiny write 0; Shopify write 0; writes externos 0; public availability 0.

## Nota

A verificação pós full-live mostrou que a DB `current_local_stock` ainda estava colapsada por alguns parent/base SKUs e não resolvia variantes como `850055527140-2` pela superfície estável. Esta promoção salva essas variantes exatas na superfície local consultável usando evidência `stock_observations` já existente. Continua exigindo reconfirmação Tiny/fonte viva para promessa pública de pronta entrega.
