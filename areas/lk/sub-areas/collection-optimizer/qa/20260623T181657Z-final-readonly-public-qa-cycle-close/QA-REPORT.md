# QA final read-only — fechamento de ciclo LKGOC/Growth

**Gerado:** 2026-06-23T18:20:21.179291+00:00  
**Writes externos:** 0  
**values_printed:** false  
**Pasta:** `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T181657Z-final-readonly-public-qa-cycle-close`

## Coleções

| Superfície | HTTP | H1 | FAQPage | Guia LK | Bloco citável | Liquid error | Veredito |
|---|---:|---:|---:|---:|---:|---:|---|
| 204L | 200 | 1 | 1 | 2 | 1 | não | ✅ limpo |
| Onitsuka broad | 200 | 1 | 1 | 1 | 2 | não | ✅ limpo |
| Nike Mind 001/002 | 200 | 1 | 1 | 0 | 0 | não | ✅ limpo |
| Vomero | 200 | 1 | 1 | 0 | 0 | não | ✅ limpo |
| Alo Yoga | 200 | 1 | 0 | 0 | 0 | não | ⚠️ sem FAQPage |
| Crocs McQueen | 404 | 1 | 0 | 0 | 0 | não | ⚠️ HTTP 404 |
| Adidas Handball Spezial | 200 | 1 | 0 | 0 | 0 | não | ⚠️ sem FAQPage |
| New Balance 1906L | 200 | 1 | 0 | 0 | 0 | não | ⚠️ sem FAQPage |
| Air Jordan 1 Low | 200 | 1 | 0 | 0 | 0 | não | ⚠️ sem FAQPage |

## PDPs Nike Mind 002

| PDP | HTTP | Title público | FAQPage | Product schema | Liquid error | Veredito |
|---|---:|---|---:|---:|---:|---|
| Mind002 Black Hyper Crimson | 200 | Tênis Nike Mind 002 Black Hyper Crimson Original \| LKAmerican ExpressDiners ClubEloJCBMastercardVisa | 1 | 1 | não | ✅ limpo |
| Mind002 Light Khaki | 200 | Nike Mind 002 Light Khaki Original no Brasil \| LKAmerican ExpressDiners ClubEloJCBMastercardVisa | 1 | 1 | não | ✅ limpo |
| Mind002 Thunder Blue | 200 | Nike Mind 002 Thunder Blue Original no Brasil \| LKAmerican ExpressDiners ClubEloJCBMastercardVisa | 1 | 1 | não | ✅ limpo |
| Mind002 Light Smoke Grey | 200 | Nike Mind 002 Light Smoke Grey Original no Brasil \| LKAmerican ExpressDiners ClubEloJCBMastercardVisa | 1 | 1 | não | ✅ limpo |

## Leitura

- **204L, Onitsuka, Nike Mind e Vomero**: base técnica pública limpa no essencial: HTTP 200, H1 único, FAQPage único, sem Liquid error.
- **Mind 002 PDPs**: SEO titles públicos aparecem com os novos títulos; FAQPage e Product schema únicos; sem Liquid error.
- **Alo, Adidas Handball, 1906L e Air Jordan 1 Low**: HTTP 200/H1 único/sem Liquid error, mas sem FAQPage detectado nesta leitura pública. Isso pode ser intencional ou indicar que ainda não estão no mesmo nível GEO/FAQ do padrão 204L.
- **Crocs McQueen**: URL auditada retornou 404. Precisa localizar handle correto antes de qualquer recomendação; não tratar como erro de SEO sem confirmar a URL canônica.

## Próximos passos recomendados

1. Localizar handle correto de Crocs McQueen ou confirmar se a coleção saiu do ar.
2. Fazer QA visual mobile/desktop nas páginas limpas tecnicamente, porque esta rodada foi HTML/head/schema, não screenshot.
3. Manter 204L como benchmark; não mexer.
4. Agendar/rodar impact review GSC/GA4 D+7/D+14 dos writes de 19/06 e 22/06.
5. Só depois decidir GMC batch 100 ou ajustes incrementais em Mind/Onitsuka.

## Artefatos

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T181657Z-final-readonly-public-qa-cycle-close/collections-summary.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/qa/20260623T181657Z-final-readonly-public-qa-cycle-close/mind002-pdp-summary.json`