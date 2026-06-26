# Receipt — LKGOC NB 204L mobile title spacing DEV

Data UTC: 20260608T173609Z
Status: Corrigido em GitHub dev e Shopify DEV/unpublished

## Feedback Lucas
Espaçamento superior acima do título `New Balance 204L` estava grande demais no mobile.

## Correção
- Arquivo: `layout/theme.liquid`
- Regra alterada: `padding-top:10%!important;` → `padding-top:18px!important;`
- Escopo: apenas collection com `aria-label="Contexto editorial New Balance 204L"` em mobile.

## GitHub
- Branch: `dev`
- Commit: `6b1b030` — `fix(lkgoc): reduce NB 204L mobile title spacing`

## Shopify DEV/unpublished
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Push: sucesso, apenas `layout/theme.liquid`
- Production/main: não alterado

## Verificação
- Preview HTML contém `padding-top:18px!important`: sim
- Preview HTML contém `padding-top:10%!important`: não
- Screenshot QA local: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-spacing-18px-20260608.png`
