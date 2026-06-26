# QA LKGOC production — rich layout v4 slim

- Data UTC: 2026-06-19T16:08:04.747751Z
- Escopo: QA read-only público/renderizado das 4 coleções com bloco rico.
- Ferramentas: fetch público + Chromium headless + CSS computado via puppeteer-core.
- Writes externos: nenhum.

## Verdict

**Não está ok para escalar. Precisa hotfix técnico antes de novo batch.**

Motivo: o bloco rico existe nas 4 páginas, mas o CSS público/computado está inconsistente. O padrão v4 slim não ficou dominante em desktop; há mistura de fallback antigo, asset antigo e style inline.

## Achados por coleção

### adidas-handball-spezial
- desktop: status HTTP 200
  - rich width/height: 1400x600.0625; margin: 0px 20px; padding: 48px 40px 60px; bg: rgba(0, 0, 0, 0)
  - inner display: block; columns: none; bg: rgba(0, 0, 0, 0); padding: 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=151439757389105438591780406209
  - element screenshot: adidas-handball-spezial-desktop-rich-element.png (77505 bytes)
- mobile: status HTTP 200
  - rich width/height: 390x1351.703125; margin: 30px 0px; padding: 0px 16px; bg: rgb(255, 255, 255)
  - inner display: block; columns: minmax(260px, 0.72fr) minmax(320px, 1fr); bg: rgb(250, 248, 244); padding: 26px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: adidas-handball-spezial-mobile-rich-element.png (84514 bytes)

### new-balance-1906l
- desktop: status HTTP 200
  - rich width/height: 1160x1108.859375; margin: 72px 140px; padding: 0px 34px; bg: rgb(255, 255, 255)
  - inner display: grid; columns: 410.391px 570.016px; bg: rgb(250, 248, 244); padding: 52px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: new-balance-1906l-desktop-rich-element.png (103844 bytes)
- mobile: status HTTP 200
  - rich width/height: 390x1243.46875; margin: 30px 0px; padding: 0px 16px; bg: rgb(255, 255, 255)
  - inner display: block; columns: minmax(260px, 0.72fr) minmax(320px, 1fr); bg: rgb(250, 248, 244); padding: 26px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: new-balance-1906l-mobile-rich-element.png (79202 bytes)

### alo-yoga-1
- desktop: status HTTP 200
  - rich width/height: 1160x1086.1875; margin: 72px 140px; padding: 0px 34px; bg: rgb(255, 255, 255)
  - inner display: grid; columns: 410.391px 570.016px; bg: rgb(250, 248, 244); padding: 52px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: alo-yoga-1-desktop-rich-element.png (98399 bytes)
- mobile: status HTTP 200
  - rich width/height: 390x1251.296875; margin: 30px 0px; padding: 0px 16px; bg: rgb(255, 255, 255)
  - inner display: block; columns: minmax(260px, 0.72fr) minmax(320px, 1fr); bg: rgb(250, 248, 244); padding: 26px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: alo-yoga-1-mobile-rich-element.png (73704 bytes)

### air-jordan-1-low
- desktop: status HTTP 200
  - rich width/height: 1160x1142.953125; margin: 72px 140px; padding: 0px 34px; bg: rgb(255, 255, 255)
  - inner display: grid; columns: 410.391px 570.016px; bg: rgb(250, 248, 244); padding: 52px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: air-jordan-1-low-desktop-rich-element.png (105621 bytes)
- mobile: status HTTP 200
  - rich width/height: 390x1288.8125; margin: 30px 0px; padding: 0px 16px; bg: rgb(255, 255, 255)
  - inner display: block; columns: minmax(260px, 0.72fr) minmax(320px, 1fr); bg: rgb(250, 248, 244); padding: 26px 0px
  - style ids LKGOC: ['lk-goc-prod-204l-contract-20260604', 'lk-goc-ai-wave-rich-layout-production-20260619', 'lk-goc-ai-wave-rich-layout-v4-slim-20260619']
  - asset: https://lksneakers.com.br/cdn/shop/t/91/assets/lk-collection-v2.css?v=52883209651342979231781882944
  - element screenshot: air-jordan-1-low-mobile-rich-element.png (77357 bytes)

## Interpretação

- **Conteúdo:** presente nas 4 páginas.
- **Mobile:** renderiza sem quebra funcional, mas ainda carrega sinais de regra antiga em `grid-template-columns`; visual tende a ser aceitável, porém não está limpo.
- **Desktop:** não está no padrão slim aprovado. New Balance 1906L, Alo Yoga e Air Jordan 1 Low ainda computam `display:grid` com duas colunas. Adidas desktop recebeu asset antigo/cacheado e não carrega ids v4.
- **Cache/asset:** URLs de `lk-collection-v2.css` variam; Adidas desktop puxou versão antiga `v=151439...`; demais puxaram versão nova `v=528832...`.
- **Resumo LK:** texto existe no conteúdo. O QA computado não confirma bloco preto ativo como estilo dominante, mas a camada CSS antiga ainda aparece/compete em alguns HTMLs.

## Risco

- Escalar novas coleções agora multiplicaria dívida técnica.
- O usuário pode ver experiências diferentes por página/dispositivo/cache.
- A manutenção fica frágil porque existem múltiplas fontes de estilo competindo: asset CSS, theme inline e description fallback.

## Recomendação

1. Hotfix em DEV/unpublished: consolidar um único bloco CSS v4 slim dominante, com escopo para `.coll-rich-content`.
2. Remover dependência de style por descrição de coleção depois que o asset production estiver propagando corretamente.
3. Re-rodar QA computado desktop/mobile.
4. Só após readback público estável, pedir approval Lucas para merge/hotfix production.

## Arquivos de evidência

- Pasta QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260619T1235-lkgoc-v4-slim-production-qa`
- `qa-raw.json`: HTML/public checks.
- `computed-style-qa.json`: CSS computado por Chromium.
- screenshots full page e screenshots do elemento rico por coleção/dispositivo.
