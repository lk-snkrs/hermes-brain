# Receipt DEV — Adidas Gazelle condition hardening — 2026-06-25

Approval: Lucas approved dev/preview hardening only.

## Executed

Dev theme write only:
- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Asset: `snippets/lk-goc-guide-contract.liquid`

Changed only the Gazelle condition from handle-only to handle/id/title hardening:
- handle `adidas-gazelle`
- handle `adidas-gazelle-feminino`
- collection id contains `428761874654`
- title contains `adidas gazelle`

Production was read-only and not changed.

## QA

- Dev asset readback matched target.
- Dev canonical preview `/collections/adidas-gazelle?preview_theme_id=155065450718`: guide present; FAQPage 1; no Liquid error.
- Dev `/collections/adidas-gazelle-feminino?preview_theme_id=155065450718`: guide present; FAQPage 1; no Liquid error.
- Production canonical Gazelle remained untouched/old.
- Regression: Campus, SL72, NB530 preview routes OK.

## Interpretation

The hardening works in dev preview. It does not by itself prove production canonical will resolve, because prior production canonical issue may be template/cache/route behavior. However, this is the safest production candidate if Lucas wants the next controlled production write.

## Production approval text

`Aprovo publicar em produção o hardening da condição Gazelle conforme preview dev 155065450718, limitado ao asset snippets/lk-goc-guide-contract.liquid, mantendo o bloco restrito à coleção Adidas Gazelle por handle/id/title, sem alterar SEO title/meta, descrição da coleção, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, preservando Campus e SL72, com rollback e readback público.`
