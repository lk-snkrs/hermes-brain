# PageSpeed / CrUX readiness — 2026-05-19

## Status

- PageSpeed/CrUX está **OK para uso read-only recorrente** no LK Growth.
- Lucas habilitou as APIs no projeto Google Cloud correto:
  - Project ID: `fluid-griffin-323417`
  - Project number: `797436119355`
- API key salva no Doppler `lc-keys/prd` sem expor valor:
  - `PAGESPEED_API_KEY`
  - `GOOGLE_API_KEY` para compatibilidade com scripts Claude SEO que procuram esse nome.

## Validação executada

### PageSpeed Insights

- URL testada: `https://lksneakers.com/`
- Endpoint: PageSpeed Insights v5, mobile, performance.
- Resultado: `OK`.
- Lighthouse performance score retornado: `0.53`.
- LCP lab retornado: `5.3 s`.
- PSI trouxe CrUX embutido: sim.
- CAPTCHA: não necessário.

### CrUX API

Origins testados:

- `https://lksneakers.com`: 404 / sem dados CrUX para esse origin.
- `https://www.lksneakers.com`: 404 / sem dados CrUX para esse origin.
- `https://lksneakers.com.br`: `OK`, com métricas disponíveis.
- `https://www.lksneakers.com.br`: 404 / sem dados CrUX para esse origin.

Métricas CrUX disponíveis para `https://lksneakers.com.br`:

- INP (`interaction_to_next_paint`)
- LCP (`largest_contentful_paint`)
- CLS (`cumulative_layout_shift`)
- TTFB experimental (`experimental_time_to_first_byte`)
- RTT (`round_trip_time`)
- form factors
- atributos detalhados de recurso LCP

## Decisão operacional

- PageSpeed/PSI está OK para URLs como `https://lksneakers.com/`.
- Para CrUX field data decision-grade, priorizar o origin `https://lksneakers.com.br`, que possui dados reais de Chrome UX Report.
- Quando uma URL/origin retornar 404 no CrUX, tratar como **sem dados CrUX suficientes**, não como falha de autenticação.
- Para Claude SEO nativo, preferir injetar `GOOGLE_API_KEY` a partir do Doppler em tempo de execução, em vez de salvar o valor em `~/.config/claude-seo/google-api.json`.

## Guardrail

- Nenhum valor de chave deve ser registrado no Brain, logs finais ou relatórios.
- Nenhuma alteração foi feita em Shopify, GMC, GA4, GSC, campanhas ou produção.
- A única escrita externa foi salvar a API key fornecida por Lucas no Doppler sob os nomes acima.
