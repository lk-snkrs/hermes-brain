# Morning Visual QA Shopify — 2026-06-16

## Escopo

Pedido: Lucas pediu “Fazer 1 e o 2”. Este arquivo documenta a ação 1: QA visual mobile/browser Shopify em modo read-only.

Não houve write Shopify, upload de tema, alteração de produto, alteração de estoque, campanha, e-mail ou WhatsApp.

## Ambiente

- Storefront público: `https://lksneakers.com.br`
- Modo: Chromium headless via CDP, viewport mobile `390x844`, user-agent mobile.
- Cache-busting: `_qa=visual20260616`.
- Evidência bruta: `areas/lk/sub-areas/shopify/reports/assets/morning-visual-qa-20260616/visual-qa-results.json`
- Screenshots: `areas/lk/sub-areas/shopify/reports/assets/morning-visual-qa-20260616/*.png`

## Páginas testadas

### PDPs

- `/products/tenis-nike-vomero-premium-black-volt-preto`
- `/products/yeezy-slide-glow-green`
- `/products/air-jordan-1-mid-wolf-grey`

Resultado PDPs:

- HTTP/browser render carregou com título correto.
- `Liquid error`: 0 nas 3 PDPs.
- Sem overflow horizontal no viewport mobile (`scrollWidth=390`, `innerWidth=390`).
- Botão `Guia de tamanhos` encontrado nas 3 PDPs.
- Clique no guia abriu modal nas 3 PDPs:
  - `aria-hidden=false`
  - `display=flex`
  - `visibility=visible`
  - modal ocupando viewport mobile.
- Conteúdo esperado apareceu no modal:
  - Vomero Premium: “Nike Vomero Premium”.
  - Yeezy: “Adidas Yeezy”.
  - Jordan Mid: “Jordan 1 Mid”.

Observação de copy/sizing:

- Yeezy Slide ainda abriu a tabela/copy genérica `Adidas Yeezy`, com recomendação “subir meio número”. A memória operacional da LK registra regra específica: Yeezy Slide deve recomendar 1 tamanho acima. Como este QA foi visual/read-only, não alterei nada. Classificação: P1/P2 de conteúdo/conversão, não P0 visual.

Observação mKFashion/Provador Virtual:

- Scripts mKFashion/MK SDK foram detectados na PDP, incluindo `mk-sdk.js` e `mk-core.js`.
- No Chromium headless/mobile, não encontrei botão/texto visível `Provador Virtual` nas 3 PDPs testadas após carregamento. Pode ser comportamento condicionado pelo SDK/produto/browser ou falha de renderização do widget.
- Classificação: P1 de CRO a investigar em browser real antes de qualquer correção.

### Busca mobile

- `/search?q=204L`
- `/search?q=9060`

Resultado busca:

- `Liquid error`: 0.
- Sem overflow horizontal.
- Bloco de coleção sugerida aparece no primeiro viewport.
- `204L` aponta para `/collections/new-balance-204l`.
- `9060` aponta para `/collections/new-balance-9060`.

### Coleções mobile

- `/collections/sneakers`
- `/collections/new-balance-todos-os-modelos`
- `/collections/nike-todos-os-modelos`

Resultado coleções:

- `Liquid error`: 0.
- Sem overflow horizontal.
- H1 renderizado corretamente:
  - Sneakers: `Tênis e Sneakers Originais`
  - New Balance: `New Balance`
  - Nike: `Nike`
- Grid/links de produto presentes.

## Achados por prioridade

### P0 — venda quebrada

Nenhum P0 encontrado na amostra visual mobile.

### P1 — conversão/risco operacional

1. `Provador Virtual`/mKFashion não apareceu visualmente no headless mobile, apesar de scripts estarem presentes. Precisa validação em browser real/mobile ou DEV antes de decidir correção.
2. Yeezy Slide usa copy/tabela genérica `Adidas Yeezy`; regra operacional atual da LK pede 1 tamanho acima para Slide.

### P2 — SEO/GEO/conteúdo

- Busca 204L/9060 e coleções estratégicas passaram no check visual básico.
- Sem nova pendência SEO crítica detectada neste QA.

### P3 — acabamento visual

- Nenhum overflow horizontal detectado na amostra.
- Screenshots salvos para revisão visual humana.

## Risco

- QA headless é bom para regressão rápida, mas não substitui browser real para widget terceiro/SDK visual.
- Não consultei estoque nem disponibilidade.
- Não cliquei em comprar/adicionar ao carrinho para evitar qualquer risco operacional; o teste ficou em render, busca, modal e presença visual.

## Rollback

Não aplicável para Shopify: não houve alteração no storefront.

## Próxima decisão sugerida

1. Se quiser corrigir já: preparar approval packet para ajustar copy do Yeezy Slide no tema/snippet de size guide, com preview em DEV antes de production.
2. Para mKFashion: validar em browser real/mobile ou DEV com screenshot interativo; se confirmado ausente, abrir investigação isolada do widget/anchor antes de qualquer upload de tema.
