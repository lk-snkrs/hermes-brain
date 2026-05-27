# Moon Shoe hero-only visual fix — partial status

Data: 2026-05-26

## Destino

- Shopify production theme: `155065417950` (`lk-new-theme/production`)
- Página pública: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`

## Pedido aprovado

Lucas aprovou aplicar em production a correção visual da Moon Shoe page.

## O que foi executado

- Script local criado: `/opt/data/hermes_bruno_ingest/hermes-brain/scripts/lk_apply_moon_shoe_hero_only_fix_20260526.py`
- Backup/receipt criado em: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/moon-shoe-hero-only-fix-20260526T170619Z/`
- Asset `snippets/lk-moon-shoe-source-preview.liquid`: readback Shopify Admin confirmou remoção do override ruim `v4` e presença do bloco `v5`.

## Verificação / problema

- Asset `sections/lk-moon-shoe-source-page.liquid`: tentativa de PUT não persistiu no readback; readback manteve o override ruim `v4` e não contém `v5`.
- Browser público em `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk?_cb=170620` mostrou:
  - corpo editorial claro/branco: OK;
  - override ruim `v4` não presente no DOM público: OK;
  - bloco `v5` não presente no DOM público: não confirmado;
  - hero/topo ainda claro/branco, não preto: pendente.
- Screenshot de evidência: `/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_f85b2e68dd354fcfb9d626a447b4ba14.png`

## Status

Não marcar como concluído. A correção foi parcialmente aplicada/propagada: o corpo voltou para claro, mas o hero escuro aprovado ainda não aparece no storefront público.

## Rollback

- Restaurar os backups em `moon-shoe-hero-only-fix-20260526T170619Z/*.before` se necessário.
- Para o snippet, o rollback é substituir pelo arquivo `snippets__lk-moon-shoe-source-preview_liquid.before`.
- Para a section, o readback indica que a alteração não persistiu, então o risco de rollback efetivo na section é baixo.

## Próximo passo necessário

Executar novo write de produção, em turno sem boundary read-only, focado em persistir o CSS pós-render na section ou em um asset CSS global versionado. Depois verificar:

1. Shopify Admin readback contém `hero-only dark + light editorial body v5`.
2. Browser público mostra `.lk-source-page__header` com `background-color: rgb(17, 17, 17)`.
3. Primeiro H2/parágrafo abaixo do hero permanece preto sobre fundo claro.
