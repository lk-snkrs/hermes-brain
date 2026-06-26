# Receipt — Production rich layout v4 slim

- Data UTC: 2026-06-19T15:13:07.630497+00:00
- Aprovação Lucas: "aplicar" após aprovação visual do DEV v4 slim.
- Theme production: 155065417950 / lk-new-theme/production / role `main`
- Asset: `assets/lk-collection-v2.css`
- Ação: aplicado hotfix visual v4 slim para `coll-rich-content` em collections.
- Não alterado: preço, estoque, produtos, campanhas, feed/GMC, copy/SEO.
- Admin readback marker: False
- Rollback: restaurar `assets-lk-collection-v2.production-before.css` neste mesmo asset.


## Cache-bust layout
- Data UTC: 2026-06-19T15:14:07.001287+00:00
- Ação: inserido comentário Liquid neutro antes de `</head>` para regenerar HTML/asset_url.
- Readback cachebust marker: False
- Rollback adicional: restaurar `layout-theme.production-before-cachebust.liquid` se necessário.


## Inline style fallback
- Data UTC: 2026-06-19T15:15:11.346193+00:00
- Motivo: HTML público ainda referenciava versão antiga do asset CSS via CDN.
- Inline style id `lk-goc-ai-wave-rich-layout-v4-slim-20260619` readback: False
- Rollback adicional: restaurar `layout-theme.production-before-inline-v4.liquid` ou remover o style id.


## Section cache-bust
- Data UTC: 2026-06-19T15:16:02.581353+00:00
- Ação: comentário Liquid neutro no `sections/lk-collection.liquid` para invalidar cache de páginas de collection.


## Collection cache-bust invisível
- Data UTC: 2026-06-19T15:18:21.525827+00:00
- Ação: adicionado comentário HTML invisível em `descriptionHtml` das 6 coleções para invalidar cache de página. Texto visível não alterado.
- Rollback adicional: restaurar `collections-before-cachebust.json` ou remover comentário HTML.


## Inline style por descrição de coleção
- Data UTC: 2026-06-19T15:19:40.294279+00:00
- Motivo: cache HTML por collection alternava versões antigas do tema.
- Ação: inserido `<style>` invisível no `descriptionHtml` das 4 coleções com `coll-rich-content`.
- Rollback adicional: restaurar `collections-before-inline-style-desc.json` ou remover style id.
