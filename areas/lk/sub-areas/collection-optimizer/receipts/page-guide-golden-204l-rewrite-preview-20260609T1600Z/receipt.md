# Receipt — DEV Preview — Guia LK 204L Golden Rewrite

Data: 2026-06-09  
Owner: `[LK] Otimização de Coleções`  
Status: DEV/unpublished aplicado e validado. Production intocada.

## Escopo

Reescrita/expansão do Guia LK New Balance 204L pensando em SEO, GEO/AI Search e experiência visual.

URL pública alvo: `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk`

Preview DEV: `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk?preview_theme_id=155065450718`

## Theme

- Theme DEV: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`
- Production: não alterada

## Arquivos alterados

- `sections/lk-goc-guide-v1.liquid`
- `templates/page.nb204l-guide.json`

## Conteúdo adicionado

- New Balance 204L original no Brasil
- Por que o 204L ficou desejado
- Comparativo 204L vs 530 vs 9060 vs 2002R vs 327
- Conforto
- Feminino/masculino/unissex
- Cuidados com suede/camurça e mesh
- Galeria visual adicional
- FAQ expandido para 12 perguntas

## SEO/GEO

- H1 único mantido
- FAQPage schema mantido
- WebPage schema mantido
- BreadcrumbList schema mantido
- Bloco citável LK mantido/expandido

## Checks

Ver `checks.json` neste diretório.

Resumo:

- DEV/unpublished: OK
- Liquid error: false
- H1 count: 1
- FAQ details: 12
- img count: 20
- CTA collection: OK

## Evidências

- `dev-preview.html`
- `checks.json`
- `dev-preview-desktop.png`
- `dev-preview-mobile.png`

## Git

Branch: `hermes/lkgoc-template-standard-20260609`  
Commit: `1fa5b6d — Expand NB 204L guide for SEO`

## Pendências antes de Production

- QA visual humano desktop/mobile por Lucas.
- Ajustar title/meta da Shopify Page se aprovado.
- Ajustar OG image para hero editorial se aprovado.
- Merge/deploy controlado para Production somente com aprovação explícita.
- Rollback: reverter commit `1fa5b6d` e reaplicar assets anteriores se necessário.
