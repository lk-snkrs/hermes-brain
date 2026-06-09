# Receipt — LKGOC 204L mobile Gold Source fix

Data UTC: 20260608T153415Z
Status: GitHub branch/PR criado — sem Shopify production write

## Pedido Lucas
Corrigir primeiro o mobile da New Balance 204L antes de usá-la como Gold Source LKGOC.

## Fluxo respeitado
- Base: `origin/dev`
- Branch: `hermes/204l-mobile-gold-fix-20260608`
- Commit: `130ac40` — `fix(lkgoc): improve NB 204L mobile gold hero`
- PR para DEV: https://github.com/lk-snkrs/lk-new-theme/pull/39
- Sem merge para production.
- Sem write direto em Shopify Production/main.

## Correção
Arquivo alterado: `layout/theme.liquid`

Adicionado CSS escopado a:
`aria-label="Contexto editorial New Balance 204L"`

Mudanças:
- remove colapso visual de mídia mobile em faixa/teaser;
- card editorial principal mobile vira 16:9 visível;
- mantém botão `Ler mais` visível no mobile;
- secundárias ficam escondidas no collapsed e aparecem no estado expandido;
- escopo restrito à 204L para não alterar outras coleções LKGOC.

## Validação local
- `git diff --check`: OK
- `shopify theme check`: tentou rodar, mas não concluiu em 300s e não gerou log; validação substituta limitada por diff/CSS e render local.
- Screenshot live atual: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-current.png`
- Screenshot simulado com CSS corrigido: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-fixed-simulated.png`
- Comparativo: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-before-after-simulated.png`

## Próximo passo
Lucas revisar o antes/depois. Se aprovado, merge para `dev` e gerar preview DEV/unpublished. Production somente pelo fluxo GitHub DEV → branch Production → deploy/promoção controlada.
