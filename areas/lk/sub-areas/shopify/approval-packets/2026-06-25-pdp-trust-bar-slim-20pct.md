# Approval packet — PDP Trust Bar 20% mais slim

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — PDP / Trust Bar
- **Pedido do Lucas:** “conseguimos deixar mais slim a TRUST BAR da PDP? diminuir em 20% a altura dela?”
- **Screenshot referência:** `/opt/data/profiles/lk-shopify/image_cache/img_12386ee25f14.jpg`
- **Status:** patch local preparado; nenhum write Shopify/GitHub executado ainda.

## Evidência

Production source atual lido via GitHub `production`:

- arquivo alvo: `sections/lk-pdp.liquid`
- snapshot local: `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/prod_sections_lk-pdp.liquid`
- sha256 antes: `bf637b1dbaf5055fedd45d0865da9c58c573209fdd9c28cec09e369d39946f2f`

CSS atual relevante:

- `.lk-tg__item` com `gap: 6px`, `padding: 16px 8px`, `min-height: 88px`.
- ícones desktop `20px`.
- stars `12px`.
- label `8.6px`.
- mobile `.lk-trust-grid` com `height/min-height: 52px`.

## Interpretação

Sim, dá para deixar aproximadamente **20% mais slim** sem mudar conteúdo, ordem ou prova social.

A redução precisa mexer nos elementos que formam a altura real:

- altura mínima do item;
- padding vertical;
- gap entre ícone/texto;
- tamanho dos ícones/stars;
- ajuste equivalente no mobile.

## Patch proposto

Arquivo alvo:

- `sections/lk-pdp.liquid`

Target local:

- `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/target_sections__lk-pdp.liquid`
- sha256 depois: `42b4c4a97f443039cc59b03aeb6c103f05f8cf19e58ac7b7b6ae85b794bc1d00`

Mudanças principais:

| Elemento | Antes | Depois | Delta |
|---|---:|---:|---:|
| `.lk-tg__item min-height` | `88px` | `70px` | **-20.5%** |
| `.lk-tg__item padding` | `16px 8px` | `12px 8px` | menor |
| `.lk-tg__item gap` | `6px` | `5px` | menor |
| ícone desktop | `20px` | `18px` | menor |
| stars | `12px` | `10px` | menor |
| label desktop | `8.6px` | `8.2px` | levemente menor |
| mobile trust grid | `52px` | `42px` | **-19.2%** |
| mobile icon | `13px` | `11px` | menor |

Conteúdo permanece igual:

- Google / avaliações;
- autenticidade;
- parcelamento;
- frete;
- troca;
- loja física.

## Preview local

Preview renderizado localmente:

- HTML: `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/trust_bar_slim_preview.html`
- PNG: `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/trust_bar_slim_preview.png`
- geometria: `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/preview_geometry.json`

Static QA:

- arquivo: `/opt/data/profiles/lk-shopify/workdirs/pdp-trust-bar-slim-20260625/static_qa.json`
- Google count unchanged: yes
- changed files: `sections/lk-pdp.liquid` only

## QA planejado após aprovação

1. Upload em DEV/unpublished `lk-new-theme/dev`.
2. Readback Admin por SHA.
3. Browser/PDP em desktop e mobile:
   - Trust Bar visível e legível;
   - altura visual mais slim;
   - Google Reviews trigger ainda funciona;
   - blocos continuam alinhados 3×2 desktop;
   - mobile continua sem quebra visual.
4. Se DEV passar e Lucas aprovar Production junto, abrir PR/merge para `production`, readback Shopify e QA público.

## Risco

Baixo/médio:

- é CSS de PDP, mas afeta bloco de confiança próximo à conversão;
- redução excessiva pode diminuir legibilidade em mobile;
- mitigação: ajuste é moderado e preserva texto/estrutura.

## Rollback

- Reverter o hunk CSS em `sections/lk-pdp.liquid`.
- Em Production: revert PR/commit correspondente.
- Readback confirmando `min-height: 88px` e mobile `52px` restaurados.

## Próxima decisão

Para aplicar em DEV e, se QA passar, promover via PR/merge Production:

`Aprovo DEV e merge Production PDP Trust Bar 20% slim`
