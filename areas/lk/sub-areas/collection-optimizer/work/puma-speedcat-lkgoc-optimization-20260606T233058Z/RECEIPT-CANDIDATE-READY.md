# LKGOC Puma Speedcat — Build Candidate Ready

Timestamp: 20260606T234309Z
Status: **CANDIDATE_READY / SHOPIFY_APPLY_BLOCKED_NO_TOKEN_IN_SHELL**

## Feito
- PRD/Contract criado.
- Evidence SERP/editorial criado.
- Candidate Liquid criado para:
  - `sections/lk-collection.liquid`
  - `snippets/lk-goc-collection.liquid`
- Script de apply DEV-only criado.

## QA local do candidate
Ver: `LOCAL-CANDIDATE-QA.json`

Gates locais:
- Hero Puma render antes do loop de produtos: PASS.
- Guia Puma render depois do loop de produtos: PASS.
- Guia antes do filter overlay: PASS.
- Branch antigo phase1 visível desativado: PASS.
- Snippet tem branch Puma hero + guide: PASS.

## Bloqueio atual
O shell atual não possui:
- `SHOPIFY_STORE_URL` ou `SHOPIFY_STORE`
- `SHOPIFY_ACCESS_TOKEN` / `SHOPIFY_ADMIN_TOKEN` / `SHOPIFY_API_TOKEN`

Por isso não executei write Shopify agora.

## Apply seguro quando houver env
Rodar:

```bash
cd /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/puma-speedcat-lkgoc-optimization-20260606T233058Z
SHOPIFY_STORE=lk-sneakerss.myshopify.com SHOPIFY_ADMIN_TOKEN=*** ./apply-puma-speedcat-lkgoc-dev.py
```

O script aborta se o tema `155065450718` não retornar `role: unpublished`.

## Production
Não houve write em production. Production continua bloqueado até aprovação explícita do Lucas.
