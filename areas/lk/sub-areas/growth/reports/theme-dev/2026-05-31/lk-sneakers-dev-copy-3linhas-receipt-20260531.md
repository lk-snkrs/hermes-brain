# LK Sneakers — ajuste Dev da copy da coleção Sneakers para intro rica (~3 linhas)

Data: 2026-05-31 17:27 UTC

## Escopo

Refinamento aplicado somente no tema Dev da Shopify para `/collections/sneakers`, seguindo feedback de Lucas: como o texto fica escondido atrás de “ver mais”, a introdução pode ser mais rica para SEO/GEO sem empurrar o grid de produtos.

## Tema/asset

- Dev Theme ID: `155065450718`
- Dev theme: `lk-new-theme/dev` / `unpublished`
- Production Theme ID: `155065417950`
- Asset: `sections/lk-collection.liquid`
- Preview: `https://www.lksneakers.com.br/collections/sneakers?preview_theme_id=155065450718`

## Copy aplicada no Dev

> Sneakers originais para diferentes estilos, marcas e momentos. Na LK, você encontra tênis Nike, Adidas, New Balance, Air Jordan, Onitsuka Tiger e outras referências do universo sneaker em uma vitrine ampla e fácil de navegar. Compare clássicos, lançamentos, pares premium e modelos para o dia a dia com atendimento humano para escolher tamanho, proposta de uso e melhor caminho de compra.

## Validação

Execução final: `20260531T172717Z`

- `dev_readback_matches_target`: true
- `prod_unchanged`: true
- `forbidden_sneakers_copy_in_dev_readback`: false
- `dev_readback_panel_after_paginate`: true
- Preview público não autenticado retornou status 200 e sem erro Liquid, mas não mostrou markers Dev por limitação/cache do preview. Readback Asset API é a evidência autoritativa do Dev.

## SHA / receipt técnico

- `dev_before_sha256`: `b46ffb287835a0fd14bc7e1a960269c39c81a7e5733fb3a252abe6ce6c974ad1`
- `dev_target_sha256`: `34e5c3fbd11909030dddb13993a928f6acf19a704275a407975cd1d01d4ac928`
- `dev_readback_sha256`: `34e5c3fbd11909030dddb13993a928f6acf19a704275a407975cd1d01d4ac928`
- `prod_before_sha256`: `7be7f692f7a484b116fcb2608f6c0e535032223fb3c8f7a4cfe66366bf4f5804`
- `prod_after_sha256`: `7be7f692f7a484b116fcb2608f6c0e535032223fb3c8f7a4cfe66366bf4f5804`
- Receipt técnico: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T172717Z/`

## Não-ações

- Nenhum write em Production.
- Nenhum write em produto, coleção admin, preço, estoque, disponibilidade, GMC, campanha ou cliente.

## Rollback

Para reverter o ajuste Dev, restaurar:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/sneakers-collection-dev-preview-20260531T172717Z/sections.lk-collection.dev.before.liquid`

no asset `sections/lk-collection.liquid` do tema Dev `155065450718`.
