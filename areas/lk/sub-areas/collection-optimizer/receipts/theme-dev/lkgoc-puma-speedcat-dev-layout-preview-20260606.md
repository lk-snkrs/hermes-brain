# Receipt — LKGOC Puma Speedcat DEV layout preview

Data: 2026-06-06T15:04:54.395508+00:00

## Escopo aprovado no chat
Lucas pediu: "posta no tema DEV, para ver como ficou, utilizando o LAYOUT".

## Guardrails executados
- Tema alvo verificado por Admin API: `lk-new-theme/dev` / `155065450718` / role `unpublished`.
- Production theme não recebeu write.
- Página Shopify global não foi publicada.
- Asset hero lifestyle é referência visual de DEV e está marcado como não publicável sem licença/aprovação.

## Assets DEV escritos
- `templates/page.guia-puma-speedcat-lkgoc.json` — template usando section layout `lk-goc-guide-v1`.
- `snippets/lk-goc-puma-speedcat-dev-layout-preview.liquid` — preview visual renderizado na coleção DEV.
- `sections/lk-collection.liquid` — patch DEV com marker para renderizar o preview somente em `collection.handle == 'puma-speedcat'`.

## Readback
- Template semantic readback: `True`.
- Snippet readback equal: `True`.
- Section marker/readback: `True` / render snippet: `True`.
- HTML preview fetched via Shopify with DEV preview cookie: marker `True`, title `True`, Vogue `True`, FAQ `True`.
- Production untouched: marker `False`, render `False`.

## Preview
- URL: `https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`
- Observação: se o link abrir produção/cache, primeiro abrir o preview do tema `lk-new-theme/dev` no admin Shopify para setar cookie de preview. O HTML DEV foi validado via cookie de preview.

## Rollback DEV
Restaurar:
- `sections/lk-collection.liquid` a partir de `work/lkgoc-puma-speedcat-dev-post-20260606/sections__lk-collection.liquid.before`.
- Remover `snippets/lk-goc-puma-speedcat-dev-layout-preview.liquid` ou zerar o snippet.
- Restaurar `templates/page.guia-puma-speedcat-lkgoc.json` a partir de `.before` se necessário.
