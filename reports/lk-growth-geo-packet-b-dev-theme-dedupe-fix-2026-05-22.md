# LK Growth GEO Packet B — Dev Theme Dedupe Fix

Data: 2026-05-22
Área: LK Sneakers / Growth / Shopify Theme / GEO
Theme: `155065450718` (`lk-new-theme/dev`, draft)
Asset: `sections/lk-collection.liquid`

## Motivo

Lucas identificou no preview mobile que o Packet B adicionava uma camada de FAQ visual redundante junto à seção de FAQ já existente da collection.

## Correção aplicada

- Removido do Packet B o bloco visual `.lk-geo-p1__faq`.
- Mantido o bloco editorial `Guia LK` (`.lk-geo-p1`) para GEO/AI Search.
- Mantido o `FAQPage` JSON-LD apenas como fallback quando a página não tiver FAQ nativo (`unless has_faq`), evitando schema duplicado quando a seção existente já gera `FAQPage`.
- Nenhuma alteração em produção.

## Verificação

Readback Admin API:

- `before_sha256`: `61136fe92f7c6ce58daf787177144e0d3a243c3dfadb60eadb1454d52762f426`
- `after/readback_sha256`: `d8ecd20de34bfdfc59147e9bef5e9678a792350dc679d2bc3bff64412e9f36eb`
- `.lk-geo-p1__faq`: `0` no asset
- `unless has_faq`: presente

Browser/HTML verification nas 7 collections P1:

- `geoClassCount`: `1` em todas
- `geoFaqClassCount`: `0` em todas
- `geoFaqTitleCount`: `0` em todas
- `FAQPage` JSON-LD: `1` em todas
- `Guia LK`: presente em todas

## Collections verificadas

- `new-balance-204l`
- `onitsuka-tiger-todos-os-modelos`
- `onitsuka-tiger-mexico-66`
- `air-jordan-travis-scott`
- `adidas-samba-jane`
- `lululemon`
- `nike-mind-001`

## Rollback

Snapshot local:

`/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-geo-p1-dedupe-dev-theme-155065450718-20260522T172929Z`

Para rollback no dev theme, restaurar `sections.liquid.before` no asset `sections/lk-collection.liquid` do theme `155065450718`.

## Observação

A seção FAQ nativa/antiga das collections continua visível. O Packet B agora adiciona apenas o bloco `Guia LK` abaixo dela, sem uma segunda área de FAQ visual.
