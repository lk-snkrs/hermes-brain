# Padrão canônico `lk-collection-v2`

Status: **aprovado por Lucas em 2026-05-28** como padrão visual para replicar em próximas coleções, usando a coleção New Balance 204L no Dev Theme como gold source.

## Fonte de verdade aprovada

- Gold source: `/collections/new-balance-204l`
- Dev theme aprovado: `155065450718`
- Namespace base: `.lk-collection-v2`
- Modificador da gold source: `.lk-collection-v2--new-balance-204l`
- Escopo aprovado neste registro: **desktop hero/header editorial da coleção**. Mobile e produção continuam exigindo validação/approval próprios quando forem migrados.

## Regra de governança

- Toda coleção LK que for melhorada a partir deste ponto deve migrar para o namespace `lk-collection-v2`.
- O padrão v2 aprovado deve ser replicado como contrato visual, não como inspiração solta.
- Implementar primeiro em dev theme, validar visualmente e por computed styles, e só então promover para production com aprovação explícita, rollback e receipt.
- Não usar novos overrides soltos em `layout/theme.liquid` como padrão de evolução; se algum override tardio for necessário, ele deve fazer parte do contrato documentado e ser replicado/validado junto.

## Objetivo

Criar um contrato único para collections premium LK, evitando drift entre `lk-204l-*`, `lk-next-*` e hotfixes específicos por handle.

## Namespace

Classes base:

- `.lk-collection-v2`
- `.lk-collection-v2--{handle}`
- `.lk-collection-v2__inner`
- `.lk-collection-v2__copy`
- `.lk-collection-v2__eyebrow`
- `.lk-collection-v2__headline`
- `.lk-collection-v2__body`
- `.lk-collection-v2__media`
- `.lk-collection-v2__card`
- `.lk-collection-v2__card--large`

Elementos herdados do banner do tema que fazem parte do contrato visual:

- `.coll-banner`
- `.coll-banner__crumbs`
- `.coll-banner__title`

Handles migrados devem adicionar modificador:

- `.lk-collection-v2--new-balance-204l`
- `.lk-collection-v2--onitsuka-tiger-mexico-66`
- `.lk-collection-v2--onitsuka-tiger-mexico-66-sabot`

## Contrato desktop aprovado — 204L gold source

Valores aprovados após microajustes de Lucas:

- `.coll-banner`
  - fundo preto `#101010` via `--lk-v2-bg`
  - `padding: 40px clamp(28px,3.2vw,44px) 9px !important`
  - `margin-bottom: 0 !important`
  - mesma distância lateral da seção `.lk-collection-v2`; usar a seção como fonte de verdade.
- `.coll-banner__crumbs`
  - `font-size: 10px`
  - `line-height: 1.6`
  - `letter-spacing: .15em`
  - `margin: 0 0 14px`
  - topo do breadcrumb é a régua vertical para o topo da collage.
- `.coll-banner__title`
  - fonte: `Cormorant Garamond`
  - `font-size: clamp(42px,3.66vw,50px) !important`
  - computed aprovado no viewport validado: ~`46.85px`
  - `line-height: 1.04`
  - `max-width: min(48vw,620px)`
- `.lk-collection-v2`
  - `padding: 16px clamp(28px,3.2vw,44px) 30px !important`
  - `border-bottom: 1px solid #242424`
  - `box-shadow: 0 -1px 0 var(--lk-v2-bg)`
- `.lk-collection-v2__inner`
  - `max-width: 1440px`
  - grid desktop: `minmax(360px,.44fr) minmax(520px,.56fr)`
  - gap: `clamp(38px,4vw,64px)`
- `.lk-collection-v2__eyebrow`
  - texto aprovado: `Curadoria LK`
  - `font-size: 10px`
  - `letter-spacing: .19em`
  - `margin: 0 0 8px`
- `.lk-collection-v2__headline`
  - fonte: `Cormorant Garamond`
  - desktop médio aprovado: `32px` no breakpoint `990–1280px`
  - regra base: `clamp(30px,2.7vw,42px)`
  - `line-height: 1.02`
