# QA pós-publicação — LKGOC Lite Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Escopo aprovado por Lucas: seguir com QA visual/editorial pós-publicação das coleções P1.  
Writes externos: 0  
Produção: somente leitura/fetch/screenshot; nenhum ajuste aplicado.

## Resultado executivo

| Coleção | HTTP | H1 | FAQPage | Guia | Bloco citável | Liquid error | Pós-grid inferido | Veredito |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Alo Yoga | 200 | 1 | 1 | 1 | 1 | não | PASS | ⚠️ PASS técnico, REVIEW editorial |
| Crocs McQueen | 200 | 1 | 1 | 1 | 1 | não | PASS | ⚠️ PASS técnico, REVIEW visual/editorial |
| 204L Gold Source | 200 | 1 | 1 | 2 | 1 | não | PASS | ✅ benchmark preservado |

## Evidência gerada

### Screenshots

| Arquivo | Dimensão | Bytes |
|---|---:|---:|
| `screenshots/alo-desktop-full.png` | 1731×6334 | 1546801 |
| `screenshots/alo-mobile-full.png` | 390×8781 | 645143 |
| `screenshots/crocs-desktop-full.png` | 1731×3625 | 502407 |
| `screenshots/crocs-mobile-full.png` | 390×3569 | 182406 |

### Artefatos

- `qa-summary.json`
- `screenshots/alo-mobile-full.png`
- `screenshots/alo-desktop-full.png`
- `screenshots/crocs-mobile-full.png`
- `screenshots/crocs-desktop-full.png`

## Alo Yoga — achados

**Passou no técnico público:**

- HTTP 200.
- H1 único: `Alo Yoga`.
- `FAQPage` detectado uma vez.
- `Bloco citável LK` detectado uma vez.
- Sem `Liquid error`.
- Conteúdo LKGOC público já aparece na URL plain, indicando propagação do cache.

**Review editorial necessário:**

- O texto extraído mostra duas camadas editoriais parecidas:
  - `Como escolher Alo Yoga` + `Perguntas frequentes`;
  - `Como escolher peças Alo Yoga` + `Perguntas frequentes sobre Alo Yoga`.
- Isso sugere sobreposição entre conteúdo de `descriptionHtml` e bloco/guia já existente, ou densidade acima do ideal para Lite.
- Recomendação: consolidar em **um único bloco pós-grid** mais enxuto, preservando `FAQPage` único e o bloco citável.

## Crocs McQueen — achados

**Passou no técnico público:**

- HTTP 200.
- H1 único: `Crocs McQueen`.
- `FAQPage` detectado uma vez.
- `Bloco citável LK` detectado uma vez.
- Sem `Liquid error`.
- Conteúdo LKGOC público aparece na URL plain, indicando propagação do cache.

**Review visual/editorial necessário:**

- A coleção tem 1 item; portanto o bloco editorial aparece muito próximo do grid. Isso pode ser aceitável, mas precisa de revisão visual fina para garantir que não pareça conteúdo antes da compra.
- O rótulo `Guia editorial LK` aparece no texto extraído antes de `1 itens/Ordenar`, enquanto o conteúdo principal `Como escolher Crocs McQueen` aparece depois. Pode ser artefato de HTML/tema, mas merece correção se visualmente parecer pré-grid.
- Recomendação: manter bloco Lite, mas validar/remover rótulo duplicado/pré-grid se a screenshot confirmar ruído.

## 204L Gold Source

- 204L segue acessível e limpo como benchmark.
- Não há recomendação de alteração no 204L.

## Scorecard LKGOC

| Critério | Alo Yoga | Crocs McQueen |
|---|---:|---:|
| HTTP 200 / sem Liquid error | ✅ | ✅ |
| H1 único | ✅ | ✅ |
| FAQPage único | ✅ | ✅ |
| Bloco citável | ✅ | ✅ |
| Conteúdo pós-grid inferido | ✅ | ⚠️ revisar rótulo/visual |
| Densidade editorial Lite | ⚠️ provável excesso/duplicidade | ✅/⚠️ muito curto, mas coerente com 1 item |
| Gold Source 204L preservado | ✅ | ✅ |
| Pronto para fechar ciclo | ⚠️ não | ⚠️ não |

## Próximo pacote recomendado

Preparar uma **correção DEV/branch, sem production write**, com dois objetivos:

1. **Alo Yoga:** consolidar as duas camadas de FAQ/“Como escolher” em um único bloco Lite premium.
2. **Crocs McQueen:** verificar visualmente se `Guia editorial LK` aparece pré-grid; se sim, ajustar para manter o guia efetivamente pós-grid.

Production só deve receber correção com aprovação explícita e rollback/readback.

## Limites

- Não consultei estoque/disponibilidade.
- Não alterei Shopify, GitHub, tema, collection, descriptionHtml, GMC, Klaviyo ou campanhas.
- Claude SEO não foi executado como ferramenta externa; apliquei critérios documentados LKGOC/SEO/GEO do Brain como fallback diagnóstico.
