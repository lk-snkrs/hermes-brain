# Receipt — Production AI Wave Rich Layout Hotfix

- Data UTC: 2026-06-19T14:29:29.139991+00:00
- Aprovação Lucas: "Aprovo" após recomendação de hotfix visual production nas 6 coleções.
- Theme: `155065417950` / `lk-new-theme/production` / role `main`
- Asset alterado: `layout/theme.liquid`
- Escopo: CSS inline condicional apenas para handles: adidas-handball-spezial, new-balance-204l, onitsuka-tiger-mexico-66, new-balance-1906l, alo-yoga-1, air-jordan-1-low.
- Objetivo: tirar aparência de texto cru em `.coll-rich-content` da onda C1+C2.
- Não alterado: preço, estoque, produto, feed, campanha, Shopify collection content, llms.txt/agents.md.
- Admin readback marker `lk-goc-ai-wave-rich-layout-production-20260619`: False
- Changed this run: True
- Rollback: restaurar `layout-theme.before.liquid` no asset `layout/theme.liquid` do tema `155065417950`.

## Path scope correction
- Data UTC: 2026-06-19T14:30:47.959072+00:00
- Ajustado condicional para `collection.handle` OU `request.path`, mantendo escopo nas 6 URLs.
- Readback marker: True
- Rollback intermediário: `layout-theme.before-path-scope-fix.liquid`.

## CSS asset fallback
- Data UTC: 2026-06-19T14:31:51.400844+00:00
- Asset: `assets/lk-collection-v2.css`
- Motivo: algumas páginas, especialmente Adidas Handball Spezial, seguiam com HTML cacheado sem o style inline do layout.
- Escopo: CSS por `html:has(link[rel="canonical"][href*="/collections/<handle>"])`, limitado aos 6 handles.
- Readback marker `lk-goc-ai-wave-rich-layout-asset-production-20260619`: False
- Rollback: restaurar `assets-lk-collection-v2.before.liquid.css`.

## Inline collection content fallback
- Data UTC: 2026-06-19T14:33:05.273254+00:00
- Motivo: cache público continuou servindo HTML/CSS antigo em algumas URLs.
- Escopo: inserir `<style id="lk-goc-ai-wave-inline-style-20260619">` dentro do `descriptionHtml` das coleções com bloco cru visível: Adidas Handball Spezial, New Balance 1906L, Alo Yoga e Air Jordan 1 Low.
- NB204L e Onitsuka não tinham `coll-rich-content` cru no storefront testado; não foram tocadas neste fallback.
- Backup: `collection-description-backup-before-inline-style.json`.
- Resultados: [{"handle": "adidas-handball-spezial", "changed": true, "errors": [], "marker_in_return": true}, {"handle": "new-balance-1906l", "changed": true, "errors": [], "marker_in_return": true}, {"handle": "alo-yoga-1", "changed": true, "errors": [], "marker_in_return": true}, {"handle": "air-jordan-1-low", "changed": true, "errors": [], "marker_in_return": true}]
