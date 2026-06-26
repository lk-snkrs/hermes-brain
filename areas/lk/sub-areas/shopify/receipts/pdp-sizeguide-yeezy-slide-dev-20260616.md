# Receipt — PDP size guide Yeezy Slide DEV

Date: 2026-06-16
Owner: LK Shopify
Scope: Shopify DEV/unpublished theme only

## User approval / scope

Lucas pediu: “Fazer o 1”; contexto: corrigir o guia de tamanhos do Yeezy Slide para recomendar 1 tamanho inteiro acima.

Execução limitada a DEV/unpublished theme. Não houve alteração em Production/main, produto, preço, estoque, variante, metafield, GMC, Klaviyo, WhatsApp ou campanha.

## Target

- Theme: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verified before upload: `unpublished`
- Asset: `sections/lk-pdp.liquid`

## Change

Adicionada exceção específica para Yeezy Slide no modal de guia de tamanhos:

- Detecção: handle/title com `yeezy-slide` / `yeezy slide`
- Label no modal: `Yeezy Slide`
- Copy: `Yeezy Slide costuma vestir pequeno. Recomendamos comprar um tamanho inteiro acima do seu tamanho habitual.`
- Tabela: `Seu tamanho habitual` → `Comprar no Yeezy Slide`, com recomendação de +1 tamanho inteiro.

Controle preservado:

- Yeezy 350/Boost continua com recomendação de meio número acima.
- Jordan 1 Mid continua com recomendação de 1 tamanho acima.
- Vomero Premium continua com recomendação de tamanho habitual.

## Shopify readback

- DEV before SHA-12: `578d423d3f13`
- DEV target/readback SHA-12: `834b18e897f9`
- Readback matched local target: yes
- Production SHA-12 unchanged at verification: `7d223086fbc0`
- Production has Yeezy Slide fix: no
- `values_printed=false`

## QA

Public DEV preview checked on mobile viewport `390x844` via Chromium/CDP:

- `yeezy-slide-glow-green`: modal opens; label `Yeezy Slide`; copy +1 tamanho present; generic 350 copy absent; 0 Liquid errors; no horizontal overflow.
- `yeezy-350-v2-salt`: modal opens; generic Yeezy/Boost 350 copy present; Slide copy absent; 0 Liquid errors; no horizontal overflow.
- `air-jordan-1-mid-wolf-grey`: modal opens; Jordan Mid copy present; Slide copy absent; 0 Liquid errors; no horizontal overflow.
- `tenis-nike-vomero-premium-black-volt-preto`: modal opens; Vomero Premium copy present; Slide copy absent; 0 Liquid errors; no horizontal overflow.

Artifacts:

- Backup asset: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-dev-20260616/dev_before_sections__lk-pdp.liquid`
- Target asset: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-dev-20260616/dev_target_sections__lk-pdp.liquid`
- Readback asset: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-dev-20260616/dev_readback_sections__lk-pdp.liquid`
- QA JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-dev-20260616/assets/yeezy-slide-dev-qa-results.json`
- Screenshots: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/pdp-sizeguide-yeezy-slide-dev-20260616/assets/*.png`

## Rollback

DEV rollback: upload backup asset `dev_before_sections__lk-pdp.liquid` back to theme `155065450718`, key `sections/lk-pdp.liquid`, then read back SHA `578d423d3f13` and repeat the four PDP QA checks.

Production path if Lucas approves later: apply the same scoped change to Production/main theme only after explicit approval, then readback + public live QA + receipt.

## Status final

DEV corrigido e validado. Production intencionalmente não alterado.
