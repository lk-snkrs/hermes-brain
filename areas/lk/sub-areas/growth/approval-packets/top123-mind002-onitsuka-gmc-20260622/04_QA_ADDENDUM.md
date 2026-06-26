# QA Addendum — Top 1-2-3 — 2026-06-22

**Status:** read-only; writes externos 0; values_printed=false.  
**Gerado:** 2026-06-22T17:51:15.275930+00:00  
**Arquivo QA:** `growth/work/top123-20260622/top123-public-qa-readonly.json`

## Achados principais

### Nike Mind 002

- `/collections/nike-mind-002`: 404, então não existe collection pública própria.
- Shopify read-only encontrou 7 PDPs ativos Mind 002, todos associados à collection `nike-mind-001`.
- Hub `/collections/nike-mind-001` já renderiza title/meta com “Nike Mind 001 e 002”, H1 único e FAQPage único.
- PDPs amostrados:
  - Black Hyper Crimson: HTTP 200, H1 único, FAQPage 1 com 2 perguntas.
  - Light Smoke Grey: HTTP 200, H1 único, FAQPage 1 com 2 perguntas.
- Implicação: próximo passo é **medição/arquitetura**, não criar collection separada às cegas.

### Onitsuka

- Broad `/collections/onitsuka-tiger-todos-os-modelos`: HTTP 200, H1 único, FAQPage único com 5 perguntas.
- Mexico 66 `/collections/onitsuka-tiger-mexico-66`: HTTP 200, H1 único, FAQPage único com 5 perguntas.
- Broad tem 2 ocorrências de “Guia editorial LK” e 2 “Bloco citável LK”; schema não duplica, mas visual/copy pode estar redundante.
- Implicação: antes de novo write, fazer cleanup/refino visual/copy leve ou aceitar duplicidade se for intencional. Não reescrever pesado.

### GMC

- Base decision-grade mais recente: `reports/gmc/lk-gmc-product-data-ranking-review-2026-06-18.md`.
- Ação recomendada continua: current-state read-only + micro-piloto; sem write massivo.

## Ordem executiva

1. Mind 002: GSC/GA4 filtered + arquitetura cluster.
2. Onitsuka: cleanup/refino de redundância broad, se aprovado depois.
3. GMC: current-state + micro-piloto Shopify/Simprosys/GMC.
