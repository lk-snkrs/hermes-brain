# Approval packet — LK Stock OS fila P0/P1

- Data/hora UTC: 2026-06-10T19:23:28Z
- DB fonte: `areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db`
- Execução em paralelo: workers locais `P0` e `P1` em `areas/lk/sub-areas/stock/reports/gate-b3-p0p1-operational-queue-workers-20260610T_P0P1_QUEUE_WORKERS`
- Escopo: local/read-only; fila de decisão interna; não é promessa de pronta entrega.

## Resumo

- P0: 4 itens
- P1: 13 itens
- Tiny write: 0
- Shopify write: 0
- Writes externos: 0
- Pronta entrega pública liberada: 0

## Fila P0 — candidatos a decisão de reposição/transferência

Critério: demanda local + estoque observado 0 na DB + identidade local resolvida. Antes de qualquer ação, reconfirmar Tiny/fonte viva no momento.

- **#1 — 205759 610-8**
  - Produto: Crocs Classic Clog x The Cars Lightning McQueen Vermelho
  - Handle: `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`
  - Tamanho: `41`
  - Status identidade: `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH` | resolvido seguro: `1`
  - Estoque observado na DB: `0.0` | demanda local: `6.0` un. | receita sinal: R$ 2.999,98
  - Risco/lane: `SOLD_AND_ZERO_STOCK_IN_DB` / `REPLENISHMENT_DECISION_PACKET_CANDIDATE` | score: `98.0`
  - Próximo passo seguro: Preparar decision packet de reposição/transferência; antes de qualquer ação externa, reconfirmar Tiny/fonte viva por SKU/tamanho.
- **#2 — FQ1180001-11**
  - Produto: Tênis Yuto Horigome x Nike SB Dunk Low Azul
  - Handle: `yuto-horigome-x-nike-sb-dunk-low`
  - Tamanho: `44`
  - Status identidade: `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH` | resolvido seguro: `1`
  - Estoque observado na DB: `0.0` | demanda local: `3.0` un. | receita sinal: R$ 3.999,99
  - Risco/lane: `SOLD_AND_ZERO_STOCK_IN_DB` / `REPLENISHMENT_DECISION_PACKET_CANDIDATE` | score: `72.0`
  - Próximo passo seguro: Preparar decision packet de reposição/transferência; antes de qualquer ação externa, reconfirmar Tiny/fonte viva por SKU/tamanho.
- **#3 — IH2612-1**
  - Produto: Tênis adidas Handball Spezial Sporty & Rich Brown Marrom
  - Handle: `tenis-adidas-handball-spezial-sporty-rich-brown-marrom`
  - Tamanho: `35`
  - Status identidade: `CONSULTABLE_LOCAL_RESOLVED` | resolvido seguro: `1`
  - Estoque observado na DB: `0.0` | demanda local: `3.0` un. | receita sinal: R$ 2.999,99
  - Risco/lane: `SOLD_AND_ZERO_STOCK_IN_DB` / `REPLENISHMENT_DECISION_PACKET_CANDIDATE` | score: `68.0`
  - Próximo passo seguro: Preparar decision packet de reposição/transferência; antes de qualquer ação externa, reconfirmar Tiny/fonte viva por SKU/tamanho.
- **#4 — 205759 610-7**
  - Produto: Crocs Classic Clog x The Cars Lightning McQueen Vermelho
  - Handle: `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`
  - Tamanho: `40`
  - Status identidade: `CONSULTABLE_LOCAL_RESOLVED_BY_LIVE_EXACT_MATCH` | resolvido seguro: `1`
  - Estoque observado na DB: `0.0` | demanda local: `3.0` un. | receita sinal: R$ 1.499,99
  - Risco/lane: `SOLD_AND_ZERO_STOCK_IN_DB` / `REPLENISHMENT_DECISION_PACKET_CANDIDATE` | score: `66.5`
  - Próximo passo seguro: Preparar decision packet de reposição/transferência; antes de qualquer ação externa, reconfirmar Tiny/fonte viva por SKU/tamanho.

## Fila P1 — demanda com identidade bloqueada

Critério: demanda local material, mas identidade SKU/Tiny/Shopify bloqueada; precisa resolver antes de tratar como estoque/compra/reposição.

