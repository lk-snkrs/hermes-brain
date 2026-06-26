# Failure Audit — Puma V2 ainda não fiel ao 204L

Data UTC: 20260606T191557Z
Status: **FAIL_CONFIRMED / DO_NOT_MERGE**

## O que Lucas reportou

- Hero continua diferente.
- “Ler mais” não aparece/está incorreto.
- Guia pós-grid continua diferente do padrão 204L.

## Por que eu errei de novo

Eu corrigi usando o bloco `new-balance-204l` dentro do snippet como se ele fosse a fonte visual final. Isso foi insuficiente.

O padrão correto era comparar e reproduzir o **DOM real renderizado da 204L em production**, não confiar no bloco interno que parecia ser 204L.

Além disso, meu QA de classe/Jaccard foi fraco: ele mediu classes LKGOC agregadas no DOM, mas não fez equivalência visual/funcional real do hero e guia, incluindo “Ler mais”.

## Checks

```json
{
  "gold_hero_extracted": true,
  "puma_hero_extracted": true,
  "gold_guide_extracted": true,
  "puma_guide_extracted": true,
  "gold_has_ler_mais": true,
  "puma_has_ler_mais": true,
  "hero_class_exact": true,
  "guide_class_exact": false,
  "puma_guide_after_grid": true
}
```

## Violações

- Classes/estrutura do guia Puma não são exatamente iguais às do guia 204L real em production.

## Decisão

- Puma DEV V2: **reprovada**.
- Production: **continua bloqueado**.
- Próxima correção deve usar o DOM/estrutura real da 204L production como contrato, incluindo “Ler mais” e guia pós-grid exatamente no mesmo padrão.

## Artefatos

- Gold hero: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-v2-failure-audit-20260606T191557Z/gold-hero-section.html`
- Puma hero: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-v2-failure-audit-20260606T191557Z/puma-hero-section.html`
- Gold guide: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-v2-failure-audit-20260606T191557Z/gold-guide-section.html`
- Puma guide: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-v2-failure-audit-20260606T191557Z/puma-guide-section.html`
- Metrics: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/audits/lkgoc-puma-v2-failure-audit-20260606T191557Z/METRICS.json`
