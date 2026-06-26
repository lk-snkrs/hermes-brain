# Read-only CRO/SEO opportunity audit — Shopify PDPs & collections

Date: 2026-06-16
Owner: LK Shopify
Mode: read-only public storefront QA + public collection/search discovery
Viewport: mobile `390x844`

## Escopo

Item 2 solicitado por Lucas: auditar próximos PDPs/coleções com maior impacto CRO/SEO, sem writes.

Não houve alteração em Shopify, produto, preço, estoque, coleção, metafield, theme, GMC, Klaviyo, WhatsApp, e-mail, campanha, checkout ou desconto.

## Evidência bruta

- CDP audit script: `/tmp/lkqa-cdp/cro_seo_readonly_audit.js`
- Result JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/cro-seo-readonly-audit-20260616/cro-seo-readonly-audit-results.json`
- Public search/collection discovery executed via storefront JSON/HTML.

## Páginas auditadas

### Coleções

- `/collections/sneakers`
- `/collections/new-balance-9060`
- `/collections/new-balance-204l`
- `/collections/nike-vomero`

### Busca

- `/search?q=204L`
- `/search?q=9060`
- `/search?q=vomero`

### PDPs

- `/products/yeezy-slide-pure-2022`
- `/products/tenis-adidas-yeezy-boost-350-v2-zyon-marrom`
- `/products/tenis-nike-vomero-premium-black-volt-preto`
- `/products/tenis-nike-mind-002-sail-bege`
- `/products/new-balance-530-white-natural-indigo-1`

## Saúde geral observada

Na amostra:

- `Liquid error`: 0
- Overflow horizontal mobile: 0
- H1/canonical presentes nas páginas válidas
- Busca `204L`: coleção sugerida aparece e aponta para `/collections/new-balance-204l`
- Busca `9060`: coleção sugerida aparece e aponta para `/collections/new-balance-9060`
- Coleções `Sneakers`, `New Balance 9060` e `New Balance 204L`: title/meta/H1/canonical saudáveis em check básico
- PDPs auditados têm botão PDP `Guia de tamanhos`
- mKFashion SDK presente na amostra (`mk-sdk.js?v=1` + `mk-core.js`), mas widget visual não apareceu de forma confiável no Chromium headless; isso permanece como limitação de QA/headless e não prova quebra no browser real.

## Achados priorizados

### P1 — Search/CRO: termo `vomero` não mostra coleção sugerida

Evidência:

- `/search?q=vomero` retornou página válida com produtos, mas sem bloco `Coleção sugerida`.
- Coleções públicas existentes relacionadas:
  - `/collections/nike-vomero-5` — `Nike Vomero 5`
  - `/collections/nike-vomero-premium` — `Nike Vomero Premium`
- `/collections/nike-vomero` retorna 404.
- Termos específicos já cobertos:
  - `vomero premium` tem coleção sugerida.

Interpretação:

- Alto-intento genérico `vomero` fica preso no grid de busca e não direciona para uma coleção curada.
- Melhor próximo pacote DEV: ajustar mapa de sugestões da busca para `vomero` apontar para uma coleção apropriada ou apresentar escolha compacta quando há duas famílias (`Vomero 5` e `Vomero Premium`).

Risco:

- Baixo se feito como módulo de busca em DEV/unpublished, sem mexer em produtos.
- Precisa decisão editorial: `vomero` deve apontar para `Nike Vomero 5`, `Nike Vomero Premium`, ou um bloco com as duas opções.

### P2 — PDP SEO: Nike Mind 002 com meta description longa e title comercial demais

Evidência:

- PDP: `/products/tenis-nike-mind-002-sail-bege`
- Title observado: `Tênis Nike Mind 002 Sail Bege por R$ 3.199,99 em até 10x | LK Sneakers`
- Title length: 70
- Meta description length: 320
- Meta começa com texto longo de descrição do produto e excede faixa ideal para snippet.

Interpretação:

- O snippet pode truncar e perder proposta de valor.
- Não é P0/P1 técnico; é oportunidade de SEO/on-page para piloto de SEO fields em produto.

Risco:

- Produto SEO field write exige approval específico com before/after e rollback.
- Não mexer em H1, preço, descrição visível, estoque ou imagens.

### P2/P3 — Copy polish: falta de espaço em algumas notas do guia

Evidência:

- Vomero Premium modal: `costuma vestir normal.Recomendamos...`
- Nike Mind 002 modal: `forma correta.Recomendamos...`

Interpretação:

- Pequeno acabamento de copy dentro do mesmo componente de Guia de Tamanhos.
- Não quebra conversão, mas reduz polimento percebido em modelos premium/novos.

Risco:

- Baixo. Pode virar pacote DEV tiny-fix em `sections/lk-pdp.liquid`, com QA nos mesmos controles.

### P2 — mKFashion/Provador Virtual ainda inconclusivo no headless

Evidência:

- Scripts mKFashion aparecem carregados em páginas públicas.
- O botão/widget visual não foi encontrado consistentemente no Chromium headless.
- Lucas já informou anteriormente que “está funcionando”.

Interpretação:

- Não tratar como quebra sem browser real/mobile autenticado ou evidência do cliente.
- Manter como monitor/QA real-device quando conveniente.

Risco:

- Mexer nisso sem confirmação pode quebrar um widget que está funcionando no browser real.

## Próxima recomendação

1. **DEV packet para busca `vomero`**
   - Escopo: `sections/lk-search.liquid` ou mapa equivalente de sugestão compacta.
   - Preview: mobile `/search?q=vomero`, `/search?q=vomero+premium`, controles `204L` e `9060`.
   - Decisão necessária: `vomero` aponta para `Nike Vomero 5`, `Nike Vomero Premium`, ou bloco com duas opções.

2. **Mini-fix DEV de copy no Guia de Tamanhos**
   - Escopo: só espaço depois do ponto em Vomero/Mind 002 notes.
   - Baixo risco, mas ainda é theme write e precisa aprovação para DEV.

3. **SEO-field packet Nike Mind 002**
   - Preparar before/after de `seo.title` e `seo.description` em produto.
   - Só executar com approval específico de Shopify product SEO fields.

## Veredito

Depois da correção do Yeezy Slide, o próximo melhor alvo por impacto/risco é a **busca `vomero` sem coleção sugerida**, porque há coleção pública relevante e a correção pode ser testada em DEV sem tocar produto/preço/estoque.
