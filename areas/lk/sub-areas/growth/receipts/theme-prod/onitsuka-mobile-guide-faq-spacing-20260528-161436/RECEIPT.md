# Receipt — Onitsuka mobile guide FAQ spacing

Data: 2026-05-28
Tema: Shopify production `155065417950`
URL: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`

## Problema reportado
Lucas apontou que, no mobile, o espaçamento do Guia LK antes de “Perguntas frequentes” estava errado.

## Diagnóstico renderizado
Em viewport mobile simulada de 390px:

- Onitsuka antes do hotfix:
  - `ul_to_inFaq`: `0px`
  - `.lk-guide-standard-faq margin-top`: `0px`
  - `.lk-guide-standard-faq padding-top`: `0px`
  - `.lk-guide-standard-faq border-top`: `0px none`
  - havia `.coll-faq` legado depois do guia, gerando FAQ duplicado visualmente.

- New Balance 204L gold source:
  - `ul_to_inFaq`: `24px`
  - `.lk-guide-standard-faq margin-top`: `24px`
  - `.lk-guide-standard-faq padding-top`: `22px`
  - `.lk-guide-standard-faq border-top`: `1px solid #e2dbd0`
  - sem FAQ legado duplicado abaixo.

## Hotfix aplicado
Assets com backup/readback:

- `layout/theme.liquid`
- `sections/lk-collection.liquid`

Regra mobile escopada:

```css
@media(max-width:989px){
  #lk-guia-onitsuka-tiger-mexico-66 .lk-guide-standard-faq{
    margin-top:24px!important;
    padding-top:22px!important;
    border-top:1px solid #e2dbd0!important;
  }
  body:has(#lk-guia-onitsuka-tiger-mexico-66) .coll-faq{
    display:none!important;
  }
}
```

## Readback Admin
- `layout/theme.liquid`: readback final com patch presente.
- `sections/lk-collection.liquid`: readback final com patch presente.

## Observação de cache público
Após o Admin readback, o storefront público ainda retornava HTML antigo para a URL pública em `curl` com cache-bust. Não declarar validação pública final até o HTML servido refletir o patch ou o cache virar.

## Rollback
Restaurar os arquivos `.before` neste diretório:

- `theme.liquid.before`
- `sections__lk-collection.before.liquid`
