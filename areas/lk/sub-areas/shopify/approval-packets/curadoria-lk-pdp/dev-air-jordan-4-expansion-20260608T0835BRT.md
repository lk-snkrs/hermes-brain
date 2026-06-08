# Approval Packet — Curadoria LK PDP DEV Air Jordan 4 expansion (2026-06-08)

- values_printed: false
- tipo: read-only approval packet; **nenhum write Shopify executado**
- gatilho: Lucas disse `Perfeito seguir` após merge Production NB9060; por política, `seguir` continua em descoberta/read-only e não autoriza novo upload DEV/Production.
- próximo escopo recomendado: aplicar em DEV/unpublished um split snippet para Air Jordan 4 adulto.

## Contexto pós-NB9060

- Production NB9060 já mergeado via GitHub PR #36 e validado por Shopify readback.
- Receipt Production NB9060 commitado no Brain: commit local `a6747fc`.
- Fonte Production parseada localmente inclui snippets renderizados recursivos:
  - `lk-variante-top30-visited-v2`
  - `lk-variante-aj1-low-high-20260606`
  - `lk-variante-asics-gt2160-walesbonner-20260608`
  - `lk-variante-nb9060-expansion-20260608`
  - `lk-variante-cortez-speedcat-20260607`
  - `lk-variante-onitsuka-versace-gazelle-collabs-20260607`
- Marker NB9060 presente na fonte Production: `top30-new-balance-9060-expansion-20260608`.

## Scan read-only

Fonte base: `/opt/data/tmp/lk_curadoria_next_batch_broad_readonly_20260608.json`, reinterpretado após NB9060.

Principais oportunidades vistas:

- `nike-dunk-low`: 177 sellable adult, 122 uncovered clean — grande, mas semanticamente amplo demais para o próximo lote seguro sem segmentar SB/collabs/regular.
- `air-jordan-1-low`: 111 sellable adult, 75 uncovered clean — grande, mas mistura OG, Travis, Golf, SE/craft; melhor segmentar depois.
- `adidas-samba-og`: 52 sellable adult, 30 uncovered clean — boa oportunidade, mas precisa separar regular, collab, Wales Bonner/Liberty/pony hair.
- `air-jordan-4`: 35 sellable adult, 14 uncovered clean, 10 amostras públicas válidas — **melhor próximo lote controlado**.
- `new-balance-9060`: já foi expandido/mergeado neste ciclo; não repetir.

## Recomendação

Aplicar primeiro **Air Jordan 4 adulto — expansão controlada** em DEV/unpublished.

Motivos:

- Modelo/silhouette denso e comercial.
- Escopo menor que Dunk/AJ1/Samba, reduzindo risco de mistura semântica.
- 10/10 amostras públicas com `.js` HTTP 200 e `available: true`.
- 10/10 imagens com HEAD 200 e content-type de imagem.
- Pode usar split-snippet, mantendo o main abaixo do risco de limite Liquid.

## Produtos propostos para DEV

Proposta inicial com 9 produtos Air Jordan 4 adulto. Excluí `Air Jordan 4 RM x Nigel Sylvester Driveway Grey` do primeiro lote por ser variação RM, visualmente/semanticamente diferente do AJ4 Retro/OG/SP principal.

1. `tenis-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco`
   - label: `Nigel Brick`
   - title: `Tênis Nike Air Jordan 4 OG SP x Nigel Sylvester Brick After Brick Branco`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-air-jordan-4-og-sp-x-nigel-sylvester-brick-after-brick-branco-lk-iq8055-100-34-1975490.jpg?v=1779804614`
2. `tenis-jordan-4-retro-toro-bravo-2026-vermelho-1`
   - label: `Toro Bravo`
   - title: `Tênis Jordan 4 Retro Toro Bravo 2026 Vermelho`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-jordan-4-retro-toro-bravo-2026-vermelho-lk-fq8138-600-34-7549128.webp?v=1777383671`
3. `tenis-nike-sb-air-jordan-4-x-retro-sp-navy-branco`
   - label: `SB Navy`
   - title: `Tênis Nike SB Air Jordan 4 x Retro SP Navy Branco`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-sb-air-jordan-4-x-retro-sp-navy-branco-lk-dr5415-100-34-5549249.jpg?v=1772980991`
4. `tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho`
   - label: `Valentine Sierra`
   - title: `Tênis Nike Air Jordan 4 Retro Valentine's Day Sierra Red Vermelho`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-air-jordan-4-retro-valentines-day-sierra-red-vermelho-lk-hv0823-109-8728968.png?v=1770567133`
