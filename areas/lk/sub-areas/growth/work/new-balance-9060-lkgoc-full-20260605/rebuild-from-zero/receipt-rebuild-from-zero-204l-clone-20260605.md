# Receipt — NB9060 LKGOC rebuild from zero / 204L clone

Data UTC: 2026-06-05T09:56:43Z

## Correção de processo anotada
- Não inventar hero, guia, bloco visual ou comportamento novo.
- Não validar só texto/DOM; comparar visualmente com gold source 204L.
- Não aproveitar `lk-next-*` como Full LKGOC quando o padrão exigido é 204L.
- Não mandar preview ao Lucas antes de QA lado a lado 204L vs coleção alvo.

## Execução
Theme DEV verificado por API:
- `lk-new-theme/dev`
- ID `155065450718`
- role `unpublished`

Produção/main: não tocada.

## O que foi refeito do zero
- Hero 9060 recriado como clone/adaptação literal do bloco aprovado 204L.
- Guia pós-grid 9060 recriado como clone/adaptação do snippet `lk-goc-new-balance-204l-guide-panel`.
- Componente simplificado anterior (`lk-goc-9060-*`) não está mais renderizado.
- Hero antigo `lk-next-*` do 9060 removido da renderização para evitar duplicação/padrão errado.
- Desc override 9060 mantido só para impedir FAQ pública antiga com linguagem operacional no DEV preview.

## QA lado a lado
Desktop:
- 9060 hero class: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-goc-coll-preview--9060 lk-204l-coll-preview`
- 204L hero class: `lk-goc-coll-preview lk-goc-coll-preview--204l lk-204l-coll-preview`
- Ambos: background `rgb(16,16,16)`, largura `1440`, `main=1`, `banner=1`.
- Guia 9060 e 204L: `lk-lkgoc-guide-panel lk-guide-standard-panel`, grid desktop `919.281px 300px`, background `rgb(247,244,239)`.

Mobile:
- Ambos renderizam hero em bloco preto e guia `lk-guide-standard-panel` em bloco.
- Sem duplicação de main/banner.
- 0 ocorrências de `Qual o prazo de entrega` / `Produtos em estoque`.

## Screenshots
- `rebuild-from-zero/qa/9060-desktop.png`
- `rebuild-from-zero/qa/new-balance-9060-mobile.png`
- Comparação: `rebuild-from-zero/qa/204l-desktop.png`, `rebuild-from-zero/qa/new-balance-204l-mobile.png`

## URL DEV preview
`https://lksneakers.com.br/collections/new-balance-9060?preview_theme_id=155065450718`
