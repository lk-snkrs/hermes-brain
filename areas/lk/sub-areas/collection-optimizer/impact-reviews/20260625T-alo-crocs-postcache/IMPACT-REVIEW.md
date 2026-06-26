# Impact Review pós-cache — LKGOC Alo Yoga + Crocs McQueen

Data: 2026-06-25  
Escopo: revisão pública pós-cache da promoção LKGOC pós-grid.  
Writes externos: 0.  
Production: somente readback/QA público.  
Gold source comparado: `new-balance-204l`.  
Claude SEO/AEO checklist: aplicado como camada diagnóstica LKGOC via critérios documentados do Brain/AGENTS; sem dados GA4/GSC/GMC.

## Status executivo

**PASS** — produção estabilizada após cache/propagação.

## Readback público

| Coleção | HTTP | H1 | FAQPage | Guia LK | Bloco citável | Liquid error | Pós-grid |
|---|---:|---:|---:|---:|---:|---:|---|
| `alo-yoga-1` | 200 | 1 | 1 | 1 | 1 | não | PASS |
| `crocs-mcqueen` | 200 | 1 | 1 | 1 | 1 | não | PASS |
| `new-balance-204l` benchmark | 200 | 1 | 1 | 2 | 1 | não | PASS básico |

## Sequência produto-first / pós-grid

### Alo Yoga

Sequência textual pública:

`Ordenar:` 3052 → `Mostrando 24 de` 7955 → `Guia editorial LK` 7989

Resultado: **PASS**.

### Crocs McQueen

Sequência textual pública:

`1 itens` 2944 → `Ordenar:` 2952 → `Guia editorial LK` 3419

Resultado: **PASS**.

## Checklist LKGOC / Claude SEO-AEO

| Critério | Alo Yoga | Crocs McQueen | Observação |
|---|---|---|---|
| Produto-first / Guia pós-grid | PASS | PASS | Guia aparece após vitrine/ordenador. |
| H1 único | PASS | PASS | Sem duplicidade de H1. |
| FAQPage único | PASS | PASS | 1 ocorrência bruta de `FAQPage` por página. |
| Bloco citável | PASS | PASS | 1 bloco citável por coleção. |
| Sem Liquid error | PASS | PASS | Nenhum erro público detectado. |
| Sem promessa sensível de estoque/prazo | PASS | PASS | Termos checados: pronta entrega, baixo estoque, prazo específico, tamanho disponível = 0. |
| Gold source preservado | PASS básico | — | 204L segue HTTP 200, H1 1, FAQPage 1, sem Liquid error. |

## Screenshots gerados

- `alo-mobile.png`
- `alo-desktop.png`
- `crocs-mobile.png`
- `crocs-desktop.png`
- `204l-mobile.png`

## Artefatos

- `impact-readback.json`
- HTML público salvo para cada handle.
- Screenshots mobile/desktop citados acima.

## Decisão

Nenhum rollback recomendado. Nenhum ajuste emergencial necessário.

## Observação de qualidade

A contagem textual de “Como escolher” em Alo Yoga ainda aparece maior que 1 por causa de textos auxiliares/SEO no HTML público, mas os sinais críticos estão corretos: `Guia editorial LK = 1`, `FAQPage = 1`, `Bloco citável = 1`, sem Liquid error e guia depois do grid. Não bloqueia.
