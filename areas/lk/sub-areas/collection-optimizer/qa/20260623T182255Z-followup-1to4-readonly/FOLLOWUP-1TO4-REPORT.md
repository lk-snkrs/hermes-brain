# LKGOC/Growth — Execução 1 ao 4 — QA read-only + backlog

**Gerado:** 2026-06-23T18:25:18.603620+00:00  
**Writes externos:** 0  
**values_printed:** false  
**Pasta:** `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T182255Z-followup-1to4-readonly`

## 1) Crocs McQueen — handle correto

| URL testada | HTTP | Canonical | Veredito |
|---|---:|---|---|
| `/collections/crocs` | 200 | `https://lksneakers.com.br/collections/crocs` | ✅ ativa |
| `/collections/crocs-relampago-mcqueen` | 200 | `https://lksneakers.com.br/collections/crocs-relampago-mcqueen` | ✅ ativa |
| `/collections/crocs-mcqueen` | 200 | `https://lksneakers.com.br/collections/crocs-mcqueen` | ✅ canônica/ativa |
| `/collections/crocs-baya-alexander-mcqueen` | 404 | `https://lksneakers.com.br/404` | ❌ não usar |

**Conclusão:** a URL que eu havia auditado antes estava errada. O handle correto para a collection é **`/collections/crocs-mcqueen`**. Também existe `/collections/crocs-relampago-mcqueen` ativa.

## 2) QA visual mobile/desktop

| Página | Mobile | Desktop | Status |
|---|---|---|---|
| 204l | `204l-mobile.png` | `204l-desktop.png` | ✅ screenshots gerados |
| onitsuka | `onitsuka-mobile.png` | `onitsuka-desktop.png` | ✅ screenshots gerados |
| nike-mind | `nike-mind-mobile.png` | `nike-mind-desktop.png` | ✅ screenshots gerados |
| vomero | `vomero-mobile.png` | `vomero-desktop.png` | ✅ screenshots gerados |
| alo-yoga | `alo-yoga-mobile.png` | `alo-yoga-desktop.png` | ✅ screenshots gerados |
| handball | `handball-mobile.png` | `handball-desktop.png` | ✅ screenshots gerados |
| 1906l | `1906l-mobile.png` | `1906l-desktop.png` | ✅ screenshots gerados |
| aj1-low | `aj1-low-mobile.png` | `aj1-low-desktop.png` | ✅ screenshots gerados |
| crocs-mcqueen | `crocs-mcqueen-mobile.png` | `crocs-mcqueen-desktop.png` | ✅ screenshots gerados |

Observação: esta etapa validou renderização headless e gerou evidência visual. Não fiz write. Revisão humana/visual fina ainda é recomendada antes de qualquer promoção ou novo ajuste visual.

## 3) Backlog de nivelamento GEO/LKGOC

| Prioridade | Superfície | Achado | Recomendação | Approval |
|---|---|---|---|---|
| P1 | Alo Yoga | sem FAQPage/schema FAQ detectado; sem Guia editorial LK detectado; sem Bloco citável LK detectado | Preparar DEV/unpublished LKGOC Lite: copy citável + FAQ único + schema FAQPage, copiando padrão 204L; production só com approval. | DEV/unpublished pode ser preview; production precisa approval explícito. |
| P2 | Adidas Handball Spezial | sem FAQPage/schema FAQ detectado; sem Guia editorial LK detectado; sem Bloco citável LK detectado | Preparar DEV/unpublished LKGOC Lite: copy citável + FAQ único + schema FAQPage, copiando padrão 204L; production só com approval. | DEV/unpublished pode ser preview; production precisa approval explícito. |
| P2 | New Balance 1906L | sem FAQPage/schema FAQ detectado; sem Guia editorial LK detectado; sem Bloco citável LK detectado | Preparar DEV/unpublished LKGOC Lite: copy citável + FAQ único + schema FAQPage, copiando padrão 204L; production só com approval. | DEV/unpublished pode ser preview; production precisa approval explícito. |
| P2 | Air Jordan 1 Low | sem FAQPage/schema FAQ detectado; sem Guia editorial LK detectado; sem Bloco citável LK detectado | Preparar DEV/unpublished LKGOC Lite: copy citável + FAQ único + schema FAQPage, copiando padrão 204L; production só com approval. | DEV/unpublished pode ser preview; production precisa approval explícito. |
| P1 | Crocs McQueen | sem FAQPage/schema FAQ detectado; sem Guia editorial LK detectado; sem Bloco citável LK detectado | Usar handle correto `/collections/crocs-mcqueen`; preparar LKGOC/AI Visibility Lite a partir do padrão já existente de Crocs Relâmpago/McQueen; production só com approval. | DEV/unpublished pode ser preview; production precisa approval explícito. |

## 4) 204L preservado

- 204L segue como benchmark/gold source.
- Nenhuma mudança proposta para 204L agora.
- Usar 204L como referência de estrutura, densidade editorial, FAQ único e bloco citável para próximos DEV previews.

## Próxima decisão sugerida

Executar o próximo bloco em **DEV/unpublished** para as páginas P1:

1. Crocs McQueen — corrigir rota no backlog e preparar LKGOC Lite/FAQ/schema em DEV.
2. Alo Yoga — nivelar com FAQPage/bloco citável/Guia LK em DEV.

Produção somente após preview + QA + aprovação explícita.

## Artefatos

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T182255Z-followup-1to4-readonly/01-crocs-handle-check.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T182255Z-followup-1to4-readonly/02-visual-screenshot-manifest.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T182255Z-followup-1to4-readonly/03-backlog-input-qa.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T182255Z-followup-1to4-readonly/04-backlog-lkgoc-leveling.json`