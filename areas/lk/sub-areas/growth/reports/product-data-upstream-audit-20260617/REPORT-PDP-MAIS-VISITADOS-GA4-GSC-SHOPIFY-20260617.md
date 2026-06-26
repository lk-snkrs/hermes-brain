# Auditoria upstream Shopify — PDPs mais visitados + GSC — 2026-06-17

**Modo:** read-only. **Writes externos:** 0.
**Escopo:** produtos/PDPs mais visitados, com correções propostas para a própria Shopify como fonte de verdade.

## Fontes usadas
- GA4: últimos 30 dias até ontem, filtro `/products/`.
- Google Search Console: 2026-05-18 a 2026-06-16, páginas `/products/`.
- Shopify Admin GraphQL: leitura de produto, SEO, descrição e metafields `mm-google-shopping`.

## Achados executivos
- PDPs auditados no cruzamento GA4→Shopify: 60.
- Páginas de produto lidas no GSC: 250.
- Lacuna mais recorrente: `mm-google-shopping.google_product_category` ausente em parte dos produtos mais relevantes.
- Lacuna estrutural recorrente: MPN ausente em variantes. Não recomendo inferir MPN sem fonte confiável; deve vir de SKU/modelo/fornecedor ou regra aprovada.
- Cor (`mm-google-shopping.color`) parece muito melhor preenchida nos top PDPs do que no cluster 204L inicial; ainda precisa batch específico para long tail/cluster.

## Contagem automática de lacunas
- MPN ausente nas variantes: 60
- GMC google_product_category ausente: 29
- SEO description longa >165: 4
- SEO title longo >70: 3
- SEO title ausente: 3
- GMC color ausente em mm-google-shopping.color: 2
- GMC gender ausente: 2
- status Shopify: 1
- SEO description ausente: 1
- SKUs ausentes nas variantes: 1

## Ranking de prioridade — corrigir na Shopify primeiro

### 1. crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho
- Score: 6.72
- GA4 views: 692 | sessões: 657
- GSC: 188 cliques | 76616 impressões | CTR 0.25% | posição 7.4
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 2. slide-nike-mind-001-light-smoke-grey-cinza
- Score: 6.07
- GA4 views: 3695 | sessões: 3398
- GSC: 6 cliques | 3463 impressões | CTR 0.17% | posição 12.2
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 3. tenis-nike-vomero-premium-sail-coconut-milk-branco
- Score: 4.54
- GA4 views: 1832 | sessões: 1539
- GSC: 29 cliques | 10176 impressões | CTR 0.28% | posição 4.3
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 4. travis-scott-x-air-jordan-1-low-og-reverse-mocha
- Score: 4.53
- GA4 views: 1224 | sessões: 1151
- GSC: 45 cliques | 15209 impressões | CTR 0.30% | posição 5.3
- Shopify: ACTIVE | online: sim
- Lacunas:
  - SEO title longo >70
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 5. tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo
- Score: 4.49
- GA4 views: 2218 | sessões: 1916
- GSC: 40 cliques | 8480 impressões | CTR 0.47% | posição 4.7
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 6. tenis-nike-x-nocta-hot-step-2-branco
- Score: 3.48
- GA4 views: 748 | sessões: 701
- GSC: 58 cliques | 10637 impressões | CTR 0.55% | posição 5.1
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 7. tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege
- Score: 3.44
- GA4 views: 2743 | sessões: 2735
- GSC: sem linha no top retornado
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 8. slide-nike-mind-001-geode-teal-verde
- Score: 3.32
- GA4 views: 947 | sessões: 897
- GSC: 13 cliques | 3498 impressões | CTR 0.37% | posição 6.5
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 9. tenis-new-balance-9060-mushroom-arid-stone-camurca
- Score: 3.27
- GA4 views: 1261 | sessões: 1178
- GSC: 22 cliques | 3143 impressões | CTR 0.70% | posição 4.6
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 10. slide-nike-mind-001-light-bone-bege
- Score: 3.05
- GA4 views: 689 | sessões: 590
- GSC: 6 cliques | 3318 impressões | CTR 0.18% | posição 10.5
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 11. slide-nike-mind-001-black-chrome-preto
- Score: 3.04
- GA4 views: 2331 | sessões: 2068
- GSC: 7 cliques | 167 impressões | CTR 4.19% | posição 5.1
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 12. tenis-adidas-samba-og-x-disney-pixar-toy-story
- Score: 2.99
- GA4 views: 962 | sessões: 923
- GSC: 21 cliques | 3619 impressões | CTR 0.58% | posição 6.5
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 13. tenis-on-running-loewe-lightspray-cloudmonster-branco
- Score: 2.92
- GA4 views: 458 | sessões: 438
- GSC: 5 cliques | 285 impressões | CTR 1.75% | posição 4.4
- Shopify: DRAFT | online: não
- Lacunas:
  - status Shopify = DRAFT
  - SEO title ausente
  - SEO description ausente
  - GMC color ausente em mm-google-shopping.color
  - GMC gender ausente
  - SKUs ausentes nas variantes
  - MPN ausente nas variantes
