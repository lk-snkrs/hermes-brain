# LKGOC 204L font tune — DEV/unpublished

Data: 2026-06-08T19:39:45Z
Aprovação Lucas: “aprovado, aplicar no dev”

## Escopo
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado via Shopify CLI: `unpublished`
- Arquivo alterado: `snippets/lk-goc-collection.liquid`
- Coleção: `new-balance-204l`

## Mudança
- `Curadoria LK`: desktop `font-size:18px`, `line-height:1.16`
- `Perfil baixo, leitura fashion.`: desktop `font-size:29px`, `line-height:1.01`
- Escopo CSS limitado ao seletor `aria-label="Contexto editorial New Balance 204L"`.

## Evidência
- Push Shopify CLI concluído com sucesso para `lk-new-theme/dev` (#155065450718).
- Pull remoto do mesmo asset confirmou presença de `lk-goc-204l-font-tune-20260608T193945Z`.
- Browser headless público não conseguiu validar visual do preview porque Shopify removeu `preview_theme_id`/não serviu o theme preview sem sessão/admin; validação visual final deve ser feita no link de preview com sessão ativa.

## Rollback
- Remover o bloco `<style id="lk-goc-204l-font-tune-20260608T193945Z">…</style>` do arquivo `snippets/lk-goc-collection.liquid` e fazer push novamente para o mesmo tema DEV.
- Backup antes da alteração salvo em `before__snippets__lk-goc-collection.liquid`.
