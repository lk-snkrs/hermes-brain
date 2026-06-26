# LK Sneakers — Produção P1 Payload Promotion

Timestamp: 2026-06-01T14:45:36Z

## Aprovação

Lucas aprovou por áudio: “Ficou boa mudança, pode fazer o merge ... para Production, seguindo aquele padrão que a gente definiu antigamente.”

Interpretação operacional aplicada: promover o conjunto validado do `lk-new-theme/dev` para o tema `lk-new-theme/production`, sem merge amplo de branch local e sem publicar/alterar tema fora do production main existente.

## Tema origem

- ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role: `unpublished`

## Tema destino

- ID: `155065417950`
- Nome: `lk-new-theme/production`
- Role: `main`

## Assets promovidos

- `sections/lk-footer.liquid`
- `layout/theme.liquid`
- `assets/lk-footer.css`
- `assets/lk-footer.js`

## Readback de produção

Todos os assets foram enviados e lidos de volta por SHA com `readback_match: true`.

- `sections/lk-footer.liquid`: 25,251 bytes → 12,981 bytes
- `layout/theme.liquid`: 80,971 bytes → 81,189 bytes
- `assets/lk-footer.css`: novo asset, 8,304 bytes
- `assets/lk-footer.js`: novo asset, 4,310 bytes

Manifest técnico:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/seo-geo-weekly-audit-20260601/production-p1-payload-promotion-20260601T144536Z/manifest.json`

## QA live sem preview_theme_id

URLs testadas com cachebuster em produção:

- Home: `https://lksneakers.com.br/?hermes_prod_p1_payload=20260601T1446`
- PDP: `https://lksneakers.com.br/products/nike-dunk-low-rose-whisper?hermes_prod_p1_payload=20260601T1446`
- Collection: `https://lksneakers.com.br/collections/air-jordan-1?hermes_prod_p1_payload=20260601T1446`

Resultados:

- Home: `200`, `lk-footer.css` presente, `lk-footer.js` presente, Judge.me custom preloader `0`, sem `Liquid syntax error`, theme marker produção presente.
- PDP: `200`, `lk-footer.css` presente, `lk-footer.js` presente, Judge.me custom preloader `1`, sem `Liquid syntax error`, theme marker produção presente.
- Collection: `200`, `lk-footer.css` presente, `lk-footer.js` presente, Judge.me custom preloader `0`, sem `Liquid syntax error`, theme marker produção presente.

## Rollback

Backup antes da promoção:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/seo-geo-weekly-audit-20260601/production-p1-payload-promotion-20260601T144536Z/`

Arquivos:

- `sections__lk-footer.liquid.before`
- `layout__theme.liquid.before`
- `assets__lk-footer.css.before` — vazio/não existia antes
- `assets__lk-footer.js.before` — vazio/não existia antes

Rollback: re-upar os `.before` para o tema production ID `155065417950`; para assets que eram vazios/inexistentes, remover/zerar conforme necessidade do rollback.

## Não feito

- Não alterei produtos.
- Não alterei preço.
- Não alterei estoque.
- Não alterei checkout.
- Não removi Variant King/StarApps, Rivo, Simprosys ou Judge.me.
- Não fiz campanha, Klaviyo externo, Meta, GMC ou WhatsApp.
- Não fiz merge amplo de branch local porque o repositório local tem diffs antigos/não relacionados; a promoção seguiu o padrão seguro de asset readback aprovado.
