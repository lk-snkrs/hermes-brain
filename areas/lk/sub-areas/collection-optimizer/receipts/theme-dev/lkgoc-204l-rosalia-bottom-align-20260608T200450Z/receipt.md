# LKGOC 204L Rosalia image bottom alignment — DEV/unpublished

Data: 2026-06-08T20:04:50Z
Solicitação Lucas: corrigir imagem principal da Rosalía, alinhando pelo bottom em vez do meio.

## Escopo
- Tema: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished` verificado na listagem Shopify CLI antes do push.
- Arquivo alterado: `snippets/lk-goc-collection.liquid`
- Coleção: `new-balance-204l`
- Sem alteração em produção.

## Mudança
Adicionado no bloco scoped `lk-goc-204l-font-tune-20260608T193945Z`:

```css
html body.template-collection .lk-goc-coll-preview[aria-label="Contexto editorial New Balance 204L"] .lk-goc-card--large img,
html body.template-collection .lk-goc-coll-preview[aria-label="Contexto editorial New Balance 204L"] .lk-204l-card--large img{
  object-position:center bottom!important;
}
```

## Evidência
- `shopify theme push --theme 155065450718 --only snippets/lk-goc-collection.liquid --allow-live=false` retornou sucesso para `lk-new-theme/dev`.
- Pull remoto do mesmo asset confirmou:
  - regra de fonte 204L presente;
  - regra `object-position:center bottom!important` presente no seletor da imagem principal 204L.

## Rollback
- Remover as 4 linhas da regra de `object-position:center bottom!important` dentro do bloco `lk-goc-204l-font-tune-20260608T193945Z`, ou restaurar `before__snippets__lk-goc-collection.liquid` e fazer push para o mesmo tema DEV.
