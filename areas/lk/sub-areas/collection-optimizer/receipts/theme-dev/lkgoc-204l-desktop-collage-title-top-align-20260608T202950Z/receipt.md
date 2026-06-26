# LKGOC 204L — desktop collage aligned to coll-banner title top — DEV/unpublished

Data: 2026-06-08T20:29:50Z
Solicitação Lucas: no HERO desktop, o bloco de imagens deve começar na mesma altura/topo do `class="coll-banner__title"`.

## Escopo
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role operacional: `unpublished`
- Arquivo alterado: `layout/theme.liquid`
- Coleção: `new-balance-204l`
- Produção: não alterada.

## Implementação
Adicionado script escopado `lk-goc-204l-desktop-collage-title-top-align-20260608`.

Comportamento:
- Só roda quando existe o bloco `Contexto editorial New Balance 204L`.
- Só aplica em desktop `min-width: 990px`.
- Mede:
  - topo do `.coll-banner__title`;
  - topo do `.lk-goc-collage` / `.lk-204l-collage`.
- Calcula o delta real via `getBoundingClientRect().top`.
- Ajusta `transform: translateY(...)` e `margin-bottom` para o topo das imagens bater com o topo do título.
- Reexecuta em `DOMContentLoaded`, `load`, pequenos delays pós-render, `resize` e `shopify:section:load`.
- Em mobile remove inline `transform`/`margin-bottom` para preservar o comportamento mobile já aprovado.

## Evidência
- `shopify theme push --theme 155065450718 --only layout/theme.liquid --allow-live=false` retornou sucesso para `lk-new-theme/dev`.
- Pull remoto confirmou:
  - script `lk-goc-204l-desktop-collage-title-top-align-20260608` presente;
  - uso de `.coll-banner__title`;
  - cálculo por `getBoundingClientRect().top`;
  - aplicação de `setProperty('transform', ...)`;
  - condição desktop `(min-width: 990px)`.

## Rollback
- Remover o bloco `<script id="lk-goc-204l-desktop-collage-title-top-align-20260608">…</script>` de `layout/theme.liquid` e fazer push para o mesmo tema DEV.
- Backup pré-alteração salvo em `before__layout__theme.liquid`.
