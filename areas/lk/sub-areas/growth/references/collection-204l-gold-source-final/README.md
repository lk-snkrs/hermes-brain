# LK Collection Gold Source — New Balance 204L final aprovado

Status: **APROVADO POR LUCAS COMO PADRÃO CANÔNICO**.
Data de consolidação: 2026-05-29.
Fonte visual pública aprovada: `https://lksneakers.com.br/collections/new-balance-204l`.
Theme production usado no receipt final: `155065417950`.

Este diretório congela o padrão aprovado da coleção 204L para ser clonado/adaptado nas próximas coleções LK. A regra é preservar o layout e trocar apenas conteúdo/assets/copy da coleção-alvo, validando desktop e mobile contra a 204L.

## Arquivos congelados

Os arquivos abaixo são cópias exatas do receipt final aprovado. Não resumir estes arquivos como fonte única; usar como snapshot literal quando precisar reproduzir “cada detalhe”.

```json
{
  "section.after.liquid": {
    "bytes": 207234,
    "sha256": "adb00572edcc0e0f07ce6c2fbd486f22d049f3136d45e6c502d2ad930ea1d6ff"
  },
  "section.readback.liquid": {
    "bytes": 207234,
    "sha256": "adb00572edcc0e0f07ce6c2fbd486f22d049f3136d45e6c502d2ad930ea1d6ff"
  },
  "validation.json": {
    "bytes": 545,
    "sha256": "45047b0875dfbeec2f24c96d026de80534f2653bbf0a57e52d3e508e6d62c23e"
  },
  "receipt.json": {
    "bytes": 535,
    "sha256": "72d4743d8163ca8ca0027f4e4e336df2ad786d3655c75e66210a9a5984e607dc"
  }
}
```

Diretório do snapshot canônico:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/references/collection-204l-gold-source-final`

Receipt original:
`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-production/204l-mobile-h1-section-inline-20260529T131402Z`

## Contrato canônico resumido

- Página de coleção é **product-first**: header/hero editorial → grid de produtos → Guia Editorial LK pós-grid.
- H1 serifado premium em `Cormorant Garamond`.
- Fundo hero/coleção 204L escuro `#101010`; texto branco; linguagem mínima, premium e comercial.
- Kicker: `Curadoria LK`.
- Desktop: collage editorial à direita; copy à esquerda; hero compacto, sem empurrar excessivamente o grid.
- Mobile: breadcrumb oculto; H1 em uma linha quando couber; texto curto; mídia colapsada com “Ler mais”/reveal; grid de produto preserva prioridade.
- Guia pós-grid: off-white, H2 serifado, card branco em duas colunas no desktop, FAQ à direita alinhado ao topo, helper claro + CTA preto.
- FAQ/schema: FAQPage único; FAQ legado não deve duplicar o guia.

## Valores aprovados que não podem driftar sem nova aprovação

### Header / H1 / espaçamento

- `.coll-banner`: `padding: 40px clamp(28px,3.2vw,44px) 9px` no desktop; `padding: 28px 16px 0` no mobile.
- `.coll-banner__title`: `Cormorant Garamond`, `line-height: 1.04` desktop, `line-height: 1.02` mobile.
- Mobile final aprovado para 204L: `font-size: clamp(32px, 9.7vw, 38px)`, `white-space: nowrap`, `max-width: calc(100vw - 32px)`, `display: inline-block`.
- Breadcrumb oculto no mobile.

### Hero editorial / collage

- Namespace base novo: `.lk-collection-v2`; legado 204L em produção usa `.lk-204l-coll-preview` como fonte histórica.
- Desktop aprovado: grid texto/mídia, collage à direita, cards sem borda arredondada agressiva, imagem com `object-fit: cover`.
- Mobile aprovado: conteúdo em coluna única; body com clamp curto; collage colapsada (`max-height: 78px`) e expandida em duas colunas (`gap: 9px`, `max-height: 860px`).

### Guia pós-grid

- Fundo externo off-white/claro com borda sutil.
- Kicker: `GUIA EDITORIAL LK`.
- H2 serifado grande.
- Card interno branco com grid desktop:
  - esquerda: orientação prática “Como escolher...”;
  - direita: FAQ;
  - `border-left: 1px solid #e2dbd0` no desktop;
  - `margin-top: 0`, `padding-top: 0`, `border-top: 0` no FAQ desktop;
  - mobile troca para `margin-top: 24px`, `padding-top: 22px`, `border-top: 1px solid #e2dbd0`.
- Rodapé: helper/note claro à esquerda + CTA preto à direita.

## Extratos literais do snapshot

Os extratos abaixo são apenas para leitura rápida. A reprodução literal deve usar os arquivos congelados acima.