- `.lk-collection-v2__body`
  - `font-size: clamp(13.5px,.95vw,15.5px)`
  - em `990–1280px`: `14px`, `line-height: 1.62`
- `.lk-collection-v2__media`
  - grid collage: `1.08fr .92fr`, duas linhas
  - altura base: `clamp(340px,30vw,420px)`; em `990–1280px`: `372px`
  - desktop lift aprovado: `transform: translateY(-102px) !important`
  - compensação: `margin-bottom: -102px !important`
  - deve ficar acima visualmente do fundo do banner sem o banner cobrir as imagens.

## Invariantes de validação desktop

Antes de dizer que uma coleção está “igual ao padrão”, validar no browser:

- `titleFont` próximo do gold source no mesmo viewport.
- `titleLeft`, `crumbLeft`, `.lk-collection-v2__inner`/copy left com diferença **0px ou visualmente imperceptível**.
- `mediaTopMinusCrumbTop` próximo de `0–2px` no viewport de validação; na gold source final ficou ~`1.7px`.
- `bannerPaddingBottom` = `9px`.
- `rootPaddingTop` = `16px`.
- `eyebrowMarginBottom` = `8px`.
- `mediaTransform` = `translateY(-102px)` no desktop aprovado.
- Screenshot sem barra/máscara artificial evidente e sem sobreposição indesejada do `.coll-banner` sobre a collage.

Snippet de validação:

```js
(() => {
  const banner = document.querySelector('.coll-banner');
  const root = document.querySelector('.lk-collection-v2');
  const crumb = document.querySelector('.coll-banner__crumbs');
  const title = document.querySelector('.coll-banner__title');
  const inner = document.querySelector('.lk-collection-v2__inner');
  const copy = document.querySelector('.lk-collection-v2__copy');
  const media = document.querySelector('.lk-collection-v2__media');
  const eyebrow = document.querySelector('.lk-collection-v2__eyebrow');
  const headline = document.querySelector('.lk-collection-v2__headline');
  return {
    titleFont: getComputedStyle(title).fontSize,
    titleLeft: +title.getBoundingClientRect().left.toFixed(2),
    crumbLeft: +crumb.getBoundingClientRect().left.toFixed(2),
    innerLeft: +inner.getBoundingClientRect().left.toFixed(2),
    copyLeft: +copy.getBoundingClientRect().left.toFixed(2),
    leftDiffTitleVsInner: +(title.getBoundingClientRect().left - inner.getBoundingClientRect().left).toFixed(2),
    mediaTopMinusCrumbTop: +(media.getBoundingClientRect().top - crumb.getBoundingClientRect().top).toFixed(2),
    bannerPaddingBottom: getComputedStyle(banner).paddingBottom,
    rootPaddingTop: getComputedStyle(root).paddingTop,
    eyebrowMarginBottom: getComputedStyle(eyebrow).marginBottom,
    visualGapEyebrowHeadline: +(headline.getBoundingClientRect().top - eyebrow.getBoundingClientRect().bottom).toFixed(2),
    mediaTransform: getComputedStyle(media).transform
  };
})()
```

## Processo obrigatório para replicar em próximas coleções

1. Criar implementação no Dev Theme `155065450718`.
2. Usar a 204L aprovada como gold source e comparar no mesmo viewport/sessão.
3. Trocar apenas conteúdo, assets e modificador de handle; preservar o contrato visual.
4. Validar computed styles e screenshot.
5. Enviar preview com `preview_theme_id=155065450718` e cache-buster `lkqa=...`.
6. Produção só com aprovação explícita de Lucas, rollback e receipt.

## Não fazer

- Não corrigir cada handle com mais `:has(...)`/hotfix específico como estratégia principal.
- Não publicar production sem preview aprovado.
- Não declarar paridade apenas por métrica de DOM; validar screenshot e tipografia real.
- Não trocar a linguagem aprovada por labels como “Sinal editorial”; usar vocabulário premium e minimalista, como `Curadoria LK`.
- Não mudar espaçamentos por intuição quando Lucas pedir porcentagem; aplicar a redução/aumento literal e compensar media lift apenas quando necessário.
