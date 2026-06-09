# Receipt — LKGOC Golden template base + kicker cleanup

Data UTC: 20260608T174338Z
Status: concluído em GitHub dev + Shopify DEV/unpublished

## Decisão Lucas
- New Balance 204L aprovada vira **LAYOUT/TEMPLATE BASE / GOLDEN** das próximas coleções.
- Próximas coleções devem trocar apenas texto, fotos, links, produtos/FAQ e nuances comerciais.
- Não redesenhar layout/template sem aprovação explícita.
- `lk-204l-kicker` deve ser deletado/banido.

## Execução código
- Branch: `dev`
- Commit: `b559675` — `refactor(lkgoc): remove legacy 204l kicker class`
- Shopify DEV/unpublished atualizado:
  - tema: `lk-new-theme/dev`
  - id: `155065450718`
  - role: `unpublished`

## Arquivos do tema limpos
- `assets/lk-product-card.css`
- `sections/lk-collection.liquid`
- `snippets/lk-goc-collection.liquid`
- `snippets/lk-goc-new-balance-530-hero-204l-clone.liquid`
- `snippets/lk-goc-new-balance-9060-hero-204l-clone.liquid`
- `snippets/lk-nike-mind-collection-hero.liquid`
- `snippets/lk-samba-jane-lkgoc-v2.liquid`
- `snippets/lk-sambae-204l-hero.liquid`

## Verificação
- Worktree tema: `lk-204l-kicker` = 0 ocorrências.
- Tema DEV remoto baixado: `lk-204l-kicker` = 0 ocorrências.
- Preview validado via Chromium com cookie de preview:
  - theme: `lk-new-theme/dev`
  - role: `unpublished`
  - `lk-204l-kicker` = 0 ocorrências
  - `lk-goc-kicker` presente.

## Production
- Nenhuma alteração em production/main.
