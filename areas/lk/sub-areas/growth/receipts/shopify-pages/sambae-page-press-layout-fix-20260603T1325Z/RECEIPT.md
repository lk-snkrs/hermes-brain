# Receipt — Sambae press/radar layout fix

Data UTC: 2026-06-03T11:16:07.918009+00:00
Página: `/pages/guia-adidas-sambae`
Page ID: `127575949534`
Tema dev/draft: `155065450718`

## Escopo solicitado
Corrigir a seção **“Veículos de moda e sites que colocaram o Sambae em pauta”**, que estava renderizando como texto corrido no mobile em vez de cards/grid.

## Correções aplicadas
1. **Page body_html**
   - Inserido patch CSS mais específico para `.lk-press`, `.lk-press-grid` e `.lk-press-card`.
   - Mobile configurado para grid 2 colunas com cards compactos.
   - Snapshot: `page.before.json` / `page.after.json` / `page.readback-admin.json`.

2. **Tema dev/draft 155065450718**
   - Como o storefront/preview estava mantendo a versão anterior do body no render, foi aplicado também um patch CSS escopado no `layout/theme.liquid` do tema dev.
   - Patch ID: `lk-sambae-press-layout-fix-20260603`.
   - Afeta somente `.lk-source-page--sambae .lk-press...`.
   - Não foi feito write no tema production.
   - Snapshot: `dev-theme-layout-theme.before.liquid` / `dev-theme-layout-theme.readback.liquid`.

## QA
- Admin readback da page contém:
  - `press-layout-fix`: presente.
  - `press/radar cards`: presente.
  - `.lk-press .lk-press-grid`: presente.
- Dev theme readback contém:
  - `lk-sambae-press-layout-fix-20260603`: presente.

## Observação técnica
O CLI público não carrega o cookie de preview do navegador do Lucas; por isso o render CLI pode não mostrar o CSS do tema dev/draft. O readback do asset confirma que o patch está no tema dev usado no preview.

## Rollback
- Page: restaurar `body_html` de `page.before.json` via Admin API.
- Tema dev: restaurar `layout/theme.liquid` de `dev-theme-layout-theme.before.liquid` via Assets API.
