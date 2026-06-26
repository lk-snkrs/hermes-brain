# Receipt — LKGOC NB 204L mobile Gold Source polish

Data UTC: 20260608T154238Z
Status: PR atualizado — sem Shopify production write

## Pedido Lucas
1. `coll-banner__title`: aumentar espaçamento superior no mobile em 10%.
2. Remover classe dupla `lk-goc-kicker lk-goc-kicker`; kicker deve ficar limpo como `lk-goc-kicker`.
3. Garantir botão `Ler mais` no mobile para revelar imagens, mantendo lógica product-first.
4. Preservar desktop, já aprovado visualmente.
5. Preservar `lk-goc-guide-panel` como padrão perfeito para copiar nos próximos modelos apenas trocando texto.

## Execução
- Repo/worktree: `/opt/data/worktrees/lk-new-theme-204l-mobile-fix-20260608`
- Branch: `hermes/204l-mobile-gold-fix-20260608`
- PR: https://github.com/lk-snkrs/lk-new-theme/pull/39
- Base: `dev`
- Novo commit: `807f478199813c1ed2eb2c863d61ce31ea4f7a87` — `fix(lkgoc): polish NB 204L mobile gold source`

## Arquivos alterados
- `layout/theme.liquid`
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`
- `snippets/lk-goc-canonical-five-collections.liquid`
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-9060-hero-204l-clone.liquid`
- `snippets/lk-samba-204l-hero-v2.liquid`

## QA executado
- `git diff --check`: OK
- Chromium headless mobile, HTML live com patch local injetado:
  - collapsed screenshot: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-patched-collapsed-20260608.png`
  - expanded screenshot: `/opt/data/profiles/lk-collection-optimizer/output/204l-mobile-audit/204l-mobile-patched-expanded-20260608.png`
- Computed QA collapsed:
  - `buttonText`: `Ler mais`
  - `buttonDisplay`: `inline-flex`
  - `kickerClass`: `lk-goc-kicker`
  - cards: principal `block`; secundárias `none`
  - aspect principal: `16 / 9`
- Computed QA expanded:
  - botão escondido após abrir
  - 3 cards visíveis
  - principal `3 / 4`; secundárias `1.55 / 1`

## Observação de escopo
- Não houve write Shopify Production/main.
- PR segue aguardando revisão/merge para `dev` antes de qualquer preview DEV/unpublished.
