# QA pós-change — PDP Guia de Tamanhos

Date: 2026-06-16
Owner: LK Shopify
Mode: read-only public storefront QA
Viewport: mobile `390x844`

## Escopo

Lucas pediu: “Fazer o 1, depois o 2”. Este relatório documenta o item 1: QA pós-change da correção do guia de tamanhos do Yeezy Slide em Production.

Não houve write Shopify, produto, preço, estoque, coleção, metafield, campanha, e-mail, WhatsApp ou checkout.

## Evidência bruta

- Script: `/tmp/lkqa-cdp/sizeguide_post_change_scan.js`
- Retry script seletivo: `/tmp/lkqa-cdp/sizeguide_post_change_retry.js`
- JSON principal: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/sizeguide-post-change-20260616/sizeguide-post-change-results.json`
- JSON retry: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/sizeguide-post-change-20260616/sizeguide-post-change-retry-results.json`
- Screenshots: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/sizeguide-post-change-20260616/*.png`

## Resultado

### Primeira varredura

- PDPs testados: 13
- OK direto: 10
- Falhas aparentes: 3

As 3 falhas aparentes foram reclassificadas após retry seletivo: o seletor amplo clicou o link do footer `Guia de Tamanhos` em vez do botão PDP `.pi-size-guide` em alguns casos. O retry usou seletor específico do PDP e os controles passaram.

### Retry seletivo

- `tenis-air-jordan-1-low-lucky-green-verde`: OK
- `tenis-nike-vomero-premium-black-volt-preto`: OK
- `tenis-nike-mind-002-sail-bege`: OK

## Cobertura validada

- Yeezy Slide:
  - `yeezy-slide-pure-2022`: OK
  - `yeezy-slide-onyx`: OK
  - `yeezy-slide-glow-green`: OK
  - Modal abriu com `aria-hidden=false`.
  - Copy `Yeezy Slide costuma vestir pequeno... um tamanho inteiro acima` presente.
  - Copy genérica `Yeezy, especialmente Boost 350 V2... meio número` ausente.

- Yeezy 350:
  - `tenis-adidas-yeezy-boost-350-v2-zyon-marrom`: OK
  - `yeezy-350-v2-carbon-beluga`: OK
  - Copy genérica de Yeezy 350/meia numeração preservada.
  - Copy do Yeezy Slide ausente.

- Jordan:
  - `tenis-air-jordan-1-low-lucky-green-verde`: OK — Jordan 1 Low TTS/habitual.
  - `air-jordan-1-mid-carbon-fiber`: OK — Jordan 1 Mid +1 tamanho.
  - `air-jordan-1-high-seafoam`: OK — Jordan 1 High +1 tamanho.

- Nike:
  - `tenis-nike-vomero-premium-black-volt-preto`: OK — Vomero Premium tamanho habitual.
  - `slide-nike-mind-001-black-chrome-preto`: OK — Mind 001 próximo tamanho Nike acima.
  - `tenis-nike-mind-002-sail-bege`: OK — Mind 002 tamanho habitual.

- Outros controles:
  - `tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`: OK.
  - `tenis-adidas-samba-og-earth-strata-wonder-white-marrom`: OK.

## Invariantes técnicos

Na amostra validada:

- `Liquid error`: 0
- Overflow horizontal mobile: 0
- Modal abriu no botão PDP `.pi-size-guide`
- Production segue com correção do Yeezy Slide aplicada
- Nenhum vazamento da copy de Slide para Yeezy 350/Jordan/Vomero/Mind/Onitsuka/Adidas genérico

## Achados secundários

- Em algumas copies aparece falta de espaço visual: `normal.Recomendamos` nos blocos Vomero Premium e Mind 002. Não é regressão crítica, mas é um refinamento P3/P2 de acabamento de copy.
- O primeiro script tinha seletor amplo demais e clicava o link de footer em algumas PDPs. O retry corrigiu a metodologia usando `.pi-size-guide`.

## Veredito

A correção do Yeezy Slide está estável no live e não apresentou efeito colateral na amostra de guias especiais/controladas.