## 204L hero CSS block

```liquid
/* === LK 204L dev preview — mobile reveal source block === */
  :root{--lk-204l-bg:#101010;--lk-204l-fg:#fff;--lk-204l-muted:#d5d5d5;--lk-204l-soft:#9c9c9c}
  body:has(.lk-204l-coll-preview) .coll-banner{margin-bottom:0!important}
  body:has(.lk-204l-coll-preview) .coll-banner,body:has(.lk-204l-coll-preview) .coll-banner > *,body:has(.lk-204l-coll-preview) .coll-banner .container,body:has(.lk-204l-coll-preview) .coll-banner__inner,body:has(.lk-204l-coll-preview) .coll-banner__content,body:has(.lk-204l-coll-preview) .coll-banner__title,body:has(.lk-204l-coll-preview) .coll-banner__crumbs{background:var(--lk-204l-bg)!important;background-color:var(--lk-204l-bg)!important;color:var(--lk-204l-fg)!important;border:0!important;box-shadow:none!important}
  body:has(.lk-204l-coll-preview) .coll-banner:before,body:has(.lk-204l-coll-preview) .coll-banner:after,body:has(.lk-204l-coll-preview) .coll-banner *:before,body:has(.lk-204l-coll-preview) .coll-banner *:after{background:transparent!important;box-shadow:none!important;border:0!important}
  body:has(.lk-204l-coll-preview) .coll-banner__desc-wrap{display:none!important}
  body:has(.lk-204l-coll-preview) [aria-label="Benefícios LK Sneakers"]{display:none!important}
  .lk-204l-coll-preview{background:var(--lk-204l-bg)!important;background-color:var(--lk-204l-bg)!important;border-top:0!important;border-bottom:1px solid #242424;padding:clamp(28px,3vw,42px) clamp(22px,2.2vw,34px) 34px;color:var(--lk-204l-fg);box-shadow:0 -1px 0 var(--lk-204l-bg)!important}
  .lk-204l-coll-preview__inner{width:100%;max-width:none;margin:0;display:grid;grid-template-columns:minmax(0,.46fr) minmax(420px,.54fr);gap:clamp(36px,4.2vw,72px);align-items:start}
  .lk-204l-kicker{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--lk-204l-soft);margin:0 0 12px}.lk-204l-copy h2{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,3.5vw,54px);line-height:1;letter-spacing:-.045em;font-weight:400;color:var(--lk-204l-fg);margin:0 0 18px;max-width:780px}.lk-204l-copy p{font-size:clamp(14px,1.02vw,17px);line-height:1.62;color:var(--lk-204l-muted);margin:0 0 16px;max-width:760px}.lk-204l-read-more{display:none}
  .lk-204l-collage{display:grid;grid-template-columns:1.06fr .94fr;grid-template-rows:1fr 1fr;gap:12px;height:clamp(360px,34vw,450px);min-height:0}.lk-204l-card{position:relative;display:block;overflow:hidden;background:#141414;text-decoration:none;color:#fff;border-radius:0;border:0;padding:0;text-align:left}.lk-204l-card--large{grid-row:1 / span 2}.lk-204l-card img{display:block;width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(.96) contrast(.98)}.lk-204l-card--large img{object-position:center 24%}.lk-204l-card:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.58) 100%)}.lk-204l-card span{position:absolute;left:16px;right:16px;bottom:15px;z-index:1;font-size:11px;line-height:1.35;letter-spacing:.14em;text-transform:uppercase;color:#fff}.lk-204l-open-photo{display:none}
  @media(min-width:990px) and (max-width:1280px){.lk-204l-coll-preview__inner{grid-template-columns:minmax(390px,.48fr) minmax(470px,.52fr);gap:44px}.lk-204l-collage{height:390px}.lk-204l-copy h2{font-size:40px}.lk-204l-copy p{font-size:15px}}
  @media(max-width:989px){
    body:has(.lk-204l-coll-preview) .coll-banner__crumbs{display:none!important}
    body:has(.lk-204l-coll-preview) .coll-banner,body:has(.lk-204l-coll-preview) .coll-banner > *,body:has(.lk-204l-coll-preview) .coll-banner .container,body:has(.lk-204l-coll-preview) .coll-banner__inner,body:has(.lk-204l-coll-preview) .coll-banner__content{padding-bottom:0!important;background:var(--lk-204l-bg)!important;background-color:var(--lk-204l-bg)!important;color:var(--lk-204l-fg)!important}
    .lk-204l-coll-preview{padding:0 16px 16px;background:var(--lk-204l-bg)!important;background-color:var(--lk-204l-bg)!important;color:var(--lk-204l-fg)!important}
    .lk-204l-coll-preview__inner{display:flex;flex-direction:column;gap:0}
    .lk-204l-kicker{font-size:8px;letter-spacing:.16em;margin:0 0 7px;color:var(--lk-204l-soft)!important}
    body:has(.lk-204l-coll-preview) .coll-banner__title{font-size:44px!important;line-height:1.02}
    .lk-204l-copy h2{display:block!important;font-size:24px;line-height:1.04;margin:0 0 10px;color:var(--lk-204l-fg)!important}
    .lk-204l-copy p:not(.lk-204l-kicker){font-size:12px;line-height:1.5;max-width:none;margin:0 0 8px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;color:var(--lk-204l-muted)!important}
    .lk-204l-coll-preview.is-open .lk-204l-copy p:not(.lk-204l-kicker){display:block;-webkit-line-clamp:unset;overflow:visible}
    .lk-204l-read-more{display:inline-flex;align-items:center;justify-content:center;margin:0 0 12px;padding:8px 13px;border:1px solid rgba(255,255,255,.58);background:transparent;color:#fff;font-family:var(--font-body);font-size:9px;line-height:1;letter-spacing:.16em;text-transform:uppercase;border-radius:999px;appearance:none;-webkit-appearance:none}
    .lk-204l-coll-preview.is-open .lk-204l-read-more{display:none!important}
    .lk-204l-collage{order:2;position:relative;display:grid!important;grid-template-columns:1fr;gap:0;margin-top:0;width:100%;height:auto;max-height:78px;overflow:hidden;background:var(--lk-204l-bg)!important;transition:max-height .55s cubic-bezier(.2,.8,.2,1)}
    .lk-204l-collage:after{content:"";position:absolute;left:0;right:0;bottom:0;height:42px;z-index:5;pointer-events:none;background:linear-gradient(to bottom,rgba(16,16,16,0) 0%,rgba(16,16,16,.38) 48%,var(--lk-204l-bg) 100%)}
    .lk-204l-collage.is-open{grid-template-columns:1fr 1fr;grid-template-rows:auto auto;gap:9px;max-height:860px;margin-top:8px}
    .lk-204l-collage.is-open:after{display:none}
    .lk-204l-card{position:relative;inset:auto;display:block!important;opacity:1!important;animation:none!important;aspect-ratio:1/1;min-height:0;background:#111;border:0;padding:0;text-align:left;appearance:none;-webkit-appearance:none}
    .lk-204l-card--large{grid-column:1;grid-row:auto;aspect-ratio:16/3.2;cursor:pointer;width:100%}
    .lk-204l-collage:not(.is-open) .lk-204l-card:not(.lk-204l-card--large){display:none!important}
    .lk-204l-collage.is-open .lk-204l-card--large{grid-column:1 / -1;aspect-ratio:16/10}
    .lk-204l-card img{width:100%;height:100%;object-fit:cover;object-position:center 48%;padding:0}
    .lk-204l-card span{left:10px;right:10px;bottom:10px;font-size:8.5px;letter-spacing:.11em;line-height:1.25;z-index:2}
    .lk-204l-open-photo{display:none!important}
  }
```
## 204L guide/FAQ correction CSS

