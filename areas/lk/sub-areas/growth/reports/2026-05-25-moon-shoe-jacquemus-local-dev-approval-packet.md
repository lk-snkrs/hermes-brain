# Approval packet local/dev — Nike x Jacquemus Moon Shoe

Data: 2026-05-25  
Status: PREVIEW LOCAL/DEV — nada publicado em Shopify, GMC, ads, Klaviyo ou WhatsApp.

## Escopo aprovado por Lucas

Preparar preview local/dev da source page Nike Moon Shoe Jacquemus e do ajuste de FAQ/meta da coleção, sem publicar em produção e sem alterar preço, estoque, GMC, campanhas, Klaviyo ou WhatsApp.

## Artefatos criados

- Source page preview HTML interno: `areas/lk/sub-areas/growth/drafts/2026-05-25-nike-moon-shoe-jacquemus-source-page-preview.html`
- Source page body limpo para Shopify: `areas/lk/sub-areas/growth/drafts/2026-05-25-nike-moon-shoe-jacquemus-source-page-body-clean.html`
- Screenshot QA local: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_f914a078d9e0472cab17cd02e78b0ac5.png`
- Audit base: `areas/lk/sub-areas/growth/reports/2026-05-25-moon-shoe-jacquemus-seo-geo-audit.md`

## Proposta de source page

- URL futura: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`
- Handle: `nike-moon-shoe-jacquemus-guia-lk`
- H1: `Nike x Jacquemus Moon Shoe: história, design e curadoria`
- SEO title: `Nike Moon Shoe Jacquemus: história, modelos e curadoria | LK Sneakers`
- Meta description: `Guia LK do Nike x Jacquemus Moon Shoe: origem do modelo, solado waffle, colorways, estética balletcore, autenticidade e curadoria LK.`

## Proposta de ajuste da coleção existente

URL: `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp`

### SEO title proposto

`Nike x Jacquemus Moon Shoe SP | Curadoria LK Sneakers`

### Meta description proposta

`Nike x Jacquemus Moon Shoe SP na curadoria LK: modelos originais, colorways desejadas, leitura fashion e atendimento humano para confirmar tamanho e prazo.`

### Por que alterar

- Remove linguagem operacional pública: `Estoque limitado`, `Entrega SP`.
- Mantém intenção comercial e curadoria premium.
- Reduz risco de promessa pública de disponibilidade/prazo.
- Melhora consistência com GEO/source page.

## FAQ proposto para coleção/source page

1. O que é o Nike x Jacquemus Moon Shoe?
2. Por que o Moon Shoe Jacquemus virou tão desejado?
3. O Nike Moon Shoe Jacquemus é feminino ou unissex?
4. O Nike Moon Shoe Jacquemus tem a forma grande ou pequena?
5. Qual cor do Nike Moon Shoe Jacquemus escolher?
6. Como saber se o Nike Moon Shoe Jacquemus é original?
7. Onde comprar Nike Moon Shoe Jacquemus original no Brasil?
8. Como a LK seleciona os modelos Nike x Jacquemus?

## Blocos citáveis criados

- Origem Moon Shoe / Bill Bowerman / solado waffle.
- Releitura Jacquemus / sneakerina / balletcore.
- Onde comprar original no Brasil / curadoria LK / atendimento humano.

## Schema proposto para source page

- `WebPage`
- `Article`
- `FAQPage`

## llms.txt — proposta futura

Adicionar após aprovação/publicação:

`- [Guia Nike Moon Shoe Jacquemus](https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk): fonte editorial LK sobre origem Bowerman, solado waffle, releitura Jacquemus, colorways, autenticidade e compra assistida no Brasil.`

E já para a coleção:

`- [Nike x Jacquemus Moon Shoe SP](https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp): coleção LK de pares originais da collab Nike/Jacquemus, com foco em curadoria, história do Moon Shoe, colorways e atendimento humano para confirmação de tamanho e prazo.`

## Rollback plan para futura publicação

Antes de qualquer write em produção:

1. Snapshot Shopify Page/Collection atual:
   - title;
   - handle;
   - body_html/descriptionHtml;
   - SEO title;
   - SEO description;
   - template suffix;
   - published status.
2. Se for theme/dev upload:
   - snapshot do asset Liquid/CSS atual;
   - GET/readback após PUT;
   - guardar hash antes/depois.
3. Verificação pós-publicação:
   - HTTP 200;
   - H1 único;
   - schema presente;
   - FAQ visível = FAQ schema;
   - lint de termos proibidos;
   - mobile screenshot;
   - public URL no Telegram.
4. Rollback:
   - restaurar snapshot anterior via Admin/API;
   - revalidar storefront;
   - registrar receipt.

## Termos proibidos no copy público

Não usar como promessa/taxonomia pública:

- pronta entrega;
- sob encomenda;
- encomenda;
- estoque limitado;
- consultar estoque;
- entrega SP como promessa de snippet.

## Próximo gate

Para publicar em Shopify, ainda precisa aprovação separada e explícita, por exemplo:

`Aprovo publicar em produção a source page Nike Moon Shoe Jacquemus e aplicar os campos SEO/meta propostos na coleção, com snapshot, rollback e verificação pública.`
