# Receipt — PDP Product Suggestions v3 Production merge

- Data/hora: 2026-06-27T11:34:23Z
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou seguir merge Production após DEV Product Suggestions v3.
- Classificação: external-write
- Fontes usadas:
- DEV receipt `areas/lk/sub-areas/shopify/receipts/pdp-product-suggestions-v3-dev-family-fallback-20260627.md`; approval packet `areas/lk/sub-areas/shopify/approval-packets/pdp-product-suggestions-v3-dev-family-fallback-20260627.md`; GitHub PR #111; Shopify Production readback; public QA.
- O que foi feito:
- PR #111 criado e mergeado contra `production` com diff mínimo em `sections/lk-pdp.liquid`. Product Suggestions v3 promove fallback família `ald-hats`, strict cross-type block, Curadoria LK dedupe, marker `data-lk-related-v3="family-fallback-20260627"` e eligibility marker `pending_unknown`.
- Output/artefato:
- PR #111 MERGED: https://github.com/lk-snkrs/lk-new-theme/pull/111; merge commit `3ef578be9499335d8e1954f66e75fa590b586f5f`; GitHub production content SHA `335c0ccff633282f100c550427549c1c77bcf572`; Shopify Production Theme `155065417950` readback HTTP `200`, SHA12 `15f69b0befa2`, match target `true`; public QA HTTP `200`/Liquid errors `0` nos PDPs Saint George, AJ1 Panda, Onitsuka Mexico 66, NB9060 Quartz Grey e Vomero Premium; values_printed=false.
- Aprovação: Seguir merge
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge + Shopify Production theme sync/readback. Asset `sections/lk-pdp.liquid`. Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp/email.
- Riscos/bloqueios: Médio: JS client-side e fallback família; mitigado por diff mínimo, node --check, readback e QA público. Elegibilidade Stock permanece `pending_unknown`; sem promessa de disponibilidade.
- Rollback/mitigação: Reverter PR #111 / merge commit `3ef578be9499335d8e1954f66e75fa590b586f5f`; ou restaurar `/opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v3-20260627/prod-merge/prod_before_sections__lk-pdp.liquid` em `sections/lk-pdp.liquid` via PR.
- Próximos passos: Monitorar visualmente o PDP Saint George e aguardar `lk-stock` para contrato de elegibilidade antes de evoluir o score/eligibility além de `pending_unknown`.
- Onde foi documentado no Brain: Workdir `/opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v3-20260627/prod-merge`; receipt canônico neste arquivo.
- Source confidence: runtime-verificado

## Memory OS note

Receipt escrito no Brain canônico. O writer local voltou a apresentar comportamento de espelho profile-local em tentativa anterior; este receipt preserva os mesmos campos obrigatórios e foi registrado por hook local.