5. `tenis-travis-scott-air-jordan-4-retro-cactus-jack-nubuck-azul-6`
   - label: `Travis Cactus Jack`
   - title: `Tênis Nike Travis Scott Air Jordan 4 Retro Cactus Jack Azul`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-travis-scott-air-jordan-4-retro-cactus-jack-azul-lk-308497-406-7516724.jpg?v=1755209054`
6. `tenis-air-jordan-4-retro-og-sp-undefeated-2025-verde`
   - label: `Undefeated 2025`
   - title: `Tênis Nike Air Jordan 4 Retro OG SP Undefeated (2025) Verde`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-air-jordan-4-retro-og-sp-undefeated-2025-verde-lk-ib1519-200-1-3533093.png?v=1754521805`
7. `tenis-nike-air-jordan-4-retro-og-sp-brick-by-brick-camurca-firewood-orange`
   - label: `Brick By Brick`
   - title: `Tênis Nike Air Jordan 4 Retro OG SP Brick By Brick Camurça Firewood Vermelho`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-nike-air-jordan-4-retro-og-sp-brick-by-brick-camurca-firewood-vermelho-lk-8982111.jpg?v=1753555738`
8. `tenis-air-jordan-4-retro-red-cement-branco`
   - label: `Red Cement`
   - title: `Tênis Nike Air Jordan 4 Retro Red Cement Branco`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/files/tenis-air-jordan-4-retro-red-cement-branco-lk-sneakers-538330.jpg?v=1714517187`
9. `air-jordan-4-seafoam`
   - label: `Seafoam`
   - title: `Tênis Nike Air Jordan 4 Seafoam Branco/Verde`
   - image: `https://cdn.shopify.com/s/files/1/0621/8969/9294/products/tenis-air-jordan-4-seafoam-brancoverde-777713.jpg?v=1710449668`

## Preflight público feito

- Product `.js`: 10/10 HTTP 200 e `available: true` na amostra Air Jordan 4.
- Image HEAD: 10/10 HTTP 200 e content-type `image/jpeg` ou `image/png`.
- Produto excluído por decisão semântica, não por erro técnico:
  - `tenis-air-jordan-4-rm-x-nygel-sylvester-driveway-grey-cinza` — válido tecnicamente, mas é AJ4 RM.

## Plano de implementação se aprovado

Target proposto:

- Theme DEV/unpublished: confirmar no momento do apply, esperado `155065450718`.
- Main asset: `snippets/lk-variante-top30-visited-v2.liquid`.
- Split asset novo: `snippets/lk-variante-aj4-expansion-20260608.liquid`.
- Marker proposto: `top30-air-jordan-4-expansion-20260608`.
- Render line proposta: `{%- render 'lk-variante-aj4-expansion-20260608', product: product -%}`.

Técnica:

- split-snippet self-contained;
- section guard por `product.handle` membro;
- usar classes canônicas `lk-variante__head`, `lk-variante__rail`, `lk-variante__media`;
- renderizar até 5 alternativas, excluindo o produto atual;
- readback Admin Asset API após write;
- static QA de arrays/handles/URLs/card cap/current exclusion;
- preview público se o Shopify preservar `preview_theme_id`; se o preview cair no canonical/live, classificar como inconclusivo e usar readback como source truth.

## Riscos

- Mistura semântica baixa/moderada: todos são AJ4 adulto, mas há collabs/SP junto de colorways retro. Por isso o lote é controlado e exclui AJ4 RM.
- Edge/cache Shopify pode apresentar miss público inicial após write; não confundir com falha se readback/static QA passar.
- Main Curadoria está grande; manter split-snippet evita ultrapassar limite Liquid.

## Rollback DEV

Se aplicado em DEV e for necessário reverter:

1. Remover a render line AJ4 do main DEV.
2. Remover/zerar o split snippet `snippets/lk-variante-aj4-expansion-20260608.liquid`.
3. Readback Admin Asset API e confirmar render line count `0` e marker ausente.
4. Production permanece inalterado até aprovação separada de merge via GitHub.

## Próxima decisão necessária

Para executar somente em DEV/unpublished, responder:

`Aprovo DEV Curadoria Air Jordan 4 expansion`

Isso não autoriza Production. Production exigirá aprovação separada depois do readback DEV.
