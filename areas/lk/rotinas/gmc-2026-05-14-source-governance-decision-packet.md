# LK GMC source governance decision packet — 2026-05-14

Generated: `2026-05-14T21:48:29.196758+00:00`

Status: `decision_packet_ready_no_external_writes`

## Executive verdict

- Preço continua **amarelo/bloqueado**: o micro-piloto foi aceito por PATCH, mas 0/5 persistiu em readback Content API/Merchant v1.
- Não recomendo repetir bulk de preço enquanto o gerador/fonte upstream que reverte o input não for isolado.
- A pergunta `ProductInputs.get 404` foi esclarecida: na discovery pública da Merchant API `products_v1`, `productInputs` tem `insert`, `patch` e `delete`, mas **não tem método `get`**; portanto GET 404 nesse path não prova ausência de produto/input.
- Readback confiável para fechamento continua sendo `accounts.products.get` + `productstatuses` + evidência de settings/account.

## Evidence

- ProductInputs methods in discovery: `['delete', 'insert', 'patch']`
- Products methods in discovery: `['get', 'list']`
- Price pilot: selected `5`, execution `{'patched_price_only': 5}`, verify Content matches `0`, verify Merchant v1 matches `0`, status issues after `{'price_updated': 15}`.
- Automatic price updates effective: `True`
- Landing residual classification: `{'public_ok_status_lag_or_googlebot_specific': 1}`

## Fonte atual vs papel recomendado
- **Content API / ProductInputs DS 10636492695**
  - Papel alvo: online primary owner
  - Atributos/risco: price/title/link/image/category/GTIN/non-local attributes
  - Próxima ação: identify upstream generator/channel that rewrites stale price before any new write
- **AUTOFEED / crawl DS 10525577766**
  - Papel alvo: safety/discovery only or tightly constrained fallback
  - Atributos/risco: should not be treated as operational price owner
  - Próxima ação: do not disable yet; prepare UI/settings review packet before changing destinations/auto-update
- **Supplemental file DS 10646853947**
  - Papel alvo: non-critical enrichment only
  - Atributos/risco: color/age_group/gender/size; no price columns observed
  - Próxima ação: keep but review destinations/primary-vs-supplemental behavior in Merchant UI
- **Local/LIA DS 10636384718**
  - Papel alvo: local inventory/POS separate lane
  - Atributos/risco: local offers; keep separate from online price remediation
  - Próxima ação: no action now

## Decision options for next approved write/settings phase

1. **Recomendado — governança sem write primeiro.** Mapear no Merchant UI/export e no canal Shopify/Google quem regenera DS `10636492695`; manter auto-update ligado como rede de segurança; preparar só depois um micro-teste com rollback.
2. **Mais agressivo — limitar crawl/autofeed.** Só após packet com screenshots/export/rollback de settings; risco de perder a rede de segurança que hoje mantém servability unaffected.
3. **Não recomendado agora — novo bulk de preço.** Bloqueado porque PATCH aceito não persistiu; repetir só aumenta risco/ruído.

## Not performed
- Merchant write
- ProductInputs PATCH
- Content API write
- feed upload/fetch
- data source update/delete
- automatic item updates setting change
- Shopify/Tiny write
- campaign/message/send
