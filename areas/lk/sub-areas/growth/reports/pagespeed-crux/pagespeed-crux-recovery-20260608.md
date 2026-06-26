# PageSpeed / CrUX Recovery — 2026-06-08

Generated: `2026-06-08T19:18:14.263015+00:00`

GOOGLE_API_KEY present: `True`

Modo: read-only / sem alteração de tema ou runtime global

## Resumo executivo

Tooling recuperado: PSI e CrUX responderam para as 4 URLs após retry. Lab mobile está abaixo do ideal, mas field data aparece FAST nas URLs com dados — ou seja, o gargalo imediato é mais lab/tema potencial do que evidência de campo crítica neste recorte.

## URLs testadas

### home
- URL: https://lksneakers.com.br/
- PSI status: 200
- CrUX status: 200
- Lighthouse scores:
  - performance: 0.41
- Lab metrics:
  - largest-contentful-paint: 14.5 s
  - total-blocking-time: 600 ms
  - cumulative-layout-shift: 0
  - speed-index: 10.4 s
  - interactive: 15.6 s
- Field overall: AVERAGE
- Field metrics:
  - CUMULATIVE_LAYOUT_SHIFT_SCORE: FAST
  - EXPERIMENTAL_TIME_TO_FIRST_BYTE: AVERAGE
  - FIRST_CONTENTFUL_PAINT_MS: FAST
  - INTERACTION_TO_NEXT_PAINT: FAST
  - LARGEST_CONTENTFUL_PAINT_MS: FAST

### onitsuka_collection
- URL: https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos
- PSI status: 200
- CrUX status: 200
- Lighthouse scores:
  - performance: 0.6
- Lab metrics:
  - largest-contentful-paint: 6.6 s
  - total-blocking-time: 580 ms
  - cumulative-layout-shift: 0.011
  - speed-index: 3.1 s
  - interactive: 17.4 s
- Field overall: FAST
- Field metrics:
  - CUMULATIVE_LAYOUT_SHIFT_SCORE: FAST
  - EXPERIMENTAL_TIME_TO_FIRST_BYTE: FAST
  - FIRST_CONTENTFUL_PAINT_MS: FAST
  - LARGEST_CONTENTFUL_PAINT_MS: FAST

### new_balance_204l_collection
- URL: https://lksneakers.com.br/collections/new-balance-204l
- PSI status: 200
- CrUX status: 200
- Lighthouse scores:
  - performance: 0.69
- Lab metrics:
  - largest-contentful-paint: 13.0 s
  - total-blocking-time: 150 ms
  - cumulative-layout-shift: 0.073
  - speed-index: 3.3 s
  - interactive: 15.7 s
- Field overall: FAST
- Field metrics:
  - CUMULATIVE_LAYOUT_SHIFT_SCORE: FAST
  - EXPERIMENTAL_TIME_TO_FIRST_BYTE: FAST
  - FIRST_CONTENTFUL_PAINT_MS: FAST
  - INTERACTION_TO_NEXT_PAINT: FAST
  - LARGEST_CONTENTFUL_PAINT_MS: FAST

### nike_mind_black_chrome_pdp
- URL: https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto
- PSI status: 200
- CrUX status: 200
- Lighthouse scores:
  - performance: 0.47
  - accessibility: 0.94
  - best-practices: 0.96
  - seo: 0.92
- Lab metrics:
  - largest-contentful-paint: 17.8 s
  - total-blocking-time: 470 ms
  - cumulative-layout-shift: 0
  - speed-index: 7.0 s
  - interactive: 19.6 s
- Field overall: FAST
- Field metrics:
  - CUMULATIVE_LAYOUT_SHIFT_SCORE: FAST
  - EXPERIMENTAL_TIME_TO_FIRST_BYTE: FAST
  - FIRST_CONTENTFUL_PAINT_MS: FAST
  - LARGEST_CONTENTFUL_PAINT_MS: FAST

## Próxima ação recomendada

- Não mexer em production theme agora.
- Abrir ticket DEV para auditar LCP mobile em home e PDP Nike Mind, começando por imagem hero/product media e JS de terceiros.
- Se aprovado, criar preview/dev theme com mitigação e medir antes/depois.