```liquid
/* === LK Moon Shoe strict 204L footer/FAQ correction === */
  body:has(.lk-204l-coll-preview) .lk-moon-guide-after-grid{display:none!important}
  body:has(.lk-204l-coll-preview) .coll-enrichment{background:#fff!important;color:#0a0a0a!important}
  body:has(.lk-204l-coll-preview) .coll-faq h2,
  body:has(.lk-204l-coll-preview) .coll-faq__q{color:#0a0a0a!important;opacity:1!important;visibility:visible!important}
  body:has(.lk-204l-coll-preview) .coll-faq__item{border-color:#e2e2e2!important}
  body:has(.lk-204l-coll-preview) .coll-faq__a > div{color:#5f5f5f!important;opacity:1!important;visibility:visible!important}
```


## QA obrigatório para aplicar em outra coleção

1. Abrir 204L e coleção-alvo na mesma sessão/viewport/theme.
2. Comparar desktop e mobile separadamente.
3. Confirmar H1 serifado, largura e quebra de linha.
4. Confirmar produto antes do guia.
5. Confirmar guia pós-grid completo, não apenas FAQ.
6. Confirmar FAQ legado ausente e `FAQPage` único.
7. Confirmar sem termos públicos proibidos: estoque, encomenda, pronta entrega.
8. Enviar preview dev para aprovação antes de production.

Última consolidação técnica: 2026-05-29T13:19:22Z.