- Sugestões automáticas:
  - sugerir color: Branco

### 14. tenis-onitsuka-tiger-mexico-66-white-black-branco
- Score: 2.89
- GA4 views: 447 | sessões: 329
- GSC: 7 cliques | 11945 impressões | CTR 0.06% | posição 6.0
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 15. tenis-nike-vomero-premium-flat-stout-marrom
- Score: 2.83
- GA4 views: 2409 | sessões: 2288
- GSC: 8 cliques | 1388 impressões | CTR 0.58% | posição 3.9
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 16. ben-jerrys-x-dunk-low-sb-chunky-dunky
- Score: 2.8
- GA4 views: 330 | sessões: 316
- GSC: 38 cliques | 5318 impressões | CTR 0.71% | posição 6.8
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 17. tenis-adidas-sl72-og-maroon-almost-yellow-marrom
- Score: 2.42
- GA4 views: 406 | sessões: 360
- GSC: 26 cliques | 3356 impressões | CTR 0.77% | posição 4.2
- Shopify: ACTIVE | online: sim
- Lacunas:
  - MPN ausente nas variantes

### 18. tenis-adidas-samba-disney-101-dalmatians-penny-branco
- Score: 2.16
- GA4 views: 1420 | sessões: 1393
- GSC: 37 cliques | 827 impressões | CTR 4.47% | posição 2.5
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 19. nike-sb-dunk-low-sandy-ebay-2022
- Score: 2.13
- GA4 views: 1078 | sessões: 1040
- GSC: sem linha no top retornado
- Shopify: ACTIVE | online: sim
- Lacunas:
  - SEO title longo >70
  - GMC google_product_category ausente
  - MPN ausente nas variantes

### 20. mule-bravest-studios-bear-claw-black-preto
- Score: 2.04
- GA4 views: 1324 | sessões: 1319
- GSC: 8 cliques | 403 impressões | CTR 1.99% | posição 6.9
- Shopify: ACTIVE | online: sim
- Lacunas:
  - GMC google_product_category ausente
  - MPN ausente nas variantes

## Approval packet recomendado — não executado

### Objetivo
Corrigir na Shopify os dados upstream dos PDPs com maior tráfego/demanda, para que SEO/GMC/Simprosys leiam da fonte certa.

### Fase 1 — micro-piloto sugerido
- Escopo: top 10 do ranking acima.
- Writes propostos: somente metafields Shopify `mm-google-shopping.*` e, se aprovado item a item, SEO title/description/descrição de produto.
- Excluído: preço, estoque, disponibilidade, variante, publicação de produto, feed config, GMC direto, campanhas, theme.

### Campos candidatos
- `mm-google-shopping.google_product_category`: preencher onde ausente usando taxonomia aprovada por categoria. Para tênis/sapatos, validar o padrão já usado na LK antes do write.
- `mm-google-shopping.color`: preencher quando ausente e inferível com alta confiança pelo título/handle.
- `mm-google-shopping.gender` e `age_group`: preencher apenas com regra comercial aprovada.
- `mpn`: não inferir em massa sem fonte confiável.
- SEO title/description: ajustar só quando longo/ausente/baixo CTR, com copy premium LK.

### Backup/QA/Rollback
- Backup JSON por produto antes do write.
- Readback Shopify imediato por GraphQL.
- QA público por URL de PDP.
- Esperar sync Simprosys/GMC e validar Merchant depois.
- Rollback: restaurar metafields/SEO antigos a partir do backup.

## Artefatos
- `top-pdp-ga4-shopify-audit.json` — dados completos GA4 + Shopify + GSC consolidado.
- Este relatório consolidado.