- **#1 — CDGP2**
  - Produto: Polo Comme des Garçons PLAY Red Emblem White Branco
  - Handle: `polo-comme-des-garcons-play-branco`
  - Tamanho: `G/L`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `30.0` un. | receita sinal: R$ 17.999,90
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `246.0`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#2 — LIP**
  - Produto: The Peptide Lip Tints Rhode Multicolor
  - Handle: `the-peptide-lip-tints-rhode-multicolor`
  - Tamanho: ``
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `19.0` un. | receita sinal: R$ 3.599,87
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `181.95`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#3 — LIPCASE-11**
  - Produto: Lip Case Rhode By Hailey Bieber
  - Handle: `lip-case-rhode-by-hailey-bieber`
  - Tamanho: `Iphone 16 Pro Max`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `13.0` un. | receita sinal: R$ 6.799,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `134.85`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#4 — CD0461002**
  - Produto: Tênis Nike Air Jordan 1 High Seafoam Verde
  - Handle: `air-jordan-1-high-seafoam`
  - Tamanho: `34`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `0.0` | demanda local: `10.0` un. | receita sinal: R$ 16.059,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `94.54`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#5 — AIME11**
  - Produto: Boné 5 Panel Aimé Leon Dore Unisphere Azul
  - Handle: `bone-5-panel-aime-leon-dore-unisphere-azul`
  - Tamanho: ``
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `9.0` un. | receita sinal: R$ 6.999,93
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `80.25`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#6 — NDP006-3**
  - Produto: Camiseta Nude Project Global Soon Ash Cinza
  - Handle: `camiseta-nude-project-global-soon-ash-cinza`
  - Tamanho: `M/M`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `1.0` | demanda local: `7.0` un. | receita sinal: R$ 4.999,95
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `68.25`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#7 — ST33**
  - Produto: Camiseta Boxy Saint Studio Supima Preto
  - Handle: `camiseta-boxy-saint-studio-supima-preto`
  - Tamanho: `P/S`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `5.0` un. | receita sinal: R$ 564,67
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `45.42`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#8 — 1183A746-751-1**
  - Produto: Tênis Onitsuka Tiger Mexico 66 Kill Bill Slip-On Amarelo
  - Handle: `tenis-onitsuka-tiger-mexico-66-kill-bill-slip-on-amarelo`
  - Tamanho: `34`
  - Status identidade: `BLOCKED_TINY_MISSING` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `3.0` un. | receita sinal: R$ 2.399,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `34.05`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#9 — 1183B566.201**
  - Produto: Tênis Onitsuka Tiger Mexico 66 Gold White Dourado
  - Handle: `tenis-onitsuka-tiger-mexico-66-gold-white-dourado`
  - Tamanho: `39.5`
  - Status identidade: `BLOCKED_TINY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `3.0` un. | receita sinal: R$ 2.399,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `31.8`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#10 — CQ9446400**
  - Produto: Tênis Nike Air Jordan 1 Low Alternate Royal Toe Azul
  - Handle: `air-jordan-1-low-royal-toe`
  - Tamanho: `34`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `0.0` | demanda local: `3.0` un. | receita sinal: R$ 1.799,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `31.35`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#11 — PC9060GY-2**
  - Produto: Tênis New Balance 9060 Kids Raincloud Cinza (Infantil)
  - Handle: `tenis-new-balance-9060-kids-raincloud-cinza`
  - Tamanho: `33`
  - Status identidade: `BLOCKED_TINY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `3.0` un. | receita sinal: R$ 1.199,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `30.9`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#12 — 41499672090-4**
  - Produto: Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho
  - Handle: `chinelo-havaianas-x-dolce-gabanna-carreto-ciciliano-vermelho`
  - Tamanho: `41/42`
  - Status identidade: `BLOCKED_TINY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `2.0` un. | receita sinal: R$ 1.799,99
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `23.85`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.
- **#13 — 553558065-1**
  - Produto: Tênis Nike Air Jordan 1 Low Lucky Green Verde
  - Handle: `tenis-air-jordan-1-low-lucky-green-verde`
  - Tamanho: `40`
  - Status identidade: `BLOCKED_SHOPIFY_DUPLICATE` | resolvido seguro: `0`
  - Estoque observado na DB: `None` | demanda local: `2.0` un. | receita sinal: R$ 1.349,90
  - Risco/lane: `BLOCKED_IDENTITY` / `RESOLVE_IDENTITY_BEFORE_STOCK_DECISION` | score: `23.51`
  - Próximo passo seguro: Resolver identidade SKU/Tiny/Shopify local/read-only antes de decisão de estoque; não tratar como reposição confirmada.

## Aprovações possíveis

- `Aprovo reconfirmar Tiny/fonte viva read-only para os P0 e preparar preview de reposição/transferência, sem compra/envio/write.`
- `Aprovo resolver identidade local dos P1 em lote, sem Tiny/Shopify write e sem promessa de disponibilidade.`
- Qualquer compra, transferência real, contato externo, Tiny/Shopify write ou promessa ao cliente exige aprovação escopada separada.
