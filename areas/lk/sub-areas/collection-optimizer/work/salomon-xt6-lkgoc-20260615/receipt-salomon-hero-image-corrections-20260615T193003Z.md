# Receipt — Salomon XT-6 hero image corrections

Data UTC: 20260615T193003Z

## Pedido Lucas
- Imagem 1 Hypebeast: alinhar pelo bottom, não pelo meio.
- Imagem 2 Hypebeast: alinhar pelo bottom, não pelo meio.
- Imagem 3 Vogue: trocar.

## Execução
Escopo pontual aplicado em:
- Production theme: `lk-new-theme/production` (`role: main`)
- DEV theme: `lk-new-theme/dev` (`role: unpublished`)
- Asset: `sections/lk-collection.liquid`

Mudanças:
- Imagem 1 `interview-1.jpg`: adicionado `style="object-position: center bottom;"`.
- Imagem 2 `interview-7.jpg`: adicionado `style="object-position: center bottom;"`.
- Imagem 3 removida: Vogue `NYFW_FW26_STREETSTYLE_DAY5_PHILOH_013.jpg`.
- Imagem 3 nova: Hypebeast `solomon-beau-beaus-cafe-teoni-atlantic-interview-5.jpg`.
- Legenda 3: `Hypebeast · editorial urbano`.

## Validação
URL pública validada:
https://lksneakers.com.br/collections/salomon-xt-6?view=salomon-xt6-golden

Checks por HTML público:
- img1 com bottom: PASS
- img2 com bottom: PASS
- img3 nova presente: PASS
- Vogue antiga ausente: PASS
- bloco guia antigo ausente: PASS

Checks de imagem CDN:
- Hypebeast 1: HTTP 200 image/jpeg
- Hypebeast 7: HTTP 200 image/jpeg
- Hypebeast 5: HTTP 200 image/jpeg

## Rollback
Arquivos rollback salvos na pasta do work package com prefixo:
`rollback-salomon-image-corrections-*-20260615T193003Z.liquid`
