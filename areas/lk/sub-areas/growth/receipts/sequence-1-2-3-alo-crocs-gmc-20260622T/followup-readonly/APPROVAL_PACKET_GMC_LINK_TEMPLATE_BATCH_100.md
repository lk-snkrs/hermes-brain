# Approval packet — GMC link_template next batch 100

- Criado UTC: 2026-06-22T17:45:59.425260+00:00
- Modo: approval prep/read-only; writes externos nesta etapa: 0.
- Base: micro-piloto 10 executado em 2026-06-22 com readback OK.
- values_printed=false.

## Resultado do micro-piloto 10

Readback follow-up:
- `linkTemplate` OK: 10/10.
- `mobileLinkTemplate` OK: 10/10.
- `adsRedirect` OK: 10/10.
- Issue `mhlsf_full_missing_valid_link_template`: 0/10.
- Read errors: 0.

Evidência:
- `gmc-micro-pilot-10-followup-readback.json`

## Anti-retrabalho

A amostra exclui, quando possível, links associados às páginas em quarentena operacional:
- Nike Mind/Vomero;
- Crocs PDP já trabalhado;
- Onda C1+C2;
- Onitsuka todos modelos.

O batch não altera páginas, SEO, tema, preço, estoque ou campanhas.

## Escopo proposto

Executar próximo lote controlado de **100 offers locais/LIA** com a mesma mutation já validada:

- Merchant API `productInputs.patch`.
- Campos:
  - `productAttributes.linkTemplate`
  - `productAttributes.mobileLinkTemplate`
  - `productAttributes.adsRedirect`
- Valor: link PDP + store code template.

## Preview dos primeiros 20 do lote 100

| Offer | Título | Link |
|---|---|---|
| `LIA_JI0324-6` | Tênis Adidas Gazelle Indoor Maroon Almost Yellow Marrom | https://lksneakers.com.br/products/tenis-adidas-gazelle-indoor-maroon-almost-yel |
| `LIA_OXV-2785246-39` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown Blue Marrom | https://lksneakers.com.br/products/tenis-onitsuka-tiger-x-versace-sakura-leather |
| `LIA_SLCRCVOW-1` | Camiseta Slyce Racquet Club Off White | https://lksneakers.com.br/products/camiseta-slyce-racquet-club-off-white |
| `LIA_f99715` | Tênis Adidas Yeezy Boost 350 V2 Sesame Cinza | https://lksneakers.com.br/products/tenis-adidas-yeezy-boost-350-v2-sesame-cinza |
| `LIA_ALD-2515934-L` | Camiseta Aimé Leon Dore Musician Graphic Preta | https://lksneakers.com.br/products/camiseta-aime-leon-dore-musician-graphic-pret |
| `LIA_w6289r_02-4` | Saia Alo Yoga Grand Slam Tennis Azul Marinho | https://lksneakers.com.br/products/saia-alo-yoga-grand-slam-tennis-azul-marinho |
| `LIA_ST19-2` | Calça Saint Studio Plissada Tech Preto | https://lksneakers.com.br/products/calca-saint-studio-plissada-tech-preto |
| `LIA_1183C529.200-1` | Tênis Onitsuka Tiger Tsunahiki Slip-On Birch/Indigo Navy Bege | https://lksneakers.com.br/products/tenis-onitsuka-tiger-tsunahiki-slip-on-birch- |
| `LIA_CT08561000-5` | Tênis Nike Dunk Low x Off-White Pine Green Verde | https://lksneakers.com.br/products/tenis-nike-dunk-low-x-off-white-pine-green-ve |
| `LIA_w9681r-15` | Top Alo Yoga Airlift Line Up | https://lksneakers.com.br/products/top-alo-yoga-airlift-line-up |
| `LIA_DM4044108-1` | Tênis Nike Cortez Forrest Gump 2024 Branco | https://lksneakers.com.br/products/tenis-nike-cortez-forrest-gump-2024-branco |
| `LIA_DX5930001-35` | Tênis Nike Dunk Low Phantom Metallic Gold Dourado | https://lksneakers.com.br/products/nike-dunk-low-phantom-metallic-gold |
| `LIA_DM0032005-43` | Tênis Air Max Plus Black University Blue Preto | https://lksneakers.com.br/products/air-max-plus-black-university-blue |
| `LIA_850055527140-2` | Rhode Pocket Blush | https://lksneakers.com.br/products/rhode-pocket-blush |
| `LIA_43774078387490` | Tênis Nike Air Jordan 4 Retro TEX 'Worn Blue Denim' Azul | https://lksneakers.com.br/products/tenis-nike-air-jordan-4-retro-tex-worn-blue-d |
| `LIA_w9681r-2` | Top Alo Yoga Airlift Line Up | https://lksneakers.com.br/products/top-alo-yoga-airlift-line-up |
| `LIA_11570118-15` | Calça Lululemon SmoothCover High-Rise Tight 25" | https://lksneakers.com.br/products/calca-lululemon-smoothcover-high-rise-tight-2 |
| `LIA_ID2054-5` | Tênis Adidas Samba Collegiate Green Verde | https://lksneakers.com.br/products/adidas-samba-collegiate-green |
| `LIA_HV5979130-3` | Tênis Nike Air Force 1 07 LE Year of Snake 2025 Branco | https://lksneakers.com.br/products/tenis-nike-air-force-1-07-le-year-of-snake-20 |
| `LIA_IB1519-200-11` | Tênis Nike Air Jordan 4 Retro OG SP Undefeated (2025) Verde | https://lksneakers.com.br/products/tenis-air-jordan-4-retro-og-sp-undefeated-202 |

Arquivo completo do preview 100:
- `gmc-next-batch-100-target-preview.json`

## Critérios de execução

1. Snapshot antes dos 100 ProductInputs.
2. URL checks dos 100 links.
3. Patch com retry controlado.
4. Readback imediato.
5. Readback atrasado 20–60s.
6. Receipt com contagem OK/falha/residual.

## Rollback

- Restaurar `linkTemplate`, `mobileLinkTemplate`, `adsRedirect` por ProductInput a partir do snapshot `before_products.json` do lote 100.
- Não mexer em Shopify.

## Risco

- Médio: mesmo caminho validado em 10/10, mas pode haver overwrite posterior por Simprosys/local feed.
- Mitigação: D+1 stickiness check antes de qualquer lote maior que 100.

## Aprovação necessária

Para executar o lote 100, Lucas precisa aprovar explicitamente:

> aprovado GMC lote 100 link_template
