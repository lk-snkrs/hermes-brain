# Receipt — CRO P1 aplicado no DEV correto

## Correção operacional
- O write anterior em `[Check] - Homologação` foi rollbackado imediatamente.
- Tema correto confirmado no Brain e via Shopify API antes deste write.

## Tema alvo correto
- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role verificado: `unpublished`
- Fonte canônica: `growth/LKGOC-THEME-TARGET-CONTEXT.md` + receipts LKGOC anteriores.

## Assets alterados no DEV
- `snippets/lk-cro-p1-growth-preview.liquid`
- `layout/theme.liquid` com marker/render inserido: `inserted_after_main_open`

## Readback
- Snippet match: `True`
- Layout contém marker: `True`
- Produção alterada: `false`

## QA Playwright mobile
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: status=200, block_count=1, liquid_error=False
- https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: status=200, block_count=1, liquid_error=False
- https://lksneakers.com.br/collections/new-balance-204l: status=200, block_count=1, liquid_error=False
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: status=200, block_count=1, liquid_error=False
- https://lksneakers.com.br/collections/lululemon: status=200, block_count=1, liquid_error=False

Screenshots: `screenshots/*.png`.

## Observação
- O DEV `lk-new-theme/dev` ainda mostra alguns titles antigos de PDP no preview, diferente da produção corrigida antes. Isso é esperado porque este QA está no DEV e não deve ser usado como prova do head de produção.

## Rollback DEV
- Restaurar `layout__theme.before.liquid`.
- Remover `snippets/lk-cro-p1-growth-preview.liquid` ou restaurar `snippet.before.liquid`.
- Sem impacto em produção.
