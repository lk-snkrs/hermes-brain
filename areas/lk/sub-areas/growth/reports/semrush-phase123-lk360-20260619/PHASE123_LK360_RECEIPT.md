# LK Growth — SEMrush phase 1/2/3 + lk-360 removal — 2026-06-19

- Escopo aprovado por Lucas: “Fase 1/2 e 3, pode remover o lk-360”.
- Writes Shopify/theme executados em production e dev quando aplicável; rollback salvo.
- values_printed=false; nenhum write em estoque/Tiny/GMC/GA4/GSC/ads/Klaviyo.

## Feito

1. Fase 1 — Missing H1
- Página `lk-na-imprensa`: template `sections/lk-press.liquid` ajustado para renderizar H1 no título da página.
- Body da page mantém rollback, mas o H1 efetivo vem do template.

2. Fase 2 — Links sem anchor text
- `sections/lk-creators.liquid`: links dos creators agora têm texto oculto acessível.
- `sections/lk-header.liquid`: logo/home agora tem aria + texto oculto.
- `snippets/lk-product-card.liquid`: links de mídia dos cards agora têm texto oculto “Ver produto ...”.
- `sections/lk-pdp.liquid`: cross-sell de PDP agora tem texto oculto no link de imagem.

3. Fase 3 — Content not optimized
- Pages revisadas: `onitsuka-tiger-vs-asics-gel-1130` e `new-balance-530-vs-2002r`.
- Ajuste de SEO title/meta description e bloco contextual “Guia LK”.
- Removido H1 duplicado do body; preview final mostra H1 único.

4. Remoção lk-360
- Removidas referências em `sections/lk-pdp.liquid`.
- Deletados assets em dev e production: `assets/lk-360-viewer.js` e `assets/lk-360-viewer.css`.

## Verificação preview production

Preview usado: `?preview_theme_id=155065417950`

- `https://lksneakers.com.br/?preview_theme_id=155065417950`
  - status `200`; h1_count `1`; lk360_ref `False`; empty_no_text_no_aria `0`
  - h1: `['LK Sneakers — Curadoria de Sneakers e Lifestyle Premium | São Paulo']`
- `https://lksneakers.com.br/pages/lk-na-imprensa?preview_theme_id=155065417950`
  - status `200`; h1_count `1`; lk360_ref `False`; empty_no_text_no_aria `0`
  - h1: `['LK na Imprensa']`
- `https://lksneakers.com.br/pages/onitsuka-tiger-vs-asics-gel-1130?preview_theme_id=155065417950`
  - status `200`; h1_count `1`; lk360_ref `False`; empty_no_text_no_aria `0`
  - h1: `['Onitsuka Tiger Mexico 66 vs ASICS Gel-1130: Japão Retrô vs Japão Y2K']`
- `https://lksneakers.com.br/pages/new-balance-530-vs-2002r?preview_theme_id=155065417950`
  - status `200`; h1_count `1`; lk360_ref `False`; empty_no_text_no_aria `0`
  - h1: `['New Balance 530 vs New Balance 2002R: Qual o Melhor Para Você?']`
- `https://lksneakers.com.br/products/tenis-new-balance-204l-mushroom-arid-stone-marrom?preview_theme_id=155065417950`
  - status `200`; h1_count `1`; lk360_ref `False`; empty_no_text_no_aria `0`
  - h1: `['Tênis New Balance 204L Mushroom Arid Stone Marrom']`

## SEMrush
- Novo Site Audit relançado via API nos projetos `29110159` e `16150947` com HTTP 200.
- Resultado final depende do crawl assíncrono/cache externo.

## Evidência / rollback
- Rollback inicial: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/rollback-before-phase123-lk360.json`
- Receipt execução principal: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/execution-receipt.json`
- Follow-up H1/cache: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/execution-receipt-followup.json`
- Anchor broadening: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/execution-receipt-anchor-broadening.json`
- Product card anchor fix: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/execution-receipt-product-card-anchor-fix.json`
- Verificação final preview: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/final-preview-verify-2.json`
- SEMrush relaunch: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/semrush-phase123-lk360-20260619/semrush-relaunch-after-phase123.json`

## Decisão posterior de Lucas
- 2026-06-19: manter o LK 360 removido; só recriar em novo projeto/aprovação explícita.
