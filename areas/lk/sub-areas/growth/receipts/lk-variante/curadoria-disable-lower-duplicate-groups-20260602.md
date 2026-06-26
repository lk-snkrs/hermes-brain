# Receipt — Curadoria LK lower duplicate groups disabled — 2026-06-02

## Veredito
Segunda passada concluída. Além de impedir duplicidade visual, os 13 grupos inferiores/duplicados foram desativados por inteiro. Agora fica apenas a versão de cima/correta quando há família já coberta.

## Asset
`snippets/lk-variante-top30-visited.liquid`

## Themes
- Production: `lk-new-theme/production`, role `main`, ID `155065417950`
- Dev: `lk-new-theme/dev`, role `unpublished`, ID `155065450718`

## Marcadores inferiores desativados
- `top30-onitsuka-mexico66-regular`
- `top30-new-balance-9060`
- `top30-adidas-gazelle-active-regular`
- `top30-adidas-handball-spezial-regular`
- `top30-adidas-sl-72-regular`
- `top30-new-balance-530-regular`
- `top30-new-balance-204l-regular`
- `top30-onitsuka-mexico-66-sabot-regular`
- `top30-adidas-taekwondo-regular`
- `top30-alo-airlift-line`
- `top30-adidas-samba-jane-regular`
- `top30-alo-airbrush-line`
- `top30-air-jordan-1-low-regular`

## Readback
- Antes da segunda passada: `7320d9005f03`
- Depois/target final: `a62a0ba774c3`
- Production final readback: `a62a0ba774c3`
- Production matches target: `True`
- Dev readback: `a62a0ba774c3` / matches target `True`

## QA
Amostras pós-correção:
- NB 530 Arid Stone: 1 bloco `top30-nb-530`; labels corretos `Turtledove`, `White Indigo`, `Silver Cream`, `Silver White`, `Steel Grey`.
- NB 530 Sea Salt: 0 bloco inferior; grupo duplicado desativado.
- NB 9060: 1 bloco `top30-nb-9060`.
- Handball Spezial: 1 bloco `top30-adidas-handball-spezial`.
- Samba Jane: 1 bloco `samba-jane`.
- AJ1 Low: 1 bloco `air-jordan-1-low`.
- Alo Airlift/Airbrush amostras: sem bloco inferior duplicado.
- Zero Liquid error nas amostras.

## GitHub
- Repo: `lk-snkrs/lk-new-theme`
- Branch: `production`
- Status: `Repo production already matches final lower-duplicate disable readback`
- Repo SHA: `a62a0ba774c3`
- Target SHA: `a62a0ba774c3`

## Rollback
Backups da segunda passada:
- Production: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/disable-lower-duplicate-groups/production-before.liquid`
- Dev: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/disable-lower-duplicate-groups/dev-before.liquid`

Backup da primeira passada também preservado em:
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/fix-apply/production-before.liquid`

## Não alterado
Não foram alterados produtos, preços, estoque, checkout, apps, GMC/feed, Klaviyo, Meta, Tiny, campanhas ou menus.

## Artefatos
- Audit fonte: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/second-pass-source-audit/second-pass-source-audit.json`
- Apply final: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/disable-lower-duplicate-groups/disable-lower-result.json`
- Production readback retry: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/disable-lower-duplicate-groups/production-readback-retry.json`
- GitHub sync: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/duplicate-audit-20260602T194656Z/disable-lower-duplicate-groups/github-sync-final-result.json`
