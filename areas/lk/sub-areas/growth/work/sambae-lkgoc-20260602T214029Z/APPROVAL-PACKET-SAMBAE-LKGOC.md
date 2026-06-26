# Approval Packet — LKGOC Full Adidas Sambae

Data UTC: 2026-06-02T21:49:46Z

## Decisão pedida
Aprovar continuidade em DEV para resolver o preview render e, depois, autorizar publicação production em escopo separado.

**Não publiquei produção.**

## Link direto do preview
- Storefront preview: https://lk-sneakerss.myshopify.com/collections/adidas-sambae?preview_theme_id=155065450718
- Theme editor preview: https://admin.shopify.com/store/lk-sneakerss/themes/155065450718/editor?previewPath=/collections/adidas-sambae

## O que foi aplicado no Shopify DEV
Tema: `155065450718` — `lk-new-theme/dev`.

Assets criados:
- `snippets/lk-sambae-lkgoc-hero.liquid`
- `snippets/lk-sambae-lkgoc-guide.liquid`

Asset alterado em DEV:
- `sections/lk-collection.liquid`

Readback DEV:
- Hero render count na section: `1`
- Guide render count na section: `1`
- Section bytes: `254155`
- Abaixo de 256 KB: `True`
- Produtos na coleção: `12`

## QA HTML / Preview
- Section Rendering API e full page público retornaram `hero=0` e `guide=0` mesmo com readback DEV correto.
- Interpretação: o preview público/fetch está ignorando o tema DEV ou precisa de cookie/login. O tema está `previewable: true`.
- Screenshots gerados por Chromium:
  - Desktop: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/sambae-lkgoc-20260602T214029Z/sambae-dev-preview-desktop.png`
  - Mobile: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/sambae-lkgoc-20260602T214029Z/sambae-dev-preview-mobile.png`

## Score LKGOC
**81/100**

Motivo do score não ser >90: GSC/Ahrefs indisponíveis e QA visual do preview DEV não confirmado pelo storefront público.

## Evidências resumidas
- Search volume BR: `adidas sambae` 246k; `adidas sambae feminino` 60.5k; `sambae adidas` 74k.
- Intent: mistura transacional + informacional; página precisa vender, comparar e responder dúvidas.
- WWD: Sambae = versão premium do Samba, couro macio, plataforma gum, estética quiet luxury; ressalva para pés largos/suporte.
- Nayla Smith: review com conforto, plataforma translúcida, styling e atenção a tamanho.
- SERP BR mistura Samba OG/marketplaces; oportunidade para página LK específica e mais citável.

## Limitações
- GSC/Ahrefs não conectados.
- Adidas oficial e People tiveram fetch bloqueado/robots; usei snippets DataForSEO e fontes acessíveis.
- Não criei página Shopify pública `/pages/guia-adidas-sambae` para não fazer write customer-facing sem aprovação.
- Não alterei title/meta/collection body em produção.

## Rollback DEV
- Restaurar `dev-section.before.liquid` para `sections/lk-collection.liquid` no tema DEV.
- Remover snippets `lk-sambae-lkgoc-hero` e `lk-sambae-lkgoc-guide` se necessário.

## Próxima aprovação possível
1. Aprovar correção do roteamento/preview DEV até o storefront mostrar os blocos.
2. Depois de QA visual aprovado, aprovar publicação production com rollback escopado.
