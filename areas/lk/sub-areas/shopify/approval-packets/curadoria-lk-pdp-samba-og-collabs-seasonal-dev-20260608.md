# Approval packet — Curadoria LK PDP DEV Adidas Samba OG collabs/seasonal II (2026-06-08)

- values_printed: false
- status: aguardando aprovação explícita de Lucas
- operação proposta: **upload somente em DEV/unpublished theme**
- Production/theme main: **read-only / sem write**
- escopo: somente Curadoria PDP em tema DEV; sem produto, preço, estoque, coleção, app, checkout, ads, email, GMC, Tiny ou Klaviyo.

## Contexto

Após Samba OG especiais chegar em Production, Lucas disse `seguir`. A interpretação segura é continuar em read-only e preparar o próximo approval packet DEV, sem upload automático.

## Baseline read-only pós-Samba Production

Manutenção Curadoria LK PDP forçada/read-only:

- gerado: `2026-06-08 11:53 BRT`
- semáforo: verde `47` · amarelo `11` · vermelho `0` · cinza `3`
- handles públicos checados: `260`
- arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260608T115353-0300.md`
- nenhum write Shopify/DEV/Production executado.

Scan read-only do source Production atual:

- source commit: `8d39bf3`
- marker count: `56`
- covered handles: `754`

Principais famílias candidatas:

- `air-jordan-1-low`: sellable adult `111`, covered `36`, uncovered clean `75`, public-valid sample `6`
- `nike-dunk-low`: sellable adult `179`, covered `55`, uncovered clean `124`, public-valid sample `12`
- `adidas-samba-og`: sellable adult `52`, covered `32`, uncovered clean `20`, public-valid sample `12`

## Interpretação

Dunk Low e AJ1 Low têm mais volume, mas continuam amplos e misturados entre regular, SB, QS, collab, especiais e hype drops. Para reduzir risco semântico, o próximo batch recomendado é uma continuação controlada de **Adidas Samba OG collabs/seasonal**, aproveitando que a família já foi segmentada com sucesso e ainda tem `20` uncovered clean.

Este packet continua separado de:

- Samba OG regular;
- Wales Bonner Samba;
- Samba Jane;
- Sambae;
- Samba OG especiais / animal print / pony / seasonal já publicado no marker `top30-adidas-samba-og-specials-20260608`.

## Mudança DEV proposta

Criar split snippet no DEV:

- `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`

Adicionar uma única render line no main DEV ativo:

- `snippets/lk-variante-top30-visited-v2.liquid`
- `{%- render 'lk-variante-samba-og-collabs-seasonal-20260608', product: product -%}`

Marker proposto:

- `top30-adidas-samba-og-collabs-seasonal-20260608`

## Handles / labels propostos

- `tenis-adidas-samba-og-x-lionel-messi-triunfo-estelar-pack-branco` — Messi Triunfo
- `tenis-adidas-samba-og-x-dingyun-zhang-white-vapour-branco` — Dingyun White Vapour
- `tenis-adidas-samba-og-x-sporty-rich-usa-branco` — Sporty & Rich USA
- `tenis-adidas-samba-og-dia-de-muertos-pack-black-preto` — Día de Muertos Black
- `tenis-adidas-samba-og-dia-de-muertos-pack-off-white-branco` — Día de Muertos Off White
- `tenis-adidas-samba-og-x-naked-consortium-off-white-crystal-white-branco` — Naked Crystal White
- `tenis-adidas-samba-og-linen-green-metallic-verde` — Linen Green Metallic
- `tenis-adidas-samba-og-semi-blue-burst-azul` — Semi Blue Burst
- `tenis-adidas-samba-og-off-white-cyber-metallic-branco` — Cyber Metallic
- `tenis-adidas-samba-og-cloud-white-rose-tone-branco` — Cloud White Rose

## Static QA local do snippet proposto

- snippet SHA12: `95c389a16ce8`
- static QA: `true`
- errors: `[]`
- arrays:
  - handles: `10`
  - labels: `10`
  - images: `10`
  - titles: `10`
- simulação: `5` cards; produto atual excluído.

## Production source proof antes do DEV

Em `origin/production` pós-Samba:

- source commit: `8d39bf3`
- main SHA12: `1dd290044fd7`
- render line count para este novo snippet: `0`
- split snippet existe: `false`
- marker em source: `false`

## Risco

- Baixo/médio: é mesma silhouette e batch pequeno, mas mistura collabs e seasonal/colorways em um bloco separado.
- Mitigação: DEV-only primeiro; marker próprio; labels curtos; current product excluded; max 5 cards.
- Sem impacto em preço/estoque/produtos/collections.

## Rollback DEV

Se aplicado em DEV e precisar reverter:

1. Restaurar backup do main DEV antes do PUT.
2. Remover/zerar `snippets/lk-variante-samba-og-collabs-seasonal-20260608.liquid`.
3. Readback DEV para confirmar render line count `0` e marker ausente.

## Aprovação necessária

Para executar somente em DEV/unpublished theme:

`Aprovo DEV Curadoria Samba OG collabs seasonal`

Essa aprovação não autoriza Production/merge.
