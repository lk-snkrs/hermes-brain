# Mind 002 + Onitsuka — Read-only execution + next decision — 2026-06-22

**Pedido Lucas:** fazer 1 e 2.  
**Status:** executado em modo read-only; writes externos 0; values_printed=false.  
**Gerado:** 2026-06-22T19:06:35.794669+00:00.

## Fontes consultadas

- Shopify Admin read-only: PDPs Mind 002 e collections alvo.
- GSC Search Analytics: `sc-domain:lksneakers.com.br`, últimos 28 dias, `query,page`, limite 25.000.
- GA4 top organic pages: 2026-05-25 → 2026-06-21.
- QA público HTML/schema: Mind hub, PDPs Mind 002 amostrados, Onitsuka broad e Mexico 66.
- Theme asset map read-only: production theme `155065417950` para origem de blocos Onitsuka.

## 1. Nike Mind 002 — decisão

### Fatos

- `/collections/nike-mind-002` retorna 404.
- Shopify tem 7 PDPs ativos Mind 002, todos dentro da collection `nike-mind-001`.
- O hub `/collections/nike-mind-001` já comunica `Nike Mind 001 e 002` e está tecnicamente limpo: HTTP 200, H1 único, FAQPage único.
- DataForSEO: `nike mind 002` = 3.600 buscas/mês, transacional.

### GSC últimos 28 dias

| Grupo | Cliques | Impressões | CTR | Posição média ponderada |
|---|---:|---:|---:|---:|
| Queries Mind 002 | 12 | 2.516 | 0,48% | 9,68 |
| Páginas Mind 002 | 14 | 1.972 | 0,71% | 9,60 |
| Hub Mind 001/002 | 128 | 9.107 | 1,41% | 7,43 |

Principais achados:

- Query `nike mind 002` no PDP Black Hyper Crimson: 1.121 impressões, CTR 0,09%, posição 10,6 — maior gargalo de CTR.
- O guia Nike Mind já recebe query `nike mind 002`: 562 impressões, 2 cliques, posição 9,8.
- Algumas linhas GSC aparecem com URLs parametrizadas de Shopping (`currency`, `utm_source`, `variant`, `stkn`) para Mind 002; isso pede QA de canonical/parameter handling antes de criar nova collection.

### GA4 orgânico últimos 28 dias

| Página/grupo | Sessões | Usuários | Pageviews |
|---|---:|---:|---:|
| Hub `/collections/nike-mind-001` | 217 | 207 | 339 |
| PDPs Mind 002 detectados no top-pages | 50 | 50 | 67 |

### Recomendação

**Não criar collection Mind 002 agora.** O hub atual já é 001/002 e concentra mais tráfego. Criar `/collections/nike-mind-002` pode fragmentar sinal sem evidência suficiente.

Próximo pacote proposto:

1. QA canonical/parameter para PDPs Mind 002 que aparecem com URLs parametrizadas no GSC.
2. Ajuste fino no PDP Black Hyper Crimson e/ou linkagem do hub para elevar CTR de `nike mind 002`.
3. Só considerar collection própria se GSC mostrar crescimento sustentado e se houver regra de manutenção clara.

## 2. Onitsuka — decisão

### Fatos

- Broad `/collections/onitsuka-tiger-todos-os-modelos`: HTTP 200, H1 único, FAQPage único, title/meta já fortes.
- Mexico 66 `/collections/onitsuka-tiger-mexico-66`: HTTP 200, H1 único, FAQPage único.
- Shopify Admin broad: templateSuffix `onitsuka-ai-v7`, 160 produtos, SEO title atual `Onitsuka Tiger Original no Brasil | Mexico 66 | LK`.
- Public broad apresenta 2 ocorrências de `Guia editorial LK` e 2 de `Bloco citável LK`; schema não duplica.

### GSC últimos 28 dias

| Página | Cliques | Impressões | CTR | Posição média ponderada |
|---|---:|---:|---:|---:|
| Onitsuka broad | 585 | 50.405 | 1,16% | 6,75 |
| Onitsuka Mexico 66 | 287 | 11.550 | 2,48% | 3,00 |

Principais queries broad:

- `onitsuka tiger`: 106 cliques / 28.677 impressões / CTR 0,37% / posição 7,8.
- `tenis onitsuka tiger`: 46 cliques / 3.570 impressões / CTR 1,29% / posição 4,1.
- `onitsuka tiger brasil`: 78 cliques / 1.276 impressões / CTR 6,11% / posição 3,3.

Principais queries Mexico 66:

- `onitsuka tiger mexico 66`: 136 cliques / 6.361 impressões / CTR 2,14% / posição 2,2.
- `mexico 66`: 27 cliques / 604 impressões / CTR 4,47% / posição 1,4.

### GA4 orgânico últimos 28 dias

| Página | Sessões | Usuários | Pageviews | Engagement |
|---|---:|---:|---:|---:|
| Onitsuka broad | 910 | 808 | 1.820 | 75,6% |
| Onitsuka Mexico 66 | 331 | 320 | 757 | 78,5% |

### Theme/readback

A duplicidade visual da broad provavelmente vem da combinação:

- `sections/lk-collection.liquid` / `snippets/lk-goc-collection.liquid` — guia collection canônico.
- `sections/lk-onitsuka-ai-visibility-v7.liquid` via template `onitsuka-ai-v7` — bloco AI visibility extra.

Isso é o mesmo padrão de redundância visual que acabamos de limpar em Mind/Vomero, mas em Onitsuka o schema já está único.

### Recomendação

**Não mexer em title/meta agora** — já estão bons e aparentemente já incorporam o packet antigo. O ganho mais seguro é limpar o bloco visual extra `lk-onitsuka-ai-visibility-v7` em DEV/preview primeiro, preservando o guia canônico da collection.

## Próximos passos prontos

1. **Mind 002 canonical/CTR packet** — read-only extra + possível ajuste pontual no PDP Black Hyper Crimson/hub, com approval antes de write.
2. **Onitsuka visual dedupe preview** — no-op da section `sections/lk-onitsuka-ai-visibility-v7.liquid` em DEV se existir; se não existir no DEV, preparar production-safe como fizemos em Mind/Vomero.

## O que precisa aprovação

- Qualquer Shopify production write.
- Qualquer theme write, mesmo DEV, se alterar asset remoto.
- Qualquer alteração de PDP, collection, title/meta, descriptionHtml ou schema.

## Artefatos

- GSC: `growth/work/top123-20260622/gsc-mind002-onitsuka-28d-readonly.json`
- GA4: `growth/work/top123-20260622/ga4-top-pages-mind002-onitsuka-28d-readonly.json`
- Public QA: `growth/work/top123-20260622/top123-public-qa-readonly.json`
- Shopify Admin read-only: `growth/work/top123-20260622/shopify-collections-admin-readonly-top12.json`
- Theme asset map: `growth/work/top123-20260622/onitsuka-theme-asset-map-readonly.json`
