# LK Growth — SEMrush fixes execution receipt

- Data UTC: `2026-06-19T13:26Z–13:35Z`
- Approval: Lucas pediu no Telegram: `fazer 1`, `fazer 3`, `fazer o 4`.
- Escopo: Shopify production blog/content para itens 1 e 3; Shopify dev theme para item 4; estoque consultado=false; values_printed=false.
- Rollback: `rollback-before.json` neste diretório.
- Raw receipt: `execution-receipt.json`; verificação pública: `post-execution-public-verify.json`; cache poll: `jordan-alaska-cache-poll.json`.

## Executado

1. **Broken external image — Jordan Alaska**
   - Article ID `664814059742`.
   - Removido do `body_html` o `<img>/<figure>` com URL externa 404 `sneakerbardetroit...Alaska...jpg`.
   - Também aplicado SEO title curto e bloco de linkagem interna no artigo.

2. **Editorial SEO/linkagem interna — pacote SEMrush**
   - Artigos processados: `24`.
   - Ações: `global.title_tag` em artigos prioritários; conversão de H1 embutido no body para H2 quando encontrado; bloco de links internos para curadoria de sneakers, autenticidade, guia de tamanhos e loja física.
   - Artigos com bloco interno adicionado: `24`.
   - Artigos com SEO title setado: `8`.

3. **Links sem anchor text — dev theme**
   - Theme: `lk-new-theme/dev` / ID `155065450718`.
   - Asset: `sections/lk-category-grid.liquid`.
   - Patch: anchors de cards agora recebem `<span class="catcard__sr">Ver coleção ...</span>` com CSS screen-reader-only.
   - Produção theme não alterado neste item.

## Verificação

- Dev preview category grid: `empty_catcard_anchors=0`; `catcard__sr` presente.
- Amostras editoriais: Versace e Streetwear retornaram `h1_count=1`, title curto e marker de links internos presente.
- Jordan Alaska: Admin readback confirmou body sem URL quebrada; public cache ainda retornou alternância entre versão antiga e nova durante o poll. Últimas leituras mostraram versão nova em 2/3 leituras finais, mas não 3 consecutivas. Aguardar propagação/cache Shopify antes de re-crawl SEMrush.

## Sobre o item 2 — llms.txt

- Não foi mexido nesta execução.
- Histórico: já houve trabalho anterior em llms/robots; porém o SEMrush ainda acusou `Llms.txt has formatting issues` no snapshot atual. Validação pública mostrou comportamento inconsistente por UA/cache: SemrushBot/Googlebot recebem 200 markdown; browser simples chegou a receber 503 Shopify. Portanto não considero fechado sem normalização dedicada e recheck.

## Rollback

- Restaurar artigos afetados a partir de `rollback-before.json` por Article ID.
- Restaurar asset `sections/lk-category-grid.liquid` no theme dev `155065450718` usando o valor salvo em `rollback-before.json`.

## Impact review

- Due: `2026-06-26`.
- Checar novo SEMrush/Ahrefs: queda de `Broken external images`, `Title too long`, `Multiple H1`, `Duplicate H1/title`, `Pages with only one internal link`, `Links with no anchor text` no dev/produção conforme promoção futura.