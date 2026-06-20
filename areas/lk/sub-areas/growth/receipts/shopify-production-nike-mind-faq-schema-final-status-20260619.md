# Receipt/status — Nike Mind FAQ schema parity — 2026-06-19

- Código do tema production corrigido em `sections/lk-pdp.liquid`.
- Admin dos 2 PDPs confirma `custom.faq` com 7 perguntas.
- Cache-bust invisível aplicado nos 2 PDPs.
- Bloqueio: storefront público ainda alterna versões antigas; o marker de cache-bust ainda não aparece no HTML público.

## Validação pública resumida
- `slide-nike-mind-001-pearl-pink-rosa`: amostras `19`; visual 7/7 em `8`; schema 7/7 em `8`; schema sem FAQ institucional em `0`; disclaimer em `8`; último `{'visible': 0, 'schema': 0, 'generic_schema': 999, 'title': 'Nike Mind 001 Pearl Pink Original | LK Sneakers', 'qs': ['Os produtos são originais?', 'Qual o prazo de entrega?', 'Como é a embalagem?', 'Posso parcelar?']}`
- `slide-nike-mind-001-light-smoke-grey-cinza`: amostras `19`; visual 7/7 em `0`; schema 7/7 em `0`; schema sem FAQ institucional em `0`; disclaimer em `0`; último `{'visible': 2, 'schema': 0, 'generic_schema': 999, 'title': 'Nike Mind 001 Light Smoke Grey Original | LK Sneakers', 'qs': ['Qual tamanho escolher no Slide Nike Mind 001 Light Smoke Grey?', 'O Slide Nike Mind 001 Light Smoke Grey vendido na LK é original?', 'Posso usar o Slide Nike Mind 001 Light Smoke Grey na chuva?', 'Os produtos são originais?', 'Qual o prazo de entrega?', 'Como é a embalagem?', 'Posso parcelar?']}`

## Próximo passo

- Não fazer novo write de conteúdo agora.
- Revalidar após propagação/cache.
- Se continuar, tratar como problema de cache/tema/publish, não de copy/metafield.