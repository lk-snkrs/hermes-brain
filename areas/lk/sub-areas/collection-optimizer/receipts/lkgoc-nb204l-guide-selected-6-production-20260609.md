# Receipt — LKGOC NB 204L Guia LK: aprovação e merge para Production

Data: 2026-06-09
Aprovação Lucas: "Aprovado" em resposta ao preview DEV com 6 imagens selecionadas.

## Escopo aprovado
Página: `/pages/new-balance-204l-original-brasil-guia-lk`
DEV aprovado: `155065450718` / `lk-new-theme/dev` / role `unpublished`
Production alvo: `155065417950` / `lk-new-theme/production` / role `main`

## Ação executada
Copiados do DEV aprovado para Production:
- `sections/lk-goc-guide-v1.liquid`
- `templates/page.nb204l-guide.json`

Observação operacional: o primeiro PUT do template retornou validação 422 enquanto o schema recém-copiado ainda não estava refletido; após confirmar o section em Production com schema correto, o retry do template retornou 200.

## QA Production
URL live testada com cache-buster:
`https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk?_=...`

Resultado fetch:
- tema production/main confirmado no HTML;
- `Liquid error=False`;
- `figure image cards=6`;
- seção "New Balance 204L on feet" renderizada;
- `img_total=20`.

Resultado Playwright:
- mobile: `liquid=0`, `image_cards=6`, `role_main=true`;
- desktop: `liquid=0`, `image_cards=6`, `role_main=true`.

## Evidências locais
- Manifest + backups: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/production-promotion-20260609/manifest.json`
- HTML live verificado: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/production-promotion-20260609/live-production-nocache-verified.html`
- Screenshot mobile live: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/production-promotion-20260609/live-production-mobile-20260609.png`
- Screenshot desktop live: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/production-promotion-20260609/live-production-desktop-20260609.png`

## Rollback
Backups production-before salvos em:
`/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/production-promotion-20260609/`

Rollback: re-subir para Production os arquivos `*.production-before` correspondentes a:
- `sections/lk-goc-guide-v1.liquid`
- `templates/page.nb204l-guide.json`

## Revisão de impacto
Revisar em ~7 dias: sessões da página, CTR orgânico/GSC, cliques para coleção/PDPs, engajamento mobile e eventuais erros de renderização.
