# QA — 204L benchmark + Onitsuka/Mind002 cache recheck — 2026-06-22

**Pedido Lucas:** fazer 2 e 3.  
**Status:** read-only; writes externos 0; values_printed=false.  
**Gerado:** 2026-06-22T20:10:05.609480+00:00.

## 1. New Balance 204L — benchmark QA

### Public QA

| URL | HTTP | Title | H1 | FAQPage | Canonical | Liquid error |
|---|---:|---|---:|---:|---|---|
| `/collections/new-balance-204l` | 200 | New Balance 204L Original | LK Sneakers | 1 | 1 | self | não |
| `/pages/new-balance-204l-original-brasil-guia-lk` | 200 | New Balance 204L Original | Guia LK | 1 | 1 | self | não |

### Schema e estrutura

- Collection 204L: `CollectionPage`, `ItemList`, `FAQPage`, `BreadcrumbList`, Organization/local schema presentes.
- Guia 204L: `WebPage`, `FAQPage`, `BreadcrumbList`, `WebSite`, Organization/local schema presentes.
- Collection tem **FAQPage único com 4 perguntas**.
- Guia tem **FAQPage único com 12 perguntas**.
- Linkagem interna forte:
  - collection → guia: 2 ocorrências.
  - guia → collection: 35 ocorrências.

### GSC 28d

| Grupo | Cliques | Impressões | CTR | Posição |
|---|---:|---:|---:|---:|
| 204L collection | 75 | 7362 | 1.02% | 8.45 |
| 204L queries | 92 | 8194 | 1.12% | 7.35 |

### GA4 orgânico 28d

- 204L total detectado no top-pages: **272 sessões / 256 usuários / 447 pageviews**.
- Collection `/collections/new-balance-204l`: **143 sessões / 236 pageviews / engagement 71,3%**.

### Veredito 204L

204L segue saudável como benchmark técnico/comercial. **Não recomendo rewrite.**  
Oportunidade futura é só fina: melhorar CTR da collection se a query `204l` continuar com CTR ~1%, mas sem mexer no padrão visual agora.

## 2. Onitsuka — cache recheck

| URL | HTTP | H1 | FAQPage | Guia LK | Bloco citável | Legacy marker |
|---|---:|---:|---:|---:|---:|---:|
| plain | 200 | 1 | 1 | 2 | 2 | 1 |
| cachebuster | 200 | 1 | 1 | 1 | 1 | 0 |

### Veredito Onitsuka

- O **cachebuster está limpo**: 1 guia, 1 bloco citável, legacy ausente.
- A URL plain ainda retornou HTML antigo nesta amostra: 2 guias, 2 blocos citáveis, legacy marker 1.
- Interpretação: source está limpo, mas ainda há **cache/CDN residual** na URL sem query. Não fazer novo write.

## 3. Mind 002 — cache/head recheck

| PDP | Title/meta novo público? | H1 | FAQPage | Canonical | Liquid error |
|---|---:|---:|---:|---|---|
| Black Hyper Crimson | sim | 1 | 1 | self | não |
| Light Khaki | sim | 1 | 1 | self | não |
| Thunder Blue | sim | 1 | 1 | self | não |
| Light Smoke Grey | **não nesta amostra** | 1 | 1 | self | não |

### Veredito Mind 002

- 3/4 PDPs já refletem title/meta novo publicamente.
- Light Smoke Grey ainda retornou title/meta antigo nesta amostra, apesar de Admin readback já estar correto no receipt anterior.
- Não fazer novo write; revalidar em 24h.

## Próxima ação recomendada

1. **Não mexer em 204L** — preservar benchmark.
2. **Não mexer em Onitsuka/Mind002 hoje** — aguardar cache e medir D+7.
3. Próximo bloco com write potencial deve ser GMC micro-piloto, separado.

## Artefatos

- QA público: `growth/work/qa-204l-onitsuka-mind002-cache-20260622/qa-204l-onitsuka-mind002-cache.json`
- GSC 204L: `growth/work/qa-204l-onitsuka-mind002-cache-20260622/gsc-204l-28d-readonly.json`
- GA4 204L: `growth/work/qa-204l-onitsuka-mind002-cache-20260622/ga4-204l-28d-readonly.json`
