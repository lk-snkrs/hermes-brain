# Approval Packet — PDP SEO-only cleanup — `sob encomenda` + SEO metafield drift

Data: 2026-06-25
Owner: `[LK] Growth` → execução Shopify só após aprovação atual / LK Shopify se necessário
Status: **preparado, sem write executado**

## Origem

Cron/impact review D+7: `lkpdpseocroD7`

Relatório base:
`areas/lk/sub-areas/growth/reports/impact-reviews/pdp-cro-seo-d7-20260625T190553Z/REPORT.md`

## Veredito do D+7

- Impacto CRO/SEO ainda **misto/inconclusivo** para causalidade.
- Não recomendo rollback automático dos blocos CRO.
- O problema acionável é QA editorial/SEO nos 9 PDPs **SEO-only**:
  - `sob encomenda` público detectado em 9/9 PDPs SEO-only;
  - SEO metafields esperados do receipt 2026-06-18 batem em 4/9; 5/9 apresentam drift no readback atual.

## Escopo proposto

Fazer um patch controlado, produto por produto, limitado a:

1. remover/normalizar menções públicas de `sob encomenda` nos 9 PDPs SEO-only;
2. revisar e normalizar SEO title/description somente quando houver drift real vs intenção aprovada/receipt;
3. manter tom premium LK: curadoria, autenticidade, atendimento humano e confirmação via chat quando necessário;
4. não alterar preço, estoque, variante, disponibilidade, imagens, tags, collections, GMC, Klaviyo, campanhas, checkout ou tema.

## PDPs afetados

| Handle | Produto | Views pós GA4 | Impr. GSC pós | `sob encomenda` público | Drift SEO title | Drift SEO desc |
|---|---|---:|---:|---|---|---|
| `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` | Tênis Nike Vomero Premium SP Black Mini Chrome Swoosh Preto | 99 | 50.0 | sim | não/nd | não/nd |
| `tenis-nike-vomero-premium-white-lapis-total-orange-off-white` | Tênis Nike Vomero Premium White Lapis Total Orange Off White | 67 | 19.0 | sim | não/nd | não/nd |
| `tenis-nike-vomero-premium-particle-rose-burgundy-rosa` | Tênis Nike Vomero Premium Particle Rose Burgundy Rosa | 148 | 59.0 | sim | não/nd | não/nd |
| `tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja` | Tênis Nike Vomero Premium x Melitta Baumeister Total Orange Laranja | 61 | 135.0 | sim | não/nd | não/nd |
| `tenis-onitsuka-tiger-x-versace-sakura-leather-loafers-brown-white-marrom` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown White Marrom | 11 | 0 | sim | não/nd | não/nd |
| `tenis-nike-vomero-premium-volt-tint-sapphire-verde` | Tênis Nike Vomero Premium Volt Tint Sapphire Verde | 67 | 530.0 | sim | não/nd | não/nd |
| `tenis-new-balance-gator-run-timberwolf-bege` | Tênis New Balance Gator Run Timberwolf Bege | 23 | 2.0 | sim | não/nd | não/nd |
| `tenis-nike-x-tom-sachs-mars-yard-3-0-bege` | Tênis Nike x Tom Sachs Mars Yard 3.0 Bege | 15 | 21.0 | sim | não/nd | não/nd |
| `tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green` | Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green | 18 | 8.0 | sim | não/nd | não/nd |


## Prioridade interna

1. `tenis-nike-x-tom-sachs-mars-yard-3-0-bege` — pós com +110% impressões e CTR 4,76%; limpar copy para não desperdiçar SERP.
2. `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` — CTR pós 2,00%, mas posição piorou; limpar e revisar snippet.
3. `tenis-nike-vomero-premium-volt-tint-sapphire-verde` — impressões +80,9%, mas posição piorou; revisar promessa/meta sem preço/estoque.
4. Demais 6 — batch de higiene editorial para remover termo proibido e alinhar tom.

## Risco

- Baixo se limitado a copy/metafields.
- Médio se mexer em descrição longa sem readback, por risco de remover informação útil do PDP.
- Sem impacto esperado em checkout/GMC/campanhas se guardrails forem respeitados.

## Rollback

Antes de qualquer write:
- salvar backup Admin de cada produto: title, handle, bodyHtml, SEO title, SEO description, updatedAt;
- salvar readback público antes/depois.

Rollback:
- restaurar `bodyHtml`, `seo.title` e `seo.description` do backup por produto;
- revalidar HTTP 200 público e ausência/presença esperada de termos.

## Aprovação necessária

Para executar, Lucas precisa aprovar explicitamente:

> Aprovo preparar em dev/readback e, se o diff estiver restrito, aplicar em produção a limpeza dos 9 PDPs SEO-only do review D+7, limitada a remover/normalizar `sob encomenda` público e corrigir drift de SEO title/description conforme receipt/intenção aprovada, sem alterar preço, estoque, variantes, disponibilidade, imagens, tags, collections, GMC, Klaviyo, campanhas, checkout ou tema, com backup, rollback e readback público por PDP.

## Non-actions agora

- Nenhum write executado.
- Não consultar estoque/Tiny.
- Não fazer rollback do CRO.
- Não mexer nos PDPs CRO primeiros 5 / rodada 2 neste pacote.
