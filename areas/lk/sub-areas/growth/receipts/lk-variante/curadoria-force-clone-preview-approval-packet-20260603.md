# Curadoria LK — Force Clone Preview Approval Packet — 2026-06-03

## Escopo executado

Lucas aprovou criar clone não publicado e preparar preview forçado. Nenhum publish foi feito.

## Themes

- Production atual/main: `155065417950` — `lk-new-theme/production`
- Clone não publicado: `156623372510` — `LK Curadoria Force Fix Preview 2026-06-03`
- Estado confirmado: clone `unpublished`; Production atual continua `main`.

## O que mudou no clone

- Criado `snippets/lk-variante-force-20260603.liquid`
- Criado `assets/lk-variante-force-20260603.css`
- Criado `assets/lk-variante-force-20260603.js`
- Modificado `sections/lk-pdp.liquid` no clone para renderizar somente o novo snippet force.

## Readback do clone

- Retry de `sections/footer-group.json`: OK
- Retry de `sections/header-group.json`: OK
- Section force render count: `3`
- Old v2 render count: `0`
- Old render count: `0`
- Snippet marker: `True`
- CSS marker: `True`
- JS marker: `True`

## QA preview rodada 1 — 10/10

Pass geral: `True`

- Canonical NB 530: pass=True, group=`top30-nb-530`, labels=`Turtledove`, `Silver Cream`, `Silver White`, `Steel Grey`, `Silver Blue`
- AJ1 Mid: pass=True, group=`top30-air-jordan-1-mid-regular`, labels=`Wolf Grey`, `Panda`, `Electro Orange`, `Canyon Rust`, `Aqua Tint`
- AJ1 High: pass=True, group=`top30-air-jordan-1-high-regular`, labels=`Atmosphere`, `Lost & Found`, `Dark Mocha`, `Lucky Green`, `Next Chapter`
- Shox TL: pass=True, group=`top30-nike-shox-tl-regular`, labels=`Black Yellow`, `Blue Tint Orange`, `Orewood Brown`, `Pumice Maroon`, `Sunrise Gradient`
- Foam Runner: pass=True, group=`top30-yeezy-foam-runner-regular`, labels=`MX Cinder`, `MX Sand Grey`, `Onyx`, `Sand`, `Stone Sage`
- Adidas Tokyo: pass=True, group=`top30-adidas-tokyo-regular`, labels=`Core Black`, `White Floral`, `Black Floral`, `Pure Sulfur`, `Silver Metallic`
- Yeezy 350: pass=True, group=`top30-yeezy-350-regular`, labels=`Steel Grey`, `Zyon`, `Bone`, `Static 2023`, `Zebra`
- Alo Serenity: pass=True, group=`top30-alo-serenity-coverup-line`, labels=`Black`, `Bluestone`, `Ivory`, `Light Cocoa`, `Navy`
- Adidas Sambae: pass=True, group=`top30-adidas-sambae-regular`, labels=`KSENIA Black`, `Denim`, `Black Gold`, `White Gold`, `White Green`
- AJ1 Low OG Mocha control: pass=True, group=`None`, labels=

## QA preview rodada 2 — controles críticos

Pass geral rodada 2: `True`

- NB 530: group=`top30-nb-530`, labels=`Turtledove`, `Silver Cream`, `Silver White`, `Steel Grey`, `Silver Blue`
- AJ1 High: group=`top30-air-jordan-1-high-regular`, labels=`Atmosphere`, `Lost & Found`, `Dark Mocha`, `Lucky Green`, `Next Chapter`
- Shox TL: group=`top30-nike-shox-tl-regular`, labels=`Black Yellow`, `Blue Tint Orange`, `Orewood Brown`, `Pumice Maroon`, `Sunrise Gradient`
- Adidas Sambae: group=`top30-adidas-sambae-regular`, labels=`KSENIA Black`, `Denim`, `Black Gold`, `White Gold`, `White Green`

## Evidência

- Backup/create summary: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/clone-create-summary.json`
- Upload/readback force namespace: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/clone-force-namespace-readback.json`
- QA preview rodada 1: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/preview-qa/preview-qa-report.json`
- QA preview rodada 2: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/preview-qa/preview-qa-round2.json`
- HTMLs capturados: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/lk-variante/production-canonical-audit-20260602/option-b-preview/production-force-fix-20260603T001900Z/preview-qa`

## Interpretação

O preview do clone usa o novo namespace `lk-variante-force-20260603`, não usa mais `lk-variante-top30-visited-v2`, e exibiu labels curtos nos produtos afetados. Isso valida o caminho de correção forçada antes de qualquer alteração no storefront live.

## Risco do próximo passo

Publicar o clone é uma troca de tema live. Embora o clone tenha sido duplicado do Production atual e QA tenha passado nos PDPs, o publish afeta o storefront inteiro.

## Rollback

Se o publish for aprovado e houver regressão, rollback é republicar o tema anterior `155065417950` como main e rodar QA smoke em homepage, collection e PDPs.

## Próxima decisão requerida

Aprovação explícita para publicar o clone `156623372510` como tema principal/live.

Frase de aprovação sugerida:

`Aprovo publicar o clone 156623372510 como Production com rollback para 155065417950 se QA falhar.